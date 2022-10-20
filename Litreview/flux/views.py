from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from flux.form import TicketForm, ReviewForm
from flux.models import Ticket, Review
from django.db.models import Q


@login_required()
def flux(request):
    if request.user.is_authenticated:
        posts = Ticket.objects.all().order_by('-time_created')
        review = Review.objects.all().order_by('-time_created')

        return render(request, 'flux/flux.html', context={'posts': posts, 'review': review})


@login_required()
def create_ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            form.save()
            return redirect('posts')
    return render(request, 'flux/create_ticket.html', context={'form': form})


@login_required()
def posts(request):
    if request.user.is_authenticated:
        posts = Ticket.objects.filter(user=request.user)
        review = Review.objects.filter(user=request.user)
        posts_empty = Ticket.objects.filter(Q(image='') &
                                            Q(user=request.user))
        print(request.user)
        print(posts)
        return render(request, 'flux/posts.html',
                      {'posts': posts,
                       'review': review,
                       'posts_empty': posts_empty})


@login_required()
def update_review(request, p_id):
    ticket = Ticket.objects.get(id=p_id)
    review = Review.objects.get(ticket_id=p_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        form_review = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid() and form_review.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            form.save()
            form_review.save()
            return redirect('posts')
    else:
        form = TicketForm(instance=ticket)
        form_review = ReviewForm(instance=review)
    return render(request, 'flux/ticket_update.html',
                  context={'form': form, 'form_review': form_review,
                           'review': review})


@login_required()
def ticket_only(request, p_id):
    tickets = Ticket.objects.get(id=p_id)
    if request.method == 'POST':
        forms = TicketForm(request.POST, request.FILES, instance=tickets)
        if forms.is_valid():
            photo = forms.save(commit=False)
            photo.uploader = request.user
            photo.save()
            forms.save()
            return redirect('posts')
    else:
        forms = TicketForm(instance=tickets)
    return render(request, 'flux/ticket_update.html', context={'form': forms, 'tickets': tickets})


@login_required()
def create_critic_no_answer(request):
    form = TicketForm()
    form_rating = ReviewForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        form_rating = ReviewForm(request.POST)

        if form.is_valid() and form_rating.is_valid():
            form_critique = form.save(commit=False)
            form_critique.user = request.user
            form_critique.save()
            form_critique_rating = form_rating.save(commit=False)
            form_critique_rating.user = request.user
            form_critique_rating.ticket = form_critique
            form_critique_rating.save()
            return redirect('posts')
    return render(request, 'flux/create_critique.html',
                  context={'form': form, 'form_rating': form_rating})


@login_required()
def delete_posts(request, p_id):
    ticket = Ticket.objects.get(id=p_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('posts')
    return render(request, 'flux/posts_delete.html', context={'ticket': ticket})


def create_review_for_post(request, p_id):
    ticket = Ticket.objects.get(id=p_id)
    review = ReviewForm()
    if request.method == 'POST':
        review = ReviewForm(request.POST)
        if review.is_valid():
            form_critique = review.save(commit=False)
            form_critique.user = request.user
            form_critique.ticket = ticket
            form_critique.save()
            return redirect('posts')
    else:
        review = ReviewForm()
    return render(request, 'flux/create_critique_for_post.html',
                  context={'ticket': ticket,
                           'review': review})

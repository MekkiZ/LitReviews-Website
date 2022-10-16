from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from flux.form import TicketForm, ReviewForm
from flux.models import Ticket, Review


@login_required()
def flux(request):
    if request.user.is_authenticated:
        posts = Ticket.objects.all()
        user = request.user
        return render(request, 'flux/flux.html', context={'posts': posts})


@login_required()
def create_ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            photo_save = form.save(commit=False)
            photo_save.uploader = request.user.id
            photo_save.save()
            return redirect('posts')
    return render(request, 'flux/create_ticket.html', context={'form': form})


@login_required()
def posts(request):
    if request.user.is_authenticated:
        posts = Ticket.objects.filter(id=request.user.id)
        reviews = Review
        print(posts)
        return render(request, 'flux/posts.html',
                      {'posts': posts})


def create_critic_no_answer(request):
    form = TicketForm()
    form_rating = ReviewForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        form_rating = ReviewForm(request.POST)
        if all([form.is_valid(), form_rating.is_valid()]):
            form_critique = form.save(commit=False)
            form_critique.uploader = request.user.id
            form_critique.save()
            form_critique_rating = form.save(commit=False)
            form_critique_rating.uploader = request.user.id
            form_critique_rating.save()
            return redirect('posts')
    return render(request, 'flux/create_critique.html',
                  context={'form': form, 'form_rating': form_rating})


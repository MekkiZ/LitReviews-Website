from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from flux.form import TicketForm, ReviewForm


@login_required()
def flux(request):
    return render(request, 'flux/flux.html')


@login_required()
def create_ticket(request):
    form = TicketForm()
    if request.method == 'POST':

        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            photo_save = form.save(commit=False)
            photo_save.uploader = request.user
            photo_save.save()
            return redirect('flux')
    return render(request, 'flux/create_ticket.html', {'form': form})

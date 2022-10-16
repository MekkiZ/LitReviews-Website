from django.shortcuts import render, redirect
from authentication.form import LoginForm, SignForm
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    message = ' '
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('flux')
            else:
                message = f"Votre identifiant n'existe pas"

    return render(request, 'auth/login.html', context={'form': form, 'message': message})


def signup_user(request):
    form = SignForm()
    if request.method == "POST":
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        return render(request, 'auth/signup.html', context={'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')

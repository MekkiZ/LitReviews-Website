from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur:"}))
    password = forms.CharField(label='',max_length=30,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Mots de passe'}))


class SignForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "gtre",
        "placeholder": "Nom d'utilisateur"
    }))

    password1 = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "gtre",
        'type': 'password',
        "placeholder": "Mots de passe"
    }))

    password2 = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "gtre",
        'type': 'password',
        "placeholder": "Retaper votre mots de pass"
    }))

    class Meta(UserCreationForm.Meta):
        models = User
        fields = ('username', 'password1', 'password2')

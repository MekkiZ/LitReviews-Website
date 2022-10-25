from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               max_length=30,
                               widget=forms.TextInput(attrs={
                                   'placeholder': "Nom d'utilisateur:",
                                    "class": "input-group-text",
                                   'id': "inputGroup-sizing-lg",
                                    }))
    password = forms.CharField(label='',max_length=30,
                               widget=forms.PasswordInput(attrs={
                                'placeholder': "Mot de passe:",
                                "class": "input-group-text",
                                'id': "inputGroup-sizing-lg",
                                    }))


class SignForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "input-group-text",
        "placeholder": "Nom d'utilisateur",
        'id':"inputGroup-sizing-lg",
    }))

    password1 = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "input-group-text",
        'id':"inputGroup-sizing-lg",
        'type': 'password',
        "placeholder": "Mots de passe"
    }))

    password2 = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "input-group-text",
        'type': 'password',
        "placeholder": "Retaper votre mots de pass",
        'id':"inputGroup-sizing-lg",
    }))

    class Meta(UserCreationForm.Meta):
        models = User
        fields = ('username', 'password1', 'password2')

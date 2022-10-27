from django import forms
from . import models


class TicketForm(forms.ModelForm):
    """Form to create a new ticket."""

    title = forms.CharField(label='Titre', max_length=30,
                            widget=forms.TextInput(attrs={'class': "form-control"}))

    description = forms.CharField(label='Description', max_length=30,
                                  widget=forms.Textarea(attrs={'class': "form-control",
                                                               'id': 'exampleFormControlTextarea1',
                                                               'rows': '3'}))

    image = forms.FileField(label='', widget=forms.FileInput(attrs={'class': "custom-file-input", }), required=False)
    class Meta:
        model = models.Ticket
        fields = ('title', 'description', 'image')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image'
        }


class ReviewForm(forms.ModelForm):
    """Form to create a Review."""
    headline = forms.CharField(label='Titre', max_length=30,
                               widget=forms.TextInput(attrs={'class': "form-control"}))

    body = forms.CharField(label='Description', max_length=30,
                           widget=forms.Textarea(attrs={'class': "form-control",
                                                        'id': 'exampleFormControlTextarea1',
                                                        'rows': '3'}))
    CHOICES = [('0', '- 0'),
               ('1', '- 1'),
               ('2', '- 2'),
               ('3', '- 3'),
               ('4', '- 4'),
               ('5', '- 5'),
               ]
    rating = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'class': 'controle',
    }), choices=CHOICES, )

    class Meta:
        model = models.Review
        fields = ('headline', 'rating', 'body')
        labels = {
            'headline': 'Title',
            'rating': 'Rating',
            'body': 'Body',

        }


class FollowForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ('followed_user',)

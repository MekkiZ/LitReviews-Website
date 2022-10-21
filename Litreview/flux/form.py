from django import forms
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ('title', 'description', 'image')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image'
        }


class ReviewForm(forms.ModelForm):
    CHOICES = [('0', '- 0'),
               ('1', '- 1'),
               ('2', '- 2'),
               ('3', '- 3'),
               ('4', '- 4'),
               ('5', '- 5'),
               ]
    rating = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'class': 'controle',
    }), choices=CHOICES,)

    class Meta:
        model = models.Review
        fields = ('headline', 'rating', 'body')
        labels = {
            'headline': 'Title',
            'rating': 'Rating',
            'body': 'Body',

        }


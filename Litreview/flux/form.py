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
    title = forms.CharField(label='titre')

    class Meta:
        model = models.Review
        fields = ('rating', 'body')
        labels = {
            'title': 'Title',
            'rating': 'Rating',
            'body': 'Body',

        }

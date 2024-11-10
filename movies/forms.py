from django import forms
from . import models

class CreateMovie(forms.ModelForm):
    class Meta: 
        model = models.Movies
        fields = ['title', 'body', 'genreOne', 'genreTwo', 'genreThree', 'slug', 'date', 'banner', 'rating']

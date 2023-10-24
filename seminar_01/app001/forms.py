from django import forms
from datetime import date

from .models import Author


class AddAuthorForm(forms.Form):
    """Add a new author to database"""

    name = forms.CharField(min_length=1, max_length=100)
    surname = forms.CharField(min_length=1, max_length=100)
    email = forms.EmailField(max_length=100)
    birthday = forms.DateField(
        initial=date.today,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', })
    )
    biography = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class AddCommentary(forms.Form):
    """Add a new commentary by author to a database"""

    authors = [(f'{author.pk}', f'{author.surname} {author.name}')
               for author in Author.objects.all()]
    author_pk = forms.ChoiceField(choices=authors)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class AddArticle(forms.Form):

    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField(max_length=100)

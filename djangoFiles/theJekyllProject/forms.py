from django import forms
from django.utils import timezone
from tinymce.models import HTMLField


class PostForm(forms.Form):
    author = forms.CharField(
        help_text='Name of the author',
        label='Author',
        #initial=user.name
    )
    comments = forms.BooleanField(
        help_text='Should the comment be added?',
        label='Allow commenting'
    )
    date = forms.DateField(
        help_text='Date of posting',
        initial=timezone.now()
    )
    title = forms.CharField(
        help_text='title of the post',
    )
    content = HTMLField()

    # ModelChoiceField or add more categories
    category = forms.CharField(
        initial=PostCategory.objects.all()
    )

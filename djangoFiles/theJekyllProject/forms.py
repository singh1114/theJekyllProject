from django import forms
from django.utils import timezone

from theJekyllProject.models import PostCategory
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
class AddPostForm(forms.Form):
    author = forms.CharField(
        label='Author',
        max_length=40,
        help_text='Name of the author',
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
        max_length=400
    )

    content = forms.CharField(widget=CKEditorWidget())
    # ModelChoiceField or add more categories
    category = forms.CharField(
        #initial=PostCategory.objects.all()
        max_length=20
    )

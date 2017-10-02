from django import forms
from django.forms import ModelForm
from django.utils import timezone

from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

from theJekyllProject.models import PostCategory
from theJekyllProject.models import SiteData

class AddPostForm(forms.Form):
    author = forms.CharField(
        label='Author',
        max_length=40,
        help_text='Name of the author',
    )

    comments = forms.BooleanField(
        initial=True,
        required=False
    )

    date = forms.DateTimeField(
        help_text='Date of posting',
        initial=timezone.now()
    )

    layouts = (
        ('post', 'post'),
        ('page', 'page')
    )

    layout = forms.ChoiceField(
        choices=layouts
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



class SiteProfileForm(ModelForm):
    class Meta:
        model = SiteData
        fields = '__all__'
        #initials = {
        #    'name': _('Username'),
        #}

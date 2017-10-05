from django import forms
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User

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
    # FIXME ModelChoiceField or add more categories
    category = forms.CharField(
        #initial=PostCategory.objects.all()
        max_length=20
    )



class SiteProfileForm(forms.Form):
    # TODO All these stuff must have some initialized values
    name = forms.CharField(
        max_length=200,
        help_text='Name of the site',
        required=False,
    )
    description = forms.CharField(
        max_length=2000,
        help_text='Description of the site',
        initial='Your site description',
        required=False,
    )
    avatar = forms.ImageField(
        required=False,
    )


class SiteSocialProfileForm(forms.Form):
    # TODO Add initials
    dribble = forms.CharField(
        max_length=200,
        help_text='Your dribble username',
        required=False
    )
    email = forms.EmailField(
        max_length=200,
        required=False,
        help_text='email id'
    )
    facebook = forms.CharField(
        max_length=200,
        required=False,
        help_text='facebook username'
    )
    flickr = forms.CharField(
        max_length=200,
        required=False,
        help_text='flickr username'
    )
    github = forms.CharField(
        max_length=200,
        required=False,
        help_text='GitHub username'
    )
    instagram = forms.CharField(
        max_length=200,
        required=False,
        help_text='Instagram username'
    )
    linkedin = forms.CharField(
        max_length=200,
        required=False,
        help_text='Linkedin username'
    )
    pinterest = forms.CharField(
        max_length=200,
        required=False,
        help_text='pinterest username'
    )
    rss = forms.CharField(
        max_length=200,
        required=False,
        help_text='rss username'
    )
    twitter = forms.CharField(
        max_length=200,
        required=False,
        help_text='twitter username'
    )
    stackoverflow = forms.CharField(
        max_length=200,
        required=False,
        help_text='stackoverflow username'
    )
    youtube = forms.CharField(
        max_length=200,
        required=False,
        help_text='youtube username'
    )
    googleplus = forms.CharField(
        max_length=200,
        required=False,
        help_text='google plus username'
    )
    disqus = forms.CharField(
        max_length=200,
        required=False,
        help_text='disqus username'
    )
    google_analytics = forms.CharField(
        max_length=200,
        required=False,
        help_text='google analytics tracking id'
    )


class SitePluginForm(forms.Form):
    # TODO More than one plugins are allowed
    plugins = forms.CharField(
        max_length=200,
        required=False,
        help_text='Jekyll plugins that can be used in blog'
    )


class SiteExcludeForm(forms.Form):
    # TODO More than one excludes are allowed
    excludes = forms.CharField(
        max_length=200,
        required=False,
        help_text='Jekyll plugins that can be used in blog'
    )


class SiteThemeForm(forms.Form):
    # TODO get a picture of theme ready for the user to think about
    theme = forms.CharField(
        max_length=200,
        required=False,
        help_text='Theme of the site'
    )

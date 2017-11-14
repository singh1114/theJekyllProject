from django import forms
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

from theJekyllProject.models import PostCategory
from theJekyllProject.models import SiteData


class RepoForm(forms.Form):
    repo = forms.CharField(
        label='Repo Name',
        max_length=200,
        help_text='Create a new repository with the following name',
        widget = forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'blog',
                'name': 'repo-name'
            })
    )


class AddPostForm(forms.Form):
    author = forms.CharField(
        label='Author',
        max_length=40,
        help_text='Name of the author',
        widget = forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Author...',
                'name': 'author'
            })
    )

    comments = forms.BooleanField(
        initial=True,
        required=False,
    )

    date = forms.DateField(
        help_text='Date of posting',
        initial=timezone.now().date(),
        widget = forms.TextInput(attrs= {
                'class': 'form-control date-picker',
                'name': 'date'
            })
    )

    time = forms.TimeField(
        help_text='Date of posting',
        initial=timezone.now().time(),
        widget = forms.TextInput(attrs= {
                'class': 'form-control',
                'name': 'date'
            })
    )

    layouts = (
        ('post', 'post'),
        ('page', 'page')
    )

    layout = forms.ChoiceField(
        choices=layouts,
        widget = forms.Select(attrs= {
                'class': 'form-control',
                'name': 'layout'
            })
    )

    title = forms.CharField(
        help_text='title of the post',
        max_length=400,
        widget = forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'How to make a website',
                'name': 'title'
            })
    )

    category = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Technology',
                'name': 'category'
            }
        )
    )

    content = forms.CharField(
        widget=CKEditorWidget(attrs= {
                'class': 'form-control',
                'name': 'content'
            })
    )


class SiteProfileForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        help_text='Name of the site',
        required=False,
        widget=forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'JekLog',
                'name': 'title'
            }
        )
    )
    description = forms.CharField(
        max_length=2000,
        help_text='Description of the site',
        initial='Your site description',
        required=False,
        widget=forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Web developing guide',
                'name': 'description'
            }
        )
    )
    avatar = forms.ImageField(
        required=False,
    )


class SiteSocialProfileForm(forms.Form):
    dribbble = forms.CharField(
        max_length=200,
        help_text='Your dribbble username',
        required=False,
        widget=forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Dribbble',
                'name': 'dribbble'
            }
        )

    )
    email = forms.EmailField(
        max_length=200,
        required=False,
        help_text='email id',
        widget=forms.EmailInput(attrs= {
            'class': 'form-control',
            'placeholder': 'jeklogjek@gmail.com',
            'name': 'email',
            }
        )
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


class ContactForm(forms.Form):
    first_name = forms.CharField(
        label="First Name",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ranvir...',
                'name': 'first_name'
            }
        )
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Singh...',
                'name': 'last_name'
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'jeklogjek@gmail.com...',
                'name': 'email_name'
            }
        )
    )
    message = forms.CharField(
        label="Message",
        max_length=5000,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Type your message here..',
                'name': 'message'
            }
        )
    )

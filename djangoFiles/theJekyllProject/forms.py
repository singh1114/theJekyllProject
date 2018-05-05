import re

from django import forms
from django.utils import timezone

from ckeditor.widgets import CKEditorWidget


class RepoForm(forms.Form):
    repo = forms.CharField(
        label='Repo Name',
        max_length=200,
        help_text='Create a new repository with the following name',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'blog',
                'name': 'repo-name'
            })
    )

    def clean(self):
        """
        clean the repo name. repo name should not have special characters
        """
        cleaned_data = super(RepoForm, self).clean()
        passed_repo = cleaned_data.get("repo")
        if not re.match('[\w]+|[\d]+|[\-]+', passed_repo):
            raise forms.ValidationError(('Repo should not contain special'
                                         ' characters or spaces'),)


class AddPageForm(forms.Form):
    title = forms.CharField(
        help_text='title of the post',
        max_length=400,
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'About',
                'name': 'title'
            })
    )

    permalink = forms.CharField(
        label='permalink',
        max_length=400,
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '/about/',
                'name': 'permalink'
            })
    )

    content = forms.CharField(
        widget=CKEditorWidget(attrs={
                'class': 'form-control',
                'name': 'content'
            })
    )


class AddPostForm(forms.Form):
    author = forms.CharField(
        label='Author',
        max_length=40,
        help_text='Name of the author',
        widget=forms.TextInput(attrs={
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
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'date'
            })
    )

    time = forms.TimeField(
        help_text='Date of posting',
        initial=timezone.now().time(),
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'time'
            })
    )

    layouts = (
        ('post', 'post'),
    )

    layout = forms.ChoiceField(
        choices=layouts,
        widget=forms.Select(attrs={
                'class': 'form-control',
                'name': 'layout'
            })
    )

    title = forms.CharField(
        help_text='title of the post',
        max_length=400,
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'How to make a website',
                'name': 'title'
            })
    )

    content = forms.CharField(
        widget=CKEditorWidget(attrs={
                'class': 'form-control',
                'name': 'content'
            })
    )


class SiteProfileForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        help_text='Name of the site',
        required=False,
        widget=forms.TextInput(attrs={
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
        widget=forms.TextInput(attrs={
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
        widget=forms.TextInput(attrs={
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
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'jeklogjek@gmail.com',
            'name': 'email',
            }
        )
    )
    facebook = forms.CharField(
        max_length=200,
        required=False,
        help_text='facebook username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'facebook'
            })
    )
    flickr = forms.CharField(
        max_length=200,
        required=False,
        help_text='flickr username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'flickr'
            })
    )
    github = forms.CharField(
        max_length=200,
        required=False,
        help_text='GitHub username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'singh1114',
                'name': 'github'
            })
    )
    instagram = forms.CharField(
        max_length=200,
        required=False,
        help_text='Instagram username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'instagram'
            })
    )
    linkedin = forms.CharField(
        max_length=200,
        required=False,
        help_text='Linkedin username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'linkedin'
            })
    )
    pinterest = forms.CharField(
        max_length=200,
        required=False,
        help_text='pinterest username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'pinterest'
            })
    )
    rss = forms.CharField(
        max_length=200,
        required=False,
        help_text='rss username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'rss'
            })
    )
    twitter = forms.CharField(
        max_length=200,
        required=False,
        help_text='twitter username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'twitter'
            })
    )
    stackoverflow = forms.CharField(
        max_length=200,
        required=False,
        help_text='stackoverflow username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'stackoverflow'
            })
    )
    youtube = forms.CharField(
        max_length=200,
        required=False,
        help_text='youtube username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'youtube'
            })
    )
    googleplus = forms.CharField(
        max_length=200,
        required=False,
        help_text='google plus username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'googleplus'
            })
    )
    disqus = forms.CharField(
        max_length=200,
        required=False,
        help_text='disqus username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ranvir.singh',
                'name': 'disqus'
            })
    )
    google_analytics = forms.CharField(
        max_length=200,
        required=False,
        help_text='google analytics tracking id',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'UASR32323232_',
                'name': 'google_analytics'
            })
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

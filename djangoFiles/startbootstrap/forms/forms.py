from django.utils import timezone

from django import forms


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
                'placeholder': 'Web development guide',
                'name': 'description'
            }
        )
    )

    author = forms.CharField(
        max_length=2000,
        help_text='Name of the author',
        initial='Author name',
        required=False,
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'JekLog',
                'name': 'author'
            }
        )
    )

    baseurl = forms.CharField(
        max_length=2000,
        help_text='anything after "username.github.io" is the baseurl',
        initial='/jekyllblog',
        required=False,
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'JekLog',
                'name': 'author'
            }
        )
    )


class SiteSocialForm(forms.Form):
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


class SettingsForm(forms.Form):
    markdown = forms.CharField(
        max_length=200,
        required=False,
        help_text='github allowed markdown',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'kramdown',
                'name': 'markdown'
            })
    )
    paginate = forms.IntegerField(
        required=False,
        help_text='number of posts on one page',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 5,
                'name': 'paginate'
            })
    )
    paginate_path = forms.CharField(
        max_length=200,
        required=False,
        help_text='paginate path',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '/posts/page:num/',
                'name': 'paginate_path'
            })
    )


from mediumeditor.widgets import MediumEditorTextarea

class PostForm(forms.Form):
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

    title = forms.CharField(
        help_text='title of the post',
        max_length=400,
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'How to make a website',
                'name': 'title'
            })
    )

    background = forms.ImageField(
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'background image'
            })
    )

    content = forms.CharField(
        widget=MediumEditorTextarea()
    )

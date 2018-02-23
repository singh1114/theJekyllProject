from django import forms


class CNameForm(forms.Form):
    c_name = forms.CharField(
        max_length=200,
        required=False,
        help_text='custom domain name of site',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'blog.jeklog.com',
            'name': 'custom domain'
        })
    )

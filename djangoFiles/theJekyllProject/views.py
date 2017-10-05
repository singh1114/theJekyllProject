# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.models import User

from markdown2 import Markdown

from theJekyllProject.forms import AddPostForm
from theJekyllProject.forms import SiteExcludeForm
from theJekyllProject.forms import SitePluginForm
from theJekyllProject.forms import SiteProfileForm
from theJekyllProject.forms import SiteThemeForm
from theJekyllProject.forms import SiteSocialProfileForm

from theJekyllProject.functions import assign_boolean_to_comments
from theJekyllProject.functions import save_post_database
from theJekyllProject.functions import create_file_name
from theJekyllProject.functions import header_content
from theJekyllProject.functions import convert_content
from theJekyllProject.functions import write_file
from theJekyllProject.functions import move_file
from theJekyllProject.functions import save_site_data

from theJekyllProject.models import Post
from theJekyllProject.models import SiteData


# FIXME all the views must be decorated with login_required decorators
class AddPostView(FormView):
    """AddPostView to add post

    Example:
        Click on the Add post button when the user is logged in.
        We can add posts only if the user is logged in.

    TODO:
        * Make this view for logged in people only: Not done
        * Load the form: Not Done
        * convert the stuff as required: Not Done
        * Make new files: Not Done
        * Put the files at right places: Not Done
    """
    template_name = 'theJekyllProject/addpost.html'
    form_class = AddPostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            author = request.POST['author']
            comments = request.POST['comments']
            date = request.POST['date']
            layout = request.POST['layout']
            title = request.POST['title']
            content = request.POST['content']
            category = request.POST['category']

            # This is a turnaround... I don't know why it happened.
            # Checkbox produces 'on' as the result when selected.
            comments = assign_boolean_to_comments(comments)

            # save stuff to the database
            save_post_database(author, comments, date, layout, title, content)

            # Create file name
            date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            only_date = date_obj.date()
            file_name = create_file_name(only_date, title)

            # Create header content for the markdown file
            head_content = header_content(author, comments, date, layout, title)

            # Convert the body content to markdown
            body_content = convert_content(content)

            # Write the content into files
            write_file(file_name, head_content, body_content)

            # Move file to correct location
            move_file(file_name)
        return HttpResponse('Post ADDED!')


# FIXME Take care of this function based view
# FIXME Change it to class based view
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'core/home.html')

# FIXME ends here.
# FIXME ends here.


class SiteProfileView(FormView):
    template_name = 'theJekyllProject/siteprofile.html'
    form_class = SiteProfileForm

    def get_form_kwargs(self):
        user = self.request.user
        try:
            SiteData.objects.get(user=User.objects.get(username=user.username))
            name = SiteData.objects.get(user=User.objects.get(username=user.username)).name
            description = SiteData.objects.get(user=User.objects.get(username=user.username)).description
            avatar = SiteData.objects.get(user=User.objects.get(username=user.username)).avatar

        except:
            name = 'Your new site'
            description = 'Single line description of the site'
            # FIXME add an image initial
            avatar = 'An image'

        form_kwargs = super(SiteProfileView, self).get_form_kwargs()
        form_kwargs.update({
            'initial': {
                'name': name,
                'description': description,
                'avatar': avatar,
            }
        })
        return form_kwargs

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            name = request.POST['name']
            description = request.POST['description']
            avatar = request.POST['avatar']

            # save stuff to the database
            save_site_data(user, name, description, avatar)

            return HttpResponse('Profile data saved')


class SiteSocialProfileView(FormView):
    template_name = 'theJekyllProject/socialprofile.html'
    form_class = SiteSocialProfileForm



class SitePluginView(FormView):
    template_name = 'theJekyllProject/siteplugin.html'
    form_class = SitePluginForm



class SiteExcludeView(FormView):
    template_name = 'theJekyllProject/siteexclude.html'
    form_class = SiteExcludeForm


class SiteThemeView(FormView):
    template_name = 'theJekyllProject/sitetheme.html'
    form_class = SiteThemeForm


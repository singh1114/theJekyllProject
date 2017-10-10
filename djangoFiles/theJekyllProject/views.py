# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

from markdown2 import Markdown

from theJekyllProject.forms import AddPostForm
from theJekyllProject.forms import RepoForm
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
from theJekyllProject.functions import save_site_theme_data
from theJekyllProject.functions import create_config_file
from theJekyllProject.functions import get_repo_list
from theJekyllProject.functions import save_repo_data

from theJekyllProject.models import Post
from theJekyllProject.models import SiteData
from theJekyllProject.models import SiteSocialProfile
from theJekyllProject.models import SiteTheme


class RepoListView(TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        user = User.objects.get(username=user.username)
        social = user.social_auth.get(provider='github')
        user_token = social.extra_data['access_token']

        repo_list = get_repo_list(user_token)

        return render(request, 'theJekyllProject/repo_list.html', context={
            'repo_list': repo_list,
        })


class CreateRepoView(FormView):
    template_name = 'theJekyllProject/create_repo.html'
    form_class = RepoForm

    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST)
        if form.is_valid():
            repo = request.POST['repo']
            save_repo_data(user, repo)


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
        user = request.user
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
            save_post_database(user, author, comments, date, layout, title, content)

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


class PostListView(ListView):
    model = Post
    template_name = 'theJekyllProject/post_list.html'
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        post_list = Post.objects.order_by('-date').filter(user=self.request.user)
        return post_list


class PostUpdateView(UpdateView):
    model = Post
    fields = ['author', 'comments', 'date', 'layout', 'title', 'content']
    template_name = 'theJekyllProject/addpost.html'

    def get_success_url(self):
        return reverse('home')


class SiteProfileView(FormView):
    template_name = 'theJekyllProject/siteprofile.html'
    form_class = SiteProfileForm

    def get_form_kwargs(self):
        user = self.request.user
        user = User.objects.get(username=user.username)
        try:
            SiteData.objects.get(user=user)
            title = SiteData.objects.get(user=user).title
            description = SiteData.objects.get(user=user).description
            avatar = SiteData.objects.get(user=user).avatar

        except:
            title = 'Your new site'
            description = 'Single line description of the site'
            # FIXME add an image initial
            avatar = 'An image'

        form_kwargs = super(SiteProfileView, self).get_form_kwargs()
        form_kwargs.update({
            'initial': {
                'title': title,
                'description': description,
                'avatar': avatar,
            }
        })
        return form_kwargs

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            title = request.POST['title']
            description = request.POST['description']
            avatar = request.POST['avatar']
            # save stuff to the database
            save_site_data(user, title, description, avatar)
            create_config_file(user)
            return HttpResponse('Profile data saved')


class SiteSocialProfileView(FormView):
    template_name = 'theJekyllProject/socialprofile.html'
    form_class = SiteSocialProfileForm

    def get_form_kwargs(self):
        user = self.request.user
        user = User.objects.get(username=user.username)
        try:
            SiteSocialProfile.objects.get(user=user)
            dribble = SiteSocialProfile.objects.get(user=user).dribble
            email = SiteSocialProfile.objects.get(user=user).email
            facebook = SiteSocialProfile.objects.get(user=user).facebook
            flickr = SiteSocialProfile.objects.get(user=user).flickr
            github = SiteSocialProfile.objects.get(user=user).github
            instagram = SiteSocialProfile.objects.get(user=user).instagram
            linkedin = SiteSocialProfile.objects.get(user=user).linkedin
            pinterest = SiteSocialProfile.objects.get(user=user).pinterest
            rss = SiteSocialProfile.objects.get(user=user).rss
            twitter = SiteSocialProfile.objects.get(user=user).twitter
            stackoverflow = SiteSocialProfile.objects.get(user=user).stackoverflow
            youtube = SiteSocialProfile.objects.get(user=user).youtube
            googleplus = SiteSocialProfile.objects.get(user=user).googleplus
            disqus = SiteSocialProfile.objects.get(user=user).disqus
            google_analytics = SiteSocialProfile.objects.get(user=user).google_analytics
        except:
            dribble = ''
            email = ''
            facebook = ''
            flickr = ''
            github = ''
            instagram = ''
            linkedin = ''
            pinterest = ''
            rss = ''
            twitter = ''
            stackoverflow = ''
            youtube = ''
            googleplus = ''
            disqus = ''
            google_analytics = ''

        form_kwargs = super(SiteSocialProfileView, self).get_form_kwargs()
        form_kwargs.update({
            'initial': {
                'dribble': dribble,
                'email': email,
                'facebook': facebook,
                'flickr': flickr,
                'github': github,
                'instagram': instagram,
                'linkedin': linkedin,
                'pinterest': pinterest,
                'rss': rss,
                'twitter': twitter,
                'stackoverflow': stackoverflow,
                'youtube': youtube,
                'googleplus': googleplus,
                'disqus': disqus,
                'google_analytics': google_analytics,
            }
        })
        return form_kwargs

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            dribble = request.POST['dribble']
            email = request.POST['email']
            facebook = request.POST['facebook']
            flickr = request.POST['flickr']
            github = request.POST['github']
            instagram = request.POST['instagram']
            linkedin = request.POST['linkedin']
            pinterest = request.POST['pinterest']
            rss = request.POST['rss']
            twitter = request.POST['twitter']
            stackoverflow = request.POST['stackoverflow']
            youtube = request.POST['youtube']
            googleplus = request.POST['googleplus']
            disqus = request.POST['disqus']
            google_analytics = request.POST['google_analytics']

            site_social_profile = SiteSocialProfile(
                user = user,
                dribble = dribble,
                email = email,
                facebook = facebook,
                flickr = flickr,
                github = github,
                instagram = instagram,
                linkedin = linkedin,
                pinterest = pinterest,
                rss = rss,
                twitter = twitter,
                stackoverflow = stackoverflow,
                youtube = youtube,
                googleplus = googleplus,
                disqus = disqus,
                google_analytics = google_analytics
            )
            site_social_profile.save()
            create_config_file(user)

            return HttpResponse('Social data saved')


class SitePluginView(FormView):
    template_name = 'theJekyllProject/siteplugin.html'
    form_class = SitePluginForm

class SiteExcludeView(FormView):
    template_name = 'theJekyllProject/siteexclude.html'
    form_class = SiteExcludeForm


class SiteThemeView(FormView):
    template_name = 'theJekyllProject/sitetheme.html'
    form_class = SiteThemeForm

    def get_form_kwargs(self):
        user = self.request.user
        user = User.objects.get(username=user.username)
        try:
            SiteTheme.objects.get(user=user)
            theme = SiteTheme.objects.get(user=user).theme
        except:
            theme = ''

        form_kwargs = super(SiteThemeView, self).get_form_kwargs()
        form_kwargs.update({
            'initial': {
                'theme': theme,
            }
        })
        return form_kwargs

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            theme = request.POST['theme']
            save_site_theme_data(user, theme)
            create_config_file(user)
            return HttpResponse('THEME SAVED!')

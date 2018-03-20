# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import View

from base.handlers.form_handler import FormHandler

from startbootstrap.forms import SiteProfileForm
from startbootstrap.handlers import StartBootstrapHandler


class StartBootstrapThemeView(LoginRequiredMixin, View):
    """
    First view that will do all preliminary operations for setting up the
    startbootstrap blog.
    """
    def post(self, request, *args, **kwargs):
        """
        Handle the post data. Ideally, reponame will be posted
        """
        user = self.request.user
        form_field_dict = FormHandler(request,
            self.form_class).handle_post_fields(('repo',))

        start_bootstrap = StartBootstrapHandler(user, form_field_dict['repo'])
        start_bootstrap.perform_initial_tasks()
        return HttpResponseRedirect(reverse('site-data'))


class StartBootstrapSiteDataView(LoginRequiredMixin, FormView):
    """
    Form View to handle site data of the startbootstrap theme
    """
    template_name = 'theJekyllProject/siteprofile.html'
    form_class = SiteProfileForm

    def get(self, request, *args, **kwargs):
        user = request.user
        # FIXME Add params for StartBootstrapHandler
        response = StartBootstrapHandler().load_initials(user, self.form_class)

        return render(request, TemplateName.XXXX, {'form': response})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            title = request.POST['title']
            description = request.POST['description']
            avatar = request.POST['avatar']
            # save stuff to the database
            repo = Repo.objects.get(user=user, main=True)
            save_site_data(repo, title, description, avatar)
            create_config_file(user, repo)
            push_online(user, repo)
            return HttpResponseRedirect(reverse('home'))

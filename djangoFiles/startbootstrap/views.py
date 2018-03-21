# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView

from startbootstrap.constants import TemplateName
from startbootstrap.forms import SiteProfileForm
from startbootstrap.handlers.sbs_handlers import SBSHandler


class StartBootstrapThemeView(LoginRequiredMixin, View):
    """
    First view that will do all preliminary operations for setting up the
    startbootstrap blog.
    """
    def post(self, request, *args, **kwargs):
        """
        Handle the post data. Ideally, reponame will be posted
        """
        # TODO test this other wise something is going to be wrong.
        user = self.request.user
        repo = request.data.get('repo')
        start_bootstrap = SBSHandler(user, repo)
        start_bootstrap.perform_initial_tasks()
        return HttpResponseRedirect(reverse('site-data'))


class SBSDataView(LoginRequiredMixin, FormView):
    """
    Form View to handle site data of the startbootstrap theme
    """
    form_class = SiteProfileForm

    def get(self, request, *args, **kwargs):
        response = SBSHandler.load_site_initials(
            request.user, self.form_class)

        return render(request, TemplateName.SBS_SITE_DATA, {'form': response})

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

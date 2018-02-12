# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect

from django.views import View

from oldrepo.handlers.oldrepo_handlers import OldRepoSetUp


class UseOldRepo(LoginRequiredMixin, View):
    """UseOldRepo to register a repo on already created Repository.

    Example:
        Triggers when:
        User clicks on one of the already created repository
        clamining that the repo contains the required files.

    Tasks:
        * View for logged in users only.
        * Select any repo from the repo list
        * Make some earlier checks
        * Clone the repo
        * Check if the required contents are present or not
        * If yes do the required operations:
            * Fill repo table
            * Select Main Site
        * Else give an error message
        * Integrate celery to show the amount of task completed
    """
    def get(self, request, repo_name, *args, **kwargs):
        user = request.user

        # can't send repo object as entry is not in database
        repo_name = self.kwargs['repo_name']
        old_repo_obj = OldRepoSetUp(user, repo_name)
        return_dict = old_repo_obj.use_old_repo()
        if return_dict['message_type'] is 'error':
            messages.error(request, return_dict['message'])
            # FIXME haven't really created URLs for this one
            return HttpResponseRedirect(reverse('old-repo'))
        else:
            messages.success(request, return_dict['message'])
            # FIXME same for this one
            return HttpResponseRedirect(reverse('home'))

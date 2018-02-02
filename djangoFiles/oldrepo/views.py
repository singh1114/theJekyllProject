# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

from oldrepo.handlers.oldrepo import OldRepoHandler


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
    def get(self, request, *args, **kwargs):
        user = request.user

        # can't send repo object as entry is not in database
        repo_name = kwargs['repo_name']
        OldRepoHandler(user, repo_name).use_old_repo()

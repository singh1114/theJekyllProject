# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Contact(models.Model):
    first_name = models.CharField(
        max_length=200
    )
    last_name = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    email = models.EmailField(
        max_length=200,
        null=True,
        blank=True
    )
    message = models.CharField(
        max_length=5000
    )

    def __str__(self):
        return '%s sent message %s' % (self.email, self.message)


class Repo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    repo = models.CharField(
        max_length=200,
    )
    main = models.BooleanField(
        default=False
    )

    def __str__(self):
        return '%s has made %s and is %s' % (self.user, self.repo, self.main)


class CName(models.Model):
    """
    CName model value is used to store the CNAME info of the repo
    """
    repo = models.OneToOneField(
        Repo,
        on_delete=models.CASCADE,
    )
    c_name = models.CharField(max_length=200)


class Post(models.Model):
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE,
    )
    author = models.CharField(max_length=100, null=True, blank=True)
    comments = models.BooleanField(default=True)
    date = models.DateField(auto_now_add=True,)
    time = models.TimeField(auto_now_add=True,)
    layouts = (
        ('post', 'post'),
    )
    layout = models.CharField(
        max_length=100,
        choices=layouts,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=2000)
    slug = models.CharField(max_length=2000, null=True, blank=True)
    content = RichTextField()
    background = models.ImageField(upload_to='pictures/', null=True,
                                   blank=True)

    def __str__(self):
        return '%s on %s' % (self.title, self.date)


class Page(models.Model):
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=2000)
    permalink = models.CharField(max_length=2000)
    layout = models.CharField(max_length=2000)
    content = RichTextField()


class PostCategory(models.Model):
    post = models.ForeignKey(Post)
    category = models.CharField(max_length=200, null=True, blank=True)


class SiteData(models.Model):
    repo = models.OneToOneField(
        Repo,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    title = models.CharField(
        max_length=200,
        default='Your site title',
    )
    description = models.CharField(
        max_length=2000,
        default='Description of the site',
    )
    avatar = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True
    )
    author = models.CharField(
        max_length=2000,
        default='Author of the site',
        null=True,
        blank=True
    )
    baseurl = models.CharField(
        max_length=200,
        default='/jekyllblog',
        null=True,
        blank=True
    )

class SiteSocialProfile(models.Model):
    repo = models.OneToOneField(
        Repo,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    dribbble = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    email = models.EmailField(
        max_length=200,
        null=True,
        blank=True
    )
    facebook = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    flickr = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    github = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    instagram = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    linkedin = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    pinterest = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    rss = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    twitter = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    stackoverflow = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    youtube = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    googleplus = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    disqus = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    google_analytics = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )


class SitePlugin(models.Model):
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE,
    )
    plugin = models.CharField(
        max_length=200,
    )


class SiteExclude(models.Model):
    repo = models.ForeignKey(
        Repo,
        on_delete=models.CASCADE,
    )
    exclude = models.CharField(
        max_length=200,
    )


class SiteTheme(models.Model):
    repo = models.OneToOneField(
        Repo,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    theme = models.CharField(
        max_length=200,
    )

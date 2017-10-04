#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    author = models.CharField(max_length=100, null=True, blank=True)
    comments = models.BooleanField(default=True)
    date = models.DateTimeField()
    layouts = (
        ('post', 'post'),
        ('page', 'page')
    )
    layout = models.CharField(
        max_length=100,
        choices=layouts,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=2000)
    content = RichTextField()

    def __str__(self):
        return self.title + str(self.date)


class PostCategory(models.Model):
    post = models.ForeignKey(Post)
    category = models.CharField(max_length=200, null= True, blank=True)

    def __str__(self):
        return self.category


class SiteData(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(
        max_length=200,
        default='Your site name',
    )
    description = models.CharField(
        max_length=2000,
        default='Description of the site',
    )
    avatar = models.ImageField(
        upload_to='images/',
    )


class SiteSocialProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    dribble = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    email = models.CharField(
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
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    plugin = models.CharField(
        max_length=200,
    )


class SiteExclude(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    exclude = models.CharField(
        max_length=200,
    )


class SiteTheme(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    theme = models.CharField(
        max_length=200,
    )

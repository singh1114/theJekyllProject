# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ckeditor.fields import RichTextField

class Post(models.Model):
    author = models.CharField(max_length=100, null=True, blank=True)
    comments = models.BooleanField()
    date = models.DateField()
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
        return self.title + self.date

class PostCategory(models.Model):
    post = models.ForeignKey(Post)
    category = models.CharField(max_length=200, null= True, blank=True)

    def __str__(self):
        return self.category

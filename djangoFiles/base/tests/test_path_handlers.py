from django.conf import settings

from django.contrib.auth.models import User

from django.test import TestCase

from base.handlers.path_handlers import PathHandler


class TestPathHandler(TestCase):
    def test_path_handlers(self):
        user = User.objects.create_user(username='abc', password='aweqchdufb')
        repo = 'ranvir'
        path = (settings.BASE_DIR + '/../' + 'JekLog' + '/' +user.username +
                '/' +repo)
        self.assertEqual(path, PathHandler(user, repo).create_repo_path)

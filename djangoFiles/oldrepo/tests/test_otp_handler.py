from django.test import TestCase

from oldrepo.handlers.oldrepo import OldRepoSetUp


class TestOldRepoSetUp(TestCase):
    def test_find_in_content(self):
        """
        Test find_in_content method with constant data
        """
        content = OldRepoSetUp.find_in_content(r'name:.+',
                                               'name: JekLog Official Blog')
        self.assertEqual(content, 'JekLog Official Blog')


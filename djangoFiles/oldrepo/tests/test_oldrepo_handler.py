from django.test import TestCase

from oldrepo.handlers.oldrepo import OldRepoSetUp


class TestOldRepoSetUp(TestCase):
    def test_find_in_content(self):
        """
        Test find_in_content method with constant data
        """
        content = OldRepoSetUp.find_in_content(r'name:.+',
                                               'name: JekLog Official Blog')
        self.assertEqual('JekLog Official Blog', content)

    def test_find_multi_line_content(self):
        """
        test mutli line content, multiline content is like:
            exclude:
                - Area
                - README
        """
        file_data = """name: My Blog
        exclude:
              - README
              - bin
              - active
        """
        content = OldRepoSetUp.find_multi_line_content(r'exclude:', file_data)
        return_content = ['README', 'bin', 'active']
        self.assertEqual(return_content, content)

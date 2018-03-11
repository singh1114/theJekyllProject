from base.handlers.file_handler import FileHandler

from theJekyllProject.dbio import CNameDbIO, RepoDbIO
from base.handlers.bash_script import BashScript

from django.conf import settings


class CNameHandler:
    """
    This handler will handle all the operation for the cname
    """
    def __init__(self):
        self.base_dir = settings.BASE_DIR

    def load_initials(self, user, form_class):
        """
        Load the initials from the database
        """
        cname = CNameDbIO().get_obj({'repo': RepoDbIO().get_repo(user)})
        if cname is None:
            return form_class
        return form_class(initial=cname.__dict__)

    def assign_cname(self, user, cname):
        """
        Assign the Cname to the repo
        """
        repo = RepoDbIO().get_repo(user)
        cname_obj = CNameDbIO().get_obj({'repo': repo})
        if cname_obj is None:
            CNameDbIO().create_obj({'repo': repo, 'c_name': cname})
        else:
            CNameDbIO().update_obj(cname_obj, {'c_name': cname})
        self.write_to_file(user, repo.repo, cname)
        BashScript().push_online(user, repo)

    def write_to_file(self, user, repo_name, cname):
        """
        Writes the CNAME content to the file
        """
        file_path = '/'.join([self.base_dir, '..', 'JekLog',
                              user.username, repo_name])
        FileHandler(file_path, 'CNAME').rewrite_file(cname)

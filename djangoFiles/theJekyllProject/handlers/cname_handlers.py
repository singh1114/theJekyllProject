from base.handlers.file_handlers import FileHandler

from theJekyllProject.dbio import CNameDbIO, RepoDbIO


class CNameHandler:
    """
    This handler will handle all the operation for the cname
    """
    def __init__(self):
        pass

    def load_initials(self, user, form_class):
        """
        Load the initials from the database
        """
        # FIXME What if the cname is empty
        cname = CNameDbIO().get_or_filter({'repo': RepoDbIO().get_repo(user)})
        return form_class(initial=cname.__dict__)

    def assign_cname(self, user, cname):
        """
        Assign the Cname to the repo
        """
        # FIXME same error will be encountered
        repo = RepoDbIO().get_repo(user)
        cname_obj = CNameDbIO().get_or_filter({'repo': repo})
        if cname is '':
            CNameDbIO().create_obj({'repo': repo, 'c_name': cname})
        else:
            CNameDbIO().update_obj(cname_obj, {'c_name': cname})

        return self.write_to_file(cname)

    def write_to_file(self, cname):
        """
        Writes the CNAME content to the file
        """
        file_path = '/'.join([self.base_dir, '..', 'JekLog',
                              self.user.username, self.repo_name])
        FileHandler(file_path, 'CNAME').write_full_file(cname)

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

    def assign_cname(self, user):
        """
        Assign the Cname to the repo
        """
        # FIXME same error will be encountered
        cname = CNameDbIO().get_or_filter({'repo': RepoDbIO().get_repo(user)})
        if cname is '':
            CNameDbIO().create_or_update({})

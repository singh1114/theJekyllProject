from theJekyllProject.DbIO import CNameDbIO, RepoDbIO


class CNameHandler:
    """
    This handler will handle all the operation for the cname
    """
    def __init__(self):
        pass

    def load_initials(self, user, form_class):
        repo = RepoDbIO().get_repo(user)
        form = CNameDbIO().get_or_filter({'repo': repo})
        return form_class(**form)

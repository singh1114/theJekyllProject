from theJekyllProject.dbio import RepoDbIO, SiteDataDbIO


class InitialFormHandler:
    def __init__(self, user, form_class):
        self.user = user
        self.form_class = form_class

    def load_jn_site_initials(self):
        repo = RepoDbIO().get_repo(self.user)
        site_data = SiteDataDbIO().get_obj({'repo': repo})
        if site_data:
            return self.form_class(initial=site_data.__dict__)
        return self.form_class

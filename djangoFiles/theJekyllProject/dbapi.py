from theJekyllProject.models import Repo

class RepoDbIO:
    def __init__(self):
        self.model_name = Repo

    def create_repo_main_true(self, user, repo_name):
        self.model_name.objects.create(user=user, repo=repo_name, main=True)

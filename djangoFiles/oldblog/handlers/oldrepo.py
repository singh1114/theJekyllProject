from django.conf.settings import BASE_DIR


class OldRepoHandler:
	
	def __init__(self, user, repo_name):
		self.user = user
		self.repo = repo

	def early_checks(self):
		"""
		Make some earlier checks about the code.
		"""
		return True

	def git_clone_repo(self):
    """git_clone_repo to clone the already created Repository.

    Example:
        Triggers when:
        User clicks on one of the already created repository
        clamining that the repo contains the required files.

    Tasks:
        * Works for a logged in user
        * clone the repository to particular path
    """
    path = BASE_DIR + '/../' + 'JekLog/' + self.user.username
    url = 'https://github.com/' + self.user.username + '/' + self.repo_name
    subprocess.call(['git', 'clone', url, path])


	def find_required_files(self):
	    """find_required_files to find particular files in the cloned repo.

	    Example:
	        Triggers when:
	        User clicks on one of the already created repository
	        clamining that the repo contains the required files.
	        After the repo is cloned this function is triggered

	    Tasks:
	        * Try to find the main files.
	    """
	    path = BASE_DIR + '/../' + 'JekLog/' + self.user.username + '/' + self.repo_name
	    files = os.listdir(path)
	    temp = 0
	    for file in files:
	        if(file == '_config.yml'):
	            temp = temp + 1
	        elif(file == '_posts'):
	            temp = temp + 1
	    if(temp == 2):
	        return True
	    else:
	        return False


	def fill_repo_table_for_old_repo(self):
	    """fill_repo_table_for_old_repo to fill the database for choosen old repo.

	    Example:
	        Triggers when:
	        User clicks on one of the already created repository
	        clamining that the repo contains the required files.
	        After checking of required files this function is triggered.

	    Tasks:
	        * Fill Repo table
	    """
	    repo = Repo(user=self.user, repo=self.repo_name)
	    repo.save()
	    return repo


	def fill_other_tables_from_config_file(username, repo_name):
	    """fill_repo_table_for_old_repo to fill the database for choosen old repo.

	    Example:
	        Triggers when:
	        User clicks on one of the already created repository
	        clamining that the repo contains the required files.
	        After checking of required files this function is triggered.

	    Tasks:
	        * Fill Repo table
	    """

		
	def use_old_repo(self):
		"""
		Tasks:
        * View for logged in users only.
        * Select any repo from the repo list
        * Make some earlier checks
        * Clone the repo
        * Check if the required contents are present or not
        * If yes do the required operations:
            * Fill repo table
            * Select Main Site
        * Else give an error message
        * Integrate celery to show the amount of task completed
        """
        git_clone_repo(user.username, repo_name)
        if(find_required_files(user.username, repo_name)):
            repo = fill_repo_table_for_old_repo(user.username, repo_name)
            select_main_site(user, repo.pk)
            fill_other_tables_from_config_file(user.username, repo_name)
            find_posts(user.username, repo_name)
            find_pages(user.username, repo_name)
            

        else:
            pass # or give errors
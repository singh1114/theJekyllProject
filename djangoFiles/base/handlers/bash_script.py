import subprocess

from django.conf import settings


class BashScript:
    def __init__(self):
        pass

    def push_online(self, user, repo):
        base_dir = settings.BASE_DIR
        path = '/'.join([base_dir, '..', 'gitsendupstream.sh'])
        task = subprocess.Popen(['/bin/bash', path, user.username, repo.repo,
                                base_dir])
        if task.returncode != 0:
            raise BaseException({'message': 'push error'})

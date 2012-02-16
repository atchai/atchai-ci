from fabric.context_managers import cd
from fabric.context_managers import settings
from fabric.operations import run

class deploy:
    def __init__(self, path, repo, public_path='/public',
                 db_user='test', db_pass='test', db_host='localhost', db_name='test',
                 admin_user='Admin', admin_pass='password', site_name='Test'):
        self.public = path + public_path
        self.pull(path, repo)
        self.install(db_user, db_pass, db_host, db_name, site_name, admin_user, admin_pass)

    def install(self, db_user, db_pass, db_host, db_name, site_name, admin_user, admin_pass):
        self.drush('si minimal --db-url=mysql://%s:%s@%s/%s --site-name="%s" --account-name="%s" --account-pass="%s"'
            % (db_user, db_pass, db_host, db_name, site_name, admin_user, admin_pass,), False)

    def pull(self, path, repo):
        with settings(warn_only=True):
            if run('test -d %s/.git' % path).failed:
                run('git clone %s %s' % (repo, path,))
        run('cd %s; git pull' % path)

    def drush(self, cmd, ignore_error=True):
        with settings(warn_only=ignore_error):
            run('drush --root="%s" %s -y' % (self.public, cmd,))

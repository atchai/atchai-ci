from fabric.context_managers import cd
from fabric.context_managers import settings
from fabric.operations import run

def deploy(repo='', path='/var/www/test',
           db_user='test', db_pass='test', db_host='localhost', db_name='test',
           admin_user='Admin', admin_pass='password', site_name='Test'):
    pull(repo, path)
    install(db_user, db_pass, db_host, db_name, admin_user, admin_pass, site_name)

def pull(repo, path):
    with settings(warn_only=True):
        if run('test -d %s/.git' % path).failed:
            run('git clone %s %s' % (repo, path,))
    run('git pull')

def install(path, db_user, db_pass, db_host, db_name, admin_user, admin_pass, site_name):
    run('drush --root="%s/public" si minimal --db-url=mysql://%s:%s@%s/%s --site-name="%s" --account-name="%s" --account-pass="%s" -y'
        % (path, db_user, db_pass, db_host, db_name, site_name, admin_user, admin_pass,))

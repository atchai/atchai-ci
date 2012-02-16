from fabric.state import env
import drupal

def prod():
    env['repo_path'] = '/var/www/drupal';
    env.hosts = ['example.com']

def test():
    env['repo_path'] = '/var/www/test';
    env.hosts = ['example.com']

def dev():
    env['repo_path'] = '/var/www/drupal';
    env.hosts = ['localhost']

def deploy():
    deploy = drupal.deploy(path=env['repo_path'], repo='git://github.com/example/example.git')
    deploy.drush('en example')

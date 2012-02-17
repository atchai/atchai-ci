from fabric.state import env
import drupal

def prod():
    env['repo_url'] = 'git://github.com/example/example.git'
    env['repo_path'] = '/var/www/drupal'
    env['url'] = 'http://example.com/'
    env['hosts'] = ['example.com']

def test():
    prod()
    env['repo_path'] = '/var/www/test'
    env['url'] = 'http://test.example.com/'

def dev():
    prod()
    env['repo_path'] = '/var/www/drupal'
    env['url'] = 'http://localhost/'
    env['hosts'] = ['localhost']

def deploy():
    deploy = drupal.deploy(env['repo_path'], env['repo_url'])
    deploy.install()
    deploy.drush('en example')

def run_tests():
    deploy = drupal.deploy(env['repo_path'], env['repo_url'])
    deploy.test(env['url'])

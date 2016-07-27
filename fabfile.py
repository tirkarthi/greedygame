# -*- coding: utf-8 -*-
from fabric.api import *
from contextlib import contextmanager as _contextmanager
import os

AWS_KEY_PATH = os.environ.get('AWS_DEPLOYMENT_KEY_PATH', '')

if AWS_KEY_PATH:
    if not os.path.isfile(AWS_KEY_PATH):
        raise Exception("Key file doesn't exists")
else:
    raise Exception('Deployment key path not found')

env.hosts = ['52.24.90.19']
env.user = 'ubuntu'
env.key_filename = AWS_KEY_PATH
env.activate = 'source /home/ubuntu/greedygame_env/bin/activate'
env.directory = '/home/ubuntu/greedygame/'


def change_source():
    run('cd /home/ubuntu/greedygame/')


def activate_virtualenv():
    run('source /home/ubuntu/greedygame_env/bin/activate')


def install_requirements():
    run('pip install -r requirements.txt')

def pull():
    run('git pull origin master')

def migrate():
    run('python manage.py migrate')

def get_gunicorn_pid():
    with settings(warn_only=True):
        result = sudo('supervisorctl pid greedygame')
        if result.return_code == 0:
            try:
                pid = int(str(result))
                return pid
            except:
                return None
        return None


def reload_gunicorn(pid):
    with settings(warn_only=True):
        result = run('kill -HUP %s' % (pid))
        if result.return_code != 0:
            start_gunicorn()


def start_gunicorn():
    sudo('supervisorctl restart greedygame')

# http://stackoverflow.com/questions/1180411/activate-a-virtualenv-via-fabric-as-deploy-user
@_contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield

def deploy():
    with virtualenv():
        pull()
        install_requirements()
        migrate()
        pid = get_gunicorn_pid()
        if pid:
            reload_gunicorn(pid=pid)
        else:
            start_gunicorn()

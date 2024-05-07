#!/usr/bin/python3
"""
Fabric script to archive, send and deploy codefiles
"""

from fabric.api import env
from fabric.operations import local, put, run
from datetime import datetime
import os

env.hosts = ['3.85.168.64', '18.210.20.122']


def do_pack():
    """Archive the web_static files"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    the_tgz_archive = "web_static_" + timestamp + ".tgz"
    result = local("tar -cvzf versions/{} web_static".format(the_tgz_archive))
    if result.return_code == 0:
        return os.path.abspath("versions/{}".format(the_tgz_archive))
    else:
        return None


def do_deploy(archive_path):
    """Deploys all the codefiles to the webserver."""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = os.path.basename(archive_path)
        folder_name = filename.split('.')[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, folder_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, folder_name))
        run('rm /tmp/{}'.format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, folder_name))
        return True
    except Exception as err:
        print(err)
        return False


def deploy():
    """Create and distribute an archive to web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

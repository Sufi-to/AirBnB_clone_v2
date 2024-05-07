#!/usr/bin/python3
"""A fabric module for deploying code files."""
from datetime import datetime
import os
from fabric.api import env, put, local, runs_once, run


env.hosts = ["3.85.168.64", "18.210.20.122"]\
@runs_once
def do_pack():
    """Archives the webstatic files """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
    )
    try:
        local("tar -cvzf {} web_static".format(output))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """Deploys the static files to the host servers."""
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success


def deploy():
    """Archives and deploy the all the files"""
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    else:
        False


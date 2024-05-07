#!/usr/bin/python3
"""
script that creates and distributes an archive to my
my web servers using the function deploy
"""
from datetime import datetime
from os import path
from fabric.api import env, local, put, run

env_hosts = ['3.85.168.64', '18.210.20.122']


def do_pack():
    """make a tar gzipped archive of the web_static folder"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    cr_file = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(time.year,
                                                            time.month,
                                                            time.day,
                                                            time.minute,
                                                            time.second)
    if path.isdir('versions') is False:
        if local ("mkdir -p versions").failed is True:
            return None
        


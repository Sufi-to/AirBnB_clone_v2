#!/usr/bin/python3
"""
script that generates .tgz archive from the contents of web_static using fabric
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """making an archive of the web_static folder in the airbnb repo"""
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    arch = 'web_static_' + time_now + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(arch))
    if create is not None:
        return arch
    else:
        return None

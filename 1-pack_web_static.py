#!/usr/bin/python3
"""
A fabric script that generates archive files from web_static
using task 'do_pack' with relative time'
"""

from datetime import datetime
from fabric.api import *


@task
def do_pack():
    """
    A fuction that creates archive using fabric methods
    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    local('mkdir versions')

    results = local('tar -czvf versions/{} web_static'.format(archive))
    if results is None:
        return None
    else:
        return archive

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

    local('mkdir -p versions')

    archive_path = f"versions/{archive}"

    results = local('tar -czvf {} web_static'.format(archive_path))
    if results is None:
        return None
    else:
        archive_size = os.path.getsize(archive_path)
        print(f"web_static packed: {archive_path} -> {archive_size}Bytes")
        return archive

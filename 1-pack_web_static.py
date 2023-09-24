#!/usr/bin/python3
"""Using the fabric api
"""
from fabric.api import local
from datetime import datetime
import time


def do_pack():
    """generates a .tgz archive
    Returns:
    [the archive path]: [he archive has been correctly generated]
    """
    clocktime = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")

    try:
        local('mkdir -p versions')
        localtar = local(
            'tar -czvf versions/web_static_{}.tgz web_static/'.format(
                clocktime), capture=True)
        return (localtar)
    except Exception:
        return None

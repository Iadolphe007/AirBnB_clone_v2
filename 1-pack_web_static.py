#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from fabric.api import task, local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the
    contents of the web_static folder
    Returns:
        Path to the archive if successful, None otherwise
    """
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(timestamp)
    print('Packing web_static to {}'.format(path))
    if local('{} && tar -cvzf {} web_static'.format(mkdir, path)).succeeded:
        return path
    return None

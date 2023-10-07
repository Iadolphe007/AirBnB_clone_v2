#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['52.86.110.104', '34.204.95.100']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """
    Distribute an archive to web servers
    Args:
        archive_path: Path to the archive file on the local machine
    Returns:
        True if all operations are successful, otherwise False
    """
    try:
        if not os.path.exists(archive_path):
            return False
        exit_fun = os.path.basename(archive_path)
        no_exit_fun, ext = os.path.splitext(fn_with_ext)
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("rm -rf {}{}/".format(path, no_exit_fun))
        run("mkdir -p {}{}/".format(path, no_extit_fun))
        run("tar -xzf /tmp/{} -C {}{}/".format(exit_fun, path, no_exit_fun))
        run("rm /tmp/{}".format(exit_fun))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_exit_fun))
        run("rm -rf {}{}/web_static".format(path, no_exit_fun))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_exit_fun))
        print("New version deployed!")
        return True
    except Exception:
        return False

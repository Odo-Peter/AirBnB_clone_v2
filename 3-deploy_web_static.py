#!/usr/bin/python3
""" module automating full deployment"""
from os.path import isfile
from fabric.api import *
from fabric.operations import run, local, put, sudo
from datetime import datetime
import time

env.user = 'ubuntu'
env.hosts = ['54.237.13.102', '34.204.82.139']


def do_pack():
    """compresses a file for deployment
    """
    clocktime = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    try:
        local('mkdir -p versions')
        localtar = local(
            'tar -czvf versions/web_static_{}.tgz web_static/'.format(
                clocktime), capture=True)
        return (localtar)
    except Exception as e:
        return None


def do_deploy(archive_path):
    """deploys and transfers all files to the server
    """
    if isfile(archive_path):
        put(archive_path, "/tmp/")
        archive_file = archive_path.split("/")[-1]
        folder_file = "/data/web_static/releases/" + archive_file.split(".")[0]
        sudo("mkdir -p {:s}".format(folder_file))
        sudo("tar -xzf /tmp/{:s} -C {:s}".format(archive_file, folder_file))
        sudo("rm /tmp/{:s}".format(archive_file))
        sudo("mv {:s}/web_static/* {:s}/".format(folder_file, folder_file))
        sudo("rm -rf {:s}/web_static/".format(folder_file))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {:s} /data/web_static/current".format(folder_file))
        print("New version deployed!")
        return True
    else:
        return False


def deploy():
    """deploys the final deployment
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    else:
        deploy = archive_path.__dict__["command"].split(" ")[2]
        return do_deploy(deploy)

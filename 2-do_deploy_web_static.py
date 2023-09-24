#!/usr/bin/python3
""" module for deployment of archives"""
from os.path import isfile
from fabric.api import *
from fabric.operations import run, local, put, sudo
from datetime import datetime
import time

env.user = 'ubuntu'
env.hosts = ['54.237.13.102', '34.204.82.139']


def do_deploy(archive_path):
    """deploys and transfers files
       via archive_path
    """
    if isfile(archive_path):
        put(archive_path, "/tmp/")
        archive = archive_path.split("/")[-1]
        folder = "/data/web_static/releases/" + archive.split(".")[0]

        sudo("mkdir -p {:s}".format(folder))
        sudo("tar -xzf /tmp/{:s} -C {:s}".format(archive, folder))
        sudo("rm /tmp/{:s}".format(archive))
        sudo("mv {:s}/web_static/* {:s}/".format(folder, folder))
        sudo("rm -rf {:s}/web_static/".format(folder))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {:s} /data/web_static/current".format(folder))
        print("New version deployed!")
        return True
    else:
        return False

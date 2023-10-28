#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" create_repo.py


"""

import os
import re
import sys

BASEDIR=os.path.abspath(os.path.dirname(__file__)) + "/"

def main():
    repo = sys.argv[1]

    user = None
    if "USER" in os.environ:
        user = os.environ["USER"]
    elif "USERNAME" in os.environ:
        user = os.environ["USERNAME"]

    if len(sys.argv) >= 3:
        user = sys.argv[2]

    # create repository directory
    os.mkdir(repo)

    # cd to repo
    os.chdir(repo)

    # git init
    os.system("git init")

    # gitignore
    os.system("curl -Ssl 'https://www.gitignore.io/api/vim,emacs,visualstudiocode' > .gitignore")

    # create docker-compose directory
    os.mkdir("docker_%s" % repo)

    # create docker-compose.yml
    render(
        "%s/template/docker-compose.yml" % BASEDIR,
        "docker_%s/docker-compose.yml" % repo, user, repo)
    
    # create docker directory
    os.mkdir("docker_%s/%s" % (repo, repo))

    # create Dockerfile
    render(
        "%s/template/Dockerfile" % BASEDIR,
        "docker_%s/%s/Dockerfile" % (repo,repo), user, repo)

    # create LICENSE
    render("%s/template/LICENSE" % BASEDIR, "LICENSE" , user, repo)

    # create README.md
    render("%s/template/README.md" % BASEDIR, "README.md" , user, repo)
    
    # git remote add
    os.system("git remote add origin https://github.com/%s/%s.git" % (user, repo))    

def render(ifn, ofn, user, repo):

    ifp = open(ifn)
    ofp = open(ofn, "w")
    
    for line in ifp:
        buf = line

        buf = buf.replace("%user%", user)

        buf = buf.replace("%repo%", repo)
        buf = buf.replace("%_repo_%", repo.replace("-","_"))
        buf = buf.replace("%-repo-%", repo.replace("_","-"))

        ofp.write(buf)

    ifp.close()
    ofp.close()
    
if __name__ == "__main__":
    main()

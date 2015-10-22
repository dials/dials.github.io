#!/bin/python

import getpass
from libtbx import easy_run

usermap = {
  'david': 'upintheair',
  'fcx32934': 'upintheair',
  'rjgildea': 'rjgildea',
  'hko55533': 'rjgildea',
  'sauter': 'nksauter',
}

username = getpass.getuser()
sf_username = usermap.get(username)

assert sf_username is not None, "No sourceforge username found for $USER. Have you added your details to this script?"

easy_run.call("ssh %s,dials@shell.sourceforge.net create" %sf_username)
easy_run.call("ssh %s,dials@shell.sourceforge.net /home/project-web/dials/update.sh" %sf_username)
easy_run.call("ssh %s,dials@shell.sourceforge.net shutdown" %sf_username)

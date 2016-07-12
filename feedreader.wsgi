#!/usr/bin/python

import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/root/flask_apps/feedreader/")

from feedreader import app as application

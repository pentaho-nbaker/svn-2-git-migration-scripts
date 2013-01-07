#!/usr/bin/env python
__author__ = 'nbaker'
import json
import urllib
import urllib2
import os
import commands
import sys
import logging
from base64 import encodestring


logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

if (len(sys.argv) < 2):
    logging.error("backup location not specified")
    sys.exit(-1)

logging.info('Starting backup')
#backup_location = os.getenv('HOME') + "/temp/backups"
backup_location = sys.argv[1]
logging.info("backup_location: "+backup_location)

try:
  if not os.path.exists(backup_location):
      os.makedirs(backup_location)

  url = 'https://api.github.com/orgs/pentaho/repos'

  request = urllib2.Request(url)
  request.add_header('Authorization', 'Basic %s' % "cGVudGFob2FkbWluOnp6MXFTR1ZH".replace('\n', ''))
  res = urllib2.urlopen(request)
  data = res.read();

  repos = json.loads(data);

  # print repos
  for r in repos:
    name = r['name']
    url = "git@github.com:%s.git" % r['full_name']
    logging.info(url)

    repoLocation  = backup_location + os.sep + name;
    if not os.path.exists(repoLocation):
      logging.info('cloning: ' + name)
      result = commands.getoutput('git clone --bare ' +url + ' ' + repoLocation)
      logging.info('output => '+result)
    else:
      logging.info('fetching: ' + name)
      os.chdir(repoLocation)
      result = commands.getoutput('git fetch origin')
      logging.info('output => '+result)
  logging.info('Backup Complete')
except Exception as e:
  logging.error('Error encountered in backup: ' + e.message)
  sys.exit(-1)

sys.exit(1)
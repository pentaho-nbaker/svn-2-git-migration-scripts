#!/usr/bin/env python
__author__ = 'nbaker'
import json
import urllib
import os
import commands
import sys
import logging


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
  u = urllib.urlopen(url)
  data = u.read();
  repos = json.loads(data);
  for r in repos:
    name = r['name']
    url = r['clone_url']
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
import sys
import re
import collections

def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

authors = {}
lineNo = 0
for line in open('authors.txt', 'rb'):
    lineNo = lineNo + 1
    parts = re.search('([^=]+)=(.+)', line)
    #print 'author '+parts[0]
    name = parts.group(1).strip().lower()
    email = parts.group(2).strip()
    #print '{0} = {1}'.format(name, email)
    existingEmail = authors.get(name)
    if existingEmail:
        print '{0} {1} at line {2}'.format(name, email, lineNo)
        if email.strip().lower() != existingEmail.strip().lower():
            # Prefer non-pentaho email
            if email.find("@pentaho.com") > -1 and existingEmail.find("@pentaho.com") == -1:
                authors[name] = email
            # Prefer longer email
            elif len(email) > len(existingEmail):
                authors[name] = email
            
    else:
        authors[name.lower()] = email

fil = open('authors.txt', 'w')
for name, email in collections.OrderedDict(sorted(authors.items())).iteritems():
    fil.write(name + " = " + email+'\n')


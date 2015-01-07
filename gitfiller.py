import datetime
import os
import time
from email.Utils import formatdate
import subprocess

commitdate = datetime.datetime.today() - datetime.timedelta(days=365)
now = datetime.datetime.today()

while commitdate < now:
	com = commitdate
	for _ in range(15):
		#make changes
		with open('DATE','w') as f:
			f.write(str(commitdate))
		#prepare environment variables
		cds = formatdate(time.mktime(commitdate.timetuple()))
		os.environ['GIT_AUTHOR_DATE'] = cds
		os.environ['GIT_COMMITTER_DATE'] = cds
		#git commit
		subprocess.call(['git', 'add', '.'])
		subprocess.call(['git', 'commit', '-m', 'A random change done '+cds])
		commitdate += datetime.timedelta(seconds=13)
	commitdate = com + datetime.timedelta(days=8)


import os
import sys
level=1
opdir=sys.argv[1]
if os.path.split(sys.argv[1])[1]=='':
	opdir=os.path.split(sys.argv[1])[0]


def checker(pwd):
	print os.path.split(pwd)
 	global level
	for dirpath, dirs, files in os.walk(pwd):
		print "-"*level+os.path.basename(dirpath)
		for file in files:
			print "-"*level+file
		level=level+1
		
checker(opdir)

#!/usr/bin/env python

import os

def child_process():
	print "I am the child process and my pid is %d"%os.getpid()

	print "the child is exiting"

def parent_process():
	print "I am the parent process%d"%os.getpid() 
	"""
	 os.fork() inside parent process it returns the pid of the child and
	 inside the child process it returns the value 0
	"""
	childpid = os.fork() 
	
	if childpid == 0 :
		#we are inside the child
		child_process()
	else:
	        #we are inside the parent process
		print "Our child has the pid %d"%childpid
	while True:
		pass

parent_process()


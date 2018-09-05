#!/usr/bin/python


import commands
import time
import json
import re
LOG_FILE="/root/cephstatus1.log"
def get_ceph_status():
	(status,output) = commands.getstatusoutput('ceph status -f json')
	
	output = output.replace("false","False")
	output = output.replace("true","True")
	output = eval(output)
	'''print output["pgmap"]["num_pgs"]
	print type(output["pgmap"]["num_pgs"])
	print output["pgmap"]["pgs_by_state"]'''

	print output
	print "\n\n\n"
	for (k,v) in output.items():
		print k
		print v
		print "\n"
		
	'''f = open(LOG_FILE,'a')
	pginfo = str(output['pgmap'])
	f.write(pginfo)
	f.write('\n\n')
	f.close()
	#print output['pgmap']'''
	

if __name__ == "__main__":
	get_ceph_status()

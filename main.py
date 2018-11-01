# 11/01/2018
# Justin Privitera
# Schedule Planner
# v1.1
#
# Version History:
# 10/31/2018	v1.0	added basic functionality
# 11/01/2018	v1.1	updated command line args so that they are optional; additionally added a feauture so that the user can limit the results by choosing a number of classes to view
#
# The purpose is to replace PASS with a superior scheduling applet, with greater functionality and options.
#
# run the program with the following command: "python3 main.py"

import sys

from Scheduler import scheduler

if len(sys.argv) > 3:
	print("Too many parameters supplied")
elif len(sys.argv) >= 2:
	if len(sys.argv) == 3:
		scheduler(int(sys.argv[1]), sys.argv[2])
	else:
		scheduler(int(sys.argv[1]))
else:
	scheduler()

# 11/02/2018
# Justin Privitera
# Schedule Planner
# v1.3
#
# Version History:
# 10/31/2018	v1.0	added basic functionality
# 11/01/2018	v1.1	updated command line args so that they are optional; additionally added a feauture so that the user can limit the results by choosing a number of classes to view
# 11/01/2018	v1.2	added ability to curate further by putting in the inFile a certain imperative class such that all results must contain that class.
#						further added to this feature by allowing the user to choose one class or another to apply the feature to
# 11/02/2018	v1.3	removed ability to view all results containing one class OR another and replaced it with viewing all results containing one class AND another
#
# The purpose is to replace PASS with a superior scheduling applet, with greater functionality and options.
#
# run the program with the following command: "python3 main.py" or "make" or "make run"

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

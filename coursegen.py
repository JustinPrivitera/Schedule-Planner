#!/bin/env/python3

for x in range(600):
	print("http://schedules.calpoly.edu/classes_CSC-%.3d_next.htm" % x)
	print("http://schedules.calpoly.edu/classes_CHIN-%.3d_next.htm" % x)
	print("http://schedules.calpoly.edu/classes_EE-%.3d_next.htm" % x)
	print("http://schedules.calpoly.edu/classes_CPE-%.3d_next.htm" % x)
	print("http://schedules.calpoly.edu/classes_MATH-%.3d_next.htm" % x)
	print("http://schedules.calpoly.edu/classes_MU-%.3d_next.htm" % x)
	print("http://schedules.calpoly.edu/classes_STAT-%.3d_next.htm" % x)
	print("http://schedules.calpoly.edu/classes_DATA-%.3d_next.htm" % x)
	print("http://schedules.calpoly.edu/classes_PHIL-%.3d_next.htm" % x)
	print("http://schedules.calpoly.edu/classes_PHY-%.3d_next.htm" % x)
	print("http://schedules.calpoly.edu/classes_ART-%.3d_next.htm" % x)
	if(x % 30 == 0 and x > 25):
		print("echo \"Progress: %d%%\"" % (x / 6))

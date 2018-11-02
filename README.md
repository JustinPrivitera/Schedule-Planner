# Schedule-Planner
A replacement for PASS.
INCOMPLETE

run with the following command: "python3 main.py {numClasses} {inFile}" or "make" or "make run"
both of the parameters are optional

--------
in inFile, separate imperatives with '#'. Separate all other information with tabs and newlines. example:
#class1#class2#class3
class1	12	13
class2	14	16
class3	16	17
class4	16	19

--------

for now, it has basic functionality, and runs with no errors.
still need to add:
	- days of the week, and thus a much more complicated time scheme
	- a method of putting in classes as either/or - this could be accomplished by simply limiting the output to the number of classes one wishes to take
	- format the results in a way that is conducive to schedule planning
		- you can choose a class or classes to be imperative, meaning that only schedules containing that class can be displayed
	- printScheduleList() needs to be redone, probably build a large string before printing

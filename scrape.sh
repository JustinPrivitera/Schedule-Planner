#!/bin/sh

rm -rf scraped
rm -rf happydatabase
mkdir -p happydatabase

python3 coursegen.py > happydatabase/courseurls.txt

cd happydatabase
cat courseurls.txt | sed -r 's;(http://schedules.calpoly.edu/classes_)(...-[0-9][0-9][0-9])(_next.htm);wget -O \2.htm "\1\2\3";' | bash
find . -size  0 -print0 |xargs -0 rm --


# wget -O cpe101.htm "http://schedules.calpoly.edu/classes_CPE-101_next.htm"
# python ../html2csv.py cpe101.htm

# wget -O csc349.htm "http://schedules.calpoly.edu/classes_CSC-349_next.htm"
# python ../html2csv.py csc349.htm

# ls *.csv

# echo ""

# cat *.csv



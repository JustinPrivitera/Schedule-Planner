#!/bin/sh

rm -rf scraped
rm -rf happydatabase
mkdir -p happydatabase

python3 coursegen.py > happydatabase/courseurls.txt

cd happydatabase
cat courseurls.txt | sed -r 's;(http://schedules.calpoly.edu/classes_)(...-[0-9][0-9][0-9])(_next.htm);curl -o \2.htm "\1\2\3";' > coursescript.sh
# source coursescript.sh
# find . -size 0 -delete
# ls *.htm | xargs python ../html2csv.py



# wget -O cpe101.htm "http://schedules.calpoly.edu/classes_CPE-101_next.htm"
# python ../html2csv.py cpe101.htm

# wget -O csc349.htm "http://schedules.calpoly.edu/classes_CSC-349_next.htm"
# python ../html2csv.py csc349.htm

# ls *.csv

# echo ""

# cat *.csv



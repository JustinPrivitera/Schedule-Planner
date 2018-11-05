#!/bin/sh


mkdir -p happydatabase

python3 coursegen.py > happydatabase/courseurls.txt

cd happydatabase
cat courseurls.txt | sed -r 's;(http://schedules.calpoly.edu/classes_)(.*-[0-9]*)(_next.htm);curl -o \2.htm "\1\2\3";' > coursescript.sh
bash coursescript.sh
ls *.htm | xargs -L 1 bash ../deleteif404.sh
ls *.htm | xargs -L 1 python ../html2csv.py


# find . -size 0 -delete
# ls *.htm | xargs python ../html2csv.py



# wget -O cpe101.htm "http://schedules.calpoly.edu/classes_CPE-101_next.htm"

# wget -O csc349.htm "http://schedules.calpoly.edu/classes_CSC-349_next.htm"
# python ../html2csv.py csc349.htm

# ls *.csv

# echo ""

# cat *.csv



#!/bin/sh


mkdir -p happydatabase

python3 coursegen.py > happydatabase/courseurls.txt

cd happydatabase
cat courseurls.txt | sed -r 's;(http://schedules.calpoly.edu/classes_)(.*-[0-9]*)(_next.htm);curl -o \2.htm "\1\2\3" \&> dl.tmp ;' > coursescript.sh

echo "Pinging schedules.calpoly.edu"

bash coursescript.sh

wait

echo "Finished pinging, purging invalid courses"

ls *.htm | xargs -L 1 bash ../deleteif404.sh 
wait

echo "Converting pages to csv's"
ls *.htm | xargs -L 1 python ../html2csv.py > /dev/null
wait
# echo "Here are the availible courses:"
# cat *.csv | xargs -L 1 echo | python3 ../ezsplit.py 
wait


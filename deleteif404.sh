
cat $1 | grep "The page you are looking for is not available." &> dl.tmp

if [ $? -eq 0 ]; then
    rm $1
else
	echo "" > /dev/null
fi




cat $1 | grep "The page you are looking for is not available."

if [ $? -eq 0 ]; then
    echo OK
    rm $1
else
    echo FAIL
fi



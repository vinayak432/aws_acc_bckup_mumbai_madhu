#!/bin/bash

echo "enter the file to count"
read filename
i=1
while read line
do 
	count=`echo $line | wc -c`
	echo "the no of character in line $i is $count"
	i=`expr $i + 1`
done < $filename


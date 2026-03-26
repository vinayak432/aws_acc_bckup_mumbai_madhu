#!/bin/bash

echo "enter the filename"
read filename
i=1
while read line
do
	count=`echo $line | wc -c`
	echo "the no of characters in line $i is $count"
	i=`expr $i + 1`
done < $filename

#!/bin/bash

echo "enter the filename"
read filename
i=1
while read line
do
	word=`echo $line | wc -w`
	echo "No of letters in line $i is $word"
	i=`expr $i + 1`

done < $filename

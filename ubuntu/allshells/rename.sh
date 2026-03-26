#!/bin/bash

ls *.txt > out1

while read line
do
	name=`expr $line | awk -F "." '{print $1}'`
	mv $name.txt $name.html
done < out1
ls *.html

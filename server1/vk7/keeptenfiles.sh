#!/bin/bash

list=`ls -lrt | awk -F " " 'NR>2 {print $NF}' > output`
file=`cat output`
echo "name of files are $file"

equ1=`wc -l output`
echo "total no of files/dir are $equ1"
#while read line
#do
if [ $equ1 -gt 10 ]
then
echo "last 10 files created are "
else 
	del=`ls -l
delete=`head $equ1 output`
echo "lines are $delete"


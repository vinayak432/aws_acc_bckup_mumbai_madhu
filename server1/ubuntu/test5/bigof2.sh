#!/bin/bash

#echo "enter the num1"
#read num1
#echo "enter the num2"
#read num2

if [ $1 -gt $2 ] && [ $1 -gt $3 ]
then
	echo "$1 is greater than $2 & $3"
elif [ $2 -gt $3 ] && [ $2 -gt $1 ]
then
	echo "$2 is greater than $1 & $3"
else
	echo "$3 is gt $1 & $2"
fi

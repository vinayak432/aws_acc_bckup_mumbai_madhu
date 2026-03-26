#!/bin/bash

if [ $# -ne 3 ]
then
echo "enter the three arguements"
exit 1
fi
if [ $1 -gt $2 ] && [ $1 -gt $3 ]
then 
	echo "$1 is gt than $2 and $3"
elif [ $2 -gt $1 ] && [ $2 -gt $3 ]
then 
	echo "$2 is gt $3 and $1"
else
	echo "$3 is gt $2 and $1"
fi


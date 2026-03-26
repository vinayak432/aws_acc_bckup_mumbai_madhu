#!/bin/bash

if [ $1 -gt $2 ] 
then
	echo "$1 is gt $2"
	if [ $1 -gt $3 ]
	then 
		echo "$1 is gt $3"
	else
		echo "$3 is gt $1"
	fi
else 
	echo "$2 is gt $1"
	if [ $2 -gt $3 ]
	then
		echo "$2 is gt $3"
	else 
		echo "$3 is gt $2"
	fi
fi

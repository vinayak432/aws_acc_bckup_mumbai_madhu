#!/bin/bash

echo "enter the number"
read num

if [ $((num % 2)) -eq 0 ]
then 
	echo " It is an even no"
else 
	echo " It is an odd no"
fi


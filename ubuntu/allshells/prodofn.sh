#!/bin/bash

echo "enter the value of n"
read n
prod=1
while [ $n -gt 0 ]
do
	prod=`expr $prod \* $n`
	n=`expr $n - 1`
done
echo "the result is $prod"

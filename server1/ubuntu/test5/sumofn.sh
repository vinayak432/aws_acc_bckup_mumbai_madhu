#!/bin/bash
set -x
echo "enter the nu"
read n
sum=0

while [ $n -gt 0 ]

do
	sum=`expr $sum + $n`
	n=`expr $n - 1`
done
echo "THe result is $sum"

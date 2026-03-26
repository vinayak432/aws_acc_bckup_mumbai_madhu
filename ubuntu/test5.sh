#!/bin/bash
#set -x
echo " enter the number"
read num

sum=0
i=1

while [ $i -le $num ]

do 
	sum=`expr $sum + $i`
	i=`expr $i + 1`
done

echo "sum of $num is $sum"

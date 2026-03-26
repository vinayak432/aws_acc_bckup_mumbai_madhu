#!/bin/bash

num="2 8 4 6 3"
sum=0
for i in $num
do
       	sum=`expr $sum + $i`
done 
echo "The sum ofall elements $sum"
	

#!/bin/bash

echo "enter the number"
read num
sum=0

for (( i=1; i<=$num; i++ ))
do
    sum=$((sum + i))
done

echo "sum of $num is: $sum"

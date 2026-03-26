#!/bin/bash

echo "value of the number is $num $num1 $var"
echo $0

echo $0 | awk -F "/" '{print $NF}'
echo $1 $2 $3 $4 $5 $# 

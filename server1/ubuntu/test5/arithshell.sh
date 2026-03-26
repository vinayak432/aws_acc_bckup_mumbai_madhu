#!/bin/bash

#num1=4
#read $0

sum=`expr $1 + $2`
echo "sum is $sum"

sub=`expr $1 - $2`
echo "sub is $sub"

mul=`expr $1 \* $2`
echo "mul is $mul"

mod=`expr $1 % $2`
echo "mod is $mod"

div=`expr $1 / $2`
echo "div is $div"

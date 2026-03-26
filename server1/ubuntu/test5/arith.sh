#!/bin/bash

num1=4
num2=2

sum=`expr $num1 + $num2`
echo "sum is $sum"

sub=`expr $num1 - $num2`
echo "sub is $sub"

mul=`expr $num1 \* $num2`
echo "sum is $mul"

mod=`expr $num1 % $num2`
echo "sub is $mod"

div=`expr $num1 / $num2`
echo "sub is $div"

#!/bin/bash

echo "enter the number"
read num

if [ $num -le 1 ]
then 
	echo "$num is not a prime number"
	exit 1
fi

if [ $(( $num % 2 )) -eq 0 ] && [ $num -ne 2 ] 
then 
	echo "$num is not prime no"
elif [ $(( $num % 3 )) -eq 0 ] && [ $num -ne 3 ]
then 
	echo " $num is not a prime no"
elif [ $(( $num % 5 )) -eq 0 ] && [ $num -ne 5 ]
then 
	echo " $num is not a pime no"
elif [ $(( $num % 7 )) -eq 0 ] && [ $num -ne 7 ]
then 
	echo " $num is not a prime number"
else
	echo " $num is a prime number"
fi


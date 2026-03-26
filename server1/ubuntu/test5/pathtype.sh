#!/bin/bash

echo "enter the path to check"
read name

if [ -f $name ]
then 
	echo "$name is file"
elif [ -d $name ]
then
	echo "$name is directory"
elif [ -L $name ]
then
	echo "$name is link file"
elif [ $tar $name ]
then 
	echo "$name is tar file "
else 
	echo "$name doesnot exist"
fi

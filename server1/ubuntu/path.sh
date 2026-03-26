#!/bin/bash

echo "enter the path"
read name
if [ -f $name ]
then 
	echo "$name is a file"
elif [ -d $name ]
then 
	echo " $name is a directory"
elif [ -L $name ]
then 
	echo "$name is a linkfile"
elif [ $tar $name ]
then 
	echo " it is zip file"
else
	echo "it doesnot exist"
fi


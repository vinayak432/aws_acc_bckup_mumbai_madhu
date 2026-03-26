#!/bin/bash

echo "enter the pattern to search"
read patt

grep -i -l -r "$patt" * > store
if [ $? -eq 0 ]
then
	echo "$patt pattern is found in below files"
	#cat store
	count=`cat store | wc -l`
	echo "$patt is found in $count files"
else
	echo "$patt pattern is not found in any file"
fi

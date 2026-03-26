#!/bin/bash

#set -x
echo "enter the statement"
read line
lengthy_word=""

for word in $line
do 
	if [ ${#word} -gt ${#lenthy_word} ]
	then
		lengthy_word=$word
	fi
done
echo "the longest word in a statement is $lengthy_word"

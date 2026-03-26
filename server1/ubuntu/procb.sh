#!/bin/bash

chkproc="sshd jenkins bash"

for i in $chkproc 
do 
	ps -C $i
	if [ $? -ne 0 ]
	then
	echo "process $i is not running"
	fi
done	

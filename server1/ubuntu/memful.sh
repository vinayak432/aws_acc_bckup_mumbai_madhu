#!/bin/bash

memusage=`df -h . | awk -F " " 'NR==2 {print $(NF-1)}' | sed s/%//g`

if [ $memusage -gt 50 ]
then
	 mail -s "memory crossed threshold level"  vinayakvk062@gmail.com
	echo "memory crossed threshold level of 50%"	
else
	echo "memory usage is less than the threshold level"
fi

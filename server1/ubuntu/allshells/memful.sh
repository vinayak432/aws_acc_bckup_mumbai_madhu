#!/bin/bash

memusage=`df -h . | awk -F " " 'NR==2 {print $(NF-1)}' | sed s/%//g`

if [ $memusage -ge 40 ]
then
         mail -s "memory crossed threshold level"  vinayakvk062@gmail.com
        echo "memory crossed threshold level of 40%"    
else
        echo "memory usage is less than the threshold level"
fi

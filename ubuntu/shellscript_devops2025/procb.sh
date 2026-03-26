#!/bin/bash

chkproc="sshd jenkins bash"

for i in $chkproc
do
        ps -C $i
        if [ $? -ne 0 ]
        then
        mail -s "Processes stopped working" vinayakvk062@gmail.com
        echo "process $i is not running" 
	#mail -s "Processes stopped working" vinayakvk062@gmail.com
        
       	fi
done

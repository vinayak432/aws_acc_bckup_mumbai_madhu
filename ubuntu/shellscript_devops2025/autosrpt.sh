#!/bin/bash

day=`date '+%A'`
case $day in
        'Tuesday') mkdir -p /home/ubuntu/auto
                ;;
        'Wednesday') find /home/ubuntu -type f -mtime +30 > filelist
                ;;
        'Friday') cat filelist | xargs cp -t /home/ubuntu/auto/ 
                ;;
        'Thursday') ls -ltr /home/ubuntu
                ;;
        'Monday') sudo adduser vinayak1
                ;;
        'Saturday' | 'Sunday') echo "It's holiday"
		;;
esac

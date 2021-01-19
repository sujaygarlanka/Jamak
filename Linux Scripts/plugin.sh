#!/bin/bash

DATE=$(gdate '+%Y-%m-%d %H:%M:%S.%N')
while true
do
grep -Eo "[0-9\-]*\s[0-9\:]*\.[0-9]*"
    # echo $DATE
    LOG=$(adb logcat -d -v tag,time,year -t "$DATE" JamakApp:D *:S | tail -n 1)
    DATE=$(gdate '+%Y-%m-%d %H:%M:%S.%N')
    if [[ "$LOG" == *"unformat"* ]]; then
        echo "unformat"
    elif [[ "$LOG" == *"format"* ]]; then
        echo "format"
    fi
    echo $LOG
    sleep 2.0
done
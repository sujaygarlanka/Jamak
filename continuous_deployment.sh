#!/bin/bash
echo "Start continuous deployment script"
python3 ./"Linux Scripts"/plugin.py &
while true
do
    REMOTE_STATUS=$(git remote update && git status)
    if [[ $REMOTE_STATUS == *"behind"* ]];
    then
        git pull
        killall python3
        python3 ./"Linux Scripts"/plugin.py &
    fi
    sleep 1
done

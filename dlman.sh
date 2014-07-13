#!/bin/sh

cd $(dirname $0)

LOG=dlman.log

mv $LOG $LOG.1

echo -n "Starting " >>$LOG
date >>$LOG

while true; do
    MICROPYPATH=lib micropython dlman.py >>$LOG 2>&1
    sleep 5
    echo -n "Restarting " >>$LOG
    date >>$LOG
done

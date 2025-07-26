#!/bin/bash

#1. Open `Ops1redone.sh` in VS Code.
#1. Open `Ops1redone.sh` in VS Code.
#2. Write a script that:
# Stores your name in a variable (e.g., `username="YourName"`)
# Prints a greeting (e.g., “Hello, YourName!”)
# Checks if `/var/log/syslog` exists and prints a message (e.g., “Syslog found!” or “Syslog missing!”)
#3. Save and run: `chmod +x op1redone.sh; ./ops1redone.sh` in the VS Code bash terminal.
#4. Note: If `/var/log/syslog` is missing in  VS Code, create a test file: `echo "test" > test.log` and check that instead.


username="Jky"
echo "Hello, $username!"
if [ -f /var/log/syslog ]; then
    echo "Syslog found!"
else
    echo "Syslog missing!"

fi
logfile="test.log"
echo "test" > test.log
if [ $logfile ]; then
    echo "Found!"
else
    echo "Not found!"

fi

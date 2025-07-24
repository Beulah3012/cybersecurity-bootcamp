#!/bin/bash
username="Jky"
echo "Hello, $username!"
if [ -f /var/log/syslog ]; then
    echo "Syslog found!"
else
    echo "Syslog missing!"

fi
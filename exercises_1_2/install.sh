#!/bin/bash

# Create dir for scripts if doesn't exist yet
if [ ! -d "/home/socket_server" ]; then
    mkdir /home/socket_server
fi
# Copy files to script folder
cp socket_server.py /home/socket_server/
cp script.sh /home/socket_server/
# Give exec permissions to script.sh
chmod +x /home/socket_server/script.sh

# Copy service to systemd/system dir
cp socket_script.service /lib/systemd/system
chmod 644 /lib/systemd/system/socket_script.service

echo "Created service."
echo "The service can be enabled by 'sudo systemctl enable socket_script.service'."
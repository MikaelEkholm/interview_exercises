# Exercise 1
The script requires executable permissions:
```shell
chmod +x script.sh
```
To run the script simply issue the following command:
```shell
./script.sh URL SEARCH_TERM
```

The script takes two parameters, a url and a search term. The script will output all appearances of the term to stdout.

# Exercise 2
The socket server is in socket_server.py, the socket client in socket_client.py and the system service in socket_script.service.
Python 3 is required. The scripts were tested with python version 3.7.1 on arch linux. In addition, it is assumed that python is located in /usr/bin/python.
To create the service, simply use the install script (sudo privelages assumed):
```bash
sudo bash install.sh
```
The install script will move socket_server.py and script.sh to /home/socket_server. The service is moved to /lib/systemd/system and given the appropriate permissions.
To enable and start the service, issue the following commands:
```bash
# Enable service
sudo systemctl enable socket_script.service
# Start service
sudo systemctl start socket_script.service
```
Next start the client:
```bash
python socket_client.py
```
The client will then ask for the URL and SEARCH_TERM:
```bash
Input address and search term ->
```
Inputting the arguments and pressing enter will output the appearances and then ask for input again. To close the connection, simply type 'close' and press enter.

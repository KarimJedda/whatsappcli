# whatsappcli
Control your server from Whatsapp

# What it does?

It allows you to control a server or a group of servers using whatsapp. The script is installed on the server and runs in the background. There are two ways of controlling the server:

1. Send a command to be executed on the server through ```/exec command```, example: sending ```/exec ls -tr``` will execute the  ```ls -tr``` on the server and return the results as a message on whatsapp.

![Example](http://i.imgur.com/k7RDmBu.png?1) 

2. Call a predefined python function on the server. At the moment, some dummy functions are present, like ```hello```, ```start_server```, ```memory_usage```, ```preparing_demo```.. 

![Example](http://i.imgur.com/b37Ykbu.png?1) 

![Example](http://i.imgur.com/gfHjQTl.png?1) 


In order to edit those functions, edit the ```src/routes.py``` file to suit your needs.

It can even send pictures over, or do some text to speech (it can tell jokes)

![Example](http://i.imgur.com/CUIKX6y.png?1) 

At the moment, there is no authentication or security, but it's planned.
I would not use it in production, it's a work in progress, but it already works well.

For any questions just ask

# Installation
1. Install the image handling system dependencies on ```bash opt/system-requirements.sh```
2. Create a virtualenv and install the requirements  ```pip install -r opt/requirements.pip```
3. Follow the instructions on ```src/config.py``` to get the whatsapp credentials
4. Edit the ```src/routes.py``` file to suit your CLI needs
5. Then just run the server with  ```python src/server.py```  


# Credits
Heavily inspired by joaoricardo000's work - https://github.com/joaoricardo000/whatsapp-bot-seed

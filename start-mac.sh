#!/bin/bash

# Replace 'dev' with your own Docker Machine if necessary
# Use command:
#	docker-machine ls 
# to see available docker machines in your sistem
export DockerMachine="dev"

# The IP address is the Mac IP Brigde IP Address. 
# Use command:
# 		VBoxManage list bridgedifs
# if you are unsure about the address.

export MacIP="192.168.99.1"

# This script works with other Docker Images.
# Replace this with your selected Docker Images
# e.g : jess/chrome
export DockerImage="kristiyanto/guidock"

# Script starts here ---
docker-machine start $DockerMachine
echo "Launching Socat to bind the X11 services."
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" &
echo "Launching XQuartz"
open -a xquartz &
eval $(docker-machine env $DockerMachine)
docker pull $DockerImage
docker run -ti -e DISPLAY=$MacIP:0 $DockerImage

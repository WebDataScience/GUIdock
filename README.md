<center><img src="logo.png" alt="GUIdock logo" border=none/></center>


# Docker-Bioconductor-Cytoscape
Docker file for kristiyanto/GUIdock (https://hub.docker.com/r/kristiyanto/guidock/)

Source code, installation and running script, and Dockerfile available at:<br/>
https://github.com/WebDataScience/GUIdock

The package contains: Cytoscape, R, with Bioconductor packages (igraph, Rserve, and networkBMA). 
A tutorial to get it run on Windows and Mac are available:<br/>
https://www.youtube.com/watch?v=FXOU2EZ4szI (Mac)<br/>
https://www.youtube.com/watch?v=Y1Ye5mOMBW0 (Windows)

# Linux
## Install and Run
Download and run runGUIdockLinux.sh from installation folder.<br/>
Usage:<br/>
	sh runGUIdockLinux.sh


# OSX 
## Install
Docker Toolbox needs to be downloaded and installed manually from the website.
https://www.docker.com/toolbox

In addition to Docker Toolbox, GUIdock requires Socat and XQuartz.
Download and run install-mac.sh from Installation folder.<br/>
Usage:<br/>
	sh install-mac.sh


## Run GUIdock
To Run GUIdock, download and run start-mac.sh from Installation folder.<br/>
Usage:<br/>
	sh start-mac.sh


# WINDOWS

## Install
Download and install Docker Toolbox from: https://www.docker.com/toolbox<br/>
Download and install MobaXterm from: http://mobaxterm.mobatek.net/

## Run GUIdock 
Download RunGUIdock.sh and startMoba.bat from Installation folder.<br/>
Execute RunGUIdock.sh by double-click<br/>
or by running from Windows Powershell:<br/>
	sh RunGUIdock.sh






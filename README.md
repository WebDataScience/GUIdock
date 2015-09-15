# Docker-Bioconductor-Cytoscape
Docker file for kristiyanto/GUIdock.

The package contains: Cytoscape, R, with Bioconductor packages (igraph, Rserve, and networkBMA). 

A tutorial to get it run on Windows and Mac are available: 
https://www.youtube.com/watch?v=FXOU2EZ4szI (Mac)
https://www.youtube.com/watch?v=Y1Ye5mOMBW0 (Windows)


# OSX 
## INSTALL
Docker Toolbox needs to be downloaded and installed manually from the website.
https://www.docker.com/toolbox

In addition to Docker Toolbox, GUIdock requires Socat and XQuartz.
Download and run install-mac.sh from Installation folder.
Usage
	sh install-mac.sh


## RUN GUIdock
To Run GUIdock, download and run start-mac.sh from Installation folder
Usage
	sh start-mac.sh


# WINDOWS

## INSTALL
Download and install Docker Toolbox from: https://www.docker.com/toolbox
Download and install MobaXterm from: http://mobaxterm.mobatek.net/

## RUN 
Download RunGUIdock.sh and startMoba.bat from Installation folder.
Execute RunGUIdock.sh by double-click 
or by running from Windows Powershell:
	sh RunGUIdock.sh






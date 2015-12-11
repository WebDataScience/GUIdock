![alt GUIdock Logo](logo.png)

GUIdock: Using Docker containers with a common graphics user interface to address the reproducibility of research
=======

GUIdock is a Docker Package containing the entire computational environment to run applications with a graphical user interface.  As a proof of concept, we focus on supporting Cytoscape, a Java-based standalone program with a graphical user interface for the visualization and analyses of gene networks in biology.  In addition to Cytoscape, our container includes R, Rserve, Bioconductor packages igraph, networkBMA and a Cytoscape app called CyNetworkBMA.  GUIdock contains the entire pipeline and all the tools (including Cytoscape that connects to preloaded RServe, a Bioconductor package called “networkBMA” and all its dependencies) to generate gene regulatory networks.

Docker file for kristiyanto/GUIdock (https://hub.docker.com/r/kristiyanto/guidock/)

Source code, installation and running script, and Dockerfile available at:  
https://github.com/WebDataScience/GUIdock

The package contains: Cytoscape, R, with Bioconductor packages (igraph, Rserve, and networkBMA). 

Demonstration video (for Linux, Mac, and Windows)   
https://www.youtube.com/watch?v=k1WkIx0EENo


Linux
-----
** Install and Run **
Download and run runGUIdockLinux.sh from installation folder.  
Usage:   
	`sh runGUIdockLinux.sh`

The script creates folder ~/.guidock/GUIdock-SHARED within user's home directory. The folder is linked to /root/GUIdock-SHARED in the container.   

Instructional Video: https://www.youtube.com/watch?v=HOtI1Eg2J1Q


OSX 
---
** Install **  
Docker Toolbox needs to be downloaded and installed manually from the website.
https://www.docker.com/toolbox

In addition to Docker Toolbox, GUIdock requires Socat and XQuartz.
Download and run install-mac.sh from Installation folder.  
Usage:  
	`sh install-mac.sh`

** Run GUIdock **
To Run GUIdock, download and run start-mac.sh from Installation folder.  
Usage:   
	
	`sh start-mac.sh`

Instructional Video: https://www.youtube.com/watch?v=4Qg0fCDOxhY


WINDOWS
-------
** Install **
Download and install Docker Toolbox from: https://www.docker.com/toolbox  
Download and install MobaXterm from: http://mobaxterm.mobatek.net/

** Run GUIdock **
Download RunGUIdock.sh and startMoba.bat from Installation folder.  
Execute RunGUIdock.sh by double-click or by running from Windows Powershell:  
	
	`sh RunGUIdock.sh`

Instructional Video: https://www.youtube.com/watch?v=cA7HVCB064I


Contact
-------
Ling-Hong Hung, Daniel Kristiyanto, Sung Bong Lee, Ka Yee Yeung  
Institute of Technology  
University of Washington  
Tacoma, WA 98402, USA  




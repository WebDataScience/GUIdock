![alt GUIdock Logo](https://raw.githubusercontent.com/kristiyanto/GUIdock/master/logo.png)

GUIdock: Using Docker containers with a common graphics user interface to address the reproducibility of research
=======

GUIdock is a Docker Package containing the entire computational environment to run applications with a graphical user interface.  As a proof of concept, we focus on supporting Cytoscape, a Java-based standalone program with a graphical user interface for the visualization and analyses of gene networks in biology.  In addition to Cytoscape, our container includes R, Rserve, Bioconductor packages igraph, networkBMA and a Cytoscape app called CyNetworkBMA.  GUIdock contains the entire pipeline and all the tools (including Cytoscape that connects to preloaded RServe, a Bioconductor package called “networkBMA” and all its dependencies) to generate gene regulatory networks.

Docker file for biodepot/GUIdock ([Docker Hub Page](https://hub.docker.com/r/biodepot/guidock/))

Source code, installation and running script, and Dockerfile available at:
[https://github.com/BioDepot/GUIdock](https://github.com/BioDepot/GUIdock)

The package contains: Cytoscape, R, with Bioconductor packages (igraph, Rserve, and networkBMA). 

Demonstration video (for Linux, Mac, and Windows)   
[![Demo Video](https://raw.githubusercontent.com/kristiyanto/GUIdock/master/demo.png)](https://youtu.be/Te1yC_AkvzQ)


Publication
-----------
Hung, Ling-Hong, Daniel Kristiyanto, Sung Bong Lee, and Ka Yee Yeung. **"GUIdock: Using Docker Containers with a Common Graphics User Interface to Address the Reproducibility of Research."** [_PloS one_ 11, no. 4 (2016): e0152686.](http://dx.doi.org/10.1371/journal.pone.0152686)

[http://dx.doi.org/10.1371/journal.pone.0152686](http://dx.doi.org/10.1371/journal.pone.0152686
)

Linux
-----
**Install and Run**

Download and run runGUIdockLinux.sh from installation folder.  
Usage:

```
sh runGUIdockLinux.sh
```

The script creates folder `~/.guidock/GUIdock-SHARED` within user's home directory. The folder is linked to /root/GUIdock-SHARED in the container.   

Instructional Video: [https://www.youtube.com/watch?v=HOtI1Eg2J1Q](https://www.youtube.com/watch?v=HOtI1Eg2J1Q)


OSX 
---
**Install**

Docker Toolbox needs to be downloaded and installed manually from the website.
[https://www.docker.com/toolbox](https://www.docker.com/toolbox
)

In addition to Docker Toolbox, GUIdock requires Socat and XQuartz.
Download and run install-mac.sh from Installation folder.  
Usage:

```
sh install-mac.sh
```

**Run GUIdock**

To Run GUIdock, download and run start-mac.sh from Installation folder.  
Usage:

```	
sh start-mac.sh
```

Instructional Video: [https://www.youtube.com/watch?v=4Qg0fCDOxhY](https://www.youtube.com/watch?v=4Qg0fCDOxhY)


WINDOWS
-------
**Install**

Download and install Docker Toolbox from: [https://www.docker.com/toolbox](https://www.docker.com/toolbox)  
Download and install MobaXterm from: [http://mobaxterm.mobatek.net/](http://mobaxterm.mobatek.net/)

**Run GUIdock**

Download `RunGUIdock.sh` and `startMoba.bat` from Installation folder.  
Execute RunGUIdock.sh by double-click or by running from Windows Powershell:  
	
```
sh RunGUIdock.sh
```

Instructional Video: [https://www.youtube.com/watch?v=cA7HVCB064I](https://www.youtube.com/watch?v=cA7HVCB064I)


Contact
-------
Ling-Hong Hung, Daniel Kristiyanto, Sung Bong Lee, Ka Yee Yeung  
Institute of Technology  
University of Washington  
Tacoma, WA 98402, USA  




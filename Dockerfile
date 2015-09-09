# This is the Dockefile to build GUIdock (kristiyanto/guidock)
# Base Docker Image
FROM bioconductor/release_base

# Maintainer
MAINTAINER Daniel Kristiyanto, danielkr@uw.edu 

# Java Instalation
RUN apt-get update
RUN sudo apt-get -q -y install default-jdk
RUN apt-get clean
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64

# Cytoscape Retrieval
WORKDIR /root 
ADD http://chianti.ucsd.edu/cytoscape-3.2.1/cytoscape-3.2.1.tar.gz /root/cytoscape-3.2.1.tar.gz
RUN tar -zxvf cytoscape-3.2.1.tar.gz 
RUN rm /root/cytoscape-3.2.1.tar.gz

# Install Cytoscape Apps / Plugin
ADD PACKAGE/CyNetworkBMA-1.0.0_1.jar /root/CytoscapeConfiguration/3/apps/installed/CyNetworkBMA-1.0.0_1.jar

# Dummy data for Demo
# Demo contains Cytoscape session and dummy data for Dream4, Yeast, and RNASeq
ADD DEMO/ /root/DEMO/

# Install required R Packages
RUN echo 'install.packages(c("Rserve", "igraph"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \     && Rscript /tmp/packages.R
RUN echo 'source("https://bioconductor.org/biocLite.R")' > /tmp/packages.R  
RUN echo 'biocLite("networkBMA")' >> /tmp/packages.R \ && Rscript /tmp/packages.R

# Build a Script to start Rserve
RUN echo 'library("Rserve")' > /root/rserve.R
RUN echo 'Rserve()' >> /root/rserve.R 

# Build a Script to start run Rserve and Launch Cytoscape
RUN echo 'Rscript /root/rserve.R' > /root/start.sh
RUN echo '/root/cytoscape-unix-3.2.1/cytoscape.sh' >> /root/start.sh



# Run Script on entrance
CMD sh /root/start.sh

FROM java_base_8

MAINTAINER Varun Mittal <varun91@uw.edu>

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root
WORKDIR /root

ADD http://chianti.ucsd.edu/cytoscape-3.3.0/cytoscape-3.3.0.tar.gz /root/cytoscape-3.3.0.tar.gz
RUN tar -xf cytoscape-3.3.0.tar.gz
RUN rm /root/cytoscape-3.3.0.tar.gz

RUN apt-get update
RUN apt-get install -y --force-yes --no-install-recommends software-properties-common
RUN add-apt-repository -y ppa:webupd8team/java

RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections
RUN apt-get install -y --force-yes --no-install-recommends oracle-java8-installer oracle-java8-set-default

RUN apt-get purge software-properties-common -y --force-yes
RUN apt-get -y autoclean
RUN apt-get -y autoremove
RUN rm -rf /var/lib/apt/lists/*


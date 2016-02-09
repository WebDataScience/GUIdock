FROM ubuntu:14.04

MAINTAINER Varun Mittal <varun91@uw.edu>

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

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


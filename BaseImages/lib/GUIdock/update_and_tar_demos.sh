#!/bin/bash

#Clean existing DEMO directory
rm -rf ./DEMO DEMO.tar.gz
mkdir DEMO

#Copy from root DEMO directort
cp ../../../DEMO/* ./DEMO

tar -c DEMO > DEMO.tar
gzip -9 DEMO.tar

rm -rf ./DEMO

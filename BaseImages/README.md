# Dockerfile generator

Using simple json files and dependency concept we can build dockerfile templates.
* Advantages
 * Maintaining complex dependency
 * Writing clean dockerfile and making sure that build dependencies and cache files are removed.
 * Using multiple components at the build time to create functional docker images

## Using generator
./base_image_generator.py -i sample/cytoscape_3_3_base.json <br/>
This command will use lib/cytoscape_3_3.json which has a dependency on lib/java8.json <br/>

## Library - docker scripts that can be used as dependency to create complex images
* lib/
 * java8.json - Base jdk8 image
 * cytoscape_3_3.json - Base cytoscape image with functional copy of software
 * novnc.json - X11 image with novnc support, should be included as last dependency, original contributor: https://github.com/fcwu/docker-ubuntu-vnc-desktop
 * r.json - Base r image without build tools, contains NetworkBMA compiled
 * r_dev.json - Base r image with complete toolchain, useful for installing and compiling packages, contains NetworkBMA compiled

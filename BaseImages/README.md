# Dockerfile generator

Using simple json files and dependency concept we can build dockerfile templates.
* Advantages
 * Maintaining complex dependency
 * Writing clean dockerfile and making sure that build dependencies and cache files are removed.
 * Using multiple components at the build time to create functional docker images

## Using generator
./base_image_generator.py -i sample/cytoscape_3_3_base.json <br/>
This command will use lib/cytoscape_3_3.json which has a dependency on lib/java8.json <br/>

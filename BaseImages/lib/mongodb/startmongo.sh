#!/bin/bash

/usr/bin/numactl --interleave all /usr/bin/mongod --storageEngine wiredTiger --logpath /data/log --smallfiles --dbpath /data/db --quiet

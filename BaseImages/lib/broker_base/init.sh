#!/bin/bash

cd / && tar -xf /broker.tar.gz && rm broker.tar.gz

chmod +x /broker/init.sh
/broker/init.sh

cd /broker/ && nohup python manage.py runserver 0.0.0.0:8000 &

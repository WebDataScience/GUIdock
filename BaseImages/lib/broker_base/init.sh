#!/bin/bash

cd / && tar -xf /broker.tar.gz && rm broker.tar.gz
chmod +x /broker/init.sh
/bin/bash -c /broker/init.sh

while getopts ":u:p:" opt; do
  case $opt in
    u)
      echo "-a was triggered, Parameter: $OPTARG" >&2
      echo $OPTARG >  /google_cred
      ;;
    p)
      echo "-a was triggered, Parameter: $OPTARG" >&2
      echo $OPTARG >> /google_cred
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

cd /broker && python manage.py syncdb --noinput
cd /broker/ && nohup python manage.py runserver 0.0.0.0:8000 &

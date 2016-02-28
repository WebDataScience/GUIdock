#!/bin/bash

su celery -c 'cd /broker && celery -A celery_app worker -Qfor_push_data'

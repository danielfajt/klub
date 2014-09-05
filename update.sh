#!/bin/bash
#version 0.1

set -e

git pull
source env/bin/activate
env/bin/python env/bin/pip install -r requirements --upgrade
if [ "$1" = "migrate" ]; then
   echo "Backuping db..."
   mkdir -p db_backup
   sudo -u postgres pg_dump > db_backup/`date +"%y%m%d-%H:%M:%S"`-zmapa.sql
   echo "Migrating..."
   env/bin/python ./manage.py migrate
fi
(cd apps/aklub/ && django-admin.py compilemessages)
env/bin/python ./manage.py collectstatic --noinput
touch wsgi.py
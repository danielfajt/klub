#!/bin/bash
echo Starting Gunicorn.
echo $DJANGO_SETTINGS_MODULE
pipenv run python3 manage.py migrate
exec pipenv run gunicorn wsgi:application \
	   --name klubpratel \
	   --bind 0.0.0.0:${GUNICORN_PORT:-"8000"} \
	   --workers ${GUNICORN_NUM_WORKERS:-"2"} \
	   --timeout ${GUNICORN_TIMEOUT:-"60"} \
	   --preload \
	   --log-level=debug \
	   --log-file=- \
	   --access-logfile=- \
	   "$@"

#!/bin/bash
set -ex

if [ "${ENV}" == "PROD" ]; then
	echo "Running Production Server"
	exec uwsgi --http 0.0.0.0:9090 --wsgi-file /usr/src/app/identidock.py --callable app --stats 0.0.0.0:9191
else
	echo "Running Development Server"
	exec python "identidock.py"
fi

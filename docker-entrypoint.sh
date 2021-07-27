#!/bin/bash
set -e

until psql $ENTRYPOINT_DEFAULT_DATABASE_URI -c '\l'; do
    >&2 echo "appdb is unavailable - sleeping"
    sleep 1
done
 
>&2 echo "running migrate..."
until python manage.py migrate --noinput; do 
    sleep 1
done 

>&2 echo "running gunicorn server... "
#gunicorn -c gunicorn_config.py fakeenergyapi.wsgi --access-logfile - --error-logfile -
python manage.py runserver 0.0.0.0:8000

exec "$@"
#!/bin/bash
 
# based on: http://mjduffin.net/2015/01/03/deploying-django-gunicorn-and-nginx-on-the-raspberry-pi/
 
NAME="homecontrol_app"                                  # Name of the application
DJANGODIR=/home/pi/Sites/homecontrol_project/homecontrol   # Django project directory
SOCKFILE=/webapps/homeauto_django/run/gunicorn.sock  # we will communicte using this unix socket
USER=homeauto                                        # the user to run as
GROUP=webapps                                     # the group to run as
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=homeauto.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=homeauto.wsgi                     # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-

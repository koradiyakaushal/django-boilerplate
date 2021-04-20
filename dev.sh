#!/usr/bin/env bash
echo "Reseting the master branch:"
git add .
git reset --hard
echo "Pulling the master branch:"
git pull
# echo "killing the gunicorn daemon:"
# pkill -9 gunicorn
# echo "restarting the daemon:"
# sleep 1
# gunicorn conf.wsgi --bind localhost:8000 --workers 3 --daemon
# sleep 1
echo "showing the python processes:"
ps -aux | grep python
exit

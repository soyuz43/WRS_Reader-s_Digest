#!/bin/bash

rm db.sqlite3
rm -rf ./WRS_Readersapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations WRS_Readersapi
python3 manage.py migrate WRS_Readersapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens


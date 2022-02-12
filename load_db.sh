#!/bin/bash
cd guestbook
export FLASK_APP=myapp.py
~/.poetry/bin/poetry run flask db migrate
~/.poetry/bin/poetry run flask db upgrade

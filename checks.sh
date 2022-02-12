#!/bin/bash

echo "Running checks! Making sure repo is confirming to code quality"

/home/app/.poetry/bin/poetry run black --check guestbook
/home/app/.poetry/bin/poetry run isort --check guestbook

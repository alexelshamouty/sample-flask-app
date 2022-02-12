#!/bin/bash

echo "Running checks! Making sure repo is confirming to code quality"

export PATH=$PATH:~./poetry/bin

poetry run black --check guestbook
poetry run isort --check guestbook

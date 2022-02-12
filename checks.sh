#!/bin/bash

echo "Running checks! Making sure repo is confirming to code quality"

poetry run black --check guestbook
poetry run isort --check guestbook

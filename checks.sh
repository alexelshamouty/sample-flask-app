#!/bin/bash

echo "Running checks! Making sure repo is confirming to code quality"

poetry run black --check --diff guestbook
poetry run isort --check --diff guestbook

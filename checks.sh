#!/bin/bash

echo "Running checks before"

poetry run black --check guestbook
poetry run isort --check guestbook

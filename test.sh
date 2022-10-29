#!/usr/bin/env bash

# If any command fails, exit immediately with that command's exit status
set -eo pipefail

echo "Running unittest..."
python3 -m unittest discover -v -s ./test_collection/
echo "unittest complete!"

echo "Running pylint..."
pylint **/*.py
echo "pylint complete!"

echo "Running mypy..."
mypy **/*.py
echo "mypy complete!"
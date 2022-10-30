#!/usr/bin/env bash

# If any command fails, exit immediately with that command's exit status
set -eo pipefail

echo "# Running project validation"
echo "## Running unittest with coverage..."
python3 -m coverage run -m unittest discover -v -s ./test_collection/
python3 -m coverage report
echo "unittest & coverage complete!"

echo "## Running cyclomatic analysis..."
python3 -m radon cc .
echo "cyclomatic analysis complete!"

echo "## Running pylint..."
pylint **/*.py
echo "pylint complete!"

echo "## Running mypy..."
mypy **/*.py --strict
echo "mypy complete!"

# dojo
a tool for deliberate practice. inspired by [this video](https://www.youtube.com/watch?v=QZM3xkVnKYo) the intention is to create an space for deliberate practice.
generate constraints that provide [contextual interference](https://sportscienceinsider.com/contextual-interference-effect/)

## dependencies
Make sure you have the following installed and configured:
- pip3
- python 3.6 or greater

## running the project
Run `pip3 install -r requirements.txt`

## testing the project
Tests can be found under `./test_collection` and should be run regularly as part of development!
Property-based testing is performed using Hypothesis and run via unittest.

`. ./test.sh` runs static-analysis and tests.

## contributing
Changes are welcome from anyone!
There is a zero-tolerance for errors that appear when you run `. ./test.sh` 
and for this reason it is reccomended that you run `. ./git-hooks-setup.sh` to configure your pre-commit hook to run `test.sh` before any commits.

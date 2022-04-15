#!/bin/bash

find . -name "*pycache*" -exec rm -r {} \;
find . -name "000*" -exec rm -r {} \;
find . -name "db.sqlite3" -exec rm {} \;
# Add other cleanup searches here

# git add --all .
# git commit -m "$1"
# git push origin

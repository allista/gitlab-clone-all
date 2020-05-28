#!/bin/bash

cwd=$(pwd)

abs_path_regex="s|^(?!/)|$cwd/|g"

export MYPYPATH="$1"
shift
mypy $@ | perl -pe $abs_path_regex

#!/bin/bash
#
#
readonly path_curr=$(pwd)
readonly path_parents=$(dirname "${path_curr}")
#
#
unset PYTHONPATH PYTHONDONTWRITEBYTECODE PYTHONUNBUFFERED
export PYTHONPATH=$PYTHONPATH:${path_curr}
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
#
#
unset PATH_DIR_PROJECT_ROOT
export PATH_DIR_PROJECT_ROOT="${1:-./project}"
#
#
pyconcrete-admin.py compile --source=${PATH_DIR_PROJECT_ROOT} --pye

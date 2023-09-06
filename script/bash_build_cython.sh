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
unset PATH_DIR_PROJECT_ROOT IS_MOVE_PY
export PATH_DIR_PROJECT_ROOT="${1:-./project}"
export IS_MOVE_PY="${2:-true}"
#
#
python3 ${path_curr}/module/_build_cython.py build_ext --inplace

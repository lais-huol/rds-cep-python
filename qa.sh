#!/usr/bin/env bash

echo "STEP: Lint
"
ruff .

# echo "
# STEP: Static type check
# "
# mypy --warn-unused-configs --python-version 3.10 --show-error-context --show-column-numbers --show-error-end --show-error-codes --pretty rds_cep


"
STEP: Test
"
PYTHONBREAKPOINT=ipdb.set_trace python -m pytest -s

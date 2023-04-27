#!/usr/bin/env bash

docker build -t rds-cep-python .

docker run -it --rm -v `pwd`:/app rds-cep-python bash -c 'flake8 --statistics --benchmark --doctests'

docker run -it --rm -v `pwd`:/app rds-cep-python bash -c 'mypy --warn-unused-configs --python-version 3.10 --show-error-context --show-column-numbers --show-error-end --show-error-codes --pretty rds_cep'

#!/bin/sh
set -e
python -m yamllint -c yamllint.yml .github/workflows
python -m black --check scripts tests
python -m flake8 scripts tests
python -m pyright scripts

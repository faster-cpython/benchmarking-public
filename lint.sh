#!/bin/sh
set -e
python scripts/regenerate_workflows.py --check
python -m black --check scripts tests
python -m flake8 scripts tests
python -m pyright scripts

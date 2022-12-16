#!/bin/sh
python -m black --check scripts tests
python -m flake8 scripts tests

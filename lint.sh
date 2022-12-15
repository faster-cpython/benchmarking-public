#!/bin/sh
python -m black --check scripts
python -m flake8 scripts

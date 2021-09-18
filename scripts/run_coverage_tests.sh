#!/usr/bin/env bash

echo "Running Coverage tests:"
pytest --cov mts --cov mts/classes --cov-report html tests

#!/bin/bash

echo "Building..."
python3 setup.py sdist bdist_wheel

echo "Uploading..."
twine upload dist/*

echo "Cleaning up..."
python3 setup.py clean --all

# clean build artifacts
rm -rf *.egg-info

echo "Done."

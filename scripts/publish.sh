#!/bin/bash

echo "Building..."
python3 setup_mslm.py sdist bdist_wheel
python3 setup_mslm_email_verify.py sdist bdist_wheel
python3 setup_mslm_otp.py sdist bdist_wheel

echo "Uploading..."
twine upload dist/*

echo "Cleaning up..."
python3 setup_mslm.py clean --all
python3 setup_mslm_email_verify.py clean --all
python3 setup_mslm_otp.py clean --all

# clean build artifacts
rm -rf *.egg-info

echo "Done."

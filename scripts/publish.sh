#!/bin/bash

echo "Building mslm..."
python3 setup.py sdist bdist_wheel

echo "Uploading ..."
twine upload dist/*

echo "Cleaning up..."
python3 setup.py clean --all

# clean egs
rm -rf mslm.egg-info
rm -rf mslm_email_verify.egg-info
rm -rf mslm_otp.egg-info

echo "Done."

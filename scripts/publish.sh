#!/bin/bash

echo "Building mslm..."
python3 setup_mslm.py sdist bdist_wheel

echo "Building mslm_email_verify..."
python3 setup_mslm_email_verify.py sdist bdist_wheel

echo "Building mslm_otp..."
python3 setup_mslm_otp.py sdist bdist_wheel

echo "Uploading ..."
#twine upload dist/*

echo "Cleaning up..."
python3 setup_mslm.py clean --all
python3 setup_mslm_email_verify.py clean --all
python3 setup_mslm_otp.py clean --all

# clean egs
rm -rf mslm.egg-info
rm -rf mslm_email_verify.egg-info
rm -rf mslm_otp.egg-info

echo "Done."

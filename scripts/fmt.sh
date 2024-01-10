#!/bin/bash

DIR=`dirname $0`

# Format the project.

black -l 79 \
    $DIR/../mslm \
    $DIR/../mslm_email_verify \
    $DIR/../mslm_otp \
    $DIR/../lib \


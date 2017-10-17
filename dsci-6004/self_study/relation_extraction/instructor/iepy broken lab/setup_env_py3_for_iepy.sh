#!/usr/bin/env bash
## Sets up enivornment for NLP in Python 3, Way of the Future,
#
# Requires Anaconda to be installed:
# http://docs.continuum.io/anaconda/install.html
################################################################################

# Name of environment
ENV_NAME=py3_iepy

# If it already exists, remove it
# Sometimes it doesn't work so do 'sudo conda ..'
conda env remove \
    --quiet --yes \
    --name $ENV_NAME

# Create a new environment
conda create \
    --quiet --yes \
    --name $ENV_NAME \
    python=3 \
    anaconda 

# Start using the new environment
source activate $ENV_NAME

# Update all packages
conda update --all --yes --force --quiet

# # Install conda packages
# conda install \
#     --yes --force --quiet \
#     setuptools scikit-learn spacy

# Install pip packages
pip install \
    --upgrade \
    pip iepy

iepy --download-third-party-data

# Print next steps
clear
echo
echo 'Your  environment in Python 3 (Way of the Future) is ready to go.'
echo
echo 'To activate this environment type:'
echo '$ source activate' $ENV_NAME
echo

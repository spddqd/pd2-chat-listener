#!/bin/sh
python -m venv .
source ./venv/bin/activate
pip install -r requirements
deactivate
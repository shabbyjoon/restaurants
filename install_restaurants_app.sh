#!/bin/bash

echo "***Installation commencing"
echo "***Initializing database"
python3 init_database.py
echo "***Finished initializing database"
echo "***Configuring environment"
python3 -m venv venv 
echo "***Finished configuration"
echo "***Activating Environment"
. venv/bin/activate
echo "***Environment Activated"
echo "***Installing Python Dependencies"
pip3 install -r requirements.txt
echo "***Finished Installing Python Dependencies"x
echo "***Installation complete"









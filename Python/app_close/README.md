## Description
This script is based on python v2.7.15  
Purpose: to automate manual process of closing application  

## Requirements
Python2
virtualenv python module
docker

## HOW TO SET UP ENV in your local
> python -m virtualenv app_close  
pip install -r app_close/requirements.txt  
docker-compose -f app_close/docker/docker-compose.yml up -d  

## How to execute
example  
> python -u app_close/src/app_close.py -id=1  

※ You can also see help page with -h option
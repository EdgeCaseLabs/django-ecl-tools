#!/bin/bash


python setup.py --long-description | rst2html.py > output.html

python setup.py sdist upload
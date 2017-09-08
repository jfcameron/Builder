#Purpose makes a new project at the given location
#Usage: -path ~/Workspace -projectName MyProject 
#!/usr/bin/python
import argparse
"""
import json
import os
import subprocess
import sys
import pprint
"""

parser = argparse.ArgumentParser("makes a new project at the given location")
parser.add_argument('-path',        required=True, type=str, help='path to new project')
parser.add_argument('-projectName', required=True, type=str, help='name of new project')
args = parser.parse_args()



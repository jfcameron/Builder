#Purpose perform static code analysis via cppcheck
#!/usr/bin/python
import sys
import argparse
import json
import os
import subprocess

parser = argparse.ArgumentParser("perform static code analysis on a c++ project")
parser.add_argument('-configPath', required=True, type=str, help='path to project\'s config.json')
args = parser.parse_args()

def log(aMessage):
    print(str(aMessage))

def error(aMessage):
    print("Error: " + str(aMessage))
    sys.exit()

_ConfigURI = os.getcwd() + "/" + args.configPath + "/config.json"
_JsonFile = ""
try:
    _JsonFile = open(_ConfigURI).read()
except:
    error("The config.json file does not exist!")
config = {}
try:
    config = json.loads(_JsonFile)
except Exception as ex:
    error(ex.message)
pretty = json.dumps(config, indent = 2)
log(_ConfigURI + ": \n"+pretty)

_SourceCodeRootPath = os.getcwd() + '/' + args.configPath + '/' + config["SourceCodeRootPath"]

subprocess.call([ 
    'cppcheck', _SourceCodeRootPath, "--enable=all", "--check-config", "--force"
])

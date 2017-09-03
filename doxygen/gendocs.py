#read config.json, inject into doxygen config before generation
#Usage: -platforms osx\ glfw -generator Xcode
#!/usr/bin/python
import sys
import argparse
import subprocess
import json
import os

parser = argparse.ArgumentParser("reads config.json data, parameterizes data into doxygen config")
parser.add_argument('-configPath', required=True, type=str, help='path to project\'s config.json')
args = parser.parse_args()

def log(aMessage):
    print("-- " + str(aMessage))

def error(aMessage):
    print("Error: " + str(aMessage))
    sys.exit()

_ConfigURI = os.getcwd() + "/" + args.configPath + "/config.json"#_ConfigURI = os.getcwd()+"/config.json"
_DoxygenDirectory = "/".join(str(sys.argv[0]).split("/")[:-1])+ "/"

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
log("config.json: \n"+pretty)

_Args = []
def addArg(aKey, aValue):
    _Args.append("echo '" + aKey + '=' + aValue + "'")

#Args from Config.json
addArg("PROJECT_NAME",   config["ProjectName"])
addArg("PROJECT_NUMBER", config["MajorVersion"] + "." + config["MinorVersion"])
addArg("PROJECT_BRIEF",  '"' + config["BriefDescription"] + '"')

#Const args
addArg("HTML_STYLESHEET", _DoxygenDirectory + "doxyStyle.css")

_Args = "; ".join(_Args)

ps = subprocess.Popen(
    '( cat ' + _DoxygenDirectory + "doxyconf.txt" +'; echo "";' + _Args + ' ) | doxygen -',
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT
)
output = ps.communicate()[0]
log(output)

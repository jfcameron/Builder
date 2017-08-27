#Purpose collects project configuration data, passes to cmake, which generates the project files
#Usage: -platform osx -generator Xcode
#!/usr/bin/python
import sys
import argparse
import subprocess
import json

parser = argparse.ArgumentParser("reads config.json data, parameterizes data into CMakeLists.txt")
parser.add_argument('-platform',  required=True, type=str, help='Platform code to include in generated project')
parser.add_argument('-generator', required=True, type=str, help='generator to use to generated the project')
args = parser.parse_args()

def log(aMessage):
    print("-- " + str(aMessage))

def error(aMessage):
    print("Error: " + str(aMessage))
    sys.exit()

log("Selected platform: "  + args.platform)
log("Selected generator: " + args.generator)

_CMakeDir = "../../cmake/"

_JsonFile = ""
try:
    _JsonFile = open(_CMakeDir+"config.json").read()
except:
    error("The config.json file does not exist!")

config = {}
try:
    config = json.loads(_JsonFile)
except Exception as ex:
    error(ex.message)

pretty = json.dumps(config, indent = 2)
log("config.json: \n"+pretty)

def cmakeArg(aName, aValue):
    return '-D' + str(aName) + '=' + aValue

subprocess.call([ 
    'cmake',_CMakeDir, 
    '-G' + args.generator, 
    cmakeArg("Args.Platform",args.platform),
    cmakeArg("Config.ProjectName",config["ProjectName"]),
    cmakeArg("Config.IncludePaths", '\n'.join(config["IncludePaths"]))
])

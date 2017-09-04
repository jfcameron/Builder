#Purpose collects project configuration data, passes to cmake, which generates the project files
#Usage: -platform osx -generator Xcode
#!/usr/bin/python
import argparse
import json
import os
import subprocess
import sys

parser = argparse.ArgumentParser("reads config.json data, parameterizes data into CMakeLists.txt")
parser.add_argument('-platforms',  required=True, type=str, help='Platform code to include in generated project')
parser.add_argument('-generator',  required=True, type=str, help='generator to use to generated the project')
parser.add_argument('-configPath', required=True, type=str, help='path to project\'s config.json')
args = parser.parse_args()

def log(aMessage):
    print("-- " + str(aMessage))

def error(aMessage):
    print("Error: " + str(aMessage))
    sys.exit()

log("Selected platforms: " + args.platforms)
log("Selected generator: " + args.generator)

_CMakeDir = "/".join(str(sys.argv[0]).split("/")[:-1])+ "/"

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

_SourceCodeRootPath    = os.getcwd() + '/' + args.configPath + '/' + config["SourceCodeRootPath"]
_StaticLibraryRootPath = os.getcwd() + '/' + args.configPath + '/' + config["StaticLibraryRootPath"]

def cmakeArg(aName, aValue):
    return '-D' + str(aName) + '=' + aValue

subprocess.call([ 
    'cmake',_CMakeDir, 
    '-G' + args.generator, 
    cmakeArg("Args.Platforms", args.platforms),
    cmakeArg("Config.ProjectName", config["ProjectName"]),
    cmakeArg("Config.ProjectType", config["ProjectType"]),
    cmakeArg("Config.SourceCodeRootPath", _SourceCodeRootPath),
    cmakeArg("Config.StaticLibraryRootPath", _StaticLibraryRootPath),
    cmakeArg("Config.IncludePaths",'\n'.join(config["IncludePaths"]))
])

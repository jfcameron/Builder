# Builder

##Description
![asdf](https://img.shields.io/badge/development%20status-active-green.svg)
![asdf](https://img.shields.io/badge/platforms-osx%20|%20win%20|%20linux-lightgrey.svg)
![asdf](https://img.shields.io/badge/license-MIT-blue.svg)

Multiplatform build environment for C++ projects.
Requires bash, python, cmake

## Usage
* write config.json to your project root to setup project metadata
* write shell scripts that calls cmake/generateproject.py to generate project files for your IDEs and configurations
* write shell script that calls doxygen/generatedocuments.py to generate doxygen manual for your project

## Config.json
* ProjectName : string, name of project.
* ProjectType : string enum {"Executable", "StaticLibrary", "SharedLibrary"}, determines output type of project
* MajorVersion : int, above decimal point
* MinorVersion : int, below decimal point
* IncludePaths : string list, list of paths to search for headers
* StaticLibraries : string list, list of statically linked libraries for this project
* DynamicLibraries : string list, list of dynmically linked libraries for this project

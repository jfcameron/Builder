# CppProjectTemplate
template for cross platform, IDE agnostic C++ projects. Requires CMake, Python.

## Config.json
ProjectName : string, name of project.
ProjectType : "Executable",
MajorVersion : int, above decimal point
MinorVersion : 1, below decimal point
IncludePaths : string list, list of paths to search for headers
StaticLibraries : string list, list of statically linked libraries for this project
DynamicLibraries : string list, list of dynmically linked libraries for this project

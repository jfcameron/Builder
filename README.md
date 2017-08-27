# CppProjectTemplate
template for cross platform, IDE agnostic C++ projects. Requires CMake, Python.

## Config.json
ProjectName : string, name of project.
ProjectType : string enum {"Executable", "StaticLibrary", "SharedLibrary"}, determines output type of project
MajorVersion : int, above decimal point
MinorVersion : int, below decimal point
IncludePaths : string list, list of paths to search for headers
StaticLibraries : string list, list of statically linked libraries for this project
DynamicLibraries : string list, list of dynmically linked libraries for this project

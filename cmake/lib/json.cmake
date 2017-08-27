if (DEFINED _JSON_CMAKE)
return()
endif()
set(_JSON_CMAKE yes)

include ("lib/extern/JSONParser.cmake")

macro(json_parse prefix jsonFileName)
    file(STRINGS "${jsonFileName}" jsonString)
    sbeParseJson(${prefix} "jsonString")
endmacro()

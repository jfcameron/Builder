if (DEFINED _JSON_CMAKE)
return()
endif()
set(_JSON_CMAKE yes)

include ("lib/extern/JSONParser.cmake")

macro(json_parse prefix jsonString)
    sbeParseJson(${prefix} ${jsonString})
endmacro()

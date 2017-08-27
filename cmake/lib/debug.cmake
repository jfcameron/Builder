if (DEFINED _LOG_CMAKE)
    return()
endif()
set(_LOG_CMAKE yes)

function(debug_log aMessage)
    message(STATUS "Log: ${aMessage}")
endfunction()

function(debug_error aMessage)
    message(FATAL_ERROR "Error: ${aMessage}")
endfunction()

function(debug_warn aMessage)
    message(WARNING "Warning: ${aMessage}")
endfunction()
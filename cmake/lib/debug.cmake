if (DEFINED _LOG_CMAKE)
    return()
endif()
set(_LOG_CMAKE yes)

function(debug_log aMessage)
    message(STATUS "${aMessage}")
endfunction()

function(debug_error aMessage)
    message(FATAL_ERROR "${aMessage}")
endfunction()

function(debug_warn aMessage)
    message(WARNING "${aMessage}")
endfunction()
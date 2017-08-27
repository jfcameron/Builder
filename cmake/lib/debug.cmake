if (DEFINED _LOG_CMAKE)
    return()
endif()
set(_LOG_CMAKE yes)

function(debug_log aMessage)
    message("Log: ${aMessage}")
endfunction()

function(debug_error aMessage)
    message("Error: ${aMessage}")
    return()
endfunction()

function(debug_warn aMessage)
    message("Warning: ${aMessage}")
    return()
endfunction()
#------------------------------------------------------------------------------
cmake_minimum_required( VERSION 3.15 )
project( wasm-cpp-example VERSION 1.0 LANGUAGES CXX )

#------------------------------------------------------------------------------
# List of source files.
#------------------------------------------------------------------------------
set( CLIENT_FILES
   src/client/main.cpp
)

#------------------------------------------------------------------------------
add_executable( wasm-cpp-example ${CLIENT_FILES} )

if( CMAKE_BUILD_TYPE STREQUAL "Debug" )
   # Add -g4 for sourcemap creation, and set the source-map-base (where the
   # debugger will look for the sourcemap file). 
   #
   # Make sure you have a trailing slash in the source-map-base. The filename
   # is directly appended to it.
   target_link_options( wasm-cpp-example PRIVATE 
                 -g4 --source-map-base http://localhost/wd/build/client/debug/ )
endif()

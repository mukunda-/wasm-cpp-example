#!/usr/bin/python3
import os
sh = os.system

if not os.path.exists( os.path.expanduser("~/emsdk") ):
   print( "emscripten SDK not found. Please make it available at ~/emsdk." )
   print( "Visit emscripten.org/docs to see the installation guide." )
   exit( 1 )

#------------------------------------------------------------------------------
# Including only a debug setup in this example. Release would be somewhat
# similar.
os.makedirs( "build/client/debug", exist_ok=True )
os.chdir( "build/client/debug" )

# For running CMake the first time.
if not os.path.exists( "Makefile" ):
   sh( "~/emsdk/upstream/emscripten/emcmake "
      +"cmake -DCMAKE_BUILD_TYPE=Debug ../../.." )

sh( "cmake --build ." )

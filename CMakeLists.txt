cmake_minimum_required(VERSION 3.1)
project(PyCI)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ../../pyci/lib) # TODO THIS IS UNSTABLE
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ../../pyci/lib) # TODO THIS IS UNSTABLE
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../../pyci/lib) # TODO THIS IS UNSTABLE


# Third Party
add_subdirectory(third_party/pybind11)

# Compiling
pybind11_add_module(example src/main.cpp)

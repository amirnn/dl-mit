cmake_minimum_required(VERSION 3.31.0)
project(dl-notes)

include(${CMAKE_CURRENT_SOURCE_DIR}/cmake/UseLatex.cmake)
add_latex_document(main.tex)
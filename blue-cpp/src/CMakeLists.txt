# src

# set_property(TARGET example-app PROPERTY CXX_STANDARD 17)

set(BLUE_DL_LIBRARY_NAME "blue-dl")
add_library(${BLUE_DL_LIBRARY_NAME} SHARED)
target_sources(
    ${BLUE_DL_LIBRARY_NAME}
    PRIVATE

    PUBLIC
    FILE_SET modules
    TYPE CXX_MODULES
    BASE_DIRS
    ../include
    modules/
    FILES
    ../include/Layer.ixx
    modules/layers/Dense.ixx
    modules/layers/Single.ixx
)

target_link_libraries(${BLUE_DL_LIBRARY_NAME} PUBLIC ${TORCH_LIBRARIES})

# The following code block is suggested to be used on Windows.
# According to https://github.com/pytorch/pytorch/issues/25457,
# the DLLs need to be copied to avoid memory errors.
if (MSVC)
  file(GLOB TORCH_DLLS "${TORCH_INSTALL_PREFIX}/lib/*.dll")
  add_custom_command(TARGET ${BLUE_DL_LIBRARY_NAME}
                     POST_BUILD
                     COMMAND ${CMAKE_COMMAND} -E copy_if_different
                     ${TORCH_DLLS}
                     $<TARGET_FILE_DIR:${BLUE_DL_LIBRARY_NAME}>)
endif (MSVC)
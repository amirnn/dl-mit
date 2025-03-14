# dependencies

# download libtorch in case needed
# thanks to https://github.com/pytorch/examples/blob/main/cpp/mnist/CMakeLists.txt
option(DOWNLOAD_LIBTROCH "Download the LibTorch" ON)
if (DOWNLOAD_LIBTROCH)
    message(STATUS "Downloading LibTorch")
    execute_process(
            COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/cmake/python/download_libtorch.py
            -d ${CMAKE_BINARY_DIR}/libtorch
            ERROR_VARIABLE DOWNLOAD_ERROR)
    if (DOWNLOAD_ERROR)
        message(FATAL_ERROR "Error downloading LibTorch: ${DOWNLOAD_ERROR}")
    endif()
endif()

# download mnist in case needed
# thanks to https://github.com/pytorch/examples/blob/main/cpp/mnist/CMakeLists.txt
option(DOWNLOAD_MNIST "Download the MNIST dataset from the internet" ON)
if (DOWNLOAD_MNIST)
    message(STATUS "Downloading MNIST dataset")
    execute_process(
            COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/cmake/python/download_mnist.py
            -d ${CMAKE_BINARY_DIR}/data
            ERROR_VARIABLE DOWNLOAD_ERROR)
    if (DOWNLOAD_ERROR)
        message(FATAL_ERROR "Error downloading MNIST dataset: ${DOWNLOAD_ERROR}")
    endif()
endif()


# LibTorch Needs patching described in the readme.

# for debug build
link_directories("${CMAKE_BINARY_DIR}/libtorch/out/libtorch/lib/")
find_package(Torch PATHS "${CMAKE_BINARY_DIR}/libtorch/out/libtorch" REQUIRED)

# for release build
# link_directories("C:/Local/pytorch-lib/release/libtorch/lib/")
# find_package(Torch PATHS "C:/Local/pytorch-lib/release/libtorch/share/cmake/Torch" REQUIRED)

# the same
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
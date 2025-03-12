# dependencies

# LibTorch Needs patching described in the readme.

# for debug build
link_directories("C:/Local/pytorch-lib/debug/libtorch/lib/")
find_package(Torch PATHS "C:/Local/pytorch-lib/debug/libtorch/share/cmake/Torch" REQUIRED)

# for release build
# link_directories("C:/Local/pytorch-lib/release/libtorch/lib/")
# find_package(Torch PATHS "C:/Local/pytorch-lib/release/libtorch/share/cmake/Torch" REQUIRED)

# the same
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
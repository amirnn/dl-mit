# C++ implementations for the course

## PyTorch library

### Building Patch

One needs to add the following lines to the line 131 in the file
"libtorch/share/cmake/Torch/TorchConfig.cmake". Thanks
to [here](https://github.com/pytorch/pytorch/pull/116926#issuecomment-1904728181)
and [here](https://github.com/pytorch/pytorch/issues/116242#issuecomment-1904725308).
The problem is that the nvtoolsext is now a header only library and there are
no artifacts for it in the cuda installation. So, we generate it ourselves.

```cmake
  if (TARGET torch::nvtoolsext)
    add_library(CUDA::nvToolsExt INTERFACE IMPORTED) # added
    set_property(TARGET CUDA::nvToolsExt APPEND PROPERTY
            INTERFACE_INCLUDE_DIRECTORIES "${CUDAToolkit_nvToolsExt_INCLUDE_DIRS}") # added
    list(APPEND TORCH_CUDA_LIBRARIES torch::nvtoolsext) # same as before
endif ()
```

## References

Please have a look at the following urls.

- https://pytorch.org/cppdocs/frontend.html
- https://github.com/pytorch/examples/tree/main/cpp
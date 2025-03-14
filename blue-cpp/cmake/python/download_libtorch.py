from __future__ import division
from __future__ import print_function

import argparse
import zipfile
import os
import sys
import urllib
import platform

try:
    from urllib.error import URLError
    from urllib.request import urlretrieve
except ImportError:
    from urllib2 import URLError
    from urllib import urlretrieve

Resources: dict[str, tuple[str]] = {
    "Linux": (
        # https://download.pytorch.org/libtorch/cpu/libtorch-cxx11-abi-shared-with-deps-2.6.0%2Bcpu.zip, # wo CUDA
        "https://download.pytorch.org/libtorch/cu126/libtorch-cxx11-abi-shared-with-deps-2.6.0%2Bcu126.zip", # CUDA
    ),
    "Darwin": (
        "https://download.pytorch.org/libtorch/cpu/libtorch-macos-arm64-2.6.0.zip",
    ),
    "Windows": (
        # https://download.pytorch.org/libtorch/cpu/libtorch-win-shared-with-deps-2.6.0%2Bcpu.zip, # wo CUDA
        # https://download.pytorch.org/libtorch/cpu/libtorch-win-shared-with-deps-debug-2.6.0%2Bcpu.zip, # wo CUDA
        "https://download.pytorch.org/libtorch/cu126/libtorch-win-shared-with-deps-2.6.0%2Bcu126.zip", # CUDA
        "https://download.pytorch.org/libtorch/cu126/libtorch-win-shared-with-deps-debug-2.6.0%2Bcu126.zip", # CUDA
    ),
}

Items: dict[str, tuple[str]] = {
    "Linux": (
        # "libtorch-cxx11-abi-shared-with-deps-2.6.0+cpu.zip", # wo CUDA
        "libtorch-cxx11-abi-shared-with-deps-2.6.0+cu126.zip", # CUDA
        ),
    "Darwin": ("libtorch-macos-arm64-2.6.0.zip",),
    "Windows": (
        # "libtorch-win-shared-with-deps-2.6.0+cpu.zip", # wo CUDA
        # "libtorch-win-shared-with-deps-debug-2.6.0+cpu.zip", # wo CUDA
        "libtorch-win-shared-with-deps-2.6.0+cu126.zip",
        "libtorch-win-shared-with-deps-debug-2.6.0+cu126.zip",
    ),
}


def report_download_progress(chunk_number, chunk_size, file_size):
    if file_size != -1:
        percent = min(1, (chunk_number * chunk_size) / file_size)
        bar = "#" * int(64 * percent)
        sys.stdout.write("\r0% |{:<64}| {}%".format(bar, int(percent * 100)))


def download(destination_path, url, quiet):
    if os.path.exists(destination_path):
        if not quiet:
            print("{} already exists, skipping ...".format(destination_path))
    else:
        print("Downloading {} ...".format(url))
        try:
            hook = None if quiet else report_download_progress
            urlretrieve(url, destination_path, reporthook=hook)
        except URLError:
            raise RuntimeError("Error downloading resource!")
        finally:
            if not quiet:
                # Just a newline.
                print()


def unzip(zipped_path, quiet):
    unzipped_path = "./libtorch/out" # os.path.splitext(zipped_path)[0]
    if os.path.exists(unzipped_path):
        if not quiet:
            print("{} already exists, skipping ... ".format(unzipped_path))
        return
    # with gzip.open(zipped_path, "rb") as zipped_file:
    #     with open(unzipped_path, "wb") as unzipped_file:
    #         unzipped_file.write(zipped_file.read())
    #         if not quiet:
    #             print("Unzipped {} ...".format(zipped_path))
    
    with zipfile.ZipFile(zipped_path,"r") as zip_ref:
        zip_ref.extractall(unzipped_path)



def main():
    parser = argparse.ArgumentParser(description="Download the lib-torch")
    parser.add_argument(
        "-d", "--destination", default="./libtorch", help="Destination directory"
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Don't report about progress"
    )
    options = parser.parse_args()

    if not os.path.exists(options.destination):
        os.makedirs(options.destination)

    try:
        system  = platform.system()
        sources = Resources[system]
        item = 0
        for source in sources:
            path = os.path.join(options.destination, Items[system][item])
            url = source
            download(path, url, options.quiet)
            unzip(path, options.quiet)
            item += 1
    except KeyboardInterrupt:
        print("Interrupted")


if __name__ == "__main__":
    main()

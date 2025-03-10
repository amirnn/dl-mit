#!/opt/homebrew/bin/zsh

cwd=$(pwd)
OUT_FOLDER="out"

echo "Command issued: ${1}"

if [[ ${1} = "build" ]]; then
    echo "Building..."
    if [ ! -d ${cwd}/${OUT_FOLDER} ]; then
        mkdir ${OUT_FOLDER}
    fi
    cd ${OUT_FOLDER}
    cmake ..
    make all
    cd ${cwd}
elif [[ ${1} = "clean" ]]; then
    echo "Cleaning..."
    cd ${OUT_FOLDER}
    make clean
    cd ${cwd}
fi

cmake_minimum_required(VERSION 3.8)
project(fcitx5-sitelen-pona
    VERSION 0.1.0
)

find_package(LibIMETable REQUIRED)
find_package(Fcitx5Utils REQUIRED)
find_package(Fcitx5Core REQUIRED)

# Setup some compiler option that is generally useful and compatible with Fcitx 5 (C++17)
include("${FCITX_INSTALL_CMAKECONFIG_DIR}/Fcitx5Utils/Fcitx5CompilerSettings.cmake")

add_subdirectory(src)
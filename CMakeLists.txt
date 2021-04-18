cmake_minimum_required(VERSION 3.17)
project(hw4)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(way1 main.cpp map.h)
target_link_libraries(way1 ${OpenCV_LIBS})

add_custom_command(
        OUTPUT ${CMAKE_SOURCE_DIR}/map.h
        COMMAND python3 ${CMAKE_SOURCE_DIR}/create_map.py
)

add_executable(way2 main2.cpp map.h)
target_link_libraries(way2 ${OpenCV_LIBS})

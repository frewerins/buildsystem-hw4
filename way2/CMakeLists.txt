add_custom_command(
        OUTPUT ${CMAKE_SOURCE_DIR}/way2/map.h
        COMMAND python3 ${CMAKE_SOURCE_DIR}/codegeneration/create_map.py
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/way2
)

add_executable(way2 main.cpp map.h)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
target_link_libraries(way2 ${OpenCV_LIBS})

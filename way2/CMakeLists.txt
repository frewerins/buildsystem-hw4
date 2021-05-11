find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_custom_target(create_map ALL
        COMMAND echo "end codogeneration"
        DEPENDS ${CMAKE_SOURCE_DIR}/map.h
        VERBATIM
        )

add_custom_command(
        OUTPUT ${CMAKE_SOURCE_DIR}/map.h
        COMMAND echo "start codogeneration"
        COMMAND python3 ${CMAKE_SOURCE_DIR}/way2/create_map.py
)


add_executable(way2 main2.cpp)
add_dependencies(way2 create_map)
target_link_libraries(way2 ${OpenCV_LIBS})

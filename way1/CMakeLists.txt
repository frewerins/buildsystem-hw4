find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(way1 main.cpp)
target_link_libraries(way1 ${OpenCV_LIBS})
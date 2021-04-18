add_executable(way1 main.cpp)
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
target_link_libraries(way1 ${OpenCV_LIBS})

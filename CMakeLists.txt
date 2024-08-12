cmake_minimum_required(VERSION 3.0)
project(proto C)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Add the source files for the exp_app
set(${PROJECT_NAME}_SOURCES  
    ${CMAKE_CURRENT_LIST_DIR}/nanopb/pb_common.c
    ${CMAKE_CURRENT_LIST_DIR}/nanopb/pb_encode.c
    ${CMAKE_CURRENT_LIST_DIR}/nanopb/pb_decode.c
    ${CMAKE_CURRENT_LIST_DIR}/proto_c/gpio.pb.c
    ${CMAKE_CURRENT_LIST_DIR}/proto_c/uart.pb.c
    ${CMAKE_CURRENT_LIST_DIR}/proto_c/i2c.pb.c
    ${CMAKE_CURRENT_LIST_DIR}/proto_c/ctrl.pb.c
)

# Create the static library target
add_library(${PROJECT_NAME} STATIC ${${PROJECT_NAME}_SOURCES})

# Set the include directories for the proto library
target_include_directories(${PROJECT_NAME} PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}/.
    ${CMAKE_CURRENT_LIST_DIR}/nanopb
)

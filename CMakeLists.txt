cmake_minimum_required(VERSION 3.0)
project(proto C)

set(CMAKE_CXX_STANDARD GNU89)

# Add the source files for the exp_app
set(${PROJECT_NAME}_SOURCES  
    ${CMAKE_CURRENT_LIST_DIR}/nanopb/pb_common.c
    ${CMAKE_CURRENT_LIST_DIR}/nanopb/pb_encode.c
    ${CMAKE_CURRENT_LIST_DIR}/nanopb/pb_decode.c
    ${CMAKE_CURRENT_LIST_DIR}/proto_c/gpio.pb.c
    ${CMAKE_CURRENT_LIST_DIR}/proto_c/uart.pb.c
)

# Create the static library target
add_library(${PROJECT_NAME} STATIC ${${PROJECT_NAME}_SOURCES})

# Set the include directories for the proto library
target_include_directories(${PROJECT_NAME} PUBLIC
    ${CMAKE_CURRENT_LIST_DIR}/.
    ${CMAKE_CURRENT_LIST_DIR}/nanopb
)

add_custom_command(TARGET ${PROJECT_NAME}
    POST_BUILD
    COMMAND ${ARM_NONE_EABI_OBJDUMP} -h -S lib${PROJECT_NAME}.a > ${PROJECT_NAME}.list
)

file(GLOB ClientFiles ${CMAKE_SOURCE_DIR}/client/*.py)

add_custom_target(copy ALL)
foreach(ClientFile ${ClientFiles})
    add_custom_command(TARGET copy PRE_BUILD
        COMMAND ${CMAKE_COMMAND} -E
            copy ${ClientFile} ${CMAKE_SOURCE_DIR}/Release/Client/)
endforeach()

file(COPY images DESTINATION ${CMAKE_SOURCE_DIR}/Release/Client/)

file(COPY TerminalModules DESTINATION ${CMAKE_SOURCE_DIR}/Release/Client/)
file(COPY DropperModules DESTINATION ${CMAKE_SOURCE_DIR}/Release/Client/)

file(COPY DropperModules.conf DESTINATION ${CMAKE_SOURCE_DIR}/Release/Client/)


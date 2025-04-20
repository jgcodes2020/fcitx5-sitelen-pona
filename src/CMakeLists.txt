
configure_file(sitelen-pona-addon.conf.in sitelen-pona-addon.conf)
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/sitelen-pona-addon.conf" RENAME sitelen-pona.conf DESTINATION "${FCITX_INSTALL_PKGDATADIR}/addon")
# Make the dictionary
set(mb_file "${CMAKE_CURRENT_BINARY_DIR}/sitelen-pona.main.dict")
add_custom_command(OUTPUT "sitelen-pona.main.dict"
  DEPENDS "sitelen-pona.txt"
  COMMAND LibIME::tabledict ARGS "${CMAKE_CURRENT_SOURCE_DIR}/sitelen-pona.txt"
  "${CMAKE_CURRENT_BINARY_DIR}/sitelen-pona.main.dict")
add_custom_target(table_data ALL DEPENDS "${mb_file}")

# Input Method registration file
install(FILES "${CMAKE_CURRENT_SOURCE_DIR}/sitelen-pona.conf" DESTINATION "${FCITX_INSTALL_PKGDATADIR}/inputmethod")
# Table dictionary
install(FILES "${mb_file}" DESTINATION "${FCITX_INSTALL_PKGDATADIR}/table")
###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$current_data_path = "${dir_datas}modules/$form{'m'}/$form{'m'}\.dat";
@current_data = &loadfile($current_data_path);
@db_fields_elements = ('elements_id','num','name','type_of_element','html_size','html_rows','html_cols','html_id','element_type','check_type','on_event','html_tag_free','text_min','text_max','enable_filetypes','filesize_min','filesize_max','checked_min','checked_max','element_valus','element_text','html_example','note','element_error_message','must_disp','default_value','system_disp_false','html_tag_free_top','elements_class','smartphone_element_type','confirm_hidden','return_hidden','or_disp','log_hidden');

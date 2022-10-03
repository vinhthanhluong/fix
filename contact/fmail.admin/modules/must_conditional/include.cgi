###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$current_data_path = "${dir_datas}modules/$form{'m'}/$form{'m'}\.dat";
@current_data = &loadfile($current_data_path);
@db_fields_elements = ('conditional_id','must_name','error_message','must_elements','note','conditional_type','conditional_element','conditional_value');

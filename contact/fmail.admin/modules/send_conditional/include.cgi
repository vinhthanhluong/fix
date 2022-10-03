###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$current_data_path = "${dir_datas}modules/$form{'m'}/$form{'m'}\.dat";
@current_data = &loadfile($current_data_path);
@db_fields_elements = ('conditional_id','conditional_type','conditional_name','conditional_element','conditional_value','mailaddress','numname','subject','body','note','cc','bcc');

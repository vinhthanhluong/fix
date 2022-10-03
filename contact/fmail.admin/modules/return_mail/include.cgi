###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$current_data_path = "${dir_datas}modules/$form{'m'}/$form{'m'}\.dat";
@current_data = &loadfile($current_data_path);
@db_fields_elements = ('return_mail_id','return_mail_type','return_mail_name','return_mail_element','return_mail_value','flag','from','sender','subject','serials','email_field','body');

###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################
$current_data_path = "$reg{'dir_module_data'}$form{'m'}/$form{'m'}\.dat";
@current_data = &loadfile($current_data_path);
@user_db_fields = ('note_id','note_title','note_body');

###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

@users = &loadfile("${dir_datas}${file_users}");
@user_db_fields = ('form_user_id','form_user_password','form_user_power','form_user_email','form_display_name','form_user_email_mobile','form_user_note');

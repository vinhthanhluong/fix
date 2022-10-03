###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '項目の削除完了';
@current_data = grep(!/^$form{'id'}\t/,@current_data);
&savefile($current_data_path,@current_data);
$redirect = "?m=$form{'m'}";

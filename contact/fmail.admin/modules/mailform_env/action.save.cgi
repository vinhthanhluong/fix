###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'メールフォーム設定の更新';
for($cnt=0;$cnt<@db_fields;$cnt++){
	$form{$db_fields[$cnt]} = &WppEncodeCharOptimize($form{$db_fields[$cnt]});
	push @save_fields,$form{$db_fields[$cnt]};
}
&savefile($current_data_path,@save_fields);
&mfp_SaveLine('./datas/serial.dat',$form{'serial_num'});

$redirect = "?m=$form{'m'}\&stat=update";

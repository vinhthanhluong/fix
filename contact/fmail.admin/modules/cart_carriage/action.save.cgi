###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '商品カート送料設定の更新';
for($cnt=0;$cnt<@db_fields;$cnt++){
	$form{$db_fields[$cnt]} = &WppEncodeCharOptimize($form{$db_fields[$cnt]});
	push @save_fields,$form{$db_fields[$cnt]};
}
&savefile($current_data_path,@save_fields);

$redirect = "?m=$form{'m'}\&stat=update";

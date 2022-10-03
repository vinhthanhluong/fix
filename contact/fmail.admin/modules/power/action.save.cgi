###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '権限の追加/更新';
for($cnt=0;$cnt<@current_db_fields;$cnt++){
	$form{$current_db_fields[$cnt]} = &WppEncodeCharOptimize($form{$current_db_fields[$cnt]});
	push @save_fields,$form{$current_db_fields[$cnt]};
}
$save_flag = 1;
if($form{'id'}){
	$save_mode = '更新';
	@current_data = grep(!/^$form{'id'}\t/,@current_data);
}
else {
	$save_mode = '追加';
	@conflict_mache = grep(/^$form{'form_power_id'}\t/,@current_data);
	if(@conflict_mache > 0){
		$save_flag = 0;
	}
}

if($form{'form_power_id'} eq $null){
	$save_flag = 0;
}

if($save_flag){
	$save_field = join("\t",@save_fields);
	unshift @current_data,$save_field;
	&savefile($current_data_path,@current_data);
	$end_status = "権限 $form{'power_id'} が${save_mode}されました";
	&rebuild_powers;
}
else {
	$end_status = "IDが重複しているか値がありません";
}
$print_html = <<"EOF";
<div class="screen">
	<p>${end_status}</p>
	<p><a href="?m=$form{'m'}">さらに追加/更新を行う</a></p>
</div>
EOF

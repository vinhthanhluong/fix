###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'お知らせの追加/更新';
for($cnt=0;$cnt<@user_db_fields;$cnt++){
	$form{$user_db_fields[$cnt]} = &WppEncodeCharOptimize($form{$user_db_fields[$cnt]});
	push @save_fields,$form{$user_db_fields[$cnt]};
}
$save_flag = 1;
if($form{'id'}){
	$save_mode = '更新';
	@current_data = grep(!/^$form{'id'}\t/,@current_data);
}
else {
	$save_mode = '追加';
	@conflict_mache = grep(/^$form{'note_id'}\t/,@current_data);
	if(@conflict_mache > 0){
		$save_flag = 0;
	}
}

if($form{'note_id'} eq $null){
	$save_flag = 0;
}

if($save_flag){
	$save_field = join("\t",@save_fields);
	unshift @current_data,$save_field;
	&savefile($current_data_path,@current_data);
	$end_status = "お知らせ $form{'note_id'} が${save_mode}されました";
}
else {
	$end_status = "IDが重複しているか値がありません";
}
$print_html = <<"EOF";
<div class="screen">
	<p>${end_status}</p>
	$thum_path
	<p><a href="?m=$form{'m'}">さらに追加/更新を行う</a></p>
</div>
EOF

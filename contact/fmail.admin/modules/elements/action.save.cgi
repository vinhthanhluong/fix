###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '項目の';

$form{'num'} = sprintf("%04d",$form{'num'});

if($form{'element_type'} eq "textarea"){
	$form{'default_value'} = $form{'default_value_textarea'};
}

for($cnt=0;$cnt<@db_fields_elements;$cnt++){
	$form{$db_fields_elements[$cnt]} = &WppEncodeCharOptimize($form{$db_fields_elements[$cnt]});
	push @save_fields,$form{$db_fields_elements[$cnt]};
}

$save_flag = 1;
if($form{'id'}){
	$save_mode = '更新';
	@current_data = grep(!/^$form{'id'}\t/,@current_data);
}
else {
	$save_mode = '追加';
	@conflict_mache = grep(/^$form{'elements_id'}\t/,@current_data);
	if(@conflict_mache > 0){
		$save_flag = 0;
	}
}

if($form{'elements_id'} eq $null){
	$save_flag = 0;
}

$action_name .= $save_mode;
if($save_flag){
	$save_field = join("\t",@save_fields);
	push @current_data,$save_field;
	@current_data = sort { (split(/\t/,$b))[1] cmp (split(/\t/,$a))[1]} @current_data;
	&savefile($current_data_path,@current_data);
	$end_status = "管理ユーザ $form{'user_id'} が${save_mode}されました";
	$redirect = "?m=$form{'m'}";
}
else {
	$print_html = <<"	EOF";
	<div class="screen">
		<p>IDが重複しているか値がありません</p>
		<p><a href="?m=$form{'m'}">さらに追加/更新を行う</a></p>
	</div>
	EOF
}

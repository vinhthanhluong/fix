###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'レジストリの追加/更新';
for($cnt=0;$cnt<@registry_db_fields;$cnt++){
	$form{$registry_db_fields[$cnt]} = &WppEncodeCharOptimize($form{$registry_db_fields[$cnt]});
	push @save_fields,$form{$registry_db_fields[$cnt]};
}
$save_flag = 1;
if($form{'id'}){
	$save_mode = '更新';
	@registry = grep(!/^$form{'id'}\t/,@registry);
}
else {
	$save_mode = '追加';
	@conflict_mache = grep(/^$form{'form_registry_id'}\t/,@registry);
	if(@conflict_mache > 0){
		$save_flag = 0;
	}
}
if($form{'form_registry_id'} eq $null){
	$save_flag = 0;
}
if($save_flag){
	$save_field = join("\t",@save_fields);
	#push @registry,$save_field;
	unshift @registry,$save_field;
	&savefile("${dir_datas}${file_registry}",@registry);
	$end_status = "レジストリ $form{'registry_id'} が${save_mode}されました";
	$save_registry = "## REGISTRY FILE\n";
	for($cnt=0;$cnt<@registry;$cnt++){
		@regist = split(/\t/,$registry[$cnt]);
		if($regist[3]){
			@reg_list = split(/\,/,$regist[1]);
			$reg_list = join("\'\,\'",@reg_list);
			$save_registry .= '@' . $regist[0] . ' = (' . "\'${reg_list}\'" . ")\;\n";
		}
		else {
			$save_registry .= '$reg{"' . $regist[0] . '"} = ' . "\'${regist[1]}\'" . "\;\n";
		}
	}
	$save_registry .= "## REGISTRY FILE EOF";
	rename $registry,"${registry}\.backup";
	flock(FH, LOCK_EX);
		open(FH,">${registry}");
			print FH $save_registry;
		close(FH);
	flock(FH, LOCK_NB);
}
else {
	$end_status = "IDが重複しています";
}
$print_html = <<"EOF";
<div class="screen">
	<p>${end_status}</p>
	<p><a href="?m=$form{'m'}">さらに追加/更新を行う</a></p>
</div>
EOF

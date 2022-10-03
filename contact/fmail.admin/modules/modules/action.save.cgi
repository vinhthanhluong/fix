###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

@registry = &loadfile("${dir_datas}$form{'m'}\/$form{'module'}\.dat");
for($cnt=0;$cnt<@registry_db_fields;$cnt++){
	$form{$registry_db_fields[$cnt]} = &WppEncodeCharOptimize($form{$registry_db_fields[$cnt]});
	push @save_fields,$form{$registry_db_fields[$cnt]};
}
$save_flag = 1;
if($form{'id'} ne $null && $form{'id'} eq $form{'form_registry_id'}){
	$save_mode = '更新';
	@registry = grep(!/^$form{'id'}\t/,@registry);
}
else {
	$save_mode = '追加';
	@conflict_mache = grep(/^$form{'form_registry_id'}\t/,@registry);
}
$action_name = 'レジストリの' . $save_mode;
if($form{'form_registry_id'} eq $null){
	$save_flag = 0;
}
if($save_flag){
	$save_field = join("\t",@save_fields);
	push @registry,$save_field;
	&savefile("${dir_datas}$form{'m'}\/$form{'module'}\.dat",@registry);
	$end_status = "レジストリ $form{'registry_id'} が${save_mode}されました";
	$registry = "${dir_datas}$form{'m'}\/$form{'module'}\.cgi";
	$save_registry = "## REGISTRY FILE\n";
	for($cnt=0;$cnt<@registry;$cnt++){
		@regist = split(/\t/,$registry[$cnt]);
		if($regist[3]){
			@reg_list = split(/\,/,$regist[1]);
			$reg_list = join("\'\,\'",@reg_list);
			$save_registry .= '@' . $regist[0] . ' = (' . "\'${reg_list}\'" . ")\;\n";
		}
		else {
			$save_registry .= '$modules{"' . $regist[0] . '"} = ' . "\'${regist[1]}\'" . "\;\n";
		}
	}
	$save_registry .= "## REGISTRY FILE EOF";
	
	##rebuild module list
	@mache = grep(/^$form{'module'}\t/,@users);
	@module_record = split(/\t/,$mache[0]);
	%set = ();
	for($cnt=0;$cnt<@registry;$cnt++){
		@reg = split(/\t/,$registry[$cnt]);
		$set{$reg[0]} = $reg[1];
	}
	@module_fields = ($form{'module'},$module_record[1],$set{'name'},$set{'name_sub'},$set{"auth"});
	$module_fields = join("\t",@module_fields);
	@users = grep(!/^$form{'module'}\t/,@users);
	unshift @users,$module_fields;
	@users = sort { (split(/\t/,$b))[1] cmp (split(/\t/,$a))[1]} @users;
	&savefile("${dir_datas}$form{'m'}\.dat",@users);
	&rebuild_module_list;
	rename $registry,"${registry}\.backup";
	&WppSaveLine($registry,$save_registry);
	&rebuild_module_registry($form{'module'});
}
else {
	$end_status = "IDが重複しています";
}
$print_html = <<"EOF";
<div class="screen">
	<p>${end_status}</p>
	<p><a href="?m=$form{'m'}&a=reg&id=$form{'module'}">さらに追加/更新を行う</a></p>
</div>
EOF

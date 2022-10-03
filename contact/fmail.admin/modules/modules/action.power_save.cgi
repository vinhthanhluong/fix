###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = $form{'module'} . 'モジュール／' . $form{'id'} . 'のアクセス権の更新';
$current_path = "${dir_datas}$form{'m'}\/$form{'module'}\.power\.dat";

@current_data = &loadfile($current_path);
$save_mode = '更新';
@current_data = grep(!/^$form{'id'}\t/,@current_data);
@save_fields = ($form{'id'},$form{'post_powers'});
$save_field = join("\t",@save_fields);
unshift @current_data,$save_field;
&savefile($current_path,@current_data);
if($form{'id'} eq "module_main"){
	my(@rebuild_module_list) = &loadfile("${dir_datas}$form{'m'}\.dat");
	@current_record = grep(/^$form{'module'}\t/,@rebuild_module_list);
	@current_record = split(/\t/,$current_record[0]);
	@rebuild_module_list = grep(!/^$form{'module'}\t/,@rebuild_module_list);
	if($form{'post_powers'} ne "null"){
		@current_record_powers = split(/\,/,$form{'post_powers'});
		$current_record[4] = '%%' . join('%%,%%',@current_record_powers) . '%%';
	}
	else {
		$current_record[4] = "null";
	}
	$save_current_record = join("\t",@current_record);
	unshift @rebuild_module_list,$save_current_record;
	@rebuild_module_list = sort { (split(/\t/,$b))[1] cmp (split(/\t/,$a))[1]} @rebuild_module_list;
	&savefile("${dir_datas}$form{'m'}\.dat",@rebuild_module_list);
}
&rebuild_module_registry($form{'module'});
&rebuild_module_list;
$print_html = <<"EOF";
<div class="screen">
	<p>$form{'module'} モジュール／$form{'id'}のアクセス権を更新しました</p>
	<p><a href="?m=$form{'m'}&a=power&id=$form{'module'}">さらに更新を行う</a></p>
</div>
EOF

###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'モジュールのインストール';
$user_dir_path = "${dir_datas}modules/$form{'id'}\/";
mkdir $user_dir_path;
chmod 0777, $user_dir_path;
$module_path = "modules\/$form{'id'}\/";
$module_conf_path = "${module_path}set_registry.cgi";
if((-d $module_path) && (-f $module_conf_path)){
	%set = ();
	require $module_conf_path;
	@save_fields = ($form{'id'},"000",$set{'name'},$set{'name_sub'},$set{"auth"});
	$save_field = join("\t",@save_fields);
	push @users,$save_field;
	@users = sort { (split(/\t/,$b))[1] cmp (split(/\t/,$a))[1]} @users;
	&savefile("${dir_datas}$form{'m'}\.dat",@users);
	$end_status = "モジュール $form{'id'} がインストールされました";
	$session_data = "## MODULE \[ $form{'id'} \] REGISTRY FILE\n";
	foreach $key ( keys( %set ) ) {
		$session_data .= "\$modules\{\'${key}\'\} \= \'$set{$key}\'\;\n";
		$reg_dat .= "${key}\t$set{$key}\t${key}\n";
	}
	## action auth
	$session_data .= "\$modules\{\'auth\'\} \= \'null\'\;\n";
	$power_dat .= "module_main\tnull\n";
	my $dir = $module_path;
	opendir DH, $dir or die "$dir:$!";
	while (my $file = readdir DH) {
		next if $file =~ /^\.{1,2}$/;
		if($file =~ /action\.(.*?)\.cgi/si){
			$session_data .= "\$action_auth\{\'${1}\'\} \= \'null\'\;\n";
			$power_dat .= "${1}\tnull\n";
		}
	}
	closedir DH;
	## action auth eof
	$session_data .= "## MODULE \[ $form{'id'} \] REGISTRY EOF";
	&WppSaveLine("${dir_datas}$form{'m'}\/$form{'id'}\.cgi",$session_data);
	&WppSaveLine("${dir_datas}$form{'m'}\/$form{'id'}\.dat",$reg_dat);
	&WppSaveLine("${dir_datas}$form{'m'}\/$form{'id'}\.power\.dat",$power_dat);
	&rebuild_module_list;
}
else {
	$end_status = "インストールに失敗しました";
}
$print_html = <<"EOF";
<div class="screen">
	<p>${end_status}</p>
	$thum_path
	<p><a href="?m=$form{'m'}">さらにモジュールの管理を行う</a></p>
</div>
EOF

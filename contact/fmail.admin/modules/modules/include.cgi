###############################################################################
# include
###############################################################################

@users = &loadfile("${dir_datas}$form{'m'}\.dat");
@registry_db_fields = ('form_registry_id','form_registry_value','form_display_name','form_registry_type','form_registry_note');
@user_db_fields = ('form_user_id','form_user_password','form_user_power','form_user_email','form_display_name','form_user_note');

sub rebuild_module_list {
	my(@rebuild_module_list) = &loadfile("${dir_datas}$form{'m'}\.dat");
	my(@rebuild_add_module_list) = ();
	my(@rebuild_add_module_name) = ();
	my(@rebuild_add_module_sub) = ();
	my(@rebuild_add_module_power) = ();
	for(my($cnt)=0;$cnt<@rebuild_module_list;$cnt++){
		my(@rebuild_current_record) = split(/\t/,$rebuild_module_list[$cnt]);
		push @rebuild_add_module_list,$rebuild_current_record[0];
		push @rebuild_add_module_name,$rebuild_current_record[2];
		push @rebuild_add_module_sub,$rebuild_current_record[3];
		if($rebuild_current_record[4] eq $null){
			$rebuild_current_record[4] = "null";
		}
		push @rebuild_add_module_power,$rebuild_current_record[4];
	}
	$module_list_save = "## MODULE LIST FILE\n";
	$module_list_save .= "\@module_list = \(\'" . join("\'\,\'",@rebuild_add_module_list) . "\'\)\;\n";
	$module_list_save .= "\@module_list_names = \(\'" . join("\'\,\'",@rebuild_add_module_name) . "\'\)\;\n";
	$module_list_save .= "\@module_list_subnames = \(\'" . join("\'\,\'",@rebuild_add_module_sub) . "\'\)\;\n";
	$module_list_save .= "\@module_list_powers = \(\'" . join("\'\,\'",@rebuild_add_module_power) . "\'\)\;\n";
	#限定クライアント用の特殊処理
	$module_list_save .= "\@module_list_powers_limited = \(\'\%\%Admin\%\%\'\,\'\%\%Admin\%\%\'\,\'\%\%Admin\%\%\'\,\'\%\%Admin\%\%\'\,\'\%\%Admin\%\%\'\,\'\%\%limited-client\%\%\'\,\'\%\%Admin\%\%\'\,\'\%\%limited-client\%\%\'\,\'\%\%Admin\%\%\'\,\'\%\%Admin\%\%\'\,\'\%\%Admin\%\%\'\,\'\%\%Admin\%\%\'\,\'\%\%Admin\%\%\'\)\;\n";
	for(my($cnt)=0;$cnt<@rebuild_add_module_list;$cnt++){
		$module_list_save .= "\$module_list_id\{\'${module_list[$cnt]}\'\} = \'${cnt}\'\;\n";
	}
	$module_list_save .= "## MODULE LIST FILE EOF";
	&WppSaveLine("commons\/modulelist\.cgi",$module_list_save);
}
sub rebuild_module_registry {
	my($rebuild_module_name) = @_;
	my(@rebuild_module_registry) = &loadfile("${dir_datas}$form{'m'}\/${rebuild_module_name}\.dat");
	my(@rebuild_module_powers) = &loadfile("${dir_datas}$form{'m'}\/${rebuild_module_name}\.power\.dat");
	my($rebuild_module_registry_path) = "${dir_datas}$form{'m'}\/${rebuild_module_name}\.cgi";
	my($rebuild_module_registry_backup_path) = "${dir_datas}$form{'m'}\/${rebuild_module_name}\.cgi\.backup";
	my($rebuild_save_registry) = "## REGISTRY FILE\n";
	for(my($cnt)=0;$cnt<@rebuild_module_registry;$cnt++){
		my(@rebuild_regist) = split(/\t/,$rebuild_module_registry[$cnt]);
		if($rebuild_regist[3]){
			@reg_list = split(/\,/,$rebuild_regist[1]);
			$reg_list = join("\'\,\'",@reg_list);
			$rebuild_save_registry .= '@' . $rebuild_regist[0] . ' = (' . "\'${reg_list}\'" . ")\;\n";
		}
		else {
			$rebuild_save_registry .= '$modules{"' . $rebuild_regist[0] . '"} = ' . "\'${rebuild_regist[1]}\'" . "\;\n";
		}
	}
	for(my($cnt)=0;$cnt<@rebuild_module_powers;$cnt++){
		my(@rebuild_powers) = split(/\t/,$rebuild_module_powers[$cnt]);
		if($rebuild_powers[1] ne "null"){
			my(@powers) = split(/\,/,$rebuild_powers[1]);
			$rebuild_powers[1] = '%%' . join('%%,%%',@powers) . '%%';
		}
		if($rebuild_powers[0] eq "module_main"){
			$rebuild_save_registry .= '$modules{"auth"} = ' . "\'${rebuild_powers[1]}\'" . "\;\n";
		}
		else {
			$rebuild_save_registry .= '$action_auth{"' . $rebuild_powers[0] . '"} = ' . "\'${rebuild_powers[1]}\'" . "\;\n";
		}
	}
	$rebuild_save_registry .= "## REGISTRY FILE EOF";
	rename $rebuild_module_registry_path,$rebuild_module_registry_backup_path;
	&WppSaveLine($rebuild_module_registry_path,$rebuild_save_registry);
}

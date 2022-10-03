###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################
$current_data_path = "${dir_datas}$form{'m'}\.dat";
@current_data = &loadfile($current_data_path);
@current_db_fields = ('form_power_id','form_display_name','form_power_note');

sub rebuild_powers {
	@create_powers_ids = ();
	@create_powers_names = ();
	$session_data = "## POWER FILE\n";
	for($cnt=0;$cnt<@current_data;$cnt++){
		@current_record = split(/\t/,$current_data[$cnt]);
		$session_data .= "\$power\{\'" . $current_record[0] . "\'\} \= \'${current_record[1]}\'\;\n";
		push @create_powers_ids,$current_record[0];
		push @create_powers_names,$current_record[1];
	}
	$create_powers_ids = join("','",@create_powers_ids);
	$create_powers_names = join("','",@create_powers_names);
	$session_data .= "\@user_powers_id \= \(\'${create_powers_ids}\'\)\;\n";
	$session_data .= "\@user_powers \= \(\'${create_powers_names}\'\)\;\n";
	$session_data .= "## POWER FILE EOF";
	&WppSaveLine("./commons/$form{'m'}\.cgi",$session_data);
}

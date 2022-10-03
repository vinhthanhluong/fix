###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################
# ‘I‘ğíœ
if($form{'flag_delete_value'} eq 'del'){
	for($cnt=0;$cnt<@current_data;$cnt++){
		@record = split(/\t/,$current_data[$cnt]);
		$deleteid = 'delete_' . $record[0];
		if($record[0] ne $form{$deleteid}){
			$current_data_remake .= "$current_data[$cnt]\n";
		}
	}
	&savefile($current_data_path,$current_data_remake);
}else{
	# sort
	$form{'num'} = sprintf("%04d",$form{'num'});
	for($cnt=0;$cnt<@current_data;$cnt++){
		@record = split(/\t/,$current_data[$cnt]);
		$record[1] = sprintf("%04d",$form{$record[0]});
		$current_data[$cnt] = join("\t",@record);
	}
	@current_data = sort { (split(/\t/,$b))[1] cmp (split(/\t/,$a))[1]} @current_data;
	&savefile($current_data_path,@current_data);
}

$redirect = "?m=$form{'m'}";

$flag{'ajax'} = 1;
$current_data_path = $reg{'file_notice'};
$split_id = '<!--ajax_spalated_id-->';
@cache = stat($current_data_path);

if($form{'stmp'} < $cache[9]){
	@current_data = &WppLoadLine($current_data_path);
	if(index($module_list_powers[$module_list_id{$current_data[1]}],"%%$current_user{'power'}%%") > -1 || $module_list_powers[$module_list_id{$current_data[1]}] eq $null || $module_list_powers[$module_list_id{$current_data[1]}] eq "null"){
		if($current_data[1] eq $null){
			$html = "\[ SYSTEM \] ${current_data[2]}" . " \/ ${stmp}";
		}
		elsif($current_data[3] ne $null){
			$html = "\[ <a href=\"?m=${current_data[1]}\">" . $module_list_names[$module_list_id{$current_data[1]}] . "</a> \] <a href=\"${current_data[3]}\" target=\"_blank\">" . $current_data[2] . "</a>" . " \/ ${stmp}";
		}
		else {
			$html = "\[ <a href=\"?m=${current_data[1]}\">" . $module_list_names[$module_list_id{$current_data[1]}] . "</a> \] " . $current_data[2] . " \/ ${stmp}";
		}
		$html .= $split_id . $cache[9];
	}
	else {
		$html = "null";
	}
}
else {
	$html = "null";
}

###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

if($form{'postcode_data'} ne $null){
	$name = $form{'postcode_data'};
	if($q->param('postcode_data') ne $null){
		my $fH = $q->upload('postcode_data');
		@fl_names = split(/\(file\)/,$name);
		$name = $fl_names[0];
		$value = $fH;
		@filenames = split(/\\/,$value);
		$filename = $filenames[-1];
		@filetypes = split /\./,$filename;
		$filetype = $filetypes[-1];
		$save_file_name = "./datas/postcode_temp/temp.${filetype}";
		$binary = "";
		open (OUT, ">$save_file_name");
		binmode (OUT);
		while(read($fH, $buffer, 1024)){
			print OUT $buffer;
			$binary .= $buffer;
		}
		close (OUT);
		close ($fH) if ($CGI::OS ne 'UNIX');
		
		if($filetype eq "zip"){
			$redirect = "zip";
		}
		else {
			unlink $save_file_name;
			$form{'postcode_data'} = $binary;
			$form{'postcode_data'} =~ s/\r//g;
			$form{'postcode_data'} =~ s/\"//g;
			$form{'postcode_data'} =~ s/ //g;
			$csv = $form{'postcode_data'};
			Jcode::convert(\$csv,'utf8');
			@csv = split(/\n/,$csv);
			@record = split(/\,/,$csv[0]);
			$count = @record;
			if(15 == @record){
				if($name =~ /KEN_ALL\.CSV/ig){
					for($cnt=0;$cnt<100;$cnt++){
						$no = sprintf("%02d",$cnt);
						#@js = grep(/\"\,\"$no/,@csv);
						@js = grep(/^.*?,$no/,@csv);
						$js = join("\n",@js);
						$js =~ s/\r\n/\r/g;
						$js =~ s/\r/\n/g;
						flock(FH, LOCK_EX);
							open(FH,">./datas/postcodes/${no}.cgi");
								print FH $js;
							close(FH);
						flock(FH, LOCK_NB);
					}
					$statmsg = &encodeURI("${name}から辞書を更新しました。");
				}
				elsif($name =~ /add_/ig){
					## update
					%file_number_flag = ();
					for($cnt=0;$cnt<@csv;$cnt++){
						@record = split(/\,/,$csv[$cnt]);
						$file_number = substr($record[2], 0, 2);
						$csv[$cnt] .= "\t${file_number}";
						if(!$file_number_flag{$file_number}){
							$file_number_flag{$file_number} = 1;
							push @file_list,$file_number;
						}
					}
					for($cnt=0;$cnt<@file_list;$cnt++){
						@original = &loadfile("${current_data_path}${file_list[$cnt]}\.cgi");
						@pickup = grep(/\t${file_list[$cnt]}$/,@csv);
						for($i=0;$i<@pickup;$i++){
							@record = split(/\,/,$pickup[$i]);
							@original = grep(!/${record[2]}/,@original);
							push @original,join(',',@record);
						}
						&savefile("${current_data_path}${file_list[$cnt]}\.cgi",@original);
					}
					$statmsg = &encodeURI("${name}から辞書を更新しました。");
				}
				elsif($name =~ /del_/ig) {
					## delete
					%file_number_flag = ();
					for($cnt=0;$cnt<@csv;$cnt++){
						@record = split(/\,/,$csv[$cnt]);
						$file_number = substr($record[2], 0, 2);
						$csv[$cnt] .= "\t${file_number}";
						if(!$file_number_flag{$file_number}){
							$file_number_flag{$file_number} = 1;
							push @file_list,$file_number;
						}
					}
					for($cnt=0;$cnt<@file_list;$cnt++){
						@original = &loadfile("${current_data_path}${file_list[$cnt]}\.cgi");
						@pickup = grep(/\t${file_list[$cnt]}$/,@csv);
						for($i=0;$i<@pickup;$i++){
							@record = split(/\,/,$pickup[$i]);
							@original = grep(!/${record[2]}/,@original);
						}
						&savefile("${current_data_path}${file_list[$cnt]}\.cgi",@original);
					}
					$statmsg = &encodeURI("${name}から辞書を更新しました。");
				}
				else {
					$errormsg = &encodeURI('該当しないCSVファイルです。');
				}
				$redirect = "?m=$form{'m'}\&stat=update&statmsg=${statmsg}&error=${errormsg}";
			}
			else {
				$errormsg = &encodeURI('CSVファイルの中身が誤っています。');
				$redirect = "?m=$form{'m'}\&stat=updateerror&error=${errormsg}";
			}
		}
	}
	else {
		$redirect = "?m=$form{'m'}\&stat=updateerror&${count}";
	}
}
else {
	$redirect = "?m=$form{'m'}\&stat=updateerror";
}
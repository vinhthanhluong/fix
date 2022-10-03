###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################
my $dir = './datas/postcode_temp/';
@stats = ();
@files = ();
opendir DH, $dir;
while (my $file = readdir DH) {
	next if $file =~ /^\.{1,2}$/;
	$filesize = -s "${dir}${file}";
	if($filesize > 0){
		if($file =~ /KEN_ALL\.CSV/ig){
			flock(FH, LOCK_EX);
				open(FH,"${dir}${file}");
					@csv = <FH>;
				close(FH);
			flock(FH, LOCK_NB);
			unlink "${dir}${file}";
			$csv = join('<->',@csv);
			Jcode::convert(\$csv,'utf8');
			@csv = split(/<->/,$csv);
			for($cnt=0;$cnt<100;$cnt++){
				$no = sprintf("%02d",$cnt);
				@js = grep(/\"\,\"$no/,@csv);
				$js = join("",@js);
				$js =~ s/\r\n/\r/g;
				$js =~ s/\r/\n/g;
				$js =~ s/$befor/$after/g;
				flock(FH, LOCK_EX);
					open(FH,">./datas/postcodes/${no}.cgi");
						print FH $js;
					close(FH);
				flock(FH, LOCK_NB);
			}
			push @stats,$file;
		}
		elsif($file =~ /ADD_.*?\.CSV/ig){
			flock(FH, LOCK_EX);
				open(FH,"${dir}${file}");
					@csv = <FH>;
				close(FH);
			flock(FH, LOCK_NB);
			unlink "${dir}${file}";
			$csv = join("",@csv);
			$csv =~ s/\r//g;
			$csv =~ s/\"//g;
			Jcode::convert(\$csv,'utf8');
			@csv = split(/\n/,$csv);
			@record = split(/\,/,$csv[0]);
			$count = @record;
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
			push @stats,$file;
		}
		elsif($file =~ /DEL_.*?\.CSV/ig){
			flock(FH, LOCK_EX);
				open(FH,"${dir}${file}");
					@csv = <FH>;
				close(FH);
			flock(FH, LOCK_NB);
			unlink "${dir}${file}";
			$csv = join("",@csv);
			$csv =~ s/\r//g;
			$csv =~ s/\"//g;
			Jcode::convert(\$csv,'utf8');
			@csv = split(/\n/,$csv);
			@record = split(/\,/,$csv[0]);
			$count = @record;
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
			push @stats,$file;
		}
		else {
			unlink "${dir}${file}";
			push @errors,$file;
		}
	}
}
if(@stats > 0){
	$statmsg = join('、',@stats) . 'を処理しました。';
}
if(@errors > 0){
	$errormsg = join('、',@errors) . 'は対応していないファイルです。';
}
$statmsg = &encodeURI($statmsg);
$errormsg = &encodeURI($errormsg);
closedir DH;
$redirect = "?m=$form{'m'}\&stat=update&statmsg=${statmsg}&error=${errormsg}";

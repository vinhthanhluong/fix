###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '管理ユーザの追加/更新';
$save_flag = 1;
if($form{'id'}){
	$save_mode = '更新';
	@current = grep(/^$current_user{'id'}\t/,@users);
	@current_record = split(/\t/,$current[0]);
	for($cnt=0;$cnt<@user_db_fields;$cnt++){
		$form{$user_db_fields[$cnt]} = &WppEncodeCharOptimize($form{$user_db_fields[$cnt]});
		if($form{$user_db_fields[$cnt]} ne $null){
			if($cnt == 1){
				if($form{$user_db_fields[$cnt]} ne 'admin' && $form{$user_db_fields[$cnt]} !~ /^admin_/){
					$form{$user_db_fields[$cnt]} = md5_hex($form{$user_db_fields[$cnt]});
				}
			}
			push @save_fields,$form{$user_db_fields[$cnt]};
		}
		else {
			push @save_fields,$current_record[$cnt];
		}
	}
	@users = grep(!/^$current_user{'id'}\t/,@users);
}
else {
	$save_mode = '追加';
	$save_flag = 0;
}
if($save_flag){
	##picture proccess
	if($form{'form_display_picture'} ne $null){
		#dir_user_pictures
		chmod 0777, "$reg{'dir_user_pictures'}$current_user{'id'}.jpg";
		chmod 0777, "$reg{'dir_user_pictures'}thum_$current_user{'id'}.jpg";
		flock(FH, LOCK_EX);
			open (OUT, ">$reg{'dir_user_pictures'}$current_user{'id'}.jpg");
				binmode (OUT);
				print (OUT $form{'form_display_picture'});
			close (OUT);
		flock(FH, LOCK_NB);
		#thum_jpg.php
		$thum_path = "<p>サムネイル生成：<script type=\"text/javascript\" src=\"$reg{'dir_user_pictures'}thum_jpg.php?path=$current_user{'id'}.jpg&w=$reg{'dir_user_pictures_thum_size'}\"></script></p>";
	}
	elsif($form{'picture_delete'}){
		chmod 0777, "$reg{'dir_user_pictures'}$current_user{'id'}.jpg";
		chmod 0777, "$reg{'dir_user_pictures'}thum_$current_user{'id'}.jpg";
		unlink "$reg{'dir_user_pictures'}$current_user{'id'}.jpg";
		unlink "$reg{'dir_user_pictures'}thum_$current_user{'id'}.jpg";
		$debug = "$reg{'form_display_picture'}$current_user{'id'}.jpg";
	}
	##dir create
	$user_dir_path = "$reg{'users_dirs'}$current_user{'id'}\/";
	$user_cache = "$reg{'users_dirs'}$current_user{'id'}\/cache\.dat";
	$save_field = join("\t",@save_fields);
	push @users,$save_field;
	&savefile("${dir_datas}${file_users}",@users);
	$end_status = "登録情報が更新されました";
	
	@current_user_field = ('id','pw','power','email','name','mobile_email','note');
	$session_data = "## SESSION FILE\n";
	for($cnt=0;$cnt<@current_user_field;$cnt++){
		if($save_fields[$cnt] ne $null){
			$session_data .= "\$current_user\{\'" . $current_user_field[$cnt] . "\'\} \= \'${save_fields[$cnt]}\'\;\n";
		}
	}
	$session_data .= "## SESSION FILE EOF";
	&WppSaveLine($user_cache,$session_data);
	#$redirect = "?m=$form{'m'}";
}
else {
	$end_status = "IDが重複しているか値がありません";
}
$print_html = <<"EOF";
<div class="screen">
	<p>${end_status}</p>
	${thum_path}
	${debug}
	<p><a href="?m=$form{'m'}">登録情報を確認する</a></p>
</div>
EOF

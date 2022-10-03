###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '管理ユーザの追加/更新';
for($cnt=0;$cnt<@user_db_fields;$cnt++){
	$form{$user_db_fields[$cnt]} = &WppEncodeCharOptimize($form{$user_db_fields[$cnt]});
	# 初期設定パスワードでなければ、暗号化する
	if($form{$user_db_fields[$cnt]} ne 'admin' && $form{$user_db_fields[$cnt]} !~ /^admin_/ ){
		if($cnt == 1){
			$form{$user_db_fields[$cnt]} = md5_hex($form{$user_db_fields[$cnt]});
		}
	}
	push @save_fields,$form{$user_db_fields[$cnt]};
}
$save_flag = 1;
if($form{'id'}){
	$save_mode = '更新';
	@users = grep(!/^$form{'id'}\t/,@users);
}
else {
	$save_mode = '追加';
	@conflict_mache = grep(/^$form{'form_user_id'}\t/,@users);
	if(@conflict_mache > 0){
		$save_flag = 0;
	}
}

if($form{'form_user_id'} eq $null){
	$save_flag = 0;
}

if($save_flag){
	##picture proccess
	if($form{'form_display_picture'} ne $null){
		#dir_user_pictures
		flock(FH, LOCK_EX);
			open (OUT, ">$reg{'dir_user_pictures'}$form{'form_user_id'}.jpg");
				binmode (OUT);
				print (OUT $form{'form_display_picture'});
			close (OUT);
		flock(FH, LOCK_NB);
		#thum_jpg.php
		$thum_path = "<p>サムネイル生成：<script type=\"text/javascript\" src=\"$reg{'dir_user_pictures'}thum_jpg.php?path=$form{'form_user_id'}.jpg&w=$reg{'dir_user_pictures_thum_size'}\"></script></p>";
	}
	elsif($form{'picture_delete'}){
		unlink "$reg{'dir_user_pictures'}$form{'form_user_id'}.jpg";
		unlink "$reg{'dir_user_pictures'}thum_$form{'form_user_id'}.jpg";
	}
	##dir create
	$user_dir_path = "$reg{'users_dirs'}$form{'form_user_id'}\/";
	$user_cache = "$reg{'users_dirs'}$form{'form_user_id'}\/cache\.dat";
	mkdir ($user_dir_path, 0777);
	chmod 0777, $user_dir_path;
	$save_field = join("\t",@save_fields);
	push @users,$save_field;
	&savefile("${dir_datas}${file_users}",@users);
	$end_status = "管理ユーザ $form{'user_id'} が${save_mode}されました";
	
	@current_user_field = ('id','pw','power','email','name','mobile_email','note');
	$session_data = "## SESSION FILE\n";
	for($cnt=0;$cnt<@current_user_field;$cnt++){
		if($save_fields[$cnt] ne $null){
			$session_data .= "\$current_user\{\'" . $current_user_field[$cnt] . "\'\} \= \'${save_fields[$cnt]}\'\;\n";
		}
	}
	$session_data .= "## SESSION FILE EOF";
	&WppSaveLine($user_cache,$session_data);
}
else {
	$end_status = "IDが重複しているか値がありません";
}
$print_html = <<"EOF";
<div class="screen">
	<p>${end_status}</p>
	$thum_path
	<p><a href="?m=$form{'m'}">さらに追加/更新を行う</a></p>
</div>
EOF

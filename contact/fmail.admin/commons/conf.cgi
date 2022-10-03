#WebSiteAdmin config file

$registry = './commons/registry.cgi';

## attached mode 1:ON / 0:OFF
$attached_method = 1;

##auther
$admin_mail = 'kaihatsu@freesale.co.jp';

## ディレクトリロック用領域
$lockdir = './datas/lock/';
$lockdir_fmail = './fmail.admin/datas/lock/';
$lockdir_cart = '../fmail.admin/datas/lock/';

## sp
$sp_copyright = '<!--WebSiteAdmin-Copyright-->';
$sp_pagetitle = '<!--WebSiteAdmin-Title-->';
$sp_topheader = '<!--WebSiteAdmin-Header-->';
$sp_contents = '<!--WebSiteAdmin-Contents-->';
$sp_include = '<!--WebSiteAdmin-Include-->';
$sp_warning = '<!--WebSiteAdmin-Warning-->';

## data file path
$dir_datas = './datas/';
$file_users = 'users.cgi';
$file_registry = 'registry.dat';

$this_url = $ENV{'SERVER_NAME'} . $ENV{'SCRIPT_NAME'};
$this_url =~ s/index\.cgi//ig;
@week = ('日','月','火','水','木','金','土');
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$mon++;$year += 1900;
$stmp = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);

sub getform {
	$q = new CGI;
	@names = $q->param;
	for($cnt=0;$cnt<@names;$cnt++){
		$name = $names[$cnt];
		$value = $q->param($names[$cnt]);
		$form{$name} = $value;
	}
}
sub setHash {
	my(@temp) = @_;
	%sethash = ();
	for(my($cnt)=0;$cnt<@temp;$cnt++){
		$temp[$cnt] =~ s/<br \/>/\n/ig;
		$temp[$cnt] =~ s/\"/&quot;/ig;
		$temp[$cnt] =~ s/</&lt;/ig;
		$temp[$cnt] =~ s/>/&gt;/ig;
		$sethash{$hash_names[$cnt]} = $temp[$cnt];
	}
	return *sethash;
}
sub display {
	if(index($modules{"auth"},"%%$current_user{'power'}%%") == -1 && $modules{"auth"} ne $null && $modules{"auth"} ne "null"){
		$action_name = '管理権限エラー';
		$print_html = <<"		EOF";
			<div class="error">
				<p>このファンクションを管理する権限がありません。</p>
				<p><a href="?">管理画面HOMEに戻る</a></p>
			</div>
		EOF
	}
	if($modules{'name'} ne $null){
		$module_name_list = "<li><a href=\"?m=$form{'m'}\">$modules{'name'}</a></li>";
		if($action_name ne $null){
			$action_name_list = "<li>${action_name}</li>";
		}
	}
	
	#各設定情報の読み出し
	#メールフォーム設定
	@mailform_env = &loadfile('./datas/modules/mailform_env/mailform_env.dat');
	$mailform_env = join("\n",@mailform_env);
	($mailform_flag,$expires_start,$expires_end,$limit,$serials,$thanks_page,$sendmail_path,$logsave,$cart_in_element,$cart_logsave,$form_logsave,$form_logsave_period,$send_mode,$attached_mode,$display_mode,$logdata_path,$cart_logdata_path,$mailform_sender_address_name,$mailform_sender_address,$mail_method,$thanks_message,$title_mailform,$title_confirm,$title_error,$title_thanks,$mail_dustclear,$mail_dustclear_zero,$client_info,$site_url,$table_style,$th_style,$td_style,$separate_before,$separate_after,$flag_afiri,$afiri1_tag,$afiri2_tag,$afiri3_tag,$afiri4_tag,$afiri5_tag,$flag_smartphone_tpl,$flag_futurephone_tpl,$setlang,$spamcheck,$domaincheck,$encheck) = split(/\n/,$mailform_env);
	#自動返信メールの設定
	@return_mail_set = &loadfile('./datas/modules/return_mail/return_mail.dat');
	for($cnt=0;$cnt<@return_mail_set;$cnt++){
		($return_mail_id,$return_mail_type,$return_mail_name,$return_mail_element,$return_mail_value,$return_mail_flag,$return_mail_from,$return_mail_sender,$return_mail_subject,$return_mail_serials,$return_mail_email_field,$return_mail_body) = split(/\t/,$return_mail_set[$cnt]);
	}
	#送信条件の設定
	@send_conditional = &loadfile('./datas/modules/send_conditional/send_conditional.dat');
	for($cnt=0;$cnt<@send_conditional;$cnt++){
		($send_conditional_id,$send_conditional_type,$send_conditional_name,$send_conditional_element,$send_conditional_value,$send_mailaddress,$send_numname,$send_subject,$send_body,$send_note,$cc,$bcc) = split(/\t/,$send_conditional[$cnt]);
	}
	#未設定スカラ初期化
	$no_setting = '';
	if(($mailform_sender_address =~ /設定してください！|\@freesale.co.jp|^$/) || ($send_mailaddress =~ /設定してください！|\@freesale.co.jp|^$/) || ($return_mail_from =~ /設定してください！|\@freesale.co.jp|^$/)){
		$no_setting = '<span class="pankuzu_caution"> メールアドレスが、初期値／未設定／@freesale.co.jp です。：';
		if($mailform_sender_address =~ /設定してください！|\@freesale.co.jp|^$/){
			$no_setting .= ' 【メールフォーム設定】 ';
		}
		if($send_mailaddress =~ /設定してください！|\@freesale.co.jp|^$/){
			$no_setting .= ' 【送信条件の設定】 ';
		}
		if($return_mail_from =~ /設定してください！|\@freesale.co.jp|^$/){
			$no_setting .= ' 【自動返信メールの設定】 ';
		}
		$no_setting .= '</span>';
	}
	
	$print_html = <<"	__print_html__";
<!--		<h2>${action_name} (version:$reg{version}) $no_setting</h2>-->
		<h2>${action_name} $no_setting</h2>
		<ul class="tree">
			<li><a href="?">HOME</a></li>
			$module_name_list
			$action_name_list
		</ul>
		<div id="contentsbody">
			<div id="inbox">
				${print_html}
			</div>
		</div>
	__print_html__
	
	if($current_user{'power'} eq 'limited-client') {
		if ($form{'m'} eq 'logview' && $form{'a'} eq 'form') {
			$html = &loadhtml('logview',$action_name,$print_html);
		} else {
			$html = &loadhtml('default-limited',$action_name,$print_html);
		}
	}
	else {
		if (($form{'m'} eq 'logview' || $form{'m'} eq 'cart_logview') && $form{'a'} eq 'form') {
			$html = &loadhtml('logview',$action_name,$print_html);
		} else {
			$html = &loadhtml('default',$action_name,$print_html);
		}
	}
}
sub mfp_LoadLine {
	my($path) = @_;
	chmod 0777, $path;
	
	# ハッシュキー生成 ---------------------------
	@hashids = split(/\//,$path);
	$hashid = $hashids[-1];
	if ($hashids[0] eq '..' && $hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_cart;
	} elsif ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock_conf($hashid);
		
		open(FH,$path);
			$str = <FH>;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock_conf($hashid);
	
	chmod 0644, $path;
	return $str;
}
sub mfp_SaveLine {
	my($path,$str) = @_;
	chmod 0777, "${path}";
	
	# ハッシュキー生成 ---------------------------
	@hashids = split(/\//,$path);
	$hashid = $hashids[-1];
	if ($hashids[0] eq '..' && $hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_cart;
	} elsif ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock_conf($hashid);
		
		open(FH,">${path}");
			print FH $str;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock_conf($hashid);
	
	chmod 0644, "${save}";
}
sub loadfile {
	my($path) = @_;
	my(@loader) = ();
	chmod 0777, $path;
	
	# ハッシュキー生成 ---------------------------
	@hashids = split(/\//,$path);
	$hashid = $hashids[-1];
	if ($hashids[0] eq '..' && $hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_cart;
	} elsif ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	
	# ファイルロック
	&file_lock_conf($hashid);
		
		open(FH,$path);
			@loader = <FH>;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock_conf($hashid);
	
	chmod 0644, $path;
	$loader = join('',@loader);
	$loader  =~ s/\r//g;
	@loader = split(/\n/,$loader);
	return @loader;
}
sub loadfile_formlog {
	my($path) = @_;
	my(@loader) = ();
	chmod 0777, $path;
		
		open(FH,$path);
			@loader = <FH>;
		close(FH);
		
	chmod 0644, $path;
	$loader = join('',@loader);
	$loader  =~ s/\r//g;
	@loader = split(/\n/,$loader);
	return @loader;
}
sub savefile {
	my($path,@data) = @_;
	my($data) = join("\n",@data);
	chmod 0777, "${path}";
	
	# ハッシュキー生成 ---------------------------
	@hashids = split(/\//,$path);
	$hashid = $hashids[-1];
	if ($hashids[0] eq '..' && $hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_cart;
	} elsif ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock_conf($hashid);
		
		open(FH,">${path}");
			print FH $data;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock_conf($hashid);
	
	chmod 0644, "${save}";
}
sub WppLoadLine {
	my($path) = @_;
	chmod 0777, $path;
	
	# ハッシュキー生成 ---------------------------
	@hashids = split(/\//,$path);
	$hashid = $hashids[-1];
	if ($hashids[0] eq '..' && $hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_cart;
	} elsif ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock_conf($hashid);
		
		open(FH,$path);
			$loader = <FH>;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock_conf($hashid);
	
	chmod 0644, $path;
	@loader = split(/\t/,$loader);
	return @loader;
}
sub WppSaveLine {
	my($path,$str) = @_;
	chmod 0777, "${path}";
	
	# ハッシュキー生成 ---------------------------
	@hashids = split(/\//,$path);
	$hashid = $hashids[-1];
	if ($hashids[0] eq '..' && $hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_cart;
	} elsif ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock_conf($hashid);
		
		open(FH,">${path}");
			print FH $str;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock_conf($hashid);
	
	chmod 0644, "${save}";
}
sub WppSaveAddLine {
	my($path,$str) = @_;
	chmod 0777, "${path}";
	
	# ハッシュキー生成 ---------------------------
	@hashids = split(/\//,$path);
	$hashid = $hashids[-1];
	if ($hashids[0] eq '..' && $hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_cart;
	} elsif ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock_conf($hashid);
		
		open(FH,">>${path}");
			print FH $str . "\n";
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock_conf($hashid);
	
	chmod 0644, "${save}";
}
sub WppEncodeCharOptimize {
	my($str) = @_;
	$str =~ s/<eq>/\=/g;
	$str =~ s/<amp>/\&/g;
	$str =~ s/</&lt;/g;
	$str =~ s/>/&gt;/g;
	$str =~ s/\r\n/\n/g;
	$str =~ s/\r/\n/g;
	$str =~ s/\n/<br \/>/g;
	$str =~ s/\t/ /g;
	return $str;
}
sub WppDecodeCharOptimize {
	my($str) = @_;
	$str =~ s/<br \/>/\n/g;
	return $str;
}
sub WppTimeFormat {
	my($sec) = @_;
	$sec = time - $sec;
	my($min) = int(($sec % 3600) / 60);
	my($hour) = int(($sec % 86400) / 3600);
	my($day) = int($sec / 86400);
	my($str) = $null;
	
	if($day > 0){
		$str .= "${day}日と";
	}
	if($hour > 0){
		$str .= "${hour}時間";
	}
	if($min > 0){
		$str .= "${min}分";
	}
	if($str ne $null){
		$str .= "経過";
	}
	return $str;
}
sub setnotice {
	
}
sub notice {
	my($notice_text,$notice_link) = @_;
	my(@saved_notice) = (time,$form{'m'},$notice_text,$notice_link);
	my($saved_notice) = join("\t",@saved_notice);
	&WppSaveLine($reg{'file_notice'},$saved_notice);
}
sub loginCheck {
	*getSes = GetCookie($ENV{'HTTP_COOKIE'});
	$session_id = $getSes{'session_id'};
	$session_path = "$reg{'dir_sessions'}${session_id}\.cgi";
	if($form{'login_user_id'} ne $null && $form{'login_user_password'} ne $null){
		&sesclear('./datas/sessions/');
		&sesclear('./datas/sessions_files/');
		## login action
		chmod 0777, "${dir_datas}${file_users}";
		
		open(FH,"${dir_datas}${file_users}");
			@users = <FH>;
		close(FH);
		
		chmod 0644, "${dir_datas}${file_users}";
		@users = grep(/^$form{'login_user_id'}\t/,@users);
		@user_info = split(/\t/,$users[0]);
		($current_user{'id'},$current_user{'pw'},$current_user{'power'},$current_user{'email'},$current_user{'name'},$current_user{'mobile_email'},$current_user{'note'}) = split(/\t/,$users[0]);
#		if($current_user{'pw'} eq $form{'login_user_password'}){
		# 初期導入時の場合は、暗号化なしでログイン。パス変更後より暗号化
		if($current_user{'pw'} eq $current_user{'id'} || $current_user{'pw'} =~ /^admin_/){
			# ここの処理内容は、23行目後の処理と同じ
			if($current_user{'pw'} eq $form{'login_user_password'}){
				$session_id = &createId;
				@current_user_info = split(/\t/,$users[0]);
				@current_user_field = ('id','pw','power','email','name','mobile_email','note');
				$session_data = "## SESSION FILE\n";
				for($cnt=0;$cnt<@current_user_field;$cnt++){
					$current_user_info[$cnt] =~ s/\n/<br \/>/g;
					if($current_user_info[$cnt] ne $null){
						$session_data .= "\$current_user\{\'" . $current_user_field[$cnt] . "\'\} \= \'${current_user_info[$cnt]}\'\;\n";
					}
				}
				$session_data .= "## SESSION FILE EOF";
				$users[0] = $session_data;
				&savefile("$reg{'dir_sessions'}${session_id}\.cgi",@users);
				&notice("$current_user{'name'}さんがログインしました");
				return 1;
			}
			else {
				$warning_message = "<strong style=\"color: #FF0000;\">ID又はパスワードが間違っています</strong>";
				return 0;
			}
		}elsif($current_user{'pw'} eq md5_hex($form{'login_user_password'})){
			$session_id = &createId;
			@current_user_info = split(/\t/,$users[0]);
			@current_user_field = ('id','pw','power','email','name','mobile_email','note');
			$session_data = "## SESSION FILE\n";
			for($cnt=0;$cnt<@current_user_field;$cnt++){
				$current_user_info[$cnt] =~ s/\n/<br \/>/g;
				if($current_user_info[$cnt] ne $null){
					$session_data .= "\$current_user\{\'" . $current_user_field[$cnt] . "\'\} \= \'${current_user_info[$cnt]}\'\;\n";
				}
			}
			$session_data .= "## SESSION FILE EOF";
			$users[0] = $session_data;
			&savefile("$reg{'dir_sessions'}${session_id}\.cgi",@users);
			&notice("$current_user{'name'}さんがログインしました");
			return 1;
		}
		else {
			$warning_message = "<strong style=\"color: #FF0000;\">ID又はパスワードが間違っています</strong>";
			return 0;
		}
	}
	elsif($form{'login_user_password'} eq "logout"){
		unlink "$reg{'dir_sessions'}${session_id}\.cgi";
		return 0;
	}
	elsif((-f $session_path) && !(-d $session_path)){
		require "$reg{'dir_sessions'}${session_id}\.cgi";
		$user_cache = "$reg{'users_dirs'}$current_user{'id'}\/cache\.dat";
		if(-f $user_cache){
			if((stat($user_cache))[9] > (stat("$reg{'dir_sessions'}${session_id}\.cgi"))[9]){
				@user_cache = &loadfile($user_cache);
				&savefile("$reg{'dir_sessions'}${session_id}\.cgi",@user_cache);
				require "$reg{'dir_sessions'}${session_id}\.cgi";
			}
			return 1;
		}
		else {
			unlink $session_path;
			return 0;
		}
	}
	elsif($form{'login_user_id'} eq $null && $form{'login_user_password'} eq $null){
		return 0;
	}
	else {
		$warning_message = "<strong style=\"color: #FF0000;\">ID又はパスワードが間違っています</strong>";
		return 0;
	}
}
sub sesclear {
	my($dir) = @_;
	opendir DH, $dir;
	while (my $file = readdir DH) {
		next if $file =~ /^\.{1,2}$/;
		if(-M "${dir}${file}" >= 1 && $file ne 'index.html') {
		    unlink "${dir}${file}";
		}
	}
	closedir DH;
}
sub dirclear {
	my($dir) = @_;
	opendir DH, $dir;
	while (my $file = readdir DH) {
		next if $file =~ /^\.{1,2}$/;
		if($file ne 'index.html'){
	    	unlink "${dir}${file}";
	    }
	}
	closedir DH;
}
sub dirsizecheck {
	my($dir) = @_;
	my($filesize);
	opendir DH, $dir;
	while (my $file = readdir DH) {
		next if $file =~ /^\.{1,2}$/;
		$filesize += -s "${dir}${file}";
	}
	closedir DH;
	$filesize = int($filesize / 1024);
	return $filesize;
}
sub createId {
	@alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z");
	$digit = 10;
	$hash_char = "";
	for($cnt=0;$cnt<$digit;$cnt++){
		my($randno) = int(rand @alphabet);
		$hash_char .= $alphabet[$randno];
	}
	$hash_char = time . $hash_char;
	return $hash_char;
}
sub GetCookie {
	my($cookie) = $ENV{'HTTP_COOKIE'};
	$cookie =~ s/ //g;
	$cookie =~ s/\;/\&/g;
	my(@cookie) = split(/\&/,$cookie);
	my(@cookies) = ();
	for(my($cnt)=0;$cnt<@cookie;$cnt++){
		my($name, $value) = split(/=/,$cookie[$cnt]);
		$cookies{$name} = $value;
	}
	return *cookies;
}
sub loadhtml {
	my($url,$title,$body) = @_;
	
	open(FH,"./tpl/${url}.tpl");
		@html = <FH>;
	close(FH);
	
	$html = join("",@html);
	$html =~ s/$sp_pagetitle/$title/ig;
	$html =~ s/$sp_contents/$body/ig;
	$html =~ s/$sp_copyright/$reg{'copyright'}/ig;
	return $html;
}
sub loadlibrary {
	my($url) = @_;
	
	# ハッシュキー生成 ---------------------------
	@hashids = split(/\//,$path);
	$hashid = $hashids[-1];
	if ($hashids[0] eq '..' && $hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_cart;
	} elsif ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock_conf($hashid);
		
		open(FH,"./Library/${url}.html");
			@html = <FH>;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock_conf($hashid);
	
	my($html) = join("",@html);
	return $html;
}
sub decodeURI {
	my($str) = @_;
	$str =~ tr/+/ /;
	$str =~ s/%([0-9A-Fa-f][0-9A-Fa-f])/pack('H2', $1)/eg;
	return $str;
}

sub encodeURI {
	my($str) = @_;
	$str =~ s/([^\w ])/'%' . unpack('H2', $1)/eg;
	$str =~ tr/ /+/;
	return $str;
}


#----------------------------------------------------------------------------------------
#  ファイルロック
#----------------------------------------------------------------------------------------
sub file_lock_conf {
	# ファイル名の読み込み
	my $param = $_[0];
	
	# ロックディレクトリの結合
	my $lockdir_combine = $lockdir . $param . '/';
	
	# エラーでファイルロックが解除されてない場合のディレクトリ掃除
	if(-e $lockdir_combine) {
		# 存在している場合は、日付で判定して削除する
		
		# 制限時間設定（1分）
		my $limit_time = 60 * 1;
		
		# ロックディレクトリの最終更新日取得
		my @stats = stat($lockdir_combine);
		my $judge_time = time - $stats[9];
		
		# 制限時間を超える場合はファイルロックディレクトを削除
		if($judge_time > $limit_time){
			# ディレクトリ削除
			rmdir($lockdir_combine);
		}
	}
	
	# ロック解除失敗時用のフラグ
	my $flag_locking = 1;
	
	for (my $i = 0; $i <= 10; $i++) {
		if (mkdir($lockdir_combine, 0755)) {
			# 成功
			$flag_locking = 0;
			last;
		} else {
			# 失敗
			# 1秒待って再トライ
			sleep(1);
		}
	}
	
	if($flag_locking){
		&error('書き込みエラー　：　しばらく経ってから、再度実行してください。');
	}
}



#----------------------------------------------------------------------------------------
#  ファイルアンロック
#----------------------------------------------------------------------------------------
sub file_unlock_conf {
	# パラメータ取得
	my $param = $_[0];
	
	# ロックディレクトリの結合
	my $lockdir_combine = $lockdir . $param . '/';
	
	# ディレクトリ削除
	rmdir($lockdir_combine);
}



#----------------------------------------------------------------------------------------
#  エラーページ
#----------------------------------------------------------------------------------------
sub error {
# デバッグ用
print "Content-type: text/html\n\n";

print <<EOD;
<!DOCTYPE html>
<html lang="ja">
<head><meta charset="utf-8"></head>
<body><p style="padding: 5px; background: #fff; border: 1px solid #000;">@_</p></body>
</html>
EOD
exit;
}

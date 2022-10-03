## 2007-08-15 mailform pro Ver.1.0 functions file

$about = 'メールフォームの関数用ファイル';

##モード設定 (0:デバッグ / 1:通常)
$config{"mode"} = 1;

##エラーコードの初期設定
$error{"code"} = 0;

##メールナンバー
$config{"serial_file"} = './fmail.admin/datas/serial.dat';

## ファイルの排他制御設定（メール送信に関わる部分の制御。管理画面は影響なし）
$lock_method = 1; # 1=ディレクトリロック(標準) / 0=排他制御なし(メール消失が多発する場合はこちらを選択)

## ディレクトリロック用領域
$lockdir = './datas/lock/';
$lockdir_fmail = './fmail.admin/datas/lock/';

##以下、初期設定項目の自動設定
@mailformENV = ('date','input_time','conversion_count','pv','unique','conversion_rate','http_referer','sitein_referrer');
@mailformENVname = ('POST DATE','INPUT TIME','CONVERSION','PAGE VIEW','UNIQUE USERS','CONVERSION RATE','REFERRER','SITE IN REFERRER');

($sec,$min,$hour,$day,$mon,$year) = gmtime(time + 9 * 3600);$mon++;$year += 1900;
$stmp = sprintf("%04d-%02d-%02d %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);
$download_file_name = sprintf("%04d-%02d-%02d.csv",$year,$mon,$day,$hour,$min,$sec);

#@construct_utf = ("\xef\xbc\x8d","\xE3\x80\x9C");
@construct_utf = ("－","～");
@construct_jis = ("\x1b\x24B\x21\x5d\x1b\x28J","\x1b\x24B\x21A\x1b\x28J");
@construct_sjis = ("\x81\x7c","\x81\x60");

@con_befor = ('ｶﾞ','ｷﾞ','ｸﾞ','ｹﾞ','ｺﾞ','ｻﾞ','ｼﾞ','ｽﾞ','ｾﾞ','ｿﾞ','ﾀﾞ','ﾁﾞ',
	'ﾂﾞ','ﾃﾞ','ﾄﾞ','ﾊﾞ','ﾋﾞ','ﾌﾞ','ﾍﾞ','ﾎﾞ','ﾊﾟ','ﾋﾟ','ﾌﾟ','ﾍﾟ','ﾎﾟ','ｦ','ｧ',
	'ｨ','ｩ','ｪ','ｫ','ｬ','ｭ','ｮ','ｯ','ｰ','ｱ','ｲ','ｳ','ｴ','ｵ','ｶ','ｷ','ｸ','ｹ',
	'ｺ','ｻ','ｼ','ｽ','ｾ','ｿ','ﾀ','ﾁ','ﾂ','ﾃ','ﾄ','ﾅ','ﾆ','ﾇ','ﾈ','ﾉ','ﾊ','ﾋ',
	'ﾌ','ﾍ','ﾎ','ﾏ','ﾐ','ﾑ','ﾒ','ﾓ','ﾔ','ﾕ','ﾖ','ﾗ','ﾘ','ﾙ','ﾚ','ﾛ','ﾜ','ﾝ',
	'Ａ','Ｂ','Ｃ','Ｄ','Ｅ','Ｆ','Ｇ','Ｈ','Ｉ','Ｊ','Ｋ','Ｌ','Ｍ','Ｎ','Ｏ','Ｐ','Ｑ','Ｒ','Ｓ','Ｔ','Ｕ','Ｖ','Ｗ','Ｘ','Ｙ','Ｚ','ａ','ｂ','ｃ','ｄ','ｅ','ｆ','ｇ','ｈ','ｉ','ｊ','Ｋ','ｌ','ｍ','ｎ','ｏ','ｐ','ｑ','ｒ','ｓ','ｔ','ｕ','ｖ','ｗ','ｘ','ｙ','ｚ','＠','．',
	'①','②','③','④','⑤','⑥','⑦','⑧','⑨','⑩','Ⅰ','Ⅱ','Ⅲ','Ⅳ','Ⅴ','Ⅵ','Ⅶ','Ⅷ','Ⅸ','Ⅹ','㈱','㈲');
@con_after = ('ガ','ギ','グ','ゲ','ゴ','ザ','ジ','ズ','ゼ','ゾ','ダ','ヂ',
	'ヅ','デ','ド','バ','ビ','ブ','ベ','ボ','パ','ピ','プ','ペ','ポ','ヲ','ァ',
	'ィ','ゥ','ェ','ォ','ャ','ュ','ョ','ッ','ー','ア','イ','ウ','エ','オ','カ',
	'キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ',
	'ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ヤ',
	'ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ン',
	'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','@','.',
	'(1)','(2)','(3)','(4)','(5)','(6)','(7)','(8)','(9)','(10)','(1)','(2)','(3)','(4)','(5)','(6)','(7)','(8)','(9)','(10)','(株)','(有)');

# 本文以外では置換する。
@con_befor2 = ('髙','﨑','閒','塚','德');
@con_after2 = ('高','崎','間','塚','徳');



sub device {
	my($device) = 0;
	for(my($cnt)=0;$cnt<@MOBILE_USER_AGENT;$cnt++){
		if(index($ENV{'HTTP_USER_AGENT'},$MOBILE_USER_AGENT[$cnt]) > -1){
			$device = 1;
		}
	}
	return $device;
}

sub sanitizing_str {
	my($str) = @_;
	for($i=0;$i<@con_befor;$i++){
		$str =~ s/${con_befor[$i]}/${con_after[$i]}/g;
	}
	return $str;
}

# メール本文以外でさらに適用（機種依存文字対応）
sub sanitizing_str2 {
	my($str) = @_;
	for($i=0;$i<@con_befor2;$i++){
		$str =~ s/${con_befor2[$i]}/${con_after2[$i]}/g;
	}
	return $str;
}

# htmlにかかわる部分のサニタイズ
sub sanitizing_meta {
	my($str) = @_;
	$str =~ s/\"/&quot;/g;
	$str =~ s/</\&lt;/g;
	$str =~ s/>/\&gt;/g;
	
	return $str;
}

# htmlにかかわる部分の逆置換
sub unsanitizing_meta {
	my($str) = @_;
	$str =~ s/&quot;/\"/g;
	$str =~ s/\&lt;/</g;
	$str =~ s/\&gt;/>/g;
	
	return $str;
}

sub gethostname {
	my($ip_address) = $ENV{'REMOTE_ADDR'};
	my(@addr) = split(/\./, $ip_address);
	my($packed_addr) = pack("C4", $addr[0], $addr[1], $addr[2], $addr[3]);
	my($name, $aliases, $addrtype, $length, @addrs);
	($name, $aliases, $addrtype, $length, @addrs) = gethostbyaddr($packed_addr, 2);
	return $name;
}
sub mfp_LoadFile {
	my($path) = @_;
	chmod 0777, $path;
	
	# ハッシュキー生成 ---------------------------
	my @hashids = split(/\//,$path);
	my $hashid = $hashids[-1];
	if ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock($hashid);
		
		open(FH,$path);
			@str = <FH>;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock($hashid);
	
	chmod 0644, $path;
	$str = join('',@str);
	return $str;
}

sub mfp_LoadLine {
	my($path) = @_;
	chmod 0777, $path;
	
	# ハッシュキー生成 ---------------------------
	my @hashids = split(/\//,$path);
	my $hashid = $hashids[-1];
	if ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock($hashid);
		
		open(FH,$path);
			$str = <FH>;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock($hashid);
	
	chmod 0644, $path;
	return $str;
}
sub mfp_SaveLine {
	# Serial Number
	my($path,$str) = @_;
	chmod 0777, "${path}";
	
	# ハッシュキー生成 ---------------------------
	my @hashids = split(/\//,$path);
	my $hashid = $hashids[-1];
	if ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock($hashid);
	
		open(FH,">${path}");
			print FH $str;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock($hashid);
	
	chmod 0644, "${path}";
}
sub mfp_SaveAddLine {
	# Log Data
	my($path,$str) = @_;
	chmod 0777, "${path}";
	
	# ハッシュキー生成 ---------------------------
	
	my @hashids = split(/\//,$path);
	my $hashid = $hashids[-1];
	if ($hashids[1] eq 'fmail.admin') {
		$lockdir = $lockdir_fmail;
	}
	# ファイルロック
	&file_lock($hashid);
		
		open(FH,">>${path}");
			print FH $str . "\n";
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock($hashid);
	
	chmod 0644, "${path}";
}
sub encodeJIS {
	my($str) = @_;
	for(my $cnt=0;$cnt<@construct_utf;$cnt++){
		$str =~ s/$construct_utf[$cnt]/<\_hotfix${cnt}\_>/g;
	}
	Jcode::convert(\$str,'jis');
	$str = &charhotfix_unescape_jis($str);
	return $str;
}
sub encodeSJIS {
	my($str) = @_;
	for(my $cnt=0;$cnt<@construct_utf;$cnt++){
		$str =~ s/$construct_utf[$cnt]/<\_hotfix${cnt}\_>/g;
	}
	Jcode::convert(\$str,'sjis');
	$str = &charhotfix_unescape_sjis($str);
	return $str;
}
sub charhotfix_unescape_jis {
	my($str) = @_;
	for(my $cnt=0;$cnt<@construct_utf;$cnt++){
		$str =~ s/<\_hotfix${cnt}\_>/$construct_jis[$cnt]/g;
	}
	return $str;
}
sub charhotfix_unescape_sjis {
	my($str) = @_;
	for(my $cnt=0;$cnt<@construct_utf;$cnt++){
		$str =~ s/<\_hotfix${cnt}\_>/$construct_sjis[$cnt]/g;
	}
	return $str;
}

sub envMailform {
	$form{'pv'} = $getCookieData{"pv"};
	$form{'unique'} = &mfp_LoadLine($config{"conversion_file"});
	&mfp_SaveLine($config{"input_time_file"},&mfp_LoadLine($config{"input_time_file"}) + $form{'input_time'});
	if($form{'unique'} eq $null || $form{'unique'} < 1){
		$form{'unique'} = 1;
	}
	$form{'conversion_rate'} = $form{'conversion_count'} / $form{'unique'} * 100;
	$form{'conversion_rate'} = round($form{'conversion_rate'}, 3) . '%';
	
	$form{'conversion_count'} = $form{'conversion_count'} . " conversions";
	$form{'unique'} = $form{'unique'} . " users";
	$form{'pv'} = $form{'pv'} . " pageviews";
	$form{'input_time'} = $form{'input_time'} . " sec";
	
	for($cnt=0;$cnt<@mailformENV;$cnt++){
		$envs .= "\[ " . $mailformENVname[$cnt] . " \] " . $form{$mailformENV[$cnt]} . "\n";
		push @field, $mailformENVname[$cnt];
		push @csv, $form{$mailformENV[$cnt]};
		$config{"return_body"} =~ s/<${mailformENV[$cnt]}>/$form{$mailformENV[$cnt]}/g;
		$config{"posted_body"} =~ s/<${mailformENV[$cnt]}>/$form{$mailformENV[$cnt]}/g;
	}
}
sub expires_check {
	if($config{"error_url"} ne $null){
		if($config{"expires"} ne $null && $config{"expires_break"} ne $null && ($config{"expires_break"} ge $form{"date"} || $form{"date"} ge $config{"expires"})){
			$error_redirect = 1;
		}
		elsif($config{"expires"} ne $null && $form{"date"} ge $config{"expires"}){
			$error_redirect = 1;
		}
		elsif($config{"expires_break"} ne $null && $config{"expires_break"} ge $form{"date"}){
			$error_redirect = 1;
		}
	}
}
sub serials {
	$serial = &mfp_LoadLine($config{"serial_file"});
	$serial_number = sprintf("%04d",$serial);
	if($return_mail_serials){
	#自動返信メールの件名にシリアル挿入
	#if($serials){
		$return_mail_subject = "\[" . $serial_number . "\] " . $return_mail_subject;
	}
	#クライアントメールの件名にシリアル挿入
	if($serials){
		$admin_subject_serial = "\[<-numname->" . $serial_number . "\] ";
	}
	$serial++;
	&mfp_SaveLine($config{"serial_file"},$serial);
	$serial--;
	$serial = sprintf("%04d",$serial);
}
sub serials_read {
	#完了画面なんかで、シリアルのみ呼び出したい場合に利用
	$serial = &mfp_LoadLine($config{"serial_file"});
	$serial--;
	$serial = sprintf("%04d",$serial);
}

sub domaincheck {
	if(index($ENV{'HTTP_REFERER'},$config{"domain"}) > -1 && $config{"domain"} != 0){
		$error{"code"} = 1;
		$error{"info"} .= "指定ドメイン以外から送信されようとしています。 $config{'domain'} / $ENV{'HTTP_REFERER'}<br>\n";
	}
}
sub confcheck {
	if(@mailto < 1){
		$error{"code"} = 2;
		$error{"info"} .= "メールアドレスが正しく設定されていません。<br>\n";
	}
	if($config{"thanks_url"} eq $null){
		$error{"code"} = 2;
		$error{"info"} .= "コンフィグが正しく設定されていません。<br>\n";
	}
}
sub javascript_check {
	if(!$form{"javascript_flag"}){
		$error{"code"} = 5;
		$error{"info"} .= "Javascriptが有効ではありません。<br>\n";
	}
}
sub spamcheck {
	if($config{"english_spam"}){
		$error{"code"} = 3;
		$error{"info"} .= "全ての入力内容が英文で記述されております。<br>\n";
	}
	if($config{"link_spam_count"} && !($config{"link_spam"})){
		$error{"code"} = 4;
		$error{"info"} .= "入力された内容に\[\/URL\]が含まれています。<br>\n";
	}
}
sub getpost {
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	}
	else {
		$buffer = $ENV{'QUERY_STRING'};
	}
	$charcode = getcode(\$buffer);
	@pairs = split(/&/, $buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$name =~ tr/+/ /;
		$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~ s/\\n/\n/g;
		if($name ne $null && $name ne "Submit" && $name ne "confirm_email" && $name ne "x" && $name ne "y" && $name ne "must_id" && $name ne "input_time" && $name ne "javascript_flag" && $name ne "http_referer" && $name ne "mailform_confirm_mode" && index($name,'[unjoin]') == -1 && $name ne "sitein_referrer"){
			if($name ne $prevName){
				$crr = "";
				if(index($value,"\n") > -1){
					$crr = "\n";
				}
				if($value ne $null){
					$resbody .= "\n\[ ${name} \]${crr} ${value} ${crr}";
					$config{"body"} .= "\n\[ ${name} \]${crr}${value}${crr}";
				}
				$config{"return_body"} =~ s/<${name}>/$value/g;
				$config{"posted_body"} =~ s/<${name}>/$value/g;
				$value =~ s/\,//ig;
				push @field, $name;
				push @csv, $value;
			}
			else{
				$resbody .= " ${value} ";
				$config{"body"} .= " ${value} ";
				$csv[-1] .= " ${value}";
			}
			if(!($value !~ /[\x80-\xff]/)){
				$config{"english_spam"} = 0;
			}
			if($value =~ /\[\/url\]/si){
				$config{"link_spam_count"} = 1;
			}
			if($value =~ /\[\/link\]/si){
				$config{"link_spam_count"} = 1;
			}
			if(index($name,'(必須)') > -1){
				$config{"link_spam_count"} = 1;
			}
			$prevName = $name;
		}
		$form{$name} = $value;
	}
}

sub logfileCreate {
	if($config{"log_file"} ne $null && $config{"password"} ne $null){
		$size = -s $config{"log_file"};
		if(-f $config{"log_file"} && $size > 0){
			chmod 0777, $config{"log_file"};
			push @csv,"\"\n";
			my($put_field) = "\"" . join("\",\"",@csv);
			$put_field = &encodeSJIS($put_field);
			
			# ハッシュキー生成 ---------------------------
			my @hashids = split(/\//,$path);
			my $hashid = $hashids[-1];
			# ファイルロック
			&file_lock($hashid);
				
				open(FH,">>".$config{"log_file"});
					print FH $put_field;
				close(FH);
				
			# ファイルロック解除 ---------------------------
			&file_unlock($hashid);
			
			chmod 0644, $config{"log_file"};
		}
		else{
			push @csv,"\"\n";
			push @field,"\"\n";
			my($put_field) = "\"" . join("\",\"",@field);
			$put_field .= "\"".  join("\",\"",@csv);
			$put_field = &encodeSJIS($put_field);
			
			# ハッシュキー生成 ---------------------------
			&error($config{"log_file"});
			$hashid = &createId;
			# ファイルロック
			&file_lock($hashid);
				
				open(FH,">".$config{"log_file"});
					print FH $put_field;
				close(FH);
				
			# ファイルロック解除 ---------------------------
			&file_unlock($hashid);
			
			chmod 0644, $config{"log_file"};
		}
	}
}

sub downloadScreen {
	print "Content-type: text/html\n\n";
	print "<html>\n";
	print "\t<head>\n";
	print "\t\t<title>mode::logfile download</title>\n";
	print "\t\t<style type=\"text/css\">\n";
	print "\t\t<!--\n";
	print "\t\t* {\n";
	print "\t\t\tfont-family: \"Arial\", \"Helvetica\", \"sans-serif\";font-size: 12px;\n";
	print "\t\t}\n";
	print "\t\t-->\n";
	print "\t\t</style>\n";
	print "\t</head>\n";
	print "\t<body>\n";
	print "\t\t<h1 style=\"font-size: 21px;color: #232323;\">mode::logfile download</h1>\n";
	print "\t\t<form name=\"getLogs\" action=\"?mode=download\" method=\"POST\">\n";
	print "\t\t\tPASSWORD <input type=\"password\" name=\"password\" style=\"ime-mode: disabled;width: 300px;\"><input type=\"hidden\" name=\"mode\" value=\"download\"><input type=\"hidden\" name=\"config\" value=\"$form{'config'}\"><input type=\"submit\" value=\"GET LOG FILE\">\n";
	print "\t\t</form>$form{'password'}</body></html>\n";
}

sub deleteScreen {
	print "Content-type: text/html\n\n";
	print "<html>\n";
	print "\t<head>\n";
	print "\t\t<title>mode::logfile delete</title>\n";
	print "\t\t<style type=\"text/css\">\n";
	print "\t\t<!--\n";
	print "\t\t* {\n";
	print "\t\t\tfont-family: \"Arial\", \"Helvetica\", \"sans-serif\";font-size: 12px;\n";
	print "\t\t}\n";
	print "\t\t-->\n";
	print "\t\t</style>\n";
	print "\t</head>\n";
	print "\t<body>\n";
	print "\t\t<h1 style=\"font-size: 21px;color: #232323;\">mode::logfile delete</h1>\n";
	print "\t\t<form name=\"getLogs\" action=\"\" method=\"POST\">\n";
	print "\t\t\tPASSWORD <input type=\"password\" name=\"password\" style=\"ime-mode: disabled;width: 300px;\"><input type=\"hidden\" name=\"mode\" value=\"delete\"><input type=\"hidden\" name=\"config\" value=\"$form{'config'}\"><input type=\"submit\" value=\"DELETE LOG FILE\">\n";
	print "\t\t</form>$form{'password'}</body></html>\n";
}

sub deleteComplate {
	unlink $config{"log_file"};
	print "Content-type: text/html\n\n";
	print "<html>\n";
	print "\t<head>\n";
	print "\t\t<title>mode::logfile delete Complate</title>\n";
	print "\t\t<style type=\"text/css\">\n";
	print "\t\t<!--\n";
	print "\t\t* {\n";
	print "\t\t\tfont-family: \"Arial\", \"Helvetica\", \"sans-serif\";font-size: 12px;\n";
	print "\t\t}\n";
	print "\t\t-->\n";
	print "\t\t</style>\n";
	print "\t</head>\n";
	print "\t<body>\n";
	print "\t\t<h1 style=\"font-size: 21px;color: #232323;\">logfile delete complate</h1>\n";
	print "\t\t</body></html>\n";
}

sub fileDownload {
	chmod 0644, $config{"log_file"};
	print "Content-type: application/octet-stream; name=\"${log_file}\"\n";
	print "Content-Disposition: attachment; filename=\"${download_file_name}\"\n\n";
	open(IN,$config{"log_file"});
	print <IN>;
	chmod 0644, $config{"log_file"};
}

sub refresh {
	my($refreshurl) = @_;
	print "Location: ${refreshurl}\n\n";
}

sub sendmail {
	my($mailto,$cc,$bcc,$mailfrom,$fromname,$subject,$body) = @_;
	my($sendmail) = $sendmail_path;
	if(!open(MAIL,"| $sendmail -f $mailfrom -t")){
		# sendmailモジュールオープンエラー
		print "Content-type: text/html\n\n";
		print <<EOD;
		<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
		<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
		<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<body>
		<p style="margin: 0 auto; padding: 5px; width: 500px; border: 2px solid #999;">
		メールの送信に失敗しました。<br />
		管理者は sendmailパス の設定をご確認ください
		</p>
		</body>
		</html>
EOD
		close(MAIL);
		exit;
	}else{
		# 通常送信機能
		print MAIL "To: $mailto\n";
		if($cc ne $null){
			print MAIL "Cc: $cc\n";
		}
		if($bcc ne $null){
			print MAIL "Bcc: $bcc\n";
		}
		print MAIL "Errors-To: $mailto\n";
		print MAIL "From: $fromname\n";
		print MAIL "Subject: $subject\n";
		print MAIL "MIME-Version:1.0\n";
		if($mail_method eq "html"){
			#$body =~ s/\n/<br>/g;
			$body =~ s/></>\n</g;
			# 多言語対応
			if($charset ne 'utf8'){
				# 多言語対応でない
				print MAIL "Content-type:text/html; charset=ISO-2022-JP\n";
				print MAIL "Content-Transfer-Encoding: 7bit\n";
			}else{
				# 多言語対応
				print MAIL "Content-type:text/html; charset=UTF-8\n";
				print MAIL "Content-Transfer-Encoding: 7bit\n";
			}
#			print MAIL "Content-Transfer-Encoding:7bit\n";
			print MAIL "X-Mailer:FREESALE MAILFORM\n\n";
			print MAIL '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">' . "\n";
			print MAIL '<html>' . "\n";
			print MAIL '<head><meta http-equiv="Content-Style-Type" content="text/css"></head>' . "\n";
			print MAIL '<body style="font-size: 1.2em;">' . "\n";
			print MAIL "$body\n";
			print MAIL "</body></html>\n";
		}
		else {
			
			# 多言語対応
			if($charset ne 'utf8'){
				# 多言語対応でない
				print MAIL "Content-type:text/plain; charset=ISO-2022-JP\n";
				print MAIL "Content-Transfer-Encoding: 7bit\n";
			}else{
				# 多言語対応
				print MAIL "Content-type:text/plain; charset=\"UTF-8\"\n";
				print MAIL "Content-Transfer-Encoding: 7bit\n";
			}

#			print MAIL "Content-Transfer-Encoding:7bit\n";
			print MAIL "X-Mailer:FREESALE MAILFORM\n\n";
			print MAIL "$body\n";
		}
	close(MAIL);
	}


##元のソース
#	my($mailto,$cc,$bcc,$mailfrom,$fromname,$subject,$body) = @_;
#	my($sendmail) = $sendmail_path;
#	open(MAIL,"| $sendmail -f $mailfrom -t");
#		print MAIL "To: $mailto\n";
#		if($cc ne $null){
#			print MAIL "Cc: $cc\n";
#		}
#		if($bcc ne $null){
#			print MAIL "Bcc: $bcc\n";
#		}
#		print MAIL "Errors-To: $mailto\n";
#		print MAIL "From: $fromname\n";
#		print MAIL "Subject: $subject\n";
#		print MAIL "MIME-Version:1.0\n";
#		if($mail_method eq "html"){
#			$body =~ s/\n/<br>/g;
#			$body =~ s/></>\n</g;
#			# 多言語対応
#			if($charset ne 'utf8'){
#				# 多言語対応でない
#				print MAIL "Content-type:text/html; charset=ISO-2022-JP\n";
#				print MAIL "Content-Transfer-Encoding: 7bit\n";
#			}else{
#				# 多言語対応
#				print MAIL "Content-type:text/html; charset=UTF-8\n";
#				print MAIL "Content-Transfer-Encoding: 7bit\n";
#			}
##			print MAIL "Content-Transfer-Encoding:7bit\n";
#			print MAIL "X-Mailer:FREESALE MAILFORM\n\n";
#			print MAIL '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">' . "\n";
#			print MAIL '<html>' . "\n";
#			print MAIL '<head></head>' . "\n";
#			print MAIL '<body bgcolor="#ffffff" text="#000000">' . "\n";
#			print MAIL "$body\n";
#			print MAIL "</body></html>\n";
#		}
#		else {
#			
#			# 多言語対応
#			if($charset ne 'utf8'){
#				# 多言語対応でない
#				print MAIL "Content-type:text/plain; charset=ISO-2022-JP\n";
#				print MAIL "Content-Transfer-Encoding: 7bit\n";
#			}else{
#				# 多言語対応
#				print MAIL "Content-type:text/plain; charset=\"UTF-8\"\n";
#				print MAIL "Content-Transfer-Encoding: 7bit\n";
#			}
#
##			print MAIL "Content-Transfer-Encoding:7bit\n";
#			print MAIL "X-Mailer:FREESALE MAILFORM\n\n";
#			print MAIL "$body\n";
#		}
#	close(MAIL);
}
sub round {
	my ($num, $decimals) = @_;
	my ($format, $magic);
	$format = '%.' . $decimals . 'f';
	$magic = ($num > 0) ? 0.5 : -0.5;
	sprintf($format, int(($num * (10 ** $decimals)) + $magic) / (10 ** $decimals));
}
sub debuglog {
	my ($print) = @_;
	
	# ハッシュキー生成 ---------------------------
	$hashid = &createId;
	# ファイルロック
	&file_lock($hashid);
		
		open(FH,">>debug.txt");
			print FH $print;
		close(FH);
		
	# ファイルロック解除 ---------------------------
	&file_unlock($hashid);
}
sub sendAttachMail ($$$$$$$$) {
	local( $from, $to, $cc ,$bcc, $subject, $body, @attach_tmp, @filename) = @_;
	local $attach = "";
	local $boundary = "-*-*-*-*-*-*-*-*-Boundary_" . time . "_" . $$;
	my($sendmail) = $sendmail_path;
	@attach_tmp = @file_datas;
	@filename = @file_paths;
	# デリミタを退避し、デフォルトの \n にする。
	$oldDelim = $/;
	undef $/;
	
	@attachs = ();
	@filenames = ();
	
	### サブジェクトを jis にして、MIME エンコード
	$subject = mimeencode(Jcode::convert(\$subject,'jis'));
	
	### 本文を jis に
	# 多言語対応
	if($charset ne 'utf8'){
		# 多言語対応しない
		$body = Jcode::convert(\$body,'jis');
	}
	
	### 添付するデータを、base64 でエンコード
	#$attach = &bodyencode($attach_tmp, "b64");
	#$attach .= &benflush("b64");
	for($i=0;$i<@attach_tmp;$i++){
		$temp = &bodyencode($attach_tmp[$i], "b64");
		$temp .= &benflush("b64");
		push @attachs, $temp;
		push @filenames, mimeencode(Jcode::convert(\$filename[$i],'jis'));
	}
	
	### ファイル名を sjis にして MIME エンコード。(推奨 ascii )
	
	
	### メールの送信
	#open MAIL, "| $sendmail -f $from -t";
	open MAIL, "| $sendmail -f $to -t";
	
	########################## メールの組み上げ
	### 全体のヘッダ
	print MAIL "To: $to\n";
	if($cc ne $null){
		print MAIL "Cc: $cc\n";
	}
	if($bcc ne $null){
		print MAIL "Bcc: $bcc\n";
		&syslog($bcc);
	}
	# 多言語対応
	if($charset ne 'utf8'){
		# 多言語対応しない
		print MAIL "From: $from\n";
		print MAIL "Subject: $subject\n";
		print MAIL "MIME-Version: 1.0\n";
		print MAIL "Content-Type: Multipart/Mixed; boundary=\"$boundary\"\n";
		print MAIL "Content-Transfer-Encoding: Base64\n";
	}else{
		# 多言語対応
		print MAIL "From: $from\n";
		print MAIL "Subject: $subject\n";
		print MAIL "Content-Type: Multipart/Mixed; boundary=\"$boundary\"\n";
		print MAIL "Content-Transfer-Encoding: 7bit\n";
		print MAIL "MIME-Version: 1.0\n";
	}
	
	### メール本文のパート
	print MAIL "--$boundary\n";
	if($mail_method eq "html"){
		$body =~ s/\n/<br>/g;
		$body =~ s/></>\n</g;
		# 多言語対応
		if($charset ne 'utf8'){
			# 多言語対応でない
			print MAIL "Content-Type: text/html; charset=\"ISO-2022-JP\"\n";
		}else{
			# 多言語対応
			print MAIL "Content-Transfer-Encoding: 7bit\n";
			print MAIL "Content-type: text/html; charset=\"UTF-8\"\n";
		}
		print MAIL "\n";
		print MAIL '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">' . "\n";
		print MAIL '<html>' . "\n";
		print MAIL '<head></head>' . "\n";
		print MAIL '<body bgcolor="#ffffff" text="#000000">' . "\n";
		print MAIL "$body\n";
		print MAIL "</body></html>\n";
	}
	else {
		# 多言語対応
		if($charset ne 'utf8'){
			# 多言語対応でない
			print MAIL "Content-Type: text/plain; charset=\"ISO-2022-JP\"\n";
		}else{
			# 多言語対応
			print MAIL "Content-Transfer-Encoding: 7bit\n";
			print MAIL "Content-type: text/plain; charset=\"UTF-8\"\n";
		}
		print MAIL "\n";
		print MAIL "$body\n";
	}
	
	### 添付ファイルのパート
	for($i=0;$i<@attachs;$i++){
		print MAIL "--$boundary\n";
		print MAIL "Content-Type: application/octet-stream; name=\"$filenames[$i]\"\n";
		print MAIL "Content-Transfer-Encoding: base64\n";
		print MAIL "Content-Disposition: attachment; filename=\"$filenames[$i]\"\n";
		print MAIL "\n";
		print MAIL "$attachs[$i]\n";
		print MAIL "\n";
	}

	
	### マルチパートのおわり。
	print MAIL "--$boundary" . "--\n";
	
	close MAIL;

# デリミタの復元
$/ = $oldDelim;
}


#----------------------------------------------------------------------------------------
#  問い合わせ済みのカートファイルの削除
#----------------------------------------------------------------------------------------
sub cart_del {
	# カートファイルの格納先設定
	$target_dir = './cart/cart.admin/datas/cart.items/';
	
	# ファイル名の引用
	
	#-- 全Cookieを取得 --#
	my %cookies = fetch CGI::Cookie;

	#-- Cookieの値を取得 --#
	if(exists $cookies{'socket'}){
		$cookies_value = $cookies{'socket'}->value; #値
		$cookies_expires = $cookies{'socket'}->expires; #賞味期限
		$cookies_domain  = $cookies{'socket'}->domain;  #有効なドメイン
		$cookies_path = $cookies{'socket'}->path; #有効なパス
	}
	
	$target_file = $target_dir . $cookies_value . '.cgi';
	
	unlink $target_file;
}



#----------------------------------------------------------------------------------------
# sendmail メールでは一行1000Byteで強制改行。
# 全角文字は3Byte構成の為、文字化けが発生する為その回避処理
#----------------------------------------------------------------------------------------
sub line1000Bytes {
	my ($str) = @_;
	my $ret = "";
	my $linebytes = 0;
	my $len = 0;
	my $count = 0;
	
	# 1000Byte
	$linebytes = 1000;
	
	# 改行分割で配列化
	my @bodys = split(/\n/, $str);
	
	for(my $i=0; @bodys>$i; $i++) {
		# Byte数の割り出し
		$len = length($bodys[$i]);
		# UTF8文字区切り
		utf8::decode($bodys[$i]);
		# 一文字ずつに分割
		my @chars = split //, $bodys[$i];
		
		if($len > $linebytes){
			# 1000Byte以上
			foreach my $char ( @chars ) {
				# 一文字ずつ取り出して、300字を超えたら折り返す
				if($count > 300) {
					$ret .= $char . "\n";
					$count = 0;
				} else {
					$ret .= $char;
					$count++;
				}
			}
			$ret .= "\n";
		} else {
			# 1000Byte未満
			$ret .= $bodys[$i] . "\n";
		}
	}
	return $ret;
}



#----------------------------------------------------------------------------------------
#  ファイルロック
#----------------------------------------------------------------------------------------
sub file_lock {
	# ディレクトリロック利用時
	if($lock_method) {
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
}



#----------------------------------------------------------------------------------------
#  ファイルアンロック
#----------------------------------------------------------------------------------------
sub file_unlock {
	# ディレクトリロック利用時
	if($lock_method) {
		# パラメータ取得
		my $param = $_[0];

		# ロックディレクトリの結合
		my $lockdir_combine = $lockdir . $param . '/';

		# ディレクトリ削除
		rmdir($lockdir_combine);
	}
}



#----------------------------------------------------------------------------------------
#  フォームログ
#----------------------------------------------------------------------------------------
sub FormLog() {
	# フォームログ取得設定時
	if ($form_logsave) {
		# セッション取得
		*getSes = GetCookie($ENV{'HTTP_COOKIE'});
		my $session = $getSes{'session'};
		# GET取得
		my $_get = $ENV{'QUERY_STRING'};
		# パラメータ分割
		@_gets = split(/&/, $_get);
		# 存在チェック用フラグ初期化
		my $flag_gets = 0;
		for(my $_get_i=0; $_get_i < @_gets; $_get_i++) {
			# 確認・エラー・戻る・完了判断と存在チェック
			if ($_gets[$_get_i] eq 'mode=confirm' || $_gets[$_get_i] eq 'mode=error' || $_gets[$_get_i] eq 'mode=back' || $_gets[$_get_i] eq 'mode=thanks') {
				$_get =~ s/mode=//g;
				$flag_gets = 1;
			}
		}
		# パラメータが存在しない為、入力ページと判断
		if (!$flag_gets) {
			$_get = 'entry';
		}
		
		my $work = @_;
		
		if (($_get ne 'error') || ($_get eq 'error' && $work)) {
			my $sesrepodata = "$year-$mon-$day-$hour-$min-$sec\t$session\t$_get\t@_\t";
			my $filename = "$year-$mon-$day.cgi";
			&mfp_SaveAddLine('./fmail.admin/datas/form_logs/' . $filename, $sesrepodata);
		}
		
		# ログデータ削除 $form_logsave_period 日間保持
		find(\&want_func, "./fmail.admin/datas/form_logs/");
	}
}



#----------------------------------------------------------------------------------------
#  古いフォームログの削除
#----------------------------------------------------------------------------------------
sub want_func{
	# 時間の取得（グリニッジ秒）
	my $nowtime = time + (9 * 3600);
	
	# 検索ファイルの内、～.cgiのみ抽出
	if($File::Find::name =~ /.cgi/){
		# ファイル名だけ抜き出し
		my @files = split(/\//,$File::Find::name);
		my $filename = $files[-1];
		# ファイルプロパティの取得
		my @filestat = stat $filename;
		
		# 現在秒 - 更新時刻秒
		my $mtime = int($nowtime - $filestat[9]);
		
		# ファイル更新日の時間差分計算
		my $del_time = int($mtime / 3600 / 24);
		
		
		# 期限切れファイル
		if ($del_time > $form_logsave_period && $form_logsave_period) {
			# 削除
			unlink $filename;
		}
	}
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

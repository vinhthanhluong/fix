###############################################################################
# Administrated Screen Start Page Functions
###############################################################################
$action_name = 'HOME';
$current_data_path = "$reg{'dir_module_data'}informations/informations\.dat";
@current_data = &loadfile($current_data_path);

for($cnt=0;$cnt<@current_data;$cnt++){
	my(@current_data_info) = split(/\t/,$current_data[$cnt]);
	($sec,$min,$hour,$day,$mon,$year) = gmtime($current_data_info[0] + 9 * 3600);
	$mon++;$year += 1900;
	$post_time_stmp = sprintf("%04d-%02d-%02d %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);
	$current_data_list .= "<dl class=\"headline\">\n";
	$current_data_list .= "<dt>${current_data_info[1]}　<span class=\"date\">（${post_time_stmp}）</span></dt>\n";
	$current_data_list .= "<dd>${current_data_info[2]}</dd>\n";
	$current_data_list .= "</dl>\n";
}

## file
if($attached_method){
	$filesize = &dirsizecheck('./datas/attached_files/');
	$usage = int($filesize / $reg{'attached_filesize'} * 100);
	if($usage > 100){
		$warning = '<strong class="warning">添付ファイルの容量が領域の100%を超えています。<br />直ちにサーバ上に保存されている添付ファイルを削除してください。</strong>';
	}
	elsif($usage > 90){
		$warning = '<strong class="warning">添付ファイルの容量が領域の90%を超えています。<br />サーバ上に保存されている添付ファイルを削除してください。</strong>';
	}
	elsif($usage > 70){
		$warning = '<strong class="warning">添付ファイルの容量が領域の70%を超えています。</strong>';
	}
	$filemsg = "<strong>${filesize}</strong>KB / $reg{'attached_filesize'}KB(${usage}%)";
}

## mailform
@update_dates = ();
my($date) = './datas/modules/mailform_env/mailform_env.dat';
my @update_dates = stat $date;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($update_dates[9] + 9 * 3600);
$mon++;$year += 1900;
$mailform_lastupdate = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);

## elements
@update_dates = ();
my($date) = './datas/modules/elements/elements.dat';
my @update_dates = stat $date;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($update_dates[9] + 9 * 3600);
$mon++;$year += 1900;
$elements_lastupdate = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);

## must conditional
@update_dates = ();
my($date) = './datas/modules/must_conditional/must_conditional.dat';
my @update_dates = stat $date;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($update_dates[9] + 9 * 3600);
$mon++;$year += 1900;
$must_conditional_lastupdate = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);

## send conditional
@update_dates = ();
my($date) = './datas/modules/send_conditional/send_conditional.dat';
my @update_dates = stat $date;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($update_dates[9] + 9 * 3600);
$mon++;$year += 1900;
$send_conditional_lastupdate = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);

## return mail
@update_dates = ();
my($date) = './datas/modules/return_mail/return_mail.dat';
my @update_dates = stat $date;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($update_dates[9] + 9 * 3600);
$mon++;$year += 1900;
$return_mail_lastupdate = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);

## log
# logdata_path setting
@mailform_env = &loadfile('./datas/modules/mailform_env/mailform_env.dat');
$mailform_env = join("\n",@mailform_env);
($mailform_flag,$expires_start,$expires_end,$limit,$serials,$thanks_page,$sendmail_path,$logsave,$cart_in_element,$cart_logsave,$form_logsave,$form_logsave_period,$send_mode,$attached_mode,$display_mode,$logdata_path,$cart_logdata_path,$mailform_sender_address_name,$mailform_sender_address,$mail_method,$thanks_message,$title_mailform,$title_confirm,$title_error,$title_thanks,$mail_dustclear,$mail_dustclear_zero,$client_info,$site_url,$table_style,$th_style,$td_style,$separate_before,$separate_after,$flag_afiri,$afiri1_tag,$afiri2_tag,$afiri3_tag,$afiri4_tag,$afiri5_tag,$flag_smartphone_tpl,$flag_futurephone_tpl,$setlang,$spamcheck,$domaincheck,$encheck) = split(/\n/,$mailform_env);

## mail log download
@log_update_dates = ();
if($logdata_path eq $null) {
	$log_date = './datas/maillog/logdata_dlstamp.cgi';
} else {
	$log_date = $logdata_path . 'logdata_dlstamp.cgi';
}
my @log_update_dates = stat $log_date;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($log_update_dates[9] + 9 * 3600);
$mon++;$year += 1900;
if(-f $log_date) {
	$log_lastupdate = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);
} else {
	$log_lastupdate = 'no history';
}

## mail log delete
@log_delete_dates = ();
if($logdata_path eq $null) {
	$log_date = './datas/maillog/logdata_delstamp.cgi';
} else {
	$log_date = $logdata_path . 'logdata_delstamp.cgi';
}
my @log_delete_dates = stat $log_date;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($log_delete_dates[9] + 9 * 3600);
$mon++;$year += 1900;
if(-f $log_date) {
	$log_lastdelete = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);
} else {
	$log_lastdelete = 'no history';
}

## mail deleteLog save
@deleteLog_save_dates = ();
if($logdata_path eq $null) {
	$deleteLog_date = './datas/maillog/deleteLog/deleteLine.cgi';
} else {
	$deleteLog_date = $logdata_path . 'deleteLog/deleteLine.cgi';
}
my @deleteLog_save_dates = stat $deleteLog_date;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($deleteLog_save_dates[9] + 9 * 3600);
$mon++;$year += 1900;
if(-f $deleteLog_date) {
	$deleteLog_lastdelete = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);
} else {
	$deleteLog_lastdelete = 'no history';
}

## cart log download
@log_update_dates = ();
if($cart_logdata_path eq $null) {
	$log_date = './datas/cartlog/cart_logdata_dlstamp.cgi';
} else {
	$log_date = $cart_logdata_path . 'cart_logdata_dlstamp.cgi';
}
my @log_update_dates = stat $log_date;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($log_update_dates[9] + 9 * 3600);
$mon++;$year += 1900;
if(-f $log_date) {
	$cart_log_lastupdate = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);
} else {
	$cart_log_lastupdate = 'no history';
}

## cart log delete
@log_delete_dates = ();
if($cart_logdata_path eq $null) {
	$log_date = './datas/cartlog/cart_logdata_delstamp.cgi';
} else {
	$log_date = $cart_logdata_path . 'cart_logdata_delstamp.cgi';
}
my @log_delete_dates = stat $log_date;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($log_delete_dates[9] + 9 * 3600);
$mon++;$year += 1900;
if(-f $log_date) {
	$cart_log_lastdelete = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);
} else {
	$cart_log_lastdelete = 'no history';
}

## postcode
@update_dates = ();
my($dir) = './datas/postcodes/';
opendir DH, $dir;
while (my $file = readdir DH) {
	next if $file =~ /^\.{1,2}$/;
	push @update_dates,(stat("${dir}${file}"))[9];
}
closedir DH;
@update_dates = reverse sort @update_dates;
($sec,$min,$hour,$day,$mon,$year,$wday,$yday,$isdst) = gmtime($update_dates[0] + 9 * 3600);
$mon++;$year += 1900;
$lastupdate = sprintf("%04d-%02d-%02d (${week[$wday]}) %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);


# メールアドレスチェック用呼び出し
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
if(($mailform_sender_address =~ /設定してください！|\@freesale.co.jp|^$/) || ($send_mailaddress =~ /設定してください！|\@freesale.co.jp|^$/) || ($return_mail_from =~ /設定してください！|\@freesale.co.jp|^$/)){
	$no_setting = '<span class="pankuzu_caution"> メールアドレスが、初期値／未設定／@freesale.co.jp です。：';
	if($mailform_sender_address =~ /設定してください！|\@freesale.co.jp|^$/){
		$env_html =<<EOD;
					<dt class="caution">└ メールアドレス：</dt>
					<dd class="caution"><span class="check">${mailform_sender_address} （本番反映前に変更してください）</span></dd>
EOD
	}
	if($send_mailaddress =~ /設定してください！|\@freesale.co.jp|^$/){
		$send_html =<<EOD;
					<dt class="caution">└ メールアドレス：</dt>
					<dd class="caution"><span class="check">${send_mailaddress} （本番反映前に変更してください）</span></dd>
EOD
	}
	if($return_mail_from =~ /設定してください！|\@freesale.co.jp|^$/){
		$return_html =<<EOD;
					<dt class="caution">└ メールアドレス：</dt>
					<dd class="caution"><span class="check">${return_mail_from} （本番反映前に変更してください）</span></dd>
EOD
	}
}




if($current_user{'power'} ne 'limited-client'){
	#管理者・通常ユーザー
	$print_html = <<"	EOF";
		<p>ようこそ、<strong class="power">$current_user{'name'}</strong> 様。この画面はメールフォームの管理画面です。</p>
		
		<div class="setting_info">設定状況一覧を開く >>></div>
		<dl class="announcement">
			<dt>Fmailバージョン：</dt>
			<dd><span class="check">$reg{version}</span></dd>
			
			<dt class="even">Perlバージョン：</dt>
			<dd class="even"><span class="check">$]</span></dd>
			
			<dt>メールフォーム設定：</dt>
			<dd><span class="check">${mailform_lastupdate}</span></dd>
			
$env_html
			
			<dt class="even">項目の設定：</dt>
			<dd class="even"><span class="check">${elements_lastupdate}</span></dd>
			
			<dt>必須条件の設定：</dt>
			<dd><span class="check">${must_conditional_lastupdate}</span></dd>
			
			<dt class="even">送信条件の設定：</dt>
			<dd class="even"><span class="check">${send_conditional_lastupdate}</span></dd>
			
$send_html
			
			<dt>自動返信メールの設定：</dt>
			<dd><span class="check">${return_mail_lastupdate}</span></dd>
			
$return_html
			
			<dt class="even">メール履歴管理・閲覧　Download：</dt>
			<dd class="even"><span class="check">${log_lastupdate}</span></dd>
			
			<dt>メール履歴管理・閲覧　初期化：</dt>
			<dd><span class="check">${log_lastdelete}</span></dd>
			
			<dt class="even">メール履歴管理・閲覧　レコード削除：</dt>
			<dd class="even"><span class="check">${deleteLog_lastdelete}</span></dd>
			
			<dt>商品カート履歴管理・閲覧　Download：</dt>
			<dd><span class="check">${cart_log_lastupdate}</span></dd>
			
			<dt class="even">商品カート履歴管理・閲覧　初期化：</dt>
			<dd class="even"><span class="check">${cart_log_lastdelete}</span></dd>
			
			<dt>郵便番号辞書更新：</dt>
			<dd><span class="check">${lastupdate}</span></dd>
			
			<dt class="even">添付ファイル領域使用状況：</dt>
			<dd class="even">
				<span class="check">${filemsg}</span><br />
				${warning}
			</dd>
			
		</dl>
		${current_data_list}
	EOF
}else{	
	#限定クライアント用の特殊処理
	$print_html = <<"	EOF";
		<p>ようこそ、<strong class="power">$current_user{'name'}</strong> 様。</p>
		<p>お問い合わせログは、「メール履歴管理・閲覧」・「商品カート履歴管理・閲覧」で確認できます。</p>
		<p>パスワードは、「環境設定」で変更できます。</p>
	EOF
}




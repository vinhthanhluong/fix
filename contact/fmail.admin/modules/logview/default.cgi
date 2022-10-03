###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################
use File::Find;

# logdata_path setting
@mailform_env = &loadfile('./datas/modules/mailform_env/mailform_env.dat');
$mailform_env = join("\n",@mailform_env);
($mailform_flag,$expires_start,$expires_end,$limit,$serials,$thanks_page,$sendmail_path,$logsave,$cart_in_element,$cart_logsave,$form_logsave,$form_logsave_period,$send_mode,$attached_mode,$display_mode,$logdata_path,$cart_logdata_path,$mailform_sender_address_name,$mailform_sender_address,$mail_method,$thanks_message,$title_mailform,$title_confirm,$title_error,$title_thanks,$mail_dustclear,$mail_dustclear_zero,$client_info,$site_url,$table_style,$th_style,$td_style,$separate_before,$separate_after,$flag_afiri,$afiri1_tag,$afiri2_tag,$afiri3_tag,$afiri4_tag,$afiri5_tag,$flag_smartphone_tpl,$flag_futurephone_tpl,$setlang,$spamcheck,$domaincheck,$encheck) = split(/\n/,$mailform_env);

# Mail log directory
if($logdata_path eq $null) {
	$maillog_dir = './datas/maillog/';
} else {
	$maillog_dir = $logdata_path;
}

# File list pickup
$maillog_filelist = '';
# File search
find(\&mail_want_func, "$maillog_dir");
# Separated ","
@maillog_filelist_arr = split(/,/,$maillog_filelist);
@maillog_filelist_arr = sort { $b cmp $a } @maillog_filelist_arr;

# Data extraction date
if($logdata_path eq $null) {
	@mailstamp = &loadfile('./datas/maillog/maillog_select.cgi');
} else {
	@mailstamp = &loadfile($logdata_path . 'maillog_select.cgi');
}

$mailstamp = join("\n",@mailstamp);
($mailstamp) = split(/\n/,$mailstamp);

if(!$mailstamp) {
	$mailstamp = sprintf("%04d-%02d",$year,$mon);
}

@mailstamp_arr = split(/-/,$mailstamp);

# Separated "-"
$mailselect = "<select name=\"maillog_target\" onchange=\"mailselect_save(this,\'$form{'m'}\');\">\n";
$mailselect .= "			<option value=\"$mailstamp_arr[0]-$mailstamp_arr[1]\" selected=\"selected\">$mailstamp_arr[0]年$mailstamp_arr[1]月</option>\n";
for($mail_i=0; $mail_i<@maillog_filelist_arr; $mail_i++) {
	@maillog_monlist_arr = split(/-/,$maillog_filelist_arr[$mail_i]);
	$maillog_monlist_arr[2] =~ s/.cgi//g;
	#$mailselect .= $maillog_monlist_arr[1] . '年' .$maillog_monlist_arr[2] . '月';
	$mailselect .= "			<option value=\"$maillog_monlist_arr[1]-$maillog_monlist_arr[2]\">$maillog_monlist_arr[1]年$maillog_monlist_arr[2]月</option>\n";
}
$mailselect .= "		</select>\n";

#$mailstamp = sprintf("%04d-%02d",$year,$mon);
#$logdata_path = './datas/maillog/mail_logdata-' . $mailstamp . '.cgi';

if($logdata_path eq $null) {
	$logdata_path = './datas/maillog/mail_logdata-' . $mailstamp . '.cgi';
} else {
	$logdata_path = $logdata_path . 'mail_logdata-' . $mailstamp . '.cgi';
}

@list = &loadfile($logdata_path);
$action_name = 'メール送信履歴';
if($form{'q'} ne $null){
	$form{'q'} =~ s/　/ /ig;
	$form{'q'} =~ s/</&lt;/g;
	$form{'q'} =~ s/>/&gt;/g;
	$form{'q'} =~ s/\[//g;
	$form{'q'} =~ s/\]//g;
	my(@keys) = split(/ /,$form{'q'});
	for($cnt=0;$cnt<@keys;$cnt++){
		@list = grep {/$keys[$cnt]/} @list;
	}
}
for($cnt=0;$cnt<@list;$cnt++){
	my(@record) = split(/\t/,$list[$cnt]);
	$users_list .= "<tr onmouseover=\"this.style.backgroundColor='#E8EEF9';\" onmouseout=\"this.style.backgroundColor='#FFFFFF';\">\n";
#	$users_list .= "<td><a href=\"?m=$form{'m'}&a=form&v=$mailstamp_arr[0]-$mailstamp_arr[1]&id=$record[1]\">${record[2]} > ${record[0]}</a></td>\n";
	$users_list .= "<td><a href=\"?m=$form{'m'}&a=form&v=$mailstamp_arr[0]-$mailstamp_arr[1]&id=$record[1]\" target=\"_blank\">${record[2]} > ${record[0]} > ${record[3]} > ${record[4]} > ${record[5]}</a></td>\n";
	$users_list .= "<td class=\"del\"><img src=\"modules/elements/images/button_delete.gif\" width=\"60\" height=\"20\" alt=\"削除\" class=\"button\" onclick=\"delete_confirm('?m=$form{'m'}&a=delete&file=$logdata_path&id=${record[1]}','${record[2]}');\" /></td>\n";
	#$users_list .= "<td style=\"width: 40px;\"><img src=\"images/button_edit.gif\" width=\"30\" height=\"20\" alt=\"編集\" class=\"button\" onclick=\"location.href='?m=$form{'m'}&a=form&id=$record[1]'\" /></td>\n";
	#$users_list .= "<td style=\"width: 40px;\"><img src=\"images/button_delete.gif\" width=\"30\" height=\"20\" alt=\"削除\" class=\"button\" onclick=\"delete_confirm('?m=$form{'m'}&a=delete&id=${record[0]}','${record[1]}');\" /></td>\n";
	$users_list .= "</tr>\n";
}
$print_html = <<"EOF";
	<span onclick="logformat(\'$mailstamp_arr[0]-$mailstamp_arr[1]\')" class="format">初期化する</span>
	<a href="download.cgi?mode=csvdownload&path=${logdata_path}&line=codebr" class="download codebr">ダウンロード（\n改行）</a>
	<a href="download.cgi?mode=csvdownload&path=${logdata_path}&line=br" class="download br">ダウンロード（BR改行）</a>
	<a href="download.cgi?mode=csvdownload&path=${logdata_path}" class="download nobr">ダウンロード（改行なし）</a>
	<p>
		※CSVファイル利用時、<span class="info">レコードが正常に表示されない場合は<strong>「改行なし」</strong>をご利用ください。</span><br />
	</p>
	<form class="dataselect" method="get">
		$mailselect
		<span class="info">対象月を選択してください</span>
	</form>
	<form id="search" method="get">
		<input type="hidden" name="m" value="$form{'m'}" />
		<input type="text" name="q" id="search_q" value="$form{'q'}" />
		<input type="submit" name="submit" id="submit" value="検索" />
	</form>
	<table cellpadding="0" cellspacing="0" class="list">
		${users_list}
	</table>
EOF


#----------------------------------------------------------------------------------------
#  Remove the old session files
#----------------------------------------------------------------------------------------
sub mail_want_func {
	# cgi file extraction
	if($File::Find::name =~ /.cgi/ && $File::Find::name !~ /.backup/ && $File::Find::name !~ /logdata_delstamp.cgi/ && $File::Find::name !~ /logdata_dlstamp.cgi/ && $File::Find::name !~ /maillog_select/ && $File::Find::name !~ /deleteLine.cgi/){
		$maillog_filelist .= "$File::Find::name,";
	}
}

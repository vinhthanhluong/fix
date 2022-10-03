###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################
use File::Find;

# logdata_path setting
@mailform_env = &loadfile('./datas/modules/mailform_env/mailform_env.dat');
$mailform_env = join("\n",@mailform_env);
($mailform_flag,$expires_start,$expires_end,$limit,$serials,$thanks_page,$sendmail_path,$logsave,$cart_in_element,$cart_logsave,$form_logsave,$form_logsave_period,$send_mode,$attached_mode,$display_mode,$logdata_path,$cart_logdata_path,$mailform_sender_address_name,$mailform_sender_address,$mail_method,$thanks_message,$title_mailform,$title_confirm,$title_error,$title_thanks,$mail_dustclear,$mail_dustclear_zero,$client_info,$site_url,$table_style,$th_style,$td_style,$separate_before,$separate_after,$flag_afiri,$afiri1_tag,$afiri2_tag,$afiri3_tag,$afiri4_tag,$afiri5_tag,$flag_smartphone_tpl,$flag_futurephone_tpl,$setlang,$spamcheck,$domaincheck,$encheck) = split(/\n/,$mailform_env);

# Cart log directory
if($cart_logdata_path eq $null) {
	$cartlog_dir = './datas/cartlog/';
} else {
	$cartlog_dir = $cart_logdata_path;
}

# File list pickup
$cartlog_filelist = '';
# File search
find(\&cart_want_func, "$cartlog_dir");
# Separated ","
@cartlog_filelist_arr = split(/,/,$cartlog_filelist);
@cartlog_filelist_arr = sort { $b cmp $a } @cartlog_filelist_arr;

# Data extraction date
if($cart_logdata_path eq $null) {
	@cartstamp = &loadfile('./datas/cartlog/cartlog_select.cgi');
} else {
	@cartstamp = &loadfile($cart_logdata_path . 'cartlog_select.cgi');
}

$cartstamp = join("\n",@cartstamp);
($cartstamp) = split(/\n/,$cartstamp);

if(!$cartstamp) {
	$cartstamp = sprintf("%04d-%02d",$year,$mon);
}

@cartstamp_arr = split(/-/,$cartstamp);

# Separated "-"
$cartselect = "<select name=\"cartlog_target\" onchange=\"cartselect_save(this,\'$form{'m'}\');\">\n";
$cartselect .= "			<option value=\"$cartstamp_arr[0]-$cartstamp_arr[1]\" selected=\"selected\">$cartstamp_arr[0]年$cartstamp_arr[1]月</option>\n";
for($cart_i=0; $cart_i<@cartlog_filelist_arr; $cart_i++) {
	@cartlog_monlist_arr = split(/-/,$cartlog_filelist_arr[$cart_i]);
	$cartlog_monlist_arr[2] =~ s/.cgi//g;
	#$cartselect .= $cartlog_monlist_arr[1] . '年' .$cartlog_monlist_arr[2] . '月';
	$cartselect .= "			<option value=\"$cartlog_monlist_arr[1]-$cartlog_monlist_arr[2]\">$cartlog_monlist_arr[1]年$cartlog_monlist_arr[2]月</option>\n";
}
$cartselect .= "		</select>\n";

#$cartstamp = sprintf("%04d-%02d",$year,$mon);
#$logdata_path = './datas/cartlog/cart_logdata-' . $cartstamp . '.cgi';

if($cart_logdata_path eq $null) {
	$logdata_path = './datas/cartlog/cart_logdata-' . $cartstamp . '.cgi';
} else {
	$logdata_path = $cart_logdata_path . 'cart_logdata-' . $cartstamp . '.cgi';
}

@list = &loadfile($logdata_path);
$action_name = '商品カート送信履歴';
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
	$users_list .= "<td><a href=\"?m=$form{'m'}&a=form&v=$cartstamp_arr[0]-$cartstamp_arr[1]&id=$record[1]\" target=\"_blank\">${record[0]} > ${record[1]} > ${record[2]} > ${record[3]}</a></td>\n";
	#$users_list .= "<td style=\"width: 40px;\"><img src=\"images/button_edit.gif\" width=\"30\" height=\"20\" alt=\"編集\" class=\"button\" onclick=\"location.href='?m=$form{'m'}&a=form&id=$record[1]'\" /></td>\n";
	#$users_list .= "<td style=\"width: 40px;\"><img src=\"images/button_delete.gif\" width=\"30\" height=\"20\" alt=\"削除\" class=\"button\" onclick=\"delete_confirm('?m=$form{'m'}&a=delete&id=${record[0]}','${record[1]}');\" /></td>\n";
	$users_list .= "</tr>\n";
}
$print_html = <<"EOF";
	<span onclick="cart_logformat(\'$cartstamp_arr[0]-$cartstamp_arr[1]\')" class="format">初期化する</span>
	<a href="download_cart.cgi?mode=csvdownload&path=${logdata_path}&line=codebr" class="download codebr">ダウンロード（\n改行）</a>
	<a href="download_cart.cgi?mode=csvdownload&path=${logdata_path}&line=br" class="download br">ダウンロード（BR改行）</a>
	<a href="download_cart.cgi?mode=csvdownload&path=${logdata_path}" class="download nobr">ダウンロード（改行なし）</a>
	<p>
		※CSVファイル利用時、<span class="info">レコードが正常に表示されない場合は<strong>「改行なし」</strong>をご利用ください。</span><br />
	</p>
	<form class="dataselect" method="get">
		$cartselect
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
sub cart_want_func {
	# cgi file extraction
	if($File::Find::name =~ /.cgi/ && $File::Find::name !~ /.backup/ && $File::Find::name !~ /cart_logdata_delstamp.cgi/ && $File::Find::name !~ /cart_logdata_dlstamp.cgi/ && $File::Find::name !~ /cartlog_select/){
		$cartlog_filelist .= "$File::Find::name,";
	}
}

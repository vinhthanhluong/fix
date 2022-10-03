###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

@mailform_env = &loadfile('./datas/modules/mailform_env/mailform_env.dat');
$mailform_env = join("\n",@mailform_env);
($mailform_flag,$expires_start,$expires_end,$limit,$serials,$thanks_page,$sendmail_path,$logsave,$cart_in_element,$cart_logsave,$form_logsave,$form_logsave_period,$send_mode,$attached_mode,$display_mode,$logdata_path,$cart_logdata_path,$mailform_sender_address_name,$mailform_sender_address,$mail_method,$thanks_message,$title_mailform,$title_confirm,$title_error,$title_thanks,$mail_dustclear,$mail_dustclear_zero,$client_info,$site_url,$table_style,$th_style,$td_style,$separate_before,$separate_after,$flag_afiri,$afiri1_tag,$afiri2_tag,$afiri3_tag,$afiri4_tag,$afiri5_tag,$flag_smartphone_tpl,$flag_futurephone_tpl,$setlang,$spamcheck,$domaincheck,$encheck) = split(/\n/,$mailform_env);

# escape
$cart_logdata_path_copy = $cart_logdata_path;

if($cart_logdata_path eq $null) {
	$cart_logdata_path = './datas/cartlog/cart_logdata-' . $form{'v'} . '.cgi';
} else {
	$cart_logdata_path = $cart_logdata_path . 'cart_logdata-' . $form{'v'} . '.cgi';
}
	
# BUファイルも定義して削除
$cart_logdata_bu_path = $cart_logdata_path . '.backup';

&dirclear('./datas/attached_files/');
&savefile($cart_logdata_path,@null);
&savefile($cart_logdata_bu_path,@null);

# 初期化履歴の保存
if($cart_logdata_path_copy eq $null){
	$delstamp_path = './datas/cartlog/cart_logdata_delstamp.cgi';
} else {
	$delstamp_path = $cart_logdata_path_copy . 'cart_logdata_delstamp.cgi';
}
$date_stamp = sprintf("%04d/%02d/%02d %02d:%02d:%02d",$year,$mon,$day,$hour,$min,$sec);
&mfp_SaveAddLine($delstamp_path,$date_stamp);

$redirect = "?m=$form{'m'}";

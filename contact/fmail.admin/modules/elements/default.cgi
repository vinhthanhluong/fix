###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

@mailform_env = &loadfile('./datas/modules/mailform_env/mailform_env.dat');
$mailform_env = join("\n",@mailform_env);
($mailform_flag,$expires_start,$expires_end,$limit,$serials,$thanks_page,$sendmail_path,$logsave,$cart_in_element,$cart_logsave,$form_logsave,$form_logsave_period,$send_mode,$attached_mode,$display_mode,$logdata_path,$cart_logdata_path,$mailform_sender_address_name,$mailform_sender_address,$mail_method,$thanks_message,$title_mailform,$title_confirm,$title_error,$title_thanks,$mail_dustclear,$mail_dustclear_zero,$client_info,$site_url,$table_style,$th_style,$td_style,$separate_before,$separate_after,$flag_afiri,$afiri1_tag,$afiri2_tag,$afiri3_tag,$afiri4_tag,$afiri5_tag,$flag_smartphone_tpl,$flag_futurephone_tpl,$setlang,$spamcheck,$domaincheck,$encheck) = split(/\n/,$mailform_env);

# Mail log directory
if($logdata_path eq $null) {
	$maillog_dir = './datas/maillog/';
} else {
	$maillog_dir = $logdata_path;
}

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

if($logdata_path eq $null) {
	$logdata_path = './datas/maillog/mail_logdata-' . $mailstamp . '.cgi';
} else {
	$logdata_path = $logdata_path . 'mail_logdata-' . $mailstamp . '.cgi';
}


if((-f $logdata_path) && $logdata_path ne $null){
	$filesize = -s $logdata_path;
}
else {
	$logdata_path = './datas/logdata.cgi';
	$filesize = -s $logdata_path;
}

$action_name = 'メールフォームの項目一覧';
if($filesize > 0){
	$print_html = <<"	EOF";
		<p>ログファイルが蓄積された状態です。<br /><a href="index.cgi?m=logview" class="strong">ログファイルを初期化、もしくは0000年00月を選択</a><br />してから再度、お試しください</p>
		<p class="caution">送信履歴が蓄積されている場合、項目内容の変更以外で、<span class="strong">項目の追加・削除を行うと送信履歴の項目がずれてしまいます</span>のでご注意ください。</p>
	EOF
}
else {
	for($cnt=0;$cnt<@current_data;$cnt++){
		#my(@current_record) = split(/\t/,$current_data[$cnt]);
		($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_element_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$current_data[$cnt]);
		
		$addclass = ${elements_class} ? qq| (追加Class:<span class="info">${elements_class}</span>)| : "";
		$sysdisp = ${system_disp_false} ? qq| <span class="caution">(非表示)</span>| : "";
		$mustdisp = ${must_disp} ? qq| <img src="../images/mfp_must.gif" class="must_icon">| : "";
		$ordisp = ${or_disp} ? qq| <img src="../images/mfp_or.gif" class="or_icon">| : "";
		
		$users_list .= qq|<tr onmouseover="this.style.backgroundColor='#E8EEF9';" onmouseout="this.style.backgroundColor='#FFFFFF';">\n|;
		$users_list .= qq|<td class="adjust_sort"><a href="?m=$form{'m'}&a=sort_one&id=${elements_id}&rank=up"><img src="modules/elements/images/sort_up.gif"></a><a href="?m=$form{'m'}&a=sort_one&id=${elements_id}&rank=down"><img src="modules/elements/images/sort_down.gif"></a></td>\n|;
		$users_list .= qq|<td class="item"><input type="text" size="4" value="${num}" name="${elements_id}" class="sort_num" /><a href="?m=$form{'m'}&a=form&id=$elements_id">${name} (${element_type})$mustdisp$ordisp$addclass$sysdisp</a></td>\n|;
		$users_list .= qq|<td class="edit"><img src="modules/elements/images/button_edit.gif" width="60" height="20" alt="編集" class="button" onclick="location.href='?m=$form{'m'}&a=form&id=$elements_id'" /></td>\n|;
		$users_list .= qq|<td class="copy"><img src="modules/elements/images/button_copy.gif" width="60" height="20" alt="複製" class="button" onclick="copy_confirm('?m=$form{'m'}&a=copy&id=${elements_id}','${name}');" /></td>\n|;
		$users_list .= qq|<td class="del"><img src="modules/elements/images/button_delete.gif" width="60" height="20" alt="削除" class="button" onclick="delete_confirm('?m=$form{'m'}&a=delete&id=${elements_id}','${name}');" /></td>\n|;
		$users_list .= qq|<td class="delete_check"><label for="delete_${elements_id}"><input type="checkbox" value="${elements_id}" name="delete_${elements_id}" id="delete_${elements_id}" /></label></td>\n|;
		$users_list .= qq|</tr>\n|;
	}
	$print_html = <<"	EOF";
		<form id="user_add" action="?m=$form{'m'}&a=sort" method="POST" onsubmit="return gosort()">
		<input type="submit" value="項目の並び替え" class="sort_button" onclick="select_delete_check('sort');" onkeyup="select_delete_check('sort');" />
		<a href="?m=$form{'m'}&a=form" class="add">項目を追加する</a>
		<input type="submit" value="選択項目の削除" class="delete_button" onclick="select_delete_check('del');" onkeyup="select_delete_check('del');" />
		<table cellpadding="0" cellspacing="0" class="list">
			${users_list}
		</table>
		<input type="submit" value="項目の並び替え" class="sort_button" onclick="select_delete_check('sort');" onkeyup="select_delete_check('sort');" />
		<a href="?m=$form{'m'}&a=form" class="add">項目を追加する</a>
		<input type="submit" value="選択項目の削除" class="delete_button" onclick="select_delete_check('del');" onkeyup="select_delete_check('del');" />
		<input type="hidden" name="flag_delete_value" value="" id="flag_delete" />
		</form>
	EOF
}

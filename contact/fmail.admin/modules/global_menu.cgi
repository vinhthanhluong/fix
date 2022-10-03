###############################################################################
# Administrated Screen Global Menu Functions
###############################################################################
#限定ユーザ判定
if($current_user{'power'} eq 'limited-client'){
	#限定ユーザ
	$gnavi_current_data_path = './datas/modules/mailform_env/mailform_env.dat';
	@gnavi_current_data = &loadfile($gnavi_current_data_path);
	$gnavi_current_data = join("\n",@gnavi_current_data);
	($gnavi_flag,$gnavi_expires_start,$gnavi_expires_end,$gnavi_limit,$gnavi_serials,$gnavi_thanks_page,$gnavi_sendmail_path,$gnavi_logsave,$gnavi_cart_in_element,$gnavi_cart_logsave,$gnavi_form_logsave,$gnavi_form_logsave_period,$gnavi_send_mode,$gnavi_attached_mode,$gnavi_display_mode,$gnavi_logdata_path,$gnavi_cart_logdata_path,$gnavi_mailform_sender_address_name,$gnavi_mailform_sender_address,$gnavi_mail_method,$gnavi_thanks_message,$gnavi_title_mailform,$gnavi_title_confirm,$gnavi_title_error,$gnavi_title_thanks,$gnavi_mail_dustclear,$gnavi_mail_dustclear_zero,$gnavi_client_info,$gnavi_site_url,$gnavi_table_style,$gnavi_th_style,$gnavi_td_style,$gnavi_separate_before,$gnavi_separate_after,$gnavi_flag_afiri,$gnavi_afiri1_tag,$gnavi_afiri2_tag,$gnavi_afiri3_tag,$gnavi_afiri4_tag,$gnavi_afiri5_tag,$gnavi_flag_smartphone_tpl,$gnavi_flag_futurephone_tpl,$gnavi_setlang,$gnavi_spamcheck,$gnavi_domaincheck,$gnavi_encheck) = split(/\n/,$gnavi_current_data);
	
	for($cnt=0;$cnt<@module_list;$cnt++){
		if(index($module_list_powers_limited[$cnt],"%%$current_user{'power'}%%") > -1 || $module_list_powers_limited[$cnt] eq $null || $module_list_powers_limited[$cnt] eq "null"){
			# カート機能がONの場合のみ限定クライアントでも、ナビにカート関連機能を表示させる
			if(${module_list[$cnt]} ne 'cart_logview') {
				$module_list .= "<li><a href=\"?m=${module_list[$cnt]}\" class=\"module\">${module_list_names[$cnt]}<span>${module_list_subnames[$cnt]}</span></a></li>\n";
			} elsif(${module_list[$cnt]} eq 'cart_logview' && $gnavi_cart_logsave) {
				$module_list .= "<li><a href=\"?m=${module_list[$cnt]}\" class=\"module\">${module_list_names[$cnt]}<span>${module_list_subnames[$cnt]}</span></a></li>\n";
			}
		}
	}
}else{
	#管理者
	for($cnt=0;$cnt<@module_list;$cnt++){
		if(index($module_list_powers[$cnt],"%%$current_user{'power'}%%") > -1 || $module_list_powers[$cnt] eq $null || $module_list_powers[$cnt] eq "null"){
			if(${module_list_subnames[$cnt]} eq 'check'){
				if($current_user{'pw'} eq 'admin'){
					$module_list .= "<li><a href=\"?m=${module_list[$cnt]}\" class=\"module\">${module_list_names[$cnt]}<span>${module_list_subnames[$cnt]}</span></a></li>\n";
				}
			}else{
				$module_list .= "<li><a href=\"?m=${module_list[$cnt]}\" class=\"module\">${module_list_names[$cnt]}<span>${module_list_subnames[$cnt]}</span></a></li>\n";
			}
		}
	}
}
#modulelist.cgi
$globalmenu = <<"EOF";
<a id="logout" href="?user_id=${user_id}&login_user_password=logout">LOGOUT</a>
EOF

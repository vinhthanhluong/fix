###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = $form{'id'} . 'モジュール アクションの一覧';
@registry = &loadfile("${dir_datas}$form{'m'}\/$form{'id'}\.power\.dat");
for($cnt=0;$cnt<@registry;$cnt++){
	my(@registry_info) = split(/\t/,$registry[$cnt]);
	$registry_list .= "<tr onmouseover=\"this.style.backgroundColor='#E8EEF9';\" onmouseout=\"this.style.backgroundColor='#FFFFFF';\">\n";
	$registry_list .= "<td><a href=\"?m=$form{'m'}&a=power_form&id=$registry_info[0]&module=$form{'id'}\">${registry_info[0]}</a></td>\n";
	$registry_list .= "<td style=\"width: 40px;\"><img src=\"images/button_edit.gif\" width=\"50\" height=\"20\" alt=\"編集\" class=\"button\" onclick=\"location.href='?m=$form{'m'}&a=power_form&id=$registry_info[0]&module=$form{'id'}'\" /></td>\n";
	$registry_list .= "</tr>\n";
}
$print_html = <<"EOF";
	<table cellpadding="0" cellspacing="0" class="list" style="margin-top: 10px;">
		${registry_list}
	</table>
EOF

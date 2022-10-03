###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = $form{'id'} . 'モジュール レジストリの一覧';
@registry = &loadfile("${dir_datas}$form{'m'}\/$form{'id'}\.dat");
for($cnt=0;$cnt<@registry;$cnt++){
	my(@registry_info) = split(/\t/,$registry[$cnt]);
	$registry_list .= "<tr onmouseover=\"this.style.backgroundColor='#E8EEF9';\" onmouseout=\"this.style.backgroundColor='#FFFFFF';\">\n";
	$registry_list .= "<td><a href=\"?m=$form{'m'}&a=form&id=$registry_info[0]&module=$form{'id'}\">${registry_info[2]}(${registry_info[0]})</a></td>\n";
	$registry_list .= "<td style=\"width: 40px;\"><img src=\"images/button_edit.gif\" width=\"50\" height=\"20\" alt=\"編集\" class=\"button\" onclick=\"location.href='?m=$form{'m'}&a=form&id=$registry_info[0]&module=$form{'id'}'\" /></td>\n";
	$registry_list .= "<td style=\"width: 40px;\"><img src=\"images/button_delete.gif\" width=\"50\" height=\"20\" alt=\"削除\" class=\"button\" onclick=\"delete_confirm('?m=$form{'m'}&a=delete&id=${registry_info[0]}&module=$form{'id'}','${registry_info[0]}');\" /></td>\n";
	$registry_list .= "</tr>\n";
}
$print_html = <<"EOF";
	<a href="?m=$form{'m'}&a=form&module=$form{'id'}" class="add">レジストリを追加する</a>
	<table cellpadding="0" cellspacing="0" class="list">
		${registry_list}
	</table>
EOF

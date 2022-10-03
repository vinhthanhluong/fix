###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '送信条件の一覧';
for($cnt=0;$cnt<@current_data;$cnt++){
	my(@current_record) = split(/\t/,$current_data[$cnt]);
	$users_list .= "<tr onmouseover=\"this.style.backgroundColor='#E8EEF9';\" onmouseout=\"this.style.backgroundColor='#FFFFFF';\">\n";
	$users_list .= "<td><a href=\"?m=$form{'m'}&a=form&id=$current_record[0]\">${current_record[2]}</a></td>\n";
	$users_list .= "<td style=\"width: 40px;\"><img src=\"images/button_edit.gif\" width=\"50\" height=\"20\" alt=\"編集\" class=\"button\" onclick=\"location.href='?m=$form{'m'}&a=form&id=$current_record[0]'\" /></td>\n";
	$users_list .= "<td style=\"width: 40px;\"><img src=\"images/button_delete.gif\" width=\"50\" height=\"20\" alt=\"削除\" class=\"button\" onclick=\"delete_confirm('?m=$form{'m'}&a=delete&id=${current_record[0]}','${current_record[2]}');\" /></td>\n";
	$users_list .= "</tr>\n";
}
$print_html = <<"EOF";
	<a href="?m=$form{'m'}&a=form" class="add">条件を追加する</a>
	<table cellpadding="0" cellspacing="0" class="list">
		${users_list}
	</table>
EOF

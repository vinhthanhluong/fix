###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'ユーザ一覧';
if($form{'q'} ne $null){
	$form{'q'} =~ s/　/ /ig;
	$form{'q'} =~ s/</&lt;/g;
	$form{'q'} =~ s/>/&gt;/g;
	$form{'q'} =~ s/\[//g;
	$form{'q'} =~ s/\]//g;
	my(@keys) = split(/ /,$form{'q'});
	for($cnt=0;$cnt<@keys;$cnt++){
		@users = grep {/$keys[$cnt]/} @users;
	}
}
for($cnt=0;$cnt<@users;$cnt++){
	my(@users_info) = split(/\t/,$users[$cnt]);
	$users_list .= "<tr onmouseover=\"this.style.backgroundColor='#E8EEF9';\" onmouseout=\"this.style.backgroundColor='#FFFFFF';\">\n";
	$users_list .= "<td><a href=\"?m=$form{'m'}&a=form&id=$users_info[0]\">${users_info[4]}($power{$users_info[2]})</a></td>\n";
	$users_list .= "<td style=\"width: 40px;\"><img src=\"images/button_edit.gif\" width=\"50\" height=\"20\" alt=\"編集\" class=\"button\" onclick=\"location.href='?m=$form{'m'}&a=form&id=$users_info[0]'\" /></td>\n";
	$users_list .= "<td style=\"width: 40px;\"><img src=\"images/button_delete.gif\" width=\"50\" height=\"20\" alt=\"削除\" class=\"button\" onclick=\"delete_confirm('?m=$form{'m'}&a=delete&id=${users_info[0]}','${users_info[4]}');\" /></td>\n";
	$users_list .= "</tr>\n";
}
$print_html = <<"EOF";
	<a href="?m=$form{'m'}&a=form" class="add">ユーザを追加する</a>
	<form id="search" method="get">
		<input type="hidden" name="m" value="$form{'m'}" />
		<input type="text" name="q" value="$form{'q'}" />
		<div class="hide"><span><input type="submit" name="submit" id="submit" /></span></div>
	</form>
	<table cellpadding="0" cellspacing="0" class="list">
		${users_list}
	</table>
EOF

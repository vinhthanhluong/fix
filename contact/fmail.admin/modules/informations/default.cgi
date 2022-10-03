###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'お知らせ一覧';
if($form{'q'} ne $null){
	$form{'q'} =~ s/　/ /ig;
	$form{'q'} =~ s/</&lt;/g;
	$form{'q'} =~ s/>/&gt;/g;
	$form{'q'} =~ s/\[//g;
	$form{'q'} =~ s/\]//g;
	my(@keys) = split(/ /,$form{'q'});
	for($cnt=0;$cnt<@keys;$cnt++){
		@current_data = grep {/$keys[$cnt]/} @current_data;
	}
}
for($cnt=0;$cnt<@current_data;$cnt++){
	my(@current_data_info) = split(/\t/,$current_data[$cnt]);
	$current_data_list .= "<tr onmouseover=\"this.style.backgroundColor='#E8EEF9';\" onmouseout=\"this.style.backgroundColor='#FFFFFF';\">\n";
	$current_data_list .= "<th><a href=\"?m=$form{'m'}&a=form&id=$current_data_info[0]\">${current_data_info[1]}</a></th>\n";
	$current_data_list .= "<td style=\"width: 40px;\"><img src=\"images/button_edit.gif\" width=\"50\" height=\"20\" alt=\"編集\" class=\"button\" onclick=\"location.href='?m=$form{'m'}&a=form&id=$current_data_info[0]'\" /></td>\n";
	$current_data_list .= "<td style=\"width: 40px;\"><img src=\"images/button_delete.gif\" width=\"50\" height=\"20\" alt=\"削除\" class=\"button\" onclick=\"delete_confirm('?m=$form{'m'}&a=delete&id=${current_data_info[0]}','${current_data_info[1]}');\" /></td>\n";
	$current_data_list .= "</tr>\n";
}
$print_html = <<"EOF";
	<a href="?m=$form{'m'}&a=form" class="add">お知らせを追加する</a>
	<form id="search" method="get">
		<input type="hidden" name="m" value="$form{'m'}" />
		<input type="text" name="q" value="$form{'q'}" class="q" />
		<div class="hide"><span><input type="submit" name="submit" id="submit" /></span></div>
	</form>
	<table cellpadding="0" cellspacing="0" class="list">
		${current_data_list}
	</table>
EOF

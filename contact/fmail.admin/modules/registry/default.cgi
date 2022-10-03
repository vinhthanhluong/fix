###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'レジストリ一覧';
if($form{'q'} ne $null){
	$form{'q'} =~ s/　/ /ig;
	$form{'q'} =~ s/</&lt;/g;
	$form{'q'} =~ s/>/&gt;/g;
	$form{'q'} =~ s/\[//g;
	$form{'q'} =~ s/\]//g;
	my(@keys) = split(/ /,$form{'q'});
	for($cnt=0;$cnt<@keys;$cnt++){
		@registry = grep {/$keys[$cnt]/} @registry;
	}
}
for($cnt=0;$cnt<@registry;$cnt++){
	my(@registry_info) = split(/\t/,$registry[$cnt]);
	$registry_list .= "<tr onmouseover=\"this.style.backgroundColor='#E8EEF9';\" onmouseout=\"this.style.backgroundColor='#FFFFFF';\">\n";
	$registry_list .= "<td><a href=\"?m=$form{'m'}&a=form&id=$registry_info[0]\">${registry_info[2]}(${registry_info[0]})</a></td>\n";
	$registry_list .= "<td style=\"width: 40px;\"><img src=\"images/button_edit.gif\" width=\"50\" height=\"20\" alt=\"編集\" class=\"button\" onclick=\"location.href='?m=$form{'m'}&a=form&id=$registry_info[0]'\" /></td>\n";
	$registry_list .= "<td style=\"width: 40px;\"><img src=\"images/button_delete.gif\" width=\"50\" height=\"20\" alt=\"削除\" class=\"button\" onclick=\"delete_confirm('?m=$form{'m'}&a=delete&id=${registry_info[0]}','${registry_info[0]}');\" /></td>\n";
	$registry_list .= "</tr>\n";
}
$print_html = <<"EOF";
<p>レジストリの一覧を\表\示します。追加編集は慎重に行ってください。動かなくなりますから。</p>
<a href="?m=$form{'m'}&a=form" class="add">レジストリを追加する</a>
<form id="search" method="get">
	<input type="hidden" name="m" value="$form{'m'}" />
	<input type="text" name="q" value="$form{'q'}" />
	<div class="hide"><span><input type="submit" name="submit" id="submit" /></span></div>
</form>
<table cellpadding="0" cellspacing="0" class="list">
	${registry_list}
</table>
EOF

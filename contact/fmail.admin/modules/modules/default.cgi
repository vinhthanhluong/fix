###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'モジュール一覧';
%disp_flag = ();
for($cnt=0;$cnt<@users;$cnt++){
	my(@users_info) = split(/\t/,$users[$cnt]);
	$disp_flag{$users_info[0]} = 1;
	$users_list .= "<tr onmouseover=\"this.style.backgroundColor='#E8EEF9';\" onmouseout=\"this.style.backgroundColor='#FFFFFF';\">\n";
	$users_list .= "<td style=\"width: 80px;\"><input type=\"text\" name=\"${users_info[0]}\" value=\"${users_info[1]}\" style=\"width: 40px;text-align: center;\" /></td>\n";
	$users_list .= "<td>${users_info[0]} (${users_info[2]})</td>\n";
	$users_list .= "<td style=\"width: 100px;\"><img src=\"images/button_power.gif\" class=\"button\" width=\"100\" heihgt=\"30\" onclick=\"location.href='?m=$form{'m'}&a=power&id=$users_info[0]'\" alt=\"アクセス権\" /></td>\n";
	$users_list .= "<td style=\"width: 100px;\"><img src=\"images/button_registry.gif\" class=\"button\" width=\"100\" heihgt=\"30\" onclick=\"location.href='?m=$form{'m'}&a=reg&id=$users_info[0]'\" alt=\"レジストリ\" /></td>\n";
	$users_list .= "<td style=\"width: 100px;\"><img src=\"images/button_uninstall.gif\" class=\"button\" width=\"100\" heihgt=\"30\" onclick=\"uninstall_confirm('?m=$form{'m'}&a=uninstall&id=$users_info[0]','$users_info[0]');\" alt=\"アンインストール\" /></td>\n";
	$users_list .= "</tr>\n";
}
my $dir = 'modules/';
opendir DH, $dir or die "$dir:$!";
while (my $file = readdir DH) {
	next if $file =~ /^\.{1,2}$/;
	$module_path = $dir . $file;
	$module_conf_path = $dir . $file . "/set_registry.cgi";
	if(-d $module_path){
		if((-f $module_conf_path) && !($disp_flag{$file})){
			$active_path = "${dir_datas}$form{'m'}\/${file}\.cgi";
			$users_list .= "<tr onmouseover=\"this.style.backgroundColor='#E8EEF9';\" onmouseout=\"this.style.backgroundColor='#FFFFFF';\">\n";
			$users_list .= "<td>&nbsp;</td>\n";
			$users_list .= "<td>${file}</td>\n";
			$users_list .= "<td>&nbsp;</td>\n";
			$users_list .= "<td>&nbsp;</td>\n";
			$users_list .= "<td style=\"width: 100px;\"><img src=\"images/button_install.gif\" class=\"button\" width=\"70\" heihgt=\"30\" onclick=\"install_confirm('?m=$form{'m'}&a=install&id=${file}','${file}');\" alt=\"インストール\" /></td>\n";
			$users_list .= "</tr>\n";
		}
	}
}
closedir DH;
$print_html = <<"EOF";
	<form method="post" action="?m=$form{'m'}&a=sort" style="padding-top: 5px;">
		<table cellpadding="0" cellspacing="0" class="list">
			${users_list}
		</table>
		<p><input type="submit" value="順番を入れ替える" /></p>
	</form>
EOF

###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

for($cnt=0;$cnt<@users;$cnt++){
	my(@users_info) = split(/\t/,$users[$cnt]);
	$users_info[1] = $form{$users_info[0]};
	$users[$cnt] = join("\t",@users_info);
}
@users = sort { (split(/\t/,$b))[1] cmp (split(/\t/,$a))[1]} @users;
&savefile("${dir_datas}$form{'m'}\.dat",@users);
&rebuild_module_list;
$print_html = <<"EOF";
<div class="screen">
	<p>モジュールのソートが完了しました</p>
	<p><a href="?m=$form{'m'}">さらにモジュールの管理を行う</a></p>
</div>
EOF

###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'レジストリの削除完了';
@registry = grep(!/^$form{'id'}\t/,@registry);
&savefile("${dir_datas}${file_registry}",@registry);
$print_html = <<"EOF";
<div class="screen">
	<p>レジストリ「$form{'id'}」の削除が完了しました</p>
	<p><a href="?m=$form{'m'}">さらに追加/更新を行う</a></p>
</div>
EOF

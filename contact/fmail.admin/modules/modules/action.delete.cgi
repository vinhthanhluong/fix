###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

@registry = &loadfile("${dir_datas}$form{'m'}\/$form{'module'}\.dat");
$action_name = 'レジストリの削除完了';
@registry = grep(!/^$form{'id'}\t/,@registry);
&savefile("${dir_datas}$form{'m'}\/$form{'module'}\.dat",@registry);
&rebuild_module_registry($form{'module'});
&rebuild_module_list;
$print_html = <<"EOF";
<div class="screen">
	<p>$form{'module'}モジュールのレジストリ「$form{'id'}」の削除が完了しました</p>
	<p><a href="?m=$form{'m'}&a=reg&id=$form{'module'}">さらに追加/更新を行う</a></p>
</div>
EOF

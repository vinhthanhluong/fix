###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '権限の削除完了';
@current_data = grep(!/^$form{'id'}\t/,@current_data);
&savefile($current_data_path,@current_data);
&rebuild_powers;
$print_html = <<"EOF";
<div class="screen">
	<p>権限「$form{'id'}」の削除が完了しました</p>
	<p><a href="?m=$form{'m'}">さらに追加/更新を行う</a></p>
</div>
EOF

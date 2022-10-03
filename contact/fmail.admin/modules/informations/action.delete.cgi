###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'お知らせの削除完了';
@current_data = grep(!/^$form{'id'}\t/,@current_data);
&savefile($current_data_path,@current_data);
$print_html = <<"EOF";
<div class="screen">
	<p>「$form{'id'}」の削除が完了しました</p>
	<p><a href="?m=$form{'m'}">さらに追加/更新を行う</a></p>
</div>
EOF

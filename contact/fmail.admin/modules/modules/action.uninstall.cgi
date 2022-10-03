###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = 'モジュールのアンインストール完了';
@users = grep(!/^$form{'id'}\t/,@users);
unlink "${dir_datas}$form{'m'}\/$form{'id'}\.cgi";
## rmdir
$dir = "${dir_datas}modules/$form{'id'}\/";
#opendir DIR, $dir;
#@files = grep { !m/^(\.|\.\.)$/g } readdir DIR;
#close DIR;
#$flag = @files;
#foreach $file(@files) {
#	chmod 0777, "$dir$file";
#	unlink "$dir$file";
#}
#chmod 0777, $reg{'dir_datas'};
#chmod 0777, $reg{'users_dirs'};
#chmod 0777, $dir;
#if (rmdir $dir) {
#	$del_res = "delete success";
#}
#else {
#	$del_res = "rmdir Error: $!";
#}
#rmdir $dir;
&savefile("${dir_datas}$form{'m'}\.dat",@users);
&rebuild_module_list;
$print_html = <<"EOF";
<div class="screen">
	<p>モジュール「$form{'id'}」のアンインストール及びモジュールデータディレクトリ「${dir}」の削除が完了しました</p>
	<p>$del_res</p>
	<p><a href="?m=$form{'m'}">さらに追加/更新を行う</a></p>
</div>
EOF

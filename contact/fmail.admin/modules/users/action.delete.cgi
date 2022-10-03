###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '管理ユーザの削除完了';
@users = grep(!/^$form{'id'}\t/,@users);
unlink "$reg{'form_display_picture'}$form{'id'}.jpg";
unlink "$reg{'form_display_picture'}thum_$form{'id'}.jpg";
&WppSaveLine("$reg{'dir_sessions'}$form{'id'}\.disabled",$null);
## rmdir
$dir = "$reg{'users_dirs'}$form{'id'}\/";
opendir DIR, $dir;
@files = grep { !m/^(\.|\.\.)$/g } readdir DIR;
close DIR;
$flag = @files;
foreach $file(@files) {
	chmod 0777, "$dir$file";
	unlink "$dir$file";
}
chmod 0777, $reg{'dir_datas'};
chmod 0777, $reg{'users_dirs'};
chmod 0777, $dir;
if(rmdir $dir){
	$del_res = "delete success";
}
else {
	$del_res = "rmdir Error: $!";
}
rmdir $dir;
&savefile("${dir_datas}${file_users}",@users);
$print_html = <<"EOF";
<div class="screen">
	<p>管理ユーザ「$form{'id'}」の削除及びユーザディレクトリ「${dir}」の削除が完了しました</p>
	<p>$del_res</p>
	<p><a href="?m=$form{'m'}">さらに追加/更新を行う</a></p>
</div>
EOF

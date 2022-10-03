###############################################################################
# Administrated Screen Users Editable Functions
# 削除対象レコードを別格納後、削除を行う処理＞間違って削除した場合は、生ログから復旧させる手段
###############################################################################

$action_name = 'ログ一件の削除完了';

# 削除対象ファイルパス
$current_data_path = "$form{'file'}";

# 削除前の別格納処理 ------------------------------------
# メールログファイルロード
@current_data = &loadfile($current_data_path);
# 削除ログファイルパスセット
$current_deleteLog_path = './datas/maillog/deleteLog/deleteLine.cgi';
# 削除レコード選択
@current_data = grep(/\t$form{'id'}\t/,@current_data);
# 削除ログへ追加書き込み
&WppSaveAddLine($current_deleteLog_path,@current_data);


# 削除処理 ----------------------------------------------
# メールログファイルロード
@current_data = &loadfile($current_data_path);
# 削除レコード以外を選択
@current_data = grep(!/\t$form{'id'}\t/,@current_data);
# 残ったレコードでファイルを再構成
&savefile($current_data_path,@current_data);
# ファイル容量を確認して、空行を足す（データが無い場合は改行は不要）
if(-s $current_data_path) {
	# 改行コードが抜けるので継ぎ足し
	&WppSaveAddLine($current_data_path,"");
}

# 削除後にコピー
if($flag_copy_mod){
	$logdata_bu_path = $form{'file'} . '.backup';
	copy($form{'file'}, $logdata_bu_path);
}

$redirect = "?m=$form{'m'}";

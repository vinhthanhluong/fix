###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '項目の複製完了';
#@current_data = grep(!/^$form{'id'}\t/,@current_data);
for($copy_cnt=0; $copy_cnt<@current_data; $copy_cnt++){
	if($current_data[$copy_cnt] =~ /^$form{'id'}/){
		# 既存データを書き込む
		$current_data_work .= "$current_data[$copy_cnt]\n";
		
		# コピーを作る
		# IDは書き換える
		@current_data_change = split(/\t/,$current_data[$copy_cnt]);
		# IDの書き換え
		$current_data_change[0] = time;
		# ソート番号
		if($current_data_change[1] == 0){
			$current_data_change[1] = $current_data_change[1] + 1;
		}else{
			$current_data_change[1] = $current_data_change[1] - 1;
		}
		# 桁数調整
		$current_data_change[1] = sprintf("%04d", $current_data_change[1]);
		# 名前の変更
		$current_data_change[2] .= '（コピー）';
		# 差し替えた情報で再構築
		for($change_cnt=0; $change_cnt<@current_data_change; $change_cnt++){
			$current_data_change_remake .= "$current_data_change[$change_cnt]\t";
		}
		# 代入
		$current_data_work .= "$current_data_change_remake\n";
	}else{
		# 既存データを書込む
		$current_data_work .= "$current_data[$copy_cnt]\n";
	}
}
&savefile($current_data_path,$current_data_work);
$redirect = "?m=$form{'m'}";

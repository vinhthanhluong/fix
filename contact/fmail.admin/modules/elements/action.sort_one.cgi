###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################
# sort
for($cnt=0;$cnt<@current_data;$cnt++){
	@record = split(/\t/,$current_data[$cnt]);
	if($record[0] eq $form{'id'}){
		# 順位UP・DOWNの判定
		if($form{'rank'} eq 'up'){
			# 前レコードが存在するかのチェック
			if(@record_before){
				# 順位UP---------------------------------------
				# 現レコードの移し変え
				$record_before[1] = $record[1];
				# 前レコードを書き込む準備
				for($record_before_cnt=0; $record_before_cnt<@record_before; $record_before_cnt++){
					$current_data_remake_work .= "$record_before[$record_before_cnt]\t";
				}
				# 順位書き換え後のレコード書込みデータの生成
				$current_data_remake .= "$current_data_remake_work\n";
				# 準備用変数の初期化
				$current_data_remake_work = "";
				
				# 現レコード書き換え準備
				for($record_cnt=0; $record_cnt<@record;$record_cnt++){
					if($record_cnt == 1){
						# 現レコードに前レコードの順位を代入
						$record_work .= "$num_before\t";
					}else{
						$record_work .= "$record[$record_cnt]\t";
					}
				}
				
				# 順位書き換え後のレコード書込みデータの生成
				@record_before = split(/\t/,$record_work);
				# 準備用変数の初期化
				$record_work = "";
				
				# 順位データのみ別途格納
				$num_before = $record_before[1];
			}else{
				# 前レコードが存在しない（つまり1レコード目）場合、順位入れ替え処理はスルー
				$current_data_remake .= $current_data[$cnt];
				# 順位コントロールの為、現レコード値の保持
				@record_before = @record;
				# 順位データのみ別途格納
				$num_before = $record[1];
			}
		}else{
			# 順位DOWN-------------------------------------
			$flag_num_after = 1;
		}
		$record[1] = sprintf("%04d",$record[1]);
		
		# 順位を下げる場合、次レコードに現レコードを持ち越す
		if($flag_num_after){
			# 前レコードを書き込み準備
			for($record_before_cnt=0; $record_before_cnt<@record_before; $record_before_cnt++){
				$current_data_remake_work .= "$record_before[$record_before_cnt]\t";
			}
			# 前レコード書込み
			$current_data_remake .= "$current_data_remake_work\n";
			# 一時変数の初期化
			$current_data_remake_work = "";
			
			# 保留レコード
			@record_before = split(/\t/,$current_data[$cnt]);
			# ソート番号を保護（第一レコードの場合、前回データがないのであえて代入）
			$num_before = $record[1];
		}
	}elsif($flag_num_after){
		# idが合致しないが、順位を下げる対象レコードはここで書き込む
		# 前レコードのソート番号に現レコードのソート番号を挿入
		$record_before[1] = $record[1];
		# 前レコードを書き込み準備
		for($record_before_cnt=0; $record_before_cnt<@record_before; $record_before_cnt++){
			$record_before_work .= "$record_before[$record_before_cnt]\t";
		}
		# 前レコード書込み
		$current_data_remake .= "$record_before_work\n";
		# 前レコード準備用変数初期化
		$record_before_work = "";
		
		# 現レコードのソート番号に、前レコードのソート番号を反映
		$record[1] = $num_before;
		# 現レコードの書き込み
		for($cnt_record=0; $cnt_record<@record; $cnt_record++){
			$record_remake .= "$record[$cnt_record]\t";
		}
		@record_before = split(/\t/,$record_remake);
		
		# 処理完了なので、フラグを初期化
		$flag_num_after = 0;
	}else{
		# 所定ＩＤと違う場合-----------------------------
		# 前レコードが存在するかのチェック
		if(@record_before){
			# 前レコードが存在する場合は、前レコードを書き込む準備
			for($record_before_cnt=0; $record_before_cnt<@record_before; $record_before_cnt++){
				$current_data_remake_work .= "$record_before[$record_before_cnt]\t";
			}
			# レコード書込みデータの生成
			$current_data_remake .= "$current_data_remake_work\n";
			# 準備用変数の初期化
			$current_data_remake_work = "";
		}
		
		# 順位コントロールの為、現レコード値の保持
		@record_before = @record;
		# 順位データのみ別途格納
		$num_before = $record[1];
	}
}

# 最終レコード書込み準備
for($record_before_cnt=0; $record_before_cnt<@record_before; $record_before_cnt++){
	$record_before_work .= "$record_before[$record_before_cnt]\t";
}
# 最終レコード書込み
$current_data_remake .= "$record_before_work\n";

@current_data = split(/\n/,$current_data_remake);
@current_data = sort { (split(/\t/,$b))[1] cmp (split(/\t/,$a))[1]} @current_data;
&savefile($current_data_path,@current_data);

$redirect = "?m=$form{'m'}";

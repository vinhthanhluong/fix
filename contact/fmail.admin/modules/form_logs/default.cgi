###############################################################################
# Administrated Screen Start Page Functions
###############################################################################
use File::Find;

$srch_start = $form{'srch_start'};
$srch_end = $form{'srch_end'};

# 抽出開始日付　ファイル名を日付フォーマットへ
@date = split(/\-/,$srch_start);
$dt_s = sprintf("%04d%02d%02d",$date[0],$date[1],$date[2]);

# 抽出終了日付　ファイル名を日付フォーマットへ
@date = split(/\-/,$srch_end);
$dt_e = sprintf("%04d%02d%02d",$date[0],$date[1],$date[2]);

# 抽出日付が存在した場合
if($srch_start && $srch_end && $dt_s <= $dt_e){
	if ($srch_start && $srch_end) {
		# フォームログのデータから抽出
		find(\&want_func, "$current_data_path");
	}

	# $logdata				ID,ページ,項目ID
	# $idlist					入力画面		セッションIDがカンマ区切り
	# $entrylist			入力あり		セッションIDがカンマ区切り
	# $confirmlist		確認画面		セッションIDがカンマ区切り
	# $errorlist			エラー画面	セッションIDがカンマ区切り
	# $error_element	エラー項目
	# $backlist				戻る画面		セッションIDがカンマ区切り
	# $thankslist			完了画面		セッションIDがカンマ区切り
	
	# 訪問者数
	@visit = split(/,/,$idlist);
	$visitor = @visit;
	$idlist_dummy = $idlist;
	
	# 確認画面到達数
	@confirmlists = split(/,/,$confirmlist);
	$confirm_cnt = @confirmlists;
	# 確認画面到達率
	if ($visitor) {
		$confirm_rate = int($confirm_cnt / $visitor * 100);
		$confirm_rate_etc = 100 - $confirm_rate;
	}
	
	# エラー画面到達数
	@errorlists = split(/,/,$errorlist);
	$error_cnt = @errorlists;
	
	# 戻る画面到達数
	@backlists = split(/,/,$backlist);
	$back_cnt = @backlists;
	
	# 完了画面到達数
	@thankslists = split(/,/,$thankslist);
	$thanks_cnt = @thankslists;
	# 完了画面到達率
	if ($visitor) {
		$thanks_rate = int($thanks_cnt / $visitor * 100);
		$thanks_rate_etc = 100 - $thanks_rate;
	}
	
	# どの項目にも入力せずに離脱
	## 入力したユーザー
	@entrylists = split(/,/,$entrylist);
	## 入力してないユーザーの照合
	### 訪問者数ループ
	for (my $m=0; $m<@visit; $m++) {
		### 入力データループ
		for (my $n=0; $n<@entrylists; $n++) {
			### ID合致
			if ($visit[$m] eq $entrylists[$n]) {
				$idlist_dummy =~ s/$entrylists[$n]\,//g;
			}
		}
	}
	@entry_noinput = split(/,/,$idlist_dummy);
	# どの項目にも入力せずに離脱　数
	$drop_cnt = @entry_noinput;
	# どの項目にも入力せずに離脱　率
	if ($visitor) {
		$drop_rate = int($drop_cnt / $visitor * 100);
		$drop_rate_etc = 100 - $drop_rate;
	}
	
	# 入力したが、確認画面へ遷移しなかった
	## 入力したユーザーのダミー
	$entrylist_dummy = $entrylist;
	## 確認画面までいかなかったユーザーの照合
	### 訪問者数ループ
	for (my $x=0; $x<@entrylists; $x++) {
		### 確認画面ループ
		for (my $y=0; $y<@confirmlists; $y++) {
			### ID合致
			if ($entrylists[$x] eq $confirmlists[$y]) {
				$entrylist_dummy =~ s/$confirmlists[$y]\,//g;
			}
		}
	}
	@confirm_nopage = split(/,/,$entrylist_dummy);
	# 入力したが、確認画面へ遷移しなかった　数
	$confirm_drop_cnt = @confirm_nopage;
	# 入力したが、確認画面へ遷移しなかった　率
	if ($visitor) {
		$confirm_drop_rate = int($confirm_drop_cnt / $visitor * 100);
		$confirm_drop_rate_etc = 100 - $confirm_drop_rate;
	}

	# エラー項目
	@error_elements = split(/,/,$error_element);
	## エラーリスト生成
	for (my $z=0; $z<@error_elements; $z++) {
		if ($error_elementlist !~ /$error_elements[$z]/) {
			$error_elementlist .= "$error_elements[$z],";
			$error_elementlistdata .= "$error_elements[$z]=0,";
		}
	}
	## エラーカウント
	@error_elementlists = split(/,/, $error_elementlist);
	### エラー項目
	for (my $l=0; $l<@error_elements; $l++) {
		### エラーリスト
		for (my $p=0; $p<@error_elementlists; $p++) {
			if ($error_elements[$l] eq $error_elementlists[$p]) {
				@spotdata = split(/=/, $error_elementlistdata[$p]);
				$cnt = $spotdata[1] + 1;
				$error_elementlistdata[$p] = "$error_elementlists[$p]=$cnt";
			}
		}
	}
	# 項目名を当て込みつつHTML生成
	for($cnt=0;$cnt<@current_elem_data;$cnt++){
		($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class) = split(/\t/,$current_elem_data[$cnt]);
		# エラーデータループ
		for (my $p=0; $p<@error_elementlistdata; $p++) {
			@spotdata = split(/=/, $error_elementlistdata[$p]);
			if ("en$elements_id" eq $spotdata[0]) {
				$error_html .= qq|<dt><span class="title">$name</span></dt><dd><span class="value">$spotdata[1]</span> 回</dd>\n|;
			}
		}
	}
}


$action_name = 'フォームログ';

#管理者・通常ユーザー
$print_html = <<"EOF";
	<div class="search">
		<p>[ 対象期間指定 ]</p>
		<form>
			<fieldset>
				<input type="text" name="srch_start" value="$srch_start" class="formlog_search" /> ～ <input type="text" name="srch_end" value="$srch_end" class="formlog_search" />
				<input type="hidden" name="m" value="form_logs" />
				<input type="submit" value="データ検索" class="button" />
			</fieldset>
		</form>
	</div>
	
	
	<div id="phase">
		<h3>フェーズ別レポート</h3>
		
		<div class="section-step-first clearfix">
			<div class="box">
				<h4>入力画面</h4>
				<p class="title">
					<span class="value">$visitor</span> user
				</p>
			</div>
			
			<p class="arrow-r">
				<img src="modules/form_logs/images/arrow-r.jpg" />
			</p>
			<p class="detail">
				<span class="title">どの項目にも入力せずに離脱</span>
				<span class="value">$drop_rate</span>％ ($drop_cnt user)
			</p>
			<p class="detail">
				<span class="title">入力したが、確認画面へ遷移しなかった</span>
				<span class="value">$confirm_drop_rate</span>％ ($confirm_drop_cnt user)
			</p>
		</div>
		
		
		<div class="section-step-second clearfix">
			<p class="arrow2">
				<img src="modules/form_logs/images/arrow2.jpg" />
			</p>
			<p class="arrow-r">
				<img src="modules/form_logs/images/arrow-r.jpg" />
			</p>
			<div class="error">
				<span class="title">[ 必須項目入力漏れ回数 ]</span>
				<dl class="clearfix">
					$error_html
				</dl>
			</div>
		</div>
		
		<div class="section-step-second clearfix">
			<div class="box">
				<h4>確認画面</h4>
				<p class="title">
					<span class="value">$confirm_rate</span> ％ ($confirm_cnt user)
				</p>
			</div>
		</div>
		
		<div class="section-step-last clearfix">
			<p class="arrow">
				<img src="modules/form_logs/images/arrow.jpg" />
			</p>
		</div>
		
		<div class="section-step-last clearfix">
			<div class="box">
				<h4>完了画面</h4>
				<p class="title">
					<span class="value">$thanks_rate</span> ％ ($thanks_cnt user)
				</p>
			</div>
		</div>
		
	</div>
	
	<link href="modules/form_logs/print.css" rel="stylesheet" type="text/css" media="print" />
	
EOF


#----------------------------------------------------------------------------------------
#  ログデータ
#----------------------------------------------------------------------------------------
sub want_func {
	
	# 検索ファイルの内、～.cgiのみ抽出
	if($File::Find::name =~ /.cgi/){
		# 抽出開始日付　ファイル名を日付フォーマットへ
		@date = split(/\-/,$srch_start);
		$dt_s = sprintf("%04d%02d%02d",$date[0],$date[1],$date[2]);
		
		# 抽出終了日付　ファイル名を日付フォーマットへ
		@date = split(/\-/,$srch_end);
		$dt_e = sprintf("%04d%02d%02d",$date[0],$date[1],$date[2]);
		
		# 実際の呼び出しは、当ファイルからの相対パス
		@current_data = &loadfile_formlog("../.$File::Find::name");
		
		# ファイルパスを分割
		@dates = split(/\//,$File::Find::name);
		# ファイル名から拡張子削除
		$dates[-1] =~ s/\.cgi//g;
		# ファイル名を日付フォーマットへ
		@date = split(/\-/,$dates[-1]);
		$dt = sprintf("%04d%02d%02d",$date[0],$date[1],$date[2]);
		
		# ファイルの日付を比較して、対象期間のファイルのみを抽出
		if ($dt_s <= $dt && $dt_e >= $dt) {
			for (my $i=0; $i<@current_data; $i++) {
				@logdatas = split(/\t/,$current_data[$i]);
				# データを再配列（セッションID,ページ,項目）
				$logdata .= "$logdatas[1],$logdatas[2],$logdatas[3]\t";
				# セッションIDのみリスト化
				if ($logdatas[1] && $idlist !~ /$logdatas[1]/) {
					$idlist .= "$logdatas[1],";
				}
				
				# セッションIDと入力データリスト化
				if ($logdatas[1] && $entrylist !~ /$logdatas[1]/) {
					# セッションIDと未入力で離脱
					if ($logdatas[2] eq 'entry') {
						if ($logdatas[3]) {
							# 入力された事があるリスト
							$entrylist .= "$logdatas[1],";
						}
					}
				}
				
				# セッションIDと確認画面到達リスト化
				if ($logdatas[1] && $confirmlist !~ /$logdatas[1]/ && $logdatas[2] eq 'confirm') {
					$confirmlist .= "$logdatas[1],";
				}
				
				# セッションIDとエラー画面到達リスト化
				if ($logdatas[1] && $errorlist !~ /$logdatas[1]/ && $logdatas[2] eq 'error') {
					$errorlist .= "$logdatas[1],";
				}
				
				# エラー項目配列
				if ($logdatas[2] eq 'error') {
					$error_element .= "$logdatas[3],";
				}
				
				# セッションIDと戻る画面到達リスト化
				if ($logdatas[1] && $backlist !~ /$logdatas[1]/ && $logdatas[2] eq 'back') {
					$backlist .= "$logdatas[1],";
				}
				
				# セッションIDと完了画面到達リスト化
				if ($logdatas[1] && $thankslist !~ /$logdatas[1]/ && $logdatas[2] eq 'thanks') {
					$thankslist .= "$logdatas[1],";
				}
			}
		}
	}

}

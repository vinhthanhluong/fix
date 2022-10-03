###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$current_data = join("\n",@current_data);
($flag,$expires_start,$expires_end,$limit,$serials,$thanks_page,$sendmail_path,$logsave,$cart_in_element,$cart_logsave,$form_logsave,$form_logsave_period,$send_mode,$attached_mode,$display_mode,$logdata_path,$cart_logdata_path,$mailform_sender_address_name,$mailform_sender_address,$mail_method,$thanks_message,$title_mailform,$title_confirm,$title_error,$title_thanks,$mail_dustclear,$mail_dustclear_zero,$client_info,$site_url,$table_style,$th_style,$td_style,$separate_before,$separate_after,$flag_afiri,$afiri1_tag,$afiri2_tag,$afiri3_tag,$afiri4_tag,$afiri5_tag,$flag_smartphone_tpl,$flag_futurephone_tpl,$setlang,$spamcheck,$domaincheck,$encheck,$txtchange) = split(/\n/,$current_data);

## path
eval{ $server_root_path = `pwd`; };
if ($@ || !$server_root_path) { $server_root_path = 'unknown'; }
if($server_root_path eq 'unknown'){
	if ($0 =~ /^(.*[\\\/])/) { $server_root_path = $1; }
	else { $server_root_path = 'unknown'; }
}
if($server_root_path eq 'unknown'){
	$server_root_path = $ENV{'SCRIPT_FILENAME'};
	@path = split(/\//,$server_root_path);
	pop @path;
	$server_root_path = join("\/",@path);
}
$server_root_path =~ s/\n//g;

if($flag){
	$flag_checked = ' checked';
}
if($serials){
	$serial_checked = ' checked';
}
if($logsave){
	$logsave_checked = ' checked';
}
if($cart_logsave){
	$cart_logsave_checked = ' checked';
}
if($form_logsave){
	$form_logsave_checked = ' checked';
}
if($send_mode){
	$send_flag_checked = ' checked';
}
if($attached_mode){
	$attached_mode_checked = ' checked';
}
if($display_mode eq "table"){
	$table_checked = ' checked';
}
else {
	$dl_checked = ' checked';
}

if($mail_method eq "text"){
	$text_checked = " checked";
}
else {
	$html_checked = " checked";
}
if($mail_dustclear){
	$mail_dustclear_checked = " checked";
}
if($mail_dustclear_zero){
	$mail_dustclear_zero_checked = " checked";
}
$thanks_message =~ s/<br \/>/\n/g;
$client_info =~ s/<br \/>/\n/g;
if(!($attached_method)){
	$attached_method_hidden = " style=\"display: none\"";
}

${table_style} =~ s/"/&quot;/g;
${th_style} =~ s/"/&quot;/g;
${td_style} =~ s/"/&quot;/g;

# アフィリエイト
if($flag_afiri){
	$flag_afiri_checked = " checked";
}
${afiri1_tag} =~ s/"/&quot;/g;
${afiri2_tag} =~ s/"/&quot;/g;
${afiri3_tag} =~ s/"/&quot;/g;
${afiri4_tag} =~ s/"/&quot;/g;
${afiri5_tag} =~ s/"/&quot;/g;


if($flag_smartphone_tpl){
	$flag_smartphone_tpl_checked = " checked";
}

if($flag_futurephone_tpl){
	$flag_futurephone_tpl_checked = " checked";
}

if($setlang eq 'utf8'){
	$setlang_utf8_checked = " checked";
}else{
	$setlang_ja_checked = " checked";
}

if($spamcheck){
	$spamcheck_checked = " checked";
}
if($domaincheck){
	$domaincheck_checked = " checked";
}
if($encheck){
	$encheck_checked = " checked";
}
if($txtchange){
	$txtchange_checked = " checked";
}

## 条件定義用の項目読み込み
@elements = &loadfile('./datas/modules/elements/elements.dat');
#送信元名用
$flag_soushinmoto = 0;
for($cnt=0;$cnt<@elements;$cnt++){
	($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class) = split(/\t/,$elements[$cnt]);
	if($element_type ne "spacer"){
		#既に登録されている値から、selectedを指定
		$checkflag_mailform_sender_address_name = ${mailform_sender_address_name};
		$checkflag_mailform_sender_address_name =~ s/&lt;//g;
		$checkflag_mailform_sender_address_name =~ s/&gt;//g;
		if($checkflag_mailform_sender_address_name eq ${elements_id}){
			$add_elements_value_list_name .= "<option value=\"<${elements_id}>\" selected=\"selected\">${name}</option>";
			#エンドユーザ情報が反映されていたので、フラグに1を立てる
			$flag_soushinmoto = 1;
		}else{
			$add_elements_value_list_name .= "<option value=\"<${elements_id}>\">${name}</option>";
		}
	}
	# 商品カート
	if(${elements_id} == ${cart_in_element} ) {
		$cart_in_element_selected = "<option value=\"${cart_in_element}\" selected=\"selected\">${name}</option>";
		$flag_cart_in_element_selected = 1;
	} elsif(!$cart_in_element) {
		$cart_in_element_selected = "<option value=\"\" selected=\"selected\">引継なし</option>";
	}
	
	if($flag_cart_in_element_selected || ($cart_in_element && !$flag_cart_in_element_selected) ){
		$cart_in_element_select_none = "<option value=\"\">引継なし</option>";
	}
	
	if($element_type eq "textarea"){
		$cart_in_element_select .= "<option value=\"${elements_id}\">${name}</option>";
	}
}
if(!$flag_soushinmoto){	$add_elements_value_list_name = "<option value=\"メールフォーム管理システム\" class=\"caution\">ユーザ情報未選択 or 手動設定</option>" . $add_elements_value_list_name;}

#送信元メールアドレス用
$flag_soushinmoto = 0;
for($cnt=0;$cnt<@elements;$cnt++){
	($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_blur,$on_focus,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note) = split(/\t/,$elements[$cnt]);
	if($element_type ne "spacer"){
		#既に登録されている値から、selectedを指定
		$checkflag_mailform_sender_address = ${mailform_sender_address};
		$checkflag_mailform_sender_address =~ s/&lt;//g;
		$checkflag_mailform_sender_address =~ s/&gt;//g;
		if($checkflag_mailform_sender_address eq ${elements_id}){
			$add_elements_value_list_mail .= "<option value=\"<${elements_id}>\" selected=\"selected\">${name}</option>";
			#エンドユーザ情報が反映されていたので、フラグに1を立てる
			$flag_soushinmoto = 1;
		}else{
			$add_elements_value_list_mail .= "<option value=\"<${elements_id}>\">${name}</option>";
		}
	}
}
if(!$flag_soushinmoto){	$add_elements_value_list_mail = "<option value=\"\" class=\"caution\">ユーザ情報未選択 or 手動設定 </option>" . $add_elements_value_list_mail;}


##初期値判定
#URL（トップページ）
if(${site_url} eq 'http://www.xx.xx/'){
	$site_url_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />初期値のままです。';
	$site_url_error_bg = 'class="error_bg"';
}elsif(!${site_url}){
	$site_url_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />入力されていません。';
	$site_url_error_bg = 'class="error_bg"';
}

#クライアント情報
$client_info_work = ${client_info};
$client_info_work =~ s/\n/<>/g;
if($client_info_work eq '株式会社○○<>〒xxx-xxxx　○○都○○区○○<>TEL：xx-xxxx-xxxx<>FAX：xx-xxxx-xxxx<>E-mail：xx@xx.xx'){
	$client_info_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />初期値のままです。';
	$client_info_error_bg = 'class="error_bg"';
}elsif(!${client_info}){
	$client_info_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />入力されていません。';
	$client_info_error_bg = 'class="error_bg"';
}

# ホスト名
$host = $ENV{'HTTP_HOST'};

## 通し番号
$serial_num = &mfp_LoadLine('./datas/serial.dat');
$action_name = 'メールフォームの設定画面';
$print_html = <<"EOF";
<p>メールフォームに関する設定を行います。</p>
<div id="stat">
	メールフォームに関する設定の保存が完了しました
</div>
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" onSubmit="return checkUserEdit(this,'${submit}');">
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr style="display: none;">
			<th>有効/無効</th>
			<td><input type="checkbox" name="flag" value="1"${flag_checked} /> メールフォームを有効にする</td>
		</tr>
		<tr style="display: none;">
			<th>期限設定</th>
			<td><input type="text" name="expires_start" id="expires_start" value="${expires_start}" /> ～ <input type="text" name="expires_end" id="expires_end" value="${expires_end}" /><span>例）2009-04-01</span></td>
		</tr>
		<tr style="display: none;">
			<th>送信数制限</th>
			<td><input type="text" name="limit" id="limit" value="${limit}" size="5" /> 回</td>
		</tr>
		<tr>
			<th>通し番号</th>
			<td><input type="checkbox" name="serials" value="1"${serial_checked} /> 件名に通し番号を付ける ／ 現在の通し番号 <input type="text" name="serial_num" value="${serial_num}" class="settingnum" style="text-align: right;ime-mode: disabled;" /></td>
		</tr>
		<tr>
			<th $site_url_error_bg>URL（トップページ）</th>
			<td $site_url_error_bg>
				<span class="error_block">$site_url_error_msg</span>
				<input type="text" name="site_url" value="${site_url}" class="data" />
				<span>※送信完了ページの「トップページへ」のリンクと<span class="caution">自動返信メールの&lt;site_url&gt;に反映します。</span>
			</td>
		</tr>
		<tr>
			<th>ユーザーから届く<br />メールの差出人設定</th>
			<td>
				<table class="table_style_none">
					<tr>
						<td>差出人表示名</td>
						<td>
							<select name="add_elements_value_list" id="add_elements_value_list">
								${add_elements_value_list_name}
							</select>
							<input type="button" value="反映" onclick="add_element_value()" />
						</td>
						<td>
							　　設定値：
							<input type="text" name="mailform_sender_address_name" value="${mailform_sender_address_name}" id="mailform_sender_address_name" class="settingdata" />
							（手動設定可能）
							</td>
					</tr>
					<tr>
						<td>差出人アドレス</td>
						<td>
							<select name="add_elements_value_list_subject" id="add_elements_value_list_subject">
								${add_elements_value_list_mail}
							</select>
							<input type="button" value="反映" onclick="add_element_value_subject()" />
						</td>
						<td>
							　　設定値：
							<input type="text" name="mailform_sender_address" value="${mailform_sender_address}" id="mailform_sender_address" class="settingdata" onblur="email_check(this.id)" />
							（手動設定可能）
						</td>
					</tr>
				</table>
				<span class="caution">差出人表示名に何も指定しない場合は、送信されたメールには送信元アドレスが表示されます。</span>
				<span>手動設定のメリット：　個人情報がメールで飛び交うのを防ぐ事もできます。</span>
				<span>　　設定例）　差出人表示名＝メールフォーム管理システム　　差出人アドレス＝xxx\@xxx.com（任意）</span>
				<span>例の通りにする事で差出人が固定され、Fmailシステムからのお知らせメール送信も可能です。</span>
			</td>
		</tr>
		<tr>
			<th $client_info_error_bg>クライアント情報</th>
			<td $client_info_error_bg>
				<span class="error_block">$client_info_error_msg</span>
				<textarea name="client_info" class="client_info">${client_info}</textarea><br />
				<span class="caution">「自動返信メールの設定」本文内&lt;client_info&gt;箇所に反映します。</span>
			</td>
		</tr>
		<tr>
			<th>サンクスメッセージ</th>
			<td>
				<textarea name="thanks_message" class="thanks_message">${thanks_message}</textarea><br />
				<span class="caution">※index.cgi?mode=thanksのサンクスページにのみ表示されます</span>
			</td>
		</tr>
		<tr>
			<th>メール履歴保存</th>
			<td><input type="checkbox" name="logsave" value="1"${logsave_checked} id="log_save" onclick="filesave_disp();" /> サーバに履歴を保存する。</td>
		</tr>
		<tr>
			<th>商品カート設定</th>
			<td>
				<input type="checkbox" name="cart_logsave" value="1"${cart_logsave_checked} id="cart_log_save" /> サーバに商品カートの履歴を保存する。<br />
				引継項目：
				<select name="cart_in_element" id="cart_in_element">
					${cart_in_element_selected}
					${cart_in_element_select_none}
					${cart_in_element_select}
				</select>
				対象：textarea （標準：引継なし）
			</td>
		</tr>
		<tr>
			<th>フォームログ取得</th>
			<td>
				<input type="checkbox" name="form_logsave" value="1"${form_logsave_checked} /> フォームログを取得　
				<input type="text" name="form_logsave_period" value="${form_logsave_period}" class="settingnum" /> 日間保存（空欄時、永遠に保存。推奨90日間）
			</td>
		</tr>
		<tr${attached_method_hidden}>
			<th>添付ファイル</th>
			<td>
				<input type="checkbox" name="attached_mode" value="1"${attached_mode_checked} id="file_save_input" onclick="filesave_disp();" /> サーバに蓄積する(メール送付しない為、大容量添付が可能)。<br />
				<span class="caution">※サーバに蓄積する場合、「履歴保存」の項目にチェックが入っていないと、データの参照が出来なくなる為、注意。</span>
				<span>※レジストリ管理の添付ファイルディレクトリ容量上限も設定しておく。</span>
			</td>
		</tr>
		<tr>
			<th>未入力項目</th>
			<td>
				<input type="checkbox" name="mail_dustclear" value="1"${mail_dustclear_checked} /> 未入力項目を確認画面以降に反映しない。<br />
				<input type="checkbox" name="mail_dustclear_zero" value="1"${mail_dustclear_zero_checked} /> 「0」または、「0個」を確認画面以降に反映しない。
				 
			</td>
		</tr>
		<tr>
			<th>\表\示モード</th>
			<td>
				<input type="radio" name="display_mode" value="table"${table_checked} /> TABLEタグ
				<input type="radio" name="display_mode" value="dl"${dl_checked} /> DLタグ
			</td>
		</tr>
		<tr>
			<th>メールモード</th>
			<td>
				<input type="radio" name="mail_method" value="text"${text_checked} /> テキストメール(推奨)
				<input type="radio" name="mail_method" value="html"${html_checked} /> HTMLメール<br />
				<span class="caution">※HTMLメールの場合、携帯電話では認識出来ない機種があります。</span>
			</td>
		</tr>
		<tr>
			<th>テキストメール</th>
			<td>
				<input type="text" name="separate_before" value="${separate_before}" size="2" />項目
				<input type="text" name="separate_after" value="${separate_after}" size="2" />値
				<span class="caution">※スペ－スも含まれます。</span>
			</td>
		</tr>
		<tr>
			<th>HTMLメール</th>
			<td>
				HTMLメールの場合、THに項目、TDに値がセットされます。
				<table class="table_style_none input_width">
					<tr><td class="item">&lt;table </td><td><input type="text" name="table_style" value="${table_style}" class="text_long" />&gt;</td></tr>
					<tr><td class="item">&lt;th </td><td><input type="text" name="th_style" value="${th_style}" class="text_long" />&gt; 項目名 &lt;/th&gt;</td></tr>
					<tr><td class="item">&lt;td </td><td><input type="text" name="td_style" value="${td_style}" class="text_long" />&gt; 値 &lt;/td&gt;</td></tr>
				</table>
				<span>※スタイルシートでもHTMLの属性でも可</sapn>
			</td>
		</tr>
		<tr>
			<th>タイトル</th>
			<td>
				<span>入力画面</span>
				<input type="text" name="title_mailform" id="title_mailform" value="${title_mailform}" class="data" />
				<span>確認画面</span>
				<input type="text" name="title_confirm" id="title_confirm" value="${title_confirm}" class="data" />
				<span>エラー画面</span>
				<input type="text" name="title_error" id="title_error" value="${title_error}" class="data" />
				<span>完了画面</span>
				<input type="text" name="title_thanks" id="title_thanks" value="${title_thanks}" class="data" />
			</td>
		</tr>
	</table>
	
	<p class="highlevel">高度な設定 &gt;&gt;&gt;</p>
	<p class="highleveldata">他デバイス設定</p>
	<table cellpadding="0" cellspacing="0" class="sheet highleveldata">
		<tr>
			<th>スマートフォン用<br />テンプレート</th>
			<td>
				<input type="checkbox" name="flag_smartphone_tpl" id="flag_smartphone_tpl" value="1"$flag_smartphone_tpl_checked /> 利用する。（標準でレスポンシブ対応しています。ソースを分けたい時にチェックをいれてください）<br />
				<span class="caution">（チェック時のみ「fmail_smartphone.tpl」がスマートフォンでの閲覧時に反映します。）</span><br />
				<span class="caution">（チェック時のみ「項目の設定」で「タイプ」を「1行テキストエリア」選択時に「email・tel・number・url」いずれかを設定している場合のみ、スマートフォンでの閲覧時に反映します。）</span>
			</td>
		</tr>
<!--
		<tr>
			<th>フィーチャーフォン用<br />テンプレート</th>
			<td>
				<input type="checkbox" name="flag_futurephone_tpl" id="flag_futurephone_tpl" value="1"$flag_futurephone_tpl_checked /> 利用する。
				<span class="caution">（チェック時のみ「fmail_mobile.tpl」がフューチャーフォンでの閲覧時に反映します。）</span>
			</td>
		</tr>
-->
	</table>
	
	<p class="highleveldata">完了ページ設定</p>
	<table cellpadding="0" cellspacing="0" class="sheet highleveldata">
		<tr>
			<th>サンクスページ指定</th>
			<td>
				<input type="text" name="thanks_page" id="thanks_page" value="${thanks_page}" size="40" /><br />
				URLの指定が無い場合は標準サンクスページ(index.cgi?mode=thanks)が表示されます。<br />
				<span class="caution">
					指定する場合は、相対パスか絶対パスかで記載。相対パスの場合、fmailフォルダ直下が現在位置となる。<br />
					<strong>例：./thank.html　（この場合は、./fmail/thank.htmlにファイルを置く。）</strong>
				</span>
			</td>
		</tr>
		<tr>
			<th>アフィリエイト</th>
			<td>
				<input type="checkbox" name="flag_afiri" id="flag_afiri" value="1"$flag_afiri_checked /> 利用する。（チェック時のみ次項のタグが完了画面に反映。<span class="caution">※ただし、thank.html指定している場合は反映しません。</span>）
			</td>
		</tr>
		<tr>
			<th>完了画面出力用<br />アフィリエイトタグ</th>
			<td>
				<span class="caution">ユニークにする部分は、　&lt;afiri_uniq_id&gt;　を挿入してください。</span><br />
				<span class="caution">項目値の反映、　&lt;ID名&gt;　を挿入。</span><br />
				<span class="caution">項目値のURLエンコード反映、　&lt;urlenc_ID名&gt;　を挿入。</span><br />
				<span class="caution">サンプル　&lt;img src="http://www.xx.xx/xx/xx?cid=xxxxx&uid=&lt;afiri_uniq_id&gt;&uname="&lt;urlenc_en1240790859&gt;"&pid=x" height="1" width="1"&gt;</span>
				<dl class="afiri_reg">
					<dt class="afiri_reg_puturn">パターン1</dt>
					<dd class="afiri_reg_tag">
						<span>タグ</span>
						<input type="text" name="afiri1_tag" id="afiri1_tag" value="${afiri1_tag}" class="text_long" />
					</dd>
				</dl>
				<dl class="afiri_reg">
					<dt class="afiri_reg_puturn">パターン2</dt>
					<dd class="afiri_reg_tag">
						<span>タグ</span>
						<input type="text" name="afiri2_tag" id="afiri2_tag" value="${afiri2_tag}" class="text_long" />
					</dd>
				</dl>
				<dl class="afiri_reg">
					<dt class="afiri_reg_puturn">パターン3</dt>
					<dd class="afiri_reg_tag">
						<span>タグ</span>
						<input type="text" name="afiri3_tag" id="afiri3_tag" value="${afiri3_tag}" class="text_long" />
					</dd>
				</dl>
				<dl class="afiri_reg">
					<dt class="afiri_reg_puturn">パターン4</dt>
					<dd class="afiri_reg_tag">
						<span>タグ</span>
						<input type="text" name="afiri4_tag" id="afiri4_tag" value="${afiri4_tag}" class="text_long" />
					</dd>
				</dl>
				<dl class="afiri_reg">
					<dt class="afiri_reg_puturn">パターン5</dt>
					<dd class="afiri_reg_tag">
						<span>タグ</span>
						<input type="text" name="afiri5_tag" id="afiri5_tag" value="${afiri5_tag}" class="text_long" />
					</dd>
				</dl>
				<span class="caution">管理者宛メールには、　&lt;afiri_uniq_id&gt;　で反映させます。</span><br />
			</td>
		</tr>
	</table>
	
	<p class="highleveldata">送信設定</p>
	<table cellpadding="0" cellspacing="0" class="sheet highleveldata">
		<tr>
			<th>メールの送信</th>
			<td><input type="checkbox" name="send_mode" value="1"${send_flag_checked} /> フォームからの内容をメールで送信する(チェックを外すとサーバでのみの閲覧になります)</td>
		</tr>
		<tr>
			<th>対応言語モード</th>
			<td>
				<input type="radio" name="setlang" id="setlang" value="utf8"$setlang_utf8_checked /> 標準UTF8モード（推奨）　
				<input type="radio" name="setlang" id="setlang" value="ja"$setlang_ja_checked /> フィーチャーフォンモード<br />
				<p>
					<span class="info">旧字体は件名や差出人では利用できない為、可能な限り新字体に置換しています。</span>
					<span class="info">フィーチャーフォンモードでは、JISコードでメール配信します。（機種依存文字・旧字体は読めません）</span>
				</p>
			</td>
		</tr>
	</table>
	
	<p class="highleveldata">パス設定</p>
	<table cellpadding="0" cellspacing="0" class="sheet highleveldata">
		<tr>
			<th>sendmailパス</th>
			<td><input type="text" name="sendmail_path" id="sendmail_path" value="${sendmail_path}" size="30" /></td>
		</tr>
		<tr>
			<th>メールログ保存先</th>
			<td>
				<input type="text" name="logdata_path" id="logdata_path" value="${logdata_path}" size="40" /><br />
				※指定が無い場合はシステム標準の保存先が適用されます。<br />
				<span class="caution">※指定する場合はサーバルートからの絶対パスで記述してください。</span><br />
				この階層のパス：${server_root_path}
			</td>
		</tr>
		<tr>
			<th>商品カートログ保存先</th>
			<td>
				<input type="text" name="cart_logdata_path" id="cart_logdata_path" value="${cart_logdata_path}" size="40" /><br />
				※指定が無い場合はシステム標準の保存先が適用されます。<br />
				<span class="caution">※指定する場合はサーバルートからの絶対パスで記述してください。</span><br />
				この階層のパス：${server_root_path}
			</td>
		</tr>
	</table>
	
	<p class="highleveldata">セキュリティ設定</p>
	<table cellpadding="0" cellspacing="0" class="sheet highleveldata">
		<tr>
			<th>セキュリティモード</th>
			<td>
				<dl>
					<dt><input type="checkbox" name="spamcheck" value="1"${spamcheck_checked} /> スパムチェック</dt>
					<dd><span>エラー条件：</span><strong>\[/link\]</strong>や<strong>\[/url\]</strong>が含まれる場合</dd>
					
					<dt><input type="checkbox" name="domaincheck" id="domaincheck" value="1"${domaincheck_checked} /> ドメインチェック</dt>
					<dd><span>エラー条件：</span>確認画面前ページが別ホストの場合 ＞ 現在のホスト ${host}</dd>
					
					<dt><input type="checkbox" name="encheck" id="encheck" value="1"${encheck_checked} /> 全文英数字チェック</dt>
					<dd><span>エラー条件：</span>全送信データが英数字のみで構成されている場合</dd>
					
					<dt><input type="checkbox" name="txtchange" id="txtchange" value="1"${txtchange_checked} /> 入力文字変換処理</dt>
					<dd><span>チェック時：</span>カナを半角→全角、英字を全角→半角、その他機種依存文字の変換を行う</dd>
				</dl>
			</td>
		</tr>
	</table>
	
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<td>&nbsp;</td>
			<td><input type="submit" name="submit" value="保存" /> <input type="button" name="submit" value="キャンセル" onclick="location.href='?m=$form{'m'}'" /></td>
		</tr>
	</table>
</form>
EOF

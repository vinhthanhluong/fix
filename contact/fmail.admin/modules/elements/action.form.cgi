###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

@elements_data = @current_data;
if($form{'id'} ne $null){
	$action_name = '項目の編集';
	@current_data = grep(/^$form{'id'}\t/,@current_data);
	@users_info = split(/\t/,$current_data[0]);
	@hash_names = @db_fields_elements;
	*gethash = &setHash(@users_info);
	$submit = '更新';
	$readonly = " readonly";
}
else {
	$action_name = '項目の追加';
	$submit = '追加';
	$gethash{'elements_id'} = time;
}

for($cnt=0;$cnt<@elements_data;$cnt++){
	@elements_record = split(/\t/,$elements_data[$cnt]);
	$elements_id_list .= "<option value=\"en${elements_record[0]}\">${elements_record[2]}</option>";
	if($elements_record[0] ne $gethash{'elements_id'} && $elements_record[8] ne "join" && $elements_record[8] ne "spacer"){
		$add_elements_value_list .= "<option value=\"${elements_record[0]}\">${elements_record[2]}</option>";
	}
}

@element_types = ('text','textarea','select','radio','checkbox','file','join','spacer','hidden');
@element_types_name = ('1行テキストエリア','複数行テキストエリア','セレクトボックス','ラジオボタン','チェックボックス','ファイル選択','項目連結','スペーサー','隠しデータ');
for($cnt=0;$cnt<@element_types;$cnt++){
	if(($element_types[$cnt] eq "file" && ($attached_method)) || $element_types[$cnt] ne "file"){
		if($element_types[$cnt] eq $gethash{'element_type'}){$selected = " selected";}
		else {$selected = "";}
		$element_type .= "<option value=\"${element_types[$cnt]}\"${selected}>${element_types_name[$cnt]}</option>";
	}
}

@smartphone_element_types = ('text','email','tel','number','url');
@smartphone_element_types_name = ('指定無し','email','tel','number','url');
for($cnt=0;$cnt<@smartphone_element_types;$cnt++){
	if($smartphone_element_types[$cnt] eq $gethash{'smartphone_element_type'}){$selected = " selected";}
	else {$selected = "";}
	$smartphone_element_type .= "<option value=\"${smartphone_element_types[$cnt]}\"${selected}>${smartphone_element_types_name[$cnt]}</option>";
}


@check_types = ('none','digit','demilit','alphabet','digitandalphabet','mail','telephone','fax','mobilephone','postcode','url','addr');
@check_types_name = ('なし','半角数字','半角数字（3桁区切り）','半角英字','半角英数字','メールアドレス','電話番号(国内)','FAX番号(国内)','携帯電話番号','郵便番号','URL','住所');
for($cnt=0;$cnt<@check_types;$cnt++){
	if($check_types[$cnt] eq $gethash{'check_type'}){$selected = " selected";}
	else {$selected = "";}
	$check_type .= "<option value=\"${check_types[$cnt]}\"${selected}>${check_types_name[$cnt]}</option>";
}

if($gethash{'element_valus'} =~ /^\n/){
	$gethash{'element_valus'} = "\n" . $gethash{'element_valus'};
}

if($gethash{'must_disp'}){
	$must_selected = ' checked';
}
if($gethash{'system_disp_false'}){
	$system_disp_false = ' checked';
}
if($gethash{'confirm_hidden'}){
	$confirm_hidden_true = ' checked';
}
if($gethash{'return_hidden'}){
	$return_hidden_true = ' checked';
}
if($gethash{'or_disp'}){
	$or_selected = ' checked';
}
if($gethash{'log_hidden'}){
	$log_hidden_true = ' checked';
}

## 初期設定チェック ############
#対応ファイル
if(!$gethash{'enable_filetypes'}){
	$enable_filetypes_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />入力されていません。';
	$enable_filetypes_error_bg = 'class="error_bg"';
}


$print_html = <<"EOF";
<p>メールフォームの項目を${submit}します。</p>
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" onSubmit="return checkUserEdit(this,'${submit}');">
	<input type="hidden" name="id" value="$form{'id'}" />
	<input type="hidden" name="elements_id" value="$gethash{'elements_id'}" />
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<th>順番</th>
			<td><input type="text" name="num" id="num" value="$gethash{'num'}" size="5" /></td>
		</tr>
		<tr>
			<th>項目名</th>
			<td>
				<input type="text" name="name" id="name" value="$gethash{'name'}" size="30" onchange="charexp(this);" />
				<span>&lt;-br-&gt;　を記載すると項目名の途中で改行可能</span>
			</td>
		</tr>
		<tr>
			<th>タイプ</th>
			<td>
				<select name="element_type" id="element_type" onchange="change_element_type()">
					${element_type}
				</select>　
				<span id="smartphone_check">
					スマホアクセス時のtype属性
					<select name="smartphone_element_type" id="smartphone_element_type">
						${smartphone_element_type}
					</select>
				</span>
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="req_icon">
		<tr>
			<th>必須アイコン</th>
			<td><input type="checkbox" name="must_disp" id="must_disp" value="1" ${must_selected} /> 必須アイコンを表示する</td>
		</tr>
		<tr>
			<th>ORアイコン</th>
			<td><input type="checkbox" name="or_disp" id="or_disp" value="1" ${or_selected} /> ORアイコンを表示する　※「必須アイコン」が指定されている場合、そちらを優先します。</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="joielement">
		<tr>
			<th>連結指定</th>
			<td>
				<textarea name="type_of_element" id="type_of_element">$gethash{'type_of_element'}</textarea><br />
				連結する項目
				<select name="add_elements_value_list" id="add_elements_value_list">
					${add_elements_value_list}
				</select>
				<input type="button" value="挿入" onclick="add_element_value()" />
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="standard_sys_disp">
		<tr>
			<th>表示</th>
			<td>
				<input type="checkbox" name="system_disp_false" id="system_disp_false" value="1"${system_disp_false} onclick="systemDispTag()" /> システムから表示しない
				<span><input type="text" id="system_disp_false_html" onfocus="this.select();" readonly /></span>
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="standard_conf_disp">
		<tr>
			<th>確認画面非表示</th>
			<td>
				<input type="checkbox" name="confirm_hidden" id="confirm_hidden" value="1"${confirm_hidden_true} /> 確認画面で表示しない
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="standard_mail_disp">
		<tr>
			<th>本文非表示</th>
			<td>
				<input type="checkbox" name="return_hidden" id="return_hidden" value="1"${return_hidden_true} /> メール本文で表示しない
				<span>管理者宛てメール・自動返信メールを対象に「&lt;resbody&gt;」の一括表示で除外されます。※個別に挿入すれば、表示されます。</span>
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="standard_mail_disp">
		<tr>
			<th>CSVログ非表示</th>
			<td>
				<input type="checkbox" name="log_hidden" id="log_hidden" value="1"${log_hidden_true} /> メール履歴管理でこの項目をCSV保存しない
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="standard_err">
		<tr>
			<th>エラー表示</th>
			<td><input type="text" name="element_error_message" id="element_error_message" value="$gethash{'element_error_message'}" size="50" /></td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="standard">
		<tr>
			<th>イベント属性</th>
			<td>
				<input type="text" name="on_event" id="on_event" value="$gethash{'on_event'}" size="60" />
				<span id="button_element_list_field" onclick="display_elements_list()">エレメントリストと実装済イベントを表示する</span>
				<div id="elements_id_list_select_field">
					<select id="elements_id_list_select" onchange="get_elements_id_list_select(this.value)">
						<option></option>
						${elements_id_list}
					</select>
					<input type="text" id="elements_id_list_select_value" onfocus="this.select();" /> ※この部分は項目の設定に干渉しません <br />
					<select id="jslibt" onchange="jslibChange(this.value)">
					</select>
				</div>
			</td>
		</tr>
		<tr>
			<th>HTMLタグ</th>
			<td>
				<strong style="display: block">HTMLタグ（前）</strong>
				<textarea name="html_tag_free_top" id="html_tag_free_top" cols="60" rows="3">$gethash{'html_tag_free_top'}</textarea>
				<strong style="display: block">HTMLタグ（後）</strong>
				<textarea name="html_tag_free" id="html_tag_free" cols="60" rows="3">$gethash{'html_tag_free'}</textarea>
				<span>エレメントと同一のtdまたはddタグ内にHTMLタグを記述できます。</span>
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="id_disp">
		<tr>
			<th>ID属性</th>
			<td><input type="text" name="id_example" id="id_example" value="en$gethash{'elements_id'}" size="20" readonly onfocus="this.select()" /><span>※radio又はcheckboxの場合、en$gethash{'elements_id'}_xxとなります。</span></td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="addclass_disp">
		<tr>
			<th>追加のClass属性</th>
			<td>
				<input type="text" name="elements_class" id="elements_class" value="$gethash{'elements_class'}" size="20" />
				<span>※&lt;tr id="r_en$gethash{'elements_id'}" class="ここにセット"&gt; または &lt;dl class="mailform ここにセット" id="r_en$gethash{'elements_id'}"&gt;</span>
				<span>※&lt;input ○○ class="fmail"&gt; 標準で fmail がセット。
				<span>※&lt;input ○○ class="fmail must"&gt; 必須アイコンセット時 mustが追加。</span>
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="size_class">
		<tr>
			<th>サイズ属性用CLASS</th>
			<td>
				<select name="html_size" id="html_size">
					<option value="$gethash{'html_size'}">$gethash{'html_size'}</option>
					<option value="size_1">size_1</option>
					<option value="size_2">size_2</option>
					<option value="size_3">size_3</option>
					<option value="size_4">size_4</option>
					<option value="size_5">size_5</option>
					<option value="size_6">size_6</option>
					<option value="size_7">size_7</option>
					<option value="size_8">size_8</option>
					<option value="size_9">size_9</option>
					<option value="size_10">size_10</option>
				</select>
			</td>
		</tr>
		<tr>
			<th>注釈</th>
			<td><textarea name="note" id="note" cols="60" rows="3">$gethash{'note'}</textarea></td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="value_check_type">
		<tr>
			<th>チェックタイプ</th>
			<td>
				<select name="check_type" id="check_type">
					${check_type}
				</select>
				<span>※住所の場合、英数字を半角化する正規表現機能がOFFになります。</span>
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="text_format">
		<tr>
			<th>入力例</th>
			<td><input type="text" name="html_example" id="html_example" value="$gethash{'html_example'}" size="40" /></td>
		</tr>
		<tr>
			<th>文字数制限</th>
			<td><input type="text" name="text_min" id="text_min" value="$gethash{'text_min'}" size="10" /> 文字 &lt; <input type="text" name="text_max" id="text_max" value="$gethash{'text_max'}" size="10" /> 文字 <input type="button" value="文字数制限なし" onclick="textnolimit()" /></td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="text_only">
		<tr>
			<th>マッチングタグ</th>
			<td><input type="text" value="&lt;input type=&quot;text&quot; name=&quot;en$gethash{'elements_id'}_match&quot; value=&quot;[[en$gethash{'elements_id'}_match]]&quot; class=&quot;fmail&quot; /&gt;" size="60" onfocus="this.select()" readonly /></td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="val_only">
		<tr>
			<th>初期値</th>
			<td><input type="text" name="default_value" id="default_value" value="$gethash{'default_value'}" size="40" /></td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="textarea_only">
		<tr class="html_rows">
			<th>高さ属性</th>
			<td><input type="text" name="html_rows" id="html_rows" value="$gethash{'html_rows'}" size="4" /></td>
		</tr>
		<tr class="html_cols">
			<th>横幅属性</th>
			<td><input type="text" name="html_cols" id="html_cols" value="$gethash{'html_cols'}" size="4" /></td>
		</tr>
		<tr>
			<th>初期値</th>
			<td><textarea name="default_value_textarea" id="default_value_textarea" cols="60" rows="3">$gethash{'default_value'}</textarea></td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="selectvals_format">
		<tr>
			<th>選択値</th>
			<td>
				<table>
					<tr>
						<td><p>value属性</p><textarea name="element_valus" id="element_valus" cols="30" rows="20" onblur="charexp(this)">$gethash{'element_valus'}</textarea></td>
						<td><p>表示</p><textarea name="element_text" id="element_text" cols="30" rows="20">$gethash{'element_text'}</textarea></td>
					</tr>
				</table>
				<span class="caution">※selectタグでoptgroupを設定する場合は表示の後ろに「表示値::所属するグループ」を記述します。</span></ br>
				<span class="caution">※selectタグでselectedを設定する場合は値の後ろに「値::selected」を記述します。</span></ br>
				<span class="caution">※radioタグ又はcheckboxでcheckedタグを設定する場合は値の後ろに「値::checked」を記述します。</span></ br>
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="filetype_only">
		<tr>
			<th $enable_filetypes_error_bg>対応ファイル</th>
			<td $enable_filetypes_error_bg>
				<span class="caution">$enable_filetypes_error_msg</span>
				<input type="text" name="enable_filetypes" id="enable_filetypes" value="$gethash{'enable_filetypes'}" size="40" />
				<span>※カンマ区切りで入力してください</span>
			</td>
		</tr>
		<tr>
			<th>ファイルサイズ</th>
			<td><input type="text" name="filesize_min" id="filesize_min" value="$gethash{'filesize_min'}" size="10" /> KB &lt; <input type="text" name="filesize_max" id="filesize_max" value="$gethash{'filesize_max'}" size="10" /> KB <span>（目安：1024 KB）サーバーの種類により上限が違います。ホスティング会社へ事前のご確認をお願いいたします。</span></td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="button">
		<tr>
			<td><input type="submit" name="submit" value="${submit}" /> <input type="button" name="submit" value="キャンセル" onclick="location.href='?m=$form{'m'}'" /></td>
		</tr>
	</table>
</form>
EOF

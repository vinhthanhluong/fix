###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

if($form{'id'} ne $null){
	$action_name = '送信条件の編集';
	@current_data = grep(/^$form{'id'}\t/,@current_data);
	@users_info = split(/\t/,$current_data[0]);
	@hash_names = @db_fields_elements;
	*gethash = &setHash(@users_info);
	$submit = '更新';
}
else {
	$action_name = '条件の追加';
	$submit = '追加';
	$gethash{'conditional_id'} = time;
}

if($gethash{'conditional_type'} == 0){
	$type_selected = ' selected';
}

## 条件定義用の項目読み込み
@elements = &loadfile('./datas/modules/elements/elements.dat');
for($cnt=0;$cnt<@elements;$cnt++){
	($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class) = split(/\t/,$elements[$cnt]);
	if($element_type eq "select" || $element_type eq "radio" || $element_type eq "checkbox"){
		$selected_flag = 0;
		if($gethash{'conditional_element'} eq $elements_id){
			$elements .= "<option value=\"${elements_id}\" selected>${name}</option>";
			$selected_flag = 1;
		}
		else {
			$elements .= "<option value=\"${elements_id}\">${name}</option>";
		}
		@element_values = split(/<br \/>/,$element_valus);
		@element_text = split(/<br \/>/,$element_text);
		for($i=0;$i<@element_values;$i++){
			#追加
			${element_values[$i]} =~ s/::checked//g;
			${element_values[$i]} =~ s/::selected//g;

			if($selected_flag){
				if($element_values[$i] eq $gethash{'conditional_value'}){
					$selected_items .= "<option value=\"${element_values[$i]}\" selected>${element_values[$i]}</option>\n";
				}
				else {
					$selected_items .= "<option value=\"${element_values[$i]}\">${element_values[$i]}</option>\n";
				}
			}
			$hidden_selected_items .= "<option value=\"${elements_id}\"${selected}>${element_values[$i]}</option>\n";
		}
	}
	if($element_type ne "spacer"){
		$add_elements_value_list .= "<option value=\"${elements_id}\">${name}</option>";
	}
}

## 初期設定チェック ############
#送信先
if($gethash{'mailaddress'} eq 'checkcheck@freesale.co.jp' || $gethash{'mailaddress'} eq 'f-check@freesale.co.jp'){
	$mailaddress_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />初期値のままです。';
	$mailaddress_error_bg = 'class="error_bg"';
}elsif(!$gethash{'mailaddress'}){
	$mailaddress_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />入力されていません。';
	$mailaddress_error_bg = 'class="error_bg"';
}

#件名
if($gethash{'subject'} eq '「○○（サイト名）」お問い合わせ　通知メール'){
	$subject_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />初期値のままです。';
	$subject_error_bg = 'class="error_bg"';
}elsif(!$gethash{'subject'}){
	$subject_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />入力されていません。';
	$subject_error_bg = 'class="error_bg"';
}

$print_html = <<"EOF";
<p>送信条件を${submit}します。</p>
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" onSubmit="return checkUserEdit(this,'${submit}');">
	<input type="hidden" name="id" value="$form{'id'}" />
	<input type="hidden" name="conditional_id" value="$gethash{'conditional_id'}" />
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<th>タイプ</th>
			<td>
				<select name="conditional_type" id="conditional_type" onchange="change_conditional_type(this)">
					<option value="1">すべて送信</option>
					<option value="0"${type_selected}>条件で送信</option>
				</select>
			</td>
		</tr>
		<tr>
			<th>条件名</th>
			<td><input type="text" name="conditional_name" id="conditional_name" value="$gethash{'conditional_name'}" class="data" /></td>
		</tr>
		<tr>
			<th $mailaddress_error_bg>送信先</th>
			<td $mailaddress_error_bg>
				<span class="caution">$mailaddress_error_msg</span>
				<input type="text" name="mailaddress" id="mailaddress" value="$gethash{'mailaddress'}" class="data" onblur="email_check(this.id)" />
				<span>※複数の場合は半角カンマで区切ってください</span>
			</td>
		</tr>
		<tr>
			<th>CC</th>
			<td>
				<input type="text" name="cc" id="cc" value="$gethash{'cc'}" class="data" onblur="email_check(this.id)" /><br />
				フォームから受け取った値を反映 →
				<select name="add_elements_value_list_cc" id="add_elements_value_list_cc">
					${add_elements_value_list}
				</select>
				<input type="button" value="挿入" onclick="add_element_value_cc()" />
				<span>※複数の場合は半角カンマで区切ってください</span>
			</td>
		</tr>
		<tr>
			<th>BCC</th>
			<td>
				<input type="text" name="bcc" id="bcc" value="$gethash{'bcc'}" class="data" onblur="email_check(this.id)" /><br />
				フォームから受け取った値を反映 →
				<select name="add_elements_value_list_bcc" id="add_elements_value_list_bcc">
					${add_elements_value_list}
				</select>
				<input type="button" value="挿入" onclick="add_element_value_bcc()" />
				<span>※複数の場合は半角カンマで区切ってください</span>
			</td>
		</tr>
		<tr>
			<th>通し番号名</th>
			<td>
				[<input type="text" name="numname" id="numname" value="$gethash{'numname'}" class="settingdata" />xxxx]件名<br />
				<span>※空欄可</span>
			</td>
		</tr>
		<tr>
			<th $subject_error_bg>件名</th>
			<td $subject_error_bg>
				<span class="caution">$subject_error_msg</span>
				<input type="text" name="subject" id="subject" value="$gethash{'subject'}" class="data" /><br />
				フォームから受け取った値を反映 →
				<select name="add_elements_value_list_subject" id="add_elements_value_list_subject">
					${add_elements_value_list}
				</select>
				<input type="button" value="挿入" onclick="add_element_value_subject()" />
			</td>
		</tr>
		<tr>
			<th>本文</th>
			<td>
				<textarea name="body" id="body" cols="40" rows="10">$gethash{'body'}</textarea><br />
				フォームから受け取った値を反映 →
				<select name="add_elements_value_list" id="add_elements_value_list">
					<option value="resbody">送信内容一覧</option>
					<option value="serial">通し番号</option>
					<option value="stmp">送信日時</option>
					<option value="env">環境情報</option>
					<option value="site_url">URL</option>
					<option value="afiri_uniq_id">アフィリエイト識別ID</option>
					${add_elements_value_list}
				</select>
				<input type="button" value="挿入" onclick="add_element_value()" />
			</td>
		</tr>
		<tr>
			<th>備考</th>
			<td><textarea name="note" id="note" cols="40" rows="10">$gethash{'note'}</textarea></td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="conditional_if">
		<tr>
			<th>条件項目</th>
			<td>
				<select name="conditional_element" id="conditional_element" onchange="change_element_type(this)">
					<option value=""></option>
					${elements}
				</select>
			</td>
		</tr>
		<tr>
			<th>条件値</th>
			<td>
				<select name="conditional_value" id="conditional_value">
					${selected_items}
				</select>
				<select name="hidden_selected_items" id="hidden_selected_items">
					${hidden_selected_items}
				</select>
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<td>&nbsp;</td>
			<td><input type="submit" name="submit" value="${submit}" /> <input type="button" name="submit" value="キャンセル" onclick="location.href='?m=$form{'m'}'" /></td>
		</tr>
	</table>
</form>
EOF

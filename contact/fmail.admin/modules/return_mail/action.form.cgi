###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

if($form{'id'} ne $null){
	$action_name = '自動返信メールの条件の編集';
	@current_data = grep(/^$form{'id'}\t/,@current_data);
	@users_info = split(/\t/,$current_data[0]);
	@hash_names = @db_fields_elements;
	*gethash = &setHash(@users_info);
	$submit = '更新';
}
else {
	$action_name = '自動返信メールの条件の追加';
	$submit = '追加';
	$gethash{'return_mail_id'} = time;
}

if($gethash{'return_mail_type'} == 0){
	$type_selected = ' selected';
}


$flag = $gethash{'flag'};
$from = $gethash{'from'};
$sender = $gethash{'sender'};
$subject = $gethash{'subject'};
$serials = $gethash{'serials'};
$email_field = $gethash{'email_field'};
$body = $gethash{'body'};
$body =~ s/<br \/>/\n/g;

if($flag){
	$flag_checked = ' checked';
}
if($serials){
	$serial_checked = ' checked';
}

## 条件定義用の項目読み込み
@elements = &loadfile('./datas/modules/elements/elements.dat');

# 返信先設定
for($cnt=0;$cnt<@elements;$cnt++){
	($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class) = split(/\t/,$elements[$cnt]);
	if($check_type eq "mail"){
		if($email_field eq $elements_id){
			$email_fields .= "<option value=\"${elements_id}\" selected>${name}</option>";
		}
		else {
			$email_fields .= "<option value=\"${elements_id}\">${name}</option>";
		}
	}
	if($element_type ne "spacer"){
		$add_elements_value_list .= "<option value=\"${elements_id}\">${name}</option>";
	}
}

# 条件項目と条件値
for($cnt=0;$cnt<@elements;$cnt++){
	($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_blur,$on_focus,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note) = split(/\t/,$elements[$cnt]);
	if($element_type eq "select" || $element_type eq "radio" || $element_type eq "checkbox"){
		$selected_flag = 0;
		if($gethash{'return_mail_element'} eq $elements_id){
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
				if($element_values[$i] eq $gethash{'return_mail_value'}){
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
#差出人アドレス
if(${from} eq 'checkcheck@freesale.co.jp' || ${from} eq 'f-check@freesale.co.jp'){
	$from_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />初期値のままです。';
	$from_error_bg = 'class="error_bg"';
}elsif(!${from}){
	$from_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />入力されていません。';
	$from_error_bg = 'class="error_bg"';
}

#自動返信先
if(!${email_fields}){
	$email_fields_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />設定されていません。';
	$email_fields_error_bg = 'class="error_bg"';
}

#差出人表示名
if(${sender} eq '○○（サイト名）'){
	$sender_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />初期値のままです。';
	$sender_error_bg = 'class="error_bg"';
}elsif(!${sender}){
	$sender_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />入力されていません。';
	$sender_error_bg = 'class="error_bg"';
}

#件名
if(${subject} eq '「○○（サイト名）」お問い合わせ　確認メール'){
	$subject_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />初期値のままです。';
	$subject_error_bg = 'class="error_bg"';
}elsif(!${subject}){
	$subject_error_msg = '<img src="../images/mfp_error.gif" class="error_img" />入力されていません。';
	$subject_error_bg = 'class="error_bg"';
}

$print_html = <<"EOF";
<p>自動返信メールに関する設定を行います。</p>
<div id="stat">
	自動返信メールに関する設定の保存が完了しました
</div>
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" onSubmit="return checkUserEdit(this,'${submit}');">
	<input type="hidden" name="id" value="$form{'id'}" />
	<input type="hidden" name="return_mail_id" value="$gethash{'return_mail_id'}" />
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<th>タイプ</th>
			<td>
				<select name="return_mail_type" id="return_mail_type" onchange="change_return_mail_type(this)">
					<option value="1">すべて送信</option>
					<option value="0"${type_selected}>条件で送信</option>
				</select>
			</td>
		</tr>
		<tr>
			<th>条件名</th>
			<td><input type="text" name="return_mail_name" id="return_mail_name" value="$gethash{'return_mail_name'}" class="data" /></td>
		</tr>
		<tr>
			<th>有効/無効</th>
			<td><input type="checkbox" name="flag" value="1"${flag_checked} /> 自動返信メールを有効にする</td>
		</tr>
		<tr>
			<th $from_error_bg>差出人アドレス</th>
			<td $from_error_bg>
				<span class="caution">$from_error_msg</span>
				<input type="text" name="from" id="from" value="${from}" onblur="email_check(this.id)" />
				<span>例）info\@freesale.co.jp</span>
			</td>
		</tr>
		<tr>
			<th $email_fields_error_bg>自動返信先</th>
			<td $email_fields_error_bg>
				<span class="caution">$email_fields_error_msg</span>
				<select name="email_field">
					<option value=""></option>
					${email_fields}
				</select>
			</td>
		</tr>
		<tr>
			<th $sender_error_bg>差出人表示名</th>
			<td $sender_error_bg>
				<span class="caution">$sender_error_msg</span>
				<input type="text" name="sender" id="sender" value="${sender}" />
				<span>例）株式会社フリーセル お客様担当</span>
				<span class="caution">未設定の場合、メール送信時に差出人表示名の代わりに差出人アドレスが表示されます。</span>
			</td>
		</tr>
		<tr>
			<th $subject_error_bg>件名</th>
			<td $subject_error_bg>
				<span class="caution">$subject_error_msg</span>
				<input type="text" name="subject" id="subject" value="${subject}" /><br />
				フォームから受け取った値を反映 →
				<select name="add_elements_value_list_subject" id="add_elements_value_list_subject">
					${add_elements_value_list}
				</select>
				<input type="button" value="挿入" onclick="add_element_value_subject()" />
				<span>例）【 フリーセル公式 】 お問い合わせのご確認</span>
			</td>
		</tr>
		<tr>
			<th>通し番号</th>
			<td><input type="checkbox" name="serials" value="1"${serial_checked} /> 件名に通し番号を付ける</td>
		</tr>
		<tr>
			<th>本文</th>
			<td>
				<textarea name="body" id="body">${body}</textarea><br />
				フォームから受け取った値を反映 →
				<select name="add_elements_value_list" id="add_elements_value_list">
					<option value="resbody">送信内容一覧</option>
					<option value="serial">通し番号</option>
					<option value="stmp">送信日時</option>
					<option value="env">環境情報</option>
					<option value="site_url">URL</option>
					<option value="client_info">クライアント情報</option>
					${add_elements_value_list}
				</select>
				<input type="button" value="挿入" onclick="add_element_value()" />
			</td>
		</tr>
	</table>
	<table cellpadding="0" cellspacing="0" class="sheet" id="return_mail_if">
		<tr>
			<th>条件項目</th>
			<td>
				<select name="return_mail_element" id="return_mail_element" onchange="change_element_type(this)">
					<option value=""></option>
					${elements}
				</select>
			</td>
		</tr>
		<tr>
			<th>条件値</th>
			<td>
				<select name="return_mail_value" id="return_mail_value">
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

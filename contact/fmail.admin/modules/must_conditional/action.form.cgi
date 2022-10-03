###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

if($form{'id'} ne $null){
	$action_name = '必須条件の編集';
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

# エラー文の標準設定
if(!$gethash{'error_message'}){
	$gethash{'error_message'} = '入力内容に誤りがあります。';
}

## 必須エレメントの分解
@must_elements = split(/\&/,$gethash{'must_elements'});
for($cnt=0;$cnt<@must_elements;$cnt++){
	($ename,$evalue) = split(/\=/,$must_elements[$cnt]);
	$must_element{$ename} = $evalue;
}

## 条件定義用の項目読み込み
@elements = &loadfile('./datas/modules/elements/elements.dat');
for($cnt=0;$cnt<@elements;$cnt++){
	($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class) = split(/\t/,$elements[$cnt]);
	if($element_type eq "select" || $element_type eq "radio" || $element_type eq "checkbox"){
		@element_values = split(/<br \/>/,$element_valus);
		@element_text = split(/<br \/>/,$element_text);
		$selected_items = "<option value=\"1\">いずれかの選択値</option>";
		for($i=0;$i<@element_values;$i++){
			if($must_element{$elements_id} eq $element_values[$i] && $element_values[$i] ne $null){
				$selected_items .= "<option value=\"${element_values[$i]}\" selected>${element_values[$i]}</option>\n";
			}
			else {
				$selected_items .= "<option value=\"${element_values[$i]}\">${element_values[$i]}</option>\n";
			}
		}
		if($must_element{$elements_id} ne $null){
			$elements .= "<li><input type=\"checkbox\" name=\"must_elements_list\" value=\"${elements_id}\" checked /> ${name} <select name=\"val${elements_id}\">${selected_items}</select></li>";
		}
		else {
			$elements .= "<li><input type=\"checkbox\" name=\"must_elements_list\" value=\"${elements_id}\" /> ${name} <select name=\"val${elements_id}\">${selected_items}</select></li>";
		}
	}
	elsif($element_type ne "join" && $element_type ne "spacer"){
		if($must_element{$elements_id} ne $null) {
			$elements .= "<li><input type=\"checkbox\" name=\"must_elements_list\" value=\"${elements_id}\" checked /> ${name}</li>";
		}
		else {
			$elements .= "<li><input type=\"checkbox\" name=\"must_elements_list\" value=\"${elements_id}\" /> ${name}</li>";
		}
	}
}

if($gethash{'conditional_type'} == 0){
	$type_selected = ' selected';
}
## 分岐定義用の項目読み込み
@elements = &loadfile('./datas/modules/elements/elements.dat');
for($cnt=0;$cnt<@elements;$cnt++){
	($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class) = split(/\t/,$elements[$cnt]);
#	if($element_type eq "select" || $element_type eq "radio" || $element_type eq "checkbox"){
	if($element_type eq "select" || $element_type eq "radio"){
		$selected_flag = 0;
		if($gethash{'conditional_element'} eq $elements_id){
			$case_elements .= "<option value=\"${elements_id}\" selected>${name}</option>";
			$selected_flag = 1;
		}
		else {
			$case_elements .= "<option value=\"${elements_id}\">${name}</option>";
		}
		@element_values = split(/<br \/>/,$element_valus);
		@element_text = split(/<br \/>/,$element_text);
		for($i=0;$i<@element_values;$i++){
			#追加
			${element_values[$i]} =~ s/::checked//g;
			${element_values[$i]} =~ s/::selected//g;

			if($selected_flag){
				if($element_values[$i] eq $gethash{'conditional_value'}){
					$case_selected_items .= "<option value=\"${element_values[$i]}\" selected>${element_values[$i]}</option>\n";
				}
				else {
					$case_selected_items .= "<option value=\"${element_values[$i]}\">${element_values[$i]}</option>\n";
				}
			}
			$hidden_selected_items .= "<option value=\"${elements_id}\"${selected}>${element_values[$i]}</option>\n";
		}
	}
	if($element_type ne "spacer"){
		$add_elements_value_list .= "<option value=\"${elements_id}\">${name}</option>";
	}
}

$print_html = <<"EOF";
<p>項目の必須条件を${submit}します。</p>
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" onSubmit="return checkUserEdit(this,'${submit}');">
	<input type="hidden" name="id" value="$form{'id'}" />
	<input type="hidden" name="conditional_id" value="$gethash{'conditional_id'}" />
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<th>必須条件名</th>
			<td><input type="text" name="must_name" id="must_name" value="$gethash{'must_name'}" size="30" /></td>
		</tr>
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
			<th>必須項目</th>
			<td>
				<ul>
					${elements}
				</ul>
				<input type="hidden" name="must_elements" value="$gethash{'must_elements'}" />
			</td>
		</tr>
		<tr>
			<th>エラー文</th>
			<td><textarea name="error_message" id="error_message" cols="40" rows="10">$gethash{'error_message'}</textarea></td>
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
					${case_elements}
				</select>
				<span class="caution">※checkboxは選択不可</span>
			</td>
		</tr>
		<tr>
			<th>条件値</th>
			<td>
				<select name="conditional_value" id="conditional_value">
					${case_selected_items}
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

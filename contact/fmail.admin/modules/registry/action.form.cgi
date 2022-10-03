###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

if($form{'id'} ne $null){
	$action_name = 'レジストリの編集';
	@registry = grep(/^$form{'id'}\t/,@registry);
	@registry_info = split(/\t/,$registry[0]);
	@hash_names = @registry_db_fields;
	*gethash = &setHash(@registry_info);
	$submit = '更新';
}
else {
	$action_name = 'レジストリの追加';
	$submit = '追加';
}
if($gethash{'form_registry_type'}){
	$checked = " checked";
}
$print_html = <<"EOF";
<div style="padding: 10px;text-align: left;">
	<p>下記のフィールドの必要な値を編集して下さい。</p>
	<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" enctype="multipart/form-data" onSubmit="return checkUserEdit(this,'${submit}');">
		<input type="hidden" name="id" value="$form{'id'}" />
		<table cellpadding="0" cellspacing="0" class="sheet">
			<tr>
				<th>ハッシュID</th>
				<td><input type="text" name="form_registry_id" id="form_registry_id" value="$gethash{'form_registry_id'}"></td>
			</tr>
			<tr>
				<th>タイプ</th>
				<td><input type="checkbox" name="form_registry_type" value="1"${checked} /> 配列</td>
			</tr>
			<tr>
				<th>値</th>
				<td><input type="text" name="form_registry_value" id="form_registry_value" value="$gethash{'form_registry_value'}"></td>
			</tr>
			<tr>
				<th>\表\示\名</th>
				<td><input type="text" name="form_display_name" id="form_display_name" value="$gethash{'form_display_name'}"></td>
			</tr>
			<tr>
				<th>役割</th>
				<td><textarea name="form_registry_note" id="form_registry_note">$gethash{'form_registry_note'}</textarea></td>
			</tr>
			<tr>
				<td>&nbsp;</td>
				<td><input type="submit" name="submit" value="${submit}" /> <input type="button" name="submit" value="キャンセル" onclick="location.href='?m=$form{'m'}'" /></td>
			</tr>
		</table>
	</form>
</div>
EOF

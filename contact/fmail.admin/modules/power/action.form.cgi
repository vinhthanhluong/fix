###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

if($form{'id'} ne $null){
	$action_name = '権限の編集';
	@current_data = grep(/^$form{'id'}\t/,@current_data);
	@current_record = split(/\t/,$current_data[0]);
	@hash_names = @current_db_fields;
	*gethash = &setHash(@current_record);
	$submit = '更新';
	$readonly = " readonly";
}
else {
	$action_name = '権限の追加';
	$submit = '追加';
}
$print_html = <<"EOF";
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" enctype="multipart/form-data" onSubmit="return checkUserEdit(this,'${submit}');">
	<input type="hidden" name="id" value="$form{'id'}" />
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<th>\表\示\名</th>
			<td><input type="text" name="form_display_name" id="form_display_name" value="$gethash{'form_display_name'}" /></td>
		</tr>
		<tr>
			<th>ID</th>
			<td><input type="text" name="form_power_id" id="form_user_id" value="$gethash{'form_power_id'}"${readonly} /></td>
		</tr>
		<tr>
			<th>備考</th>
			<td><textarea name="form_power_note" id="form_user_note">$gethash{'form_power_note'}</textarea></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td><input type="submit" name="submit" value="${submit}" /> <input type="button" name="submit" value="キャンセル" onclick="location.href='?m=$form{'m'}'" /></td>
		</tr>
	</table>
</form>
EOF

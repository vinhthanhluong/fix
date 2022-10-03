###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

if($form{'id'} ne $null){
	$action_name = '管理ユーザの編集';
	@users = grep(/^$form{'id'}\t/,@users);
	@users_info = split(/\t/,$users[0]);
	@hash_names = @user_db_fields;
	*gethash = &setHash(@users_info);
	$submit = '更新';
	$readonly = " readonly";
}
else {
	$action_name = '管理ユーザの追加';
	$submit = '追加';
}
for($cnt=0;$cnt<@user_powers;$cnt++){
	$selected = "";
	if($user_powers_id[$cnt] eq $gethash{'form_user_power'}){
		$selected = " selected";
	}
	$user_powers_select .= "<option value=\"${user_powers_id[${cnt}]}\"${selected}>${user_powers[$cnt]}</option>";
}
##pictures
$pict_path = "$reg{'dir_user_pictures'}thum_$form{'id'}.jpg";
if(-f $pict_path){
	$deletetag = "<div id=\"picture\"><img src=\"${pict_path}\" width=\"$reg{'dir_user_pictures_thum_size'}\" /></div><input type=\"checkbox\" name=\"picture_delete\" value=\"1\" /> 削除する";
}
#$gethash{'form_user_password'}
$print_html = <<"EOF";
<p>下記のホームページ管理ユーザを更新します。下記のフィールドの必要な値を編集して下さい。</p>
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" enctype="multipart/form-data" onSubmit="return checkUserEdit(this,'${submit}');">
	<input type="hidden" name="id" value="$form{'id'}" />
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<th>\表\示\名</th>
			<td><input type="text" name="form_display_name" id="form_display_name" value="$gethash{'form_display_name'}" /></td>
		</tr>
		<tr style="display: none;">
			<th>アイコン<br />(jpgのみ)</th>
			<td><input type="file" name="form_display_picture" id="form_display_picture" />$deletetag</td>
		</tr>
		<tr>
			<th>ユーザID</th>
			<td><input type="text" name="form_user_id" id="form_user_id" value="$gethash{'form_user_id'}"${readonly} /></td>
		</tr>
		<tr>
			<th>パスワード</th>
			<td><input type="text" name="form_user_password" id="form_user_password" value="" /> <input type="button" value="自動生成" onClick="random_password();" /></td>
		</tr>
		<tr>
			<th>ユーザ権限</th>
			<td><select name="form_user_power">${user_powers_select}</select></td>
		</tr>
		<tr style="display: none;">
			<th>email</th>
			<td><input type="text" name="form_user_email" id="form_user_email" value="$gethash{'form_user_email'}" /></td>
		</tr>
		<tr style="display: none;">
			<th>携帯メール</th>
			<td><input type="text" name="form_user_email_mobile" id="form_user_email_mobile" value="$gethash{'form_user_email_mobile'}" /></td>
		</tr>
		<tr>
			<th>備考</th>
			<td><textarea name="form_user_note" id="form_user_note">$gethash{'form_user_note'}</textarea></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td><input type="submit" name="submit" value="${submit}" /> <input type="button" name="submit" value="キャンセル" onclick="location.href='?m=$form{'m'}'" /></td>
		</tr>
	</table>
</form>
EOF

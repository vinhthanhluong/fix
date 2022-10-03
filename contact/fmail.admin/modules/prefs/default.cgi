###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$action_name = '登録情報';
@users = grep(/^$current_user{'id'}\t/,@users);
@users_info = split(/\t/,$users[0]);
@hash_names = @user_db_fields;
*gethash = &setHash(@users_info);
$pict_path = "$reg{'dir_user_pictures'}thum_$current_user{'id'}.jpg";
if(-f $pict_path){
	$deletetag = "<div id=\"picture\"><img src=\"${pict_path}\" width=\"$reg{'dir_user_pictures_thum_size'}\" /></div><input type=\"checkbox\" name=\"picture_delete\" value=\"1\" /> 削除する";
}

$print_html = <<"EOF";
<p>登録情報を変更する場合は、以下のフォームから変更してください。</p>
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" enctype="multipart/form-data" onSubmit="return checkUserEdit(this,'${submit}');">
	<input type="hidden" name="id" value="$current_user{'id'}" />
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<th>お名前</th>
			<td><input type="text" name="form_display_name" id="form_display_name" value="$gethash{'form_display_name'}" /></td>
		</tr>
		<!--
		<tr>
			<th>アイコン<br />(jpgのみ)</th>
			<td><input type="file" name="form_display_picture" id="form_display_picture" />$deletetag</td>
		</tr>
		-->
		<tr>
			<th>パスワード</th>
			<td><input type="password" name="form_user_password" id="form_user_password" /><span>※8文字以上の英数で入力してください</span></td>
		</tr>
		<tr>
			<th>もう一度</th>
			<td><input type="password" name="form_user_password_confirm" id="form_user_password_confirm" /></td>
		</tr>
		<!--
		<tr>
			<th>メールアドレス</th>
			<td><input type="text" name="form_user_email" id="form_user_email" value="$gethash{'form_user_email'}" /></td>
		</tr>
		<tr>
			<th>携帯メール</th>
			<td><input type="text" name="form_user_email_mobile" id="form_user_email_mobile" value="$gethash{'form_user_email_mobile'}" /></td>
		</tr>
		-->
		<tr>
			<td>&nbsp;</td>
			<td><input type="submit" name="submit" value="更新" /></td>
		</tr>
	</table>
</form>
EOF

###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

if($form{'id'} ne $null){
	$action_name = 'お知らせの編集';
	@current_data = grep(/^$form{'id'}\t/,@current_data);
	@current_data_info = split(/\t/,$current_data[0]);
	@hash_names = @user_db_fields;
	*gethash = &setHash(@current_data_info);
	$submit = '更新';
}
else {
	$action_name = 'お知らせの追加';
	$submit = '追加';
	$gethash{'note_id'} = time();
}
$print_html = <<"EOF";
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" enctype="multipart/form-data" onSubmit="return checkUserEdit(this,'${submit}');">
	<input type="hidden" name="note_id" value="$gethash{'note_id'}" />
	<input type="hidden" name="id" value="$form{'id'}" />
	<p><input type="text" name="note_title" id="note_title" value="$gethash{'note_title'}" /></p>
	<p><textarea name="note_body" id="note_body">$gethash{'note_body'}</textarea></p>
	<p><input type="submit" name="submit" value="${submit}" /> <input type="button" name="submit" value="キャンセル" onclick="location.href='?m=$form{'m'}'" /></p>
</form>
EOF

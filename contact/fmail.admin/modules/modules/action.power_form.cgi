###############################################################################
# action
###############################################################################

@registry = &loadfile("${dir_datas}$form{'m'}\/$form{'module'}\.power\.dat");
if($form{'id'} ne $null){
	$action_name = $form{'module'} . 'モジュール／' . $form{'id'} . 'のアクセス権の編集';
	@registry = grep(/^$form{'id'}\t/,@registry);
	@registry_info = split(/\t/,$registry[0]);
	$submit = '更新';
	if($registry_info[1] eq "null"){
		$selected = " selected";
	}
	if($registry_info[0] eq "module_main"){
		$disp_alluser = 'All User';
	}
	else {
		$disp_alluser = 'モジュールのアクセス権と同じ';
	}
}
else {
	$action_name = 'レジストリの追加';
	$submit = '追加';
}
for($cnt=0;$cnt<@user_powers_id;$cnt++){
	if(index($registry_info[1],$user_powers_id[$cnt]) > -1){
		$selecttag .= "<option value=\"${user_powers_id[$cnt]}\" selected>${user_powers[$cnt]}</option>";
	}
	else {
		$selecttag .= "<option value=\"${user_powers_id[$cnt]}\">${user_powers[$cnt]}</option>";
	}
}
$print_html = <<"EOF";
<div style="padding: 10px;text-align: left;">
	<form id="user_add" action="?m=$form{'m'}&a=power_save" method="POST" onSubmit="return checkPowers(this,'${submit}');">
		<input type="hidden" name="module" value="$form{'module'}" />
		<input type="hidden" name="id" value="$form{'id'}" />
		<table cellpadding="0" cellspacing="0" class="sheet">
			<tr>
				<td>
					<select name="powers" size="4" multiple class="multiple">
						$selecttag
						<option value="null"${selected}>${disp_alluser}</option>
					</select>
					<div style="display: none;">
						<input type="text" name="post_powers" style="width: 600px;" value="$registry_info[1]" />
					</div>
				</td>
			</tr>
			<tr>
				<td><input type="submit" name="submit" value="${submit}" /> <input type="button" name="submit" value="キャンセル" onclick="location.href='?m=$form{'m'}&a=power&id=$form{'module'}'" /></td>
			</tr>
		</table>
	</form>
</div>
EOF

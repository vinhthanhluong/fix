###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$current_data = join("\n",@current_data);
($carriage_place,$carriage_price,$flag_free,$carriage_limit) = split(/\n/,$current_data);

# 改行タグ置換 送付先
$carriage_place =~ s/&lt\;br \/&gt\;/\n/g;
$carriage_place =~ s/<br \/>/\n/g;
# 改行タグ置換 送料
$carriage_price =~ s/&lt\;br \/&gt\;/\n/g;
$carriage_price =~ s/<br \/>/\n/g;

# 送料無料フラグ
if($flag_free){
	$flag_checked = ' checked="checked"';
}

$action_name = '商品カート送料設定画面';
$print_html = <<"EOF";
<p>商品カートの送料に関する設定を行います。</p>
<div id="stat">
	商品カートの送料に関する設定の保存が完了しました
</div>
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" onSubmit="return checkUserEdit(this,'${submit}');">
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<th>送付先と送料</th>
			<td>
				<ul class="textarea clearfix">
					<li><span class="item">[ 郵送先地域 ]</span><textarea name="carriage_place">$carriage_place</textarea></li>
					<li><span class="item">[ 送料（税込） ]</span><textarea name="carriage_price" id="carriage_price" onchange="num_adjust(this.id);">$carriage_price</textarea></li>
				</ul>
			</td>
		</tr>
		<tr>
			<th>送料無料設定</th>
			<td>
				<input type="checkbox" name="flag_free" value="1"$flag_checked /> 送料無料にする　　
				<input type="text" name="carriage_limit" value="${carriage_limit}" id="carriage_limit" class="data" onchange="num_adjust(this.id);" /> 円以上のお買い上げで送料無料にする。
			</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td><input type="submit" name="submit" value="保存" /> <input type="button" name="submit" value="キャンセル" onclick="location.href='?m=$form{'m'}'" /></td>
		</tr>
	</table>
</form>
EOF

###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$current_data = join("\n",@current_data);
($size_1_w,$size_1_h,$size_2_w,$size_2_h,$size_3_w,$size_3_h,$size_4_w,$size_4_h,$size_5_w,$size_5_h,$size_6_w,$size_6_h,$size_7_w,$size_7_h,$size_8_w,$size_8_h,$size_9_w,$size_9_h,$size_10_w,$size_10_h) = split(/\n/,$current_data);


## 項目読み込み
@elements = &loadfile('./datas/modules/elements/elements.dat');
for($cnt=0;$cnt<@elements;$cnt++){
	($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class) = split(/\t/,$elements[$cnt]);
	if ($html_size eq 'size_1') {
		$itemname_1 .= "${name} / ";
	} elsif ($html_size eq 'size_2') {
		$itemname_2 .= "${name} / ";
	} elsif ($html_size eq 'size_3') {
		$itemname_3 .= "${name} / ";
	} elsif ($html_size eq 'size_4') {
		$itemname_4 .= "${name} / ";
	} elsif ($html_size eq 'size_5') {
		$itemname_5 .= "${name} / ";
	} elsif ($html_size eq 'size_6') {
		$itemname_6 .= "${name} / ";
	} elsif ($html_size eq 'size_7') {
		$itemname_7 .= "${name} / ";
	} elsif ($html_size eq 'size_8') {
		$itemname_8 .= "${name} / ";
	} elsif ($html_size eq 'size_9') {
		$itemname_9 .= "${name} / ";
	} elsif ($html_size eq 'size_10') {
		$itemname_10 .= "${name} / ";
	}
}
$itemname_1 =~ s/\s\/\s$//g;
$itemname_2 =~ s/\s\/\s$//g;
$itemname_3 =~ s/\s\/\s$//g;
$itemname_4 =~ s/\s\/\s$//g;
$itemname_5 =~ s/\s\/\s$//g;
$itemname_6 =~ s/\s\/\s$//g;
$itemname_7 =~ s/\s\/\s$//g;
$itemname_8 =~ s/\s\/\s$//g;
$itemname_9 =~ s/\s\/\s$//g;
$itemname_10 =~ s/\s\/\s$//g;


$action_name = '項目サイズ';
$print_html = <<"EOF";
<p>項目サイズCLASSに関わる設定を行います。</p>
<div id="stat">
	項目サイズに関する設定の保存が完了しました
</div>
<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" onSubmit="return checkUserEdit(this,'${submit}');">
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<th>class="size_1"</th>
			<td>
				横幅 <input type="text" name="size_1_w" value="${size_1_w}" id="size_1_w" class="num" onchange="dataadjust(this.id);" />　/　
				高さ <input type="text" name="size_1_h" value="${size_1_h}" id="size_1_h" class="num" onchange="dataadjust(this.id);" />　
				<span class="target">対象項目</span>$itemname_1
			</td>
		</tr>
		<tr>
			<th>class="size_2"</th>
			<td>
				横幅 <input type="text" name="size_2_w" value="${size_2_w}" id="size_2_w" class="num" onchange="dataadjust(this.id);" />　/　
				高さ <input type="text" name="size_2_h" value="${size_2_h}" id="size_2_h" class="num" onchange="dataadjust(this.id);" />　
				<span class="target">対象項目</span>$itemname_2
			</td>
		</tr>
		<tr>
			<th>class="size_3"</th>
			<td>
				横幅 <input type="text" name="size_3_w" value="${size_3_w}" id="size_3_w" class="num" onchange="dataadjust(this.id);" />　/　
				高さ <input type="text" name="size_3_h" value="${size_3_h}" id="size_3_h" class="num" onchange="dataadjust(this.id);" />　
				<span class="target">対象項目</span>$itemname_3
			</td>
		</tr>
		<tr>
			<th>class="size_4"</th>
			<td>
				横幅 <input type="text" name="size_4_w" value="${size_4_w}" id="size_4_w" class="num" onchange="dataadjust(this.id);" />　/　
				高さ <input type="text" name="size_4_h" value="${size_4_h}" id="size_4_h" class="num" onchange="dataadjust(this.id);" />　
				<span class="target">対象項目</span>$itemname_4
			</td>
		</tr>
		<tr>
			<th>class="size_5"</th>
			<td>
				横幅 <input type="text" name="size_5_w" value="${size_5_w}" id="size_5_w" class="num" onchange="dataadjust(this.id);" />　/　
				高さ <input type="text" name="size_5_h" value="${size_5_h}" id="size_5_h" class="num" onchange="dataadjust(this.id);" />　
				<span class="target">対象項目</span>$itemname_5
			</td>
		</tr>
		<tr>
			<th>class="size_6"</th>
			<td>
				横幅 <input type="text" name="size_6_w" value="${size_6_w}" id="size_6_w" class="num" onchange="dataadjust(this.id);" />　/　
				高さ <input type="text" name="size_6_h" value="${size_6_h}" id="size_6_h" class="num" onchange="dataadjust(this.id);" />　
				<span class="target">対象項目</span>$itemname_6
			</td>
		</tr>
		<tr>
			<th>class="size_7"</th>
			<td>
				横幅 <input type="text" name="size_7_w" value="${size_7_w}" id="size_7_w" class="num" onchange="dataadjust(this.id);" />　/　
				高さ <input type="text" name="size_7_h" value="${size_7_h}" id="size_7_h" class="num" onchange="dataadjust(this.id);" />　
				<span class="target">対象項目</span>$itemname_7
			</td>
		</tr>
		<tr>
			<th>class="size_8"</th>
			<td>
				横幅 <input type="text" name="size_8_w" value="${size_8_w}" id="size_8_w" class="num" onchange="dataadjust(this.id);" />　/　
				高さ <input type="text" name="size_8_h" value="${size_8_h}" id="size_8_h" class="num" onchange="dataadjust(this.id);" />　
				<span class="target">対象項目</span>$itemname_8
			</td>
		</tr>
		<tr>
			<th>class="size_9"</th>
			<td>
				横幅 <input type="text" name="size_9_w" value="${size_9_w}" id="size_9_w" class="num" onchange="dataadjust(this.id);" />　/　
				高さ <input type="text" name="size_9_h" value="${size_9_h}" id="size_9_h" class="num" onchange="dataadjust(this.id);" />　
				<span class="target">対象項目</span>$itemname_9
			</td>
		</tr>
		<tr>
			<th>class="size_10"</th>
			<td>
				横幅 <input type="text" name="size_10_w" value="${size_10_w}" id="size_10_w" class="num" onchange="dataadjust(this.id);" />　/　
				高さ <input type="text" name="size_10_h" value="${size_10_h}" id="size_10_h" class="num" onchange="dataadjust(this.id);" />　
				<span class="target">対象項目</span>$itemname_10
			</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td><input type="submit" name="submit" value="保存" /> <input type="button" name="submit" value="キャンセル" onclick="location.href='?m=$form{'m'}'" /></td>
		</tr>
	</table>
</form>
EOF

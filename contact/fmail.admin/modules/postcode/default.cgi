###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################
my $dir = './datas/postcode_temp/';
@files = ();
#opendir DH, $dir;
#while (my $file = readdir DH) {
#	next if $file =~ /^\.{1,2}$/;
#	unlink "${dir}${file}";
#}
#closedir DH;

$action_name = '郵便番号辞書の更新';
$print_html = <<"EOF";
<p>郵便番号辞書を更新します。</p>
<div id="update">
	郵便番号辞書を更新しました
</div>
<div id="updateerror">
	郵便番号辞書の形式が不正です
</div>
<p><a href="http://www.post.japanpost.jp/" target="_blank">日本郵便ホームページ</a>から更新したい差分データをダウンロードしてください。</p>
<p><a href="http://www.post.japanpost.jp/" target="_blank">日本郵便ホームページ</a>から更新する場合。（トップ > 郵便番号検索 > 郵便番号データダウンロード > <a href="http://www.post.japanpost.jp/zipcode/dl/kogaki-zip.html" target="_blank">読み仮名データの促音・拗音を小書きで表記するもの(zip形式)</a>　※ページ下部の差分データのダウンロード）</p>
<dl class="howto">
	<dt>CSV形式でアップロードする場合</dt>
	<dd>ダウンロードしたlzhファイルを解凍し、CSVファイルをアップロードします。<strong>DEL_</strong>から始まる廃止ファイルをアップロード後、<strong>ADD_</strong>から始まる追加ファイルをアップロードしてください。</dd>
</dl>
<dl class="howto">
	<dt>ZIP形式でアップロードする場合</dt>
	<dd>ダウンロードしたZipファイルをアップロードします。<strong>DEL_</strong>から始まる廃止ファイルをアップロード後、<strong>ADD_</strong>から始まる追加ファイルをアップロードしてください。zipファイルの中には複数の更新ファイルを含める事ができます。</dd>
</dl>

<form id="user_add" action="?m=$form{'m'}&a=save" method="POST" onSubmit="return checkUserEdit(this,'${submit}');" enctype="multipart/form-data">
	<table cellpadding="0" cellspacing="0" class="sheet">
		<tr>
			<th>更新ファイル</th>
			<td><input type="file" name="postcode_data" id="postcode_data" /></td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td><input type="submit" name="submit" value="更新" /></td>
		</tr>
	</table>
</form>
EOF

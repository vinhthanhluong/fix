$(document).ready(function() {
	$('input.fmail').blur(function() {
	var aaa = $(this).attr("name");
		// 階層定義
		var fmail_dir = './';
		// 値チェック
		if ($(this).val()) {
			var eleNM = $(this).attr('name');
		} else {
			var eleNM = '';
		}
		//POSTメソッドで送るデータを定義します var data = {パラメータ名 : 値};
		var data = {element : eleNM};
		
		$.ajax({
			type: "POST",
			url: fmail_dir + 'fmail.formlog.cgi',
			data: data,
			success: function(data, dataType) { /** Ajax通信が成功した場合に呼び出される */
				
			}
		});
	});
});

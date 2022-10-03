<!--
$(document).ready(function() {
	// 商品掲載ページから見た場合のFmailフォルダの位置を記載します。（設定箇所は一か所のみ）
	var fmail_dir = './contact/';
	
	
	base64dtext = 'WTJGeWRDOWpZWEowTG1Ga2JXbHVMMlJoZEdGekwyTmhjblF1YVhSbGJYTXY=';
	var work = fmail_dir + Base64.decode(Base64.decode(base64dtext)) + $.cookie("socket") + '.cgi';
	$("#cart_icon").load(work, null, function(responseText, status, XMLHttpRequest) {
		//alert("[ 通信完了！]\n" 
		//+ "--- responseText ---\n" + responseText + "\n"
		//+ "--- status ---\n" + status + "\n"
		//+ "--- XMLHttpRequest ---\n" + XMLHttpRequest
		//);
		if (responseText.match(/Error/i)) {
			//alert("Match");
			$('div#cart_icon a').prepend('<img src="' + fmail_dir + 'cart/images/cart_icon_in.jpg" alt="カートを確認">');
		} else {
			//alert("unMatch");
			$('div#cart_icon a').prepend('<img src="' + fmail_dir + 'cart/images/cart_icon_none.jpg" alt="カートを確認">');
		}
		
	});
	

	
		
	//$('div#cart_icon2 a').prepend('<img src="' + fmail_dir + 'cart/images/cart_icon_none.jpg" alt="カートを確認">');
	//$('div#cart_icon2 a').prepend('<img src="' + fmail_dir + 'cart/images/cart_icon_in.jpg" alt="カートを確認">');
	
	/** 送信ボタンクリック */
	$('.form_submit').click(function() {
		
		$(this).closest('form').find('.loading').show();
		
		//POSTメソッドで送るデータを定義します var data = {パラメータ名 : 値};
		var data = {pcode : $(this).closest('form').find('.pcode').val(), pname : $(this).closest('form').find('.pname').val(), pdetail1 : $(this).closest('form').find('.pdetail1').val(), pdetail2 : $(this).closest('form').find('.pdetail2').val(), pprice : $(this).closest('form').find('.pprice').val(), pnum : $(this).closest('form').find('.pnum').val(), pnum_hidden : $(this).closest('form').find('.pnum_hidden').val(), mode : $(this).closest('form').find('.mode').val()};
		/**
		 * Ajax通信メソッド
		 * @param type  : HTTP通信の種類
		 * @param url   : リクエスト送信先のURL
		 * @param data  : サーバに送信する値
		 */
		$.ajax({
			type: "POST",
			url: fmail_dir + 'cart/',
			data: data,
			success: function(data, dataType) { /** Ajax通信が成功した場合に呼び出される */
				$(".loading").fadeOut("slow");
			}
		});
		
		// カートに入ったので画像の切替
		$('div#cart_icon a').fadeIn(1500).html('<img src="' + fmail_dir + 'cart/images/cart_icon_in.jpg" alt="カートを確認">カートを確認');
	});
	
	/** 送信ボタンクリック-スマフォ */
	$('.form_submit_sp').click(function() {
		
		$(this).closest('form').find('.loading').show();
		
		//POSTメソッドで送るデータを定義します var data = {パラメータ名 : 値};
		var data = {pcode : $(this).closest('form').find('.pcode').val(), pname : $(this).closest('form').find('.pname').val(), pdetail1 : $(this).closest('form').find('.pdetail1').val(), pdetail2 : $(this).closest('form').find('.pdetail2').val(), pprice : $(this).closest('form').find('.pprice').val(), pnum : $(this).closest('form').find('.pnum').val(), pnum_hidden : $(this).closest('form').find('.pnum_hidden').val(), mode : $(this).closest('form').find('.mode').val()};
		/**
		 * Ajax通信メソッド
		 * @param type  : HTTP通信の種類
		 * @param url   : リクエスト送信先のURL
		 * @param data  : サーバに送信する値
		 */
		$.ajax({
			type: "POST",
			url: fmail_dir + 'cart/',
			data: data,
			success: function(data, dataType) { /** Ajax通信が成功した場合に呼び出される */
				$(".loading").fadeOut("slow");
			}
		});
		
		// カートに入ったので画像の切替
		$('div#cart_icon a').fadeIn(1500).html('<img src="' + fmail_dir + 'cart/images/cart_icon_in.jpg" alt="カートを確認">カートを確認');
	});
	
	/** サブミット後、ページをリロードしないようにする */
	$('form').submit(function() {
		return false;
	});
});
// -->

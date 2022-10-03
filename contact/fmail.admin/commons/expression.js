<!--
//メールアドレス正規化
function email_check(str_id) {
	var c = document.getElementById(str_id).value;
	
	//Unicodeでブラウザ毎の表記ゆれを無くす
	//メールアドレス形式
	var check_mail = /[\u0021-\u007E]+\u0040[\u0021-\u007E]+\.[\u0021-\u007E]+$/;
	
	//IDタグを使う場合あるので<0～9>の形式
	var check_tag = /<[\u0030-\u0039]+>+$/;
	
	if(!c.match(check_mail) && !c.match(check_tag) && c){
		alert("メールアドレスが正しくない可能性があります。");
	}
}
//-->
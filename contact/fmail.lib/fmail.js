<!--
	var ua = navigator.userAgent.toUpperCase();
	var kanaElementFocus = 1;
	var fkana,fname;
	var baseVal = "";
	var kanaFlag  = 1;
	var kanatimer = false;
	var example_color = "#999999";
	var enabled_color = "#000000";
	
	function fmail_sending(obj) {
		if(document.forms["fmail"]) {
			var formObj = document.forms["fmail"];
			for(i=0;i<formObj.length;i++) {
				if(exampleObj[formObj.elements[i].id] != undefined && formObj.elements[i].value == exampleObj[formObj.elements[i].id]) {
					formObj.elements[i].value = "";
				}
			}
		}
		// ローディング画像の表示時間
		jQuery(function($){
			twex_fullscreenObject();
			$("#twex").delay(1000).fadeOut();
			obj.submit();
		});

	}
	var hiddenObject = "";
	function selectedHidden(obj) {
		hiddenObject = obj
		for(i=0;i<obj.length;i++) {
			if(obj.elements[i].type == "select-multiple" || obj.elements[i].type == "select-one") {
				if(document.all) {
					obj.elements[i].style.visibility = "hidden";
				}
				else if(document.getElementById) {
					obj.elements[i].style.visibility = "hidden";
				}
			}
		}
	}
	function selectedVisible() {
		var obj = hiddenObject;
		for(i=0;i<obj.length;i++) {
			if(obj.elements[i].type == "select-multiple" || obj.elements[i].type == "select-one") {
				if(document.all) {
					obj.elements[i].style.visibility = "visible";
				}
				else if(document.getElementById) {
					obj.elements[i].style.visibility = "visible";
				}
			}
		}
	}
	var loading_image = '<img src="images/mfp_loading.gif" id="loading_proccess_image" width="40" height="40" />';
	var twex_body = document['CSS1Compat' == document.compatMode ? 'documentElement' : 'body'];
	var twex_flag = 1;
	
	if(document.getElementsByTagName('BODY').length == 0)
		document.write('<body>');
	var element = document.createElement('div');
	element.id = "twex";
	var objBody = document.getElementsByTagName("body").item(0);
	objBody.appendChild(element);
	document.getElementById('twex').innerHTML = loading_image;
	
	function twex_fullscreenObject() {
		twex_hideObject();
		twex_resize();
		if(document.all) {
			document.all('twex').style.display = "block";
		}
		else if(document.getElementById) {
			document.getElementById('twex').style.display = "block";
		}
	}
	function twex_resize() {
		var ua = navigator.userAgent;
		var nWidth, nHeight, nTop, nLeft;
		var nHit = ua.indexOf("MSIE");
		var bIE = (nHit >=  0);
		var bVer6 = (bIE && ua.substr(nHit+5, 1) == "6");
		var bStd = (document.compatMode && document.compatMode=="CSS1Compat");
		if (bIE) {
			if (bVer6 && bStd) {
				nWidth = document.documentElement.clientWidth;
				nHeight = document.documentElement.clientHeight;
				nTop = document.documentElement.scrollTop;
				nLeft = document.documentElement.scrollLeft;
			}
			else {
				if (typeof document.body.style.maxHeight != "undefined") {
					// IE7
					nWidth = document.documentElement.clientWidth;
					nHeight = document.documentElement.clientHeight;
					nTop = document.documentElement.scrollTop;
					nLeft = document.documentElement.scrollLeft;
				}
				else {
					nWidth = document.body.clientWidth;
					nHeight = document.body.clientHeight;
					nTop = document.body.scrollTop;
					nLeft = document.body.scrollLeft;
				}
			}
		}
		else {
			nWidth = window.innerWidth - 20;
			nHeight = window.innerHeight;
			nTop = document.body.scrollTop  || document.documentElement.scrollTop;
			nLeft = document.body.scrollLeft || document.documentElement.scrollLeft;
		}
		
		var lTop = (nHeight - 40) / 2;
		var lLeft = (nWidth - 40) / 2;
		
		if(document.getElementById('twex')) {
			document.getElementById('twex').style.width = nWidth + "px";
			document.getElementById('twex').style.height = nHeight + "px";
			document.getElementById('twex').style.top = nTop + "px";
			document.getElementById('twex').style.left = nLeft + "px";
			document.getElementById('loading_proccess_image').style.top = lTop + "px";
			document.getElementById('loading_proccess_image').style.left = lLeft + "px";
		}
	}
	function twex_closefullscreenObject() {
		if(document.getElementById('twex')) {
			document.getElementById('twex').style.visibility = "hidden";
			document.getElementById('twex').style.width = "1px";
			document.getElementById('twex').style.display = "none";
		}
		twex_showObject();
	}
	function twex_showObject() {
		var flashObjects = document.getElementsByTagName("object");
		for (i = 0; i < flashObjects.length; i++) {
			flashObjects[i].style.visibility = "visible";
		}
		var flashEmbeds = document.getElementsByTagName("embed");
		for (i = 0; i < flashEmbeds.length; i++) {
			flashEmbeds[i].style.visibility = "visible";
		}
		var flashSelect = document.getElementsByTagName("select");
		for (i = 0; i < flashSelect.length; i++) {
			flashSelect[i].style.visibility = "visible";
		}
	}
	function twex_hideObject() {
		var flashObjects = document.getElementsByTagName("object");
		for (i = 0; i < flashObjects.length; i++) {
			flashObjects[i].style.visibility = "hidden";
		}
		var flashEmbeds = document.getElementsByTagName("embed");
		for (i = 0; i < flashEmbeds.length; i++) {
			flashEmbeds[i].style.visibility = "hidden";
		}
		var flashSelect = document.getElementsByTagName("select");
		for (i = 0; i < flashSelect.length; i++) {
			flashSelect[i].style.visibility = "hidden";
		}
	}
	var focuselements;
	function fmailf(obj) {
		focuselements = obj;
		kanaElementFocus = 1;
		if(obj.value == exampleObj[obj.id]) {
			obj.value = "";
			obj.style.color = enabled_color;
		}
	}
	function fmailb(obj) {
		if(obj.value == "" && exampleObj[obj.id] != undefined) {
			obj.value = exampleObj[obj.id];
			obj.style.color = example_color;
		}
	}
	function kWatch(obj,kanaObjId) {
		document.forms["fmail"].elements[kanaObjId].style.color = enabled_color;
		if(document.forms["fmail"].elements[kanaObjId].value == exampleObj[kanaObjId]) {
			document.forms["fmail"].elements[kanaObjId].value = "";
		}
		if(ua.indexOf("FIREFOX") > -1 || ua.indexOf("OPERA") > -1) {
			clearTimeout(kanatimer);
			kanatimer = loopWatchTimer(obj.id,kanaObjId);
		}
	}
	function falsesubmit(obj) {
		var flag;
		var movefocus;
		for(i=0;i<obj.length;i++) {
			if(flag && obj.elements[i].type != "hidden") {
				movefocus = obj.elements[i];
				flag = 0;
			}
			if(obj.elements[i] == focuselements) {
				flag = 1;
			}
		}
		if(movefocus)
			movefocus.focus();
		return false;
	}
	
	// KANA
	// カタカナ＝1	ひらがな＝2
	var flag_kana = 1;
	
	var alphabet = new Array("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z");
	var kana = new Array(	"ア","イ","ウ","エ","オ",
				"カ","キ","ク","ケ","コ",
				"サ","シ","ス","セ","ソ",
				"タ","チ","ツ","テ","ト",
				"ナ","ニ","ヌ","ネ","ノ",
				"ハ","ヒ","フ","フ","ヘ",
				"マ","ミ","ム","メ","モ",
				"ヤ","ユ","ヨ",
				"ラ","リ","ル","レ","ロ",
				"ワ","ヰ","ヱ","ヲ",
				"ン",
				"イェ",
				"シ","チ","ツ",
				"ファ","フィ","フェ","フォ",
				"ァ","ィ","ゥ","ェ","ォ",
				"ヴァ","ヴィ","ヴ","ヴェ","ヴォ",
				"クァ","クィ","クェ","クォ",
				"ガ","ギ","グ","ゲ","ゴ",
				"ザ","ジ","ジ","ズ","ゼ","ゾ",
				"ダ","ヂ","ヅ","デ","ド",
				"ホ","バ","ビ","ブ","ベ","ボ",
				"パ","ピ","プ","ペ","ポ",
				"ジャ","ジュ","ジョ",
				"キャ","キュ","キョ",
				"ギャ","ギュ","ギョ",
				"シャ","シュ","ショ",
				"シャ","シュ","ショ",
				"ジャ","ジュ","ジョ",
				"チャ","チュ","チョ",
				"ヂャ","ヂュ","ヂョ",
				"チャ","チュ","チョ",
				"ニャ","ニュ","ニョ",
				"ヒャ","ヒュ","ヒョ",
				"ビャ","ビュ","ビョ",
				"ピャ","ピュ","ピョ",
				"ミャ","ミュ","ミョ",
				"リャ","リュ","リョ",
				"シェ","ジェ","シェ","ジェ",
				"チェ","チェ",
				"ツァ","ツェ","ツォ",
				"ティ","ディ","デュ",
				"ヵ","ヶ","ッ",
				"ャ","ュ","ョ","ヮ",
				"ウィ","ウィ","ウェ","ウェ","ウォ",
				"ヴュ","ツィ",
				"クァ","クィ","クェ","クォ","グァ",
				"ジャ","ジュ","ジョ",
				"チャ","チュ","チョ",
				"ティ","ディ","テュ",
				"トゥ","ドゥ",
				"ファ","フィ","フェ","フォ",
				"フュ","フュ",
				"ンb","ンc","ンd","ンf","ンg","ンh","ンj","ンk","ンl","ンm","ンp","ンq","ンr","ンs","ンt","ンv","ンw","ンx","ンz",
				"ッb","ッc","ッd","ッf","ッg","ッh","ッj","ッk","ッl","ッm","ッp","ッq","ッr","ッs","ッt","ッv","ッw","ッx","ッy","ッz");
	var hirakana = new Array(	"あ","い","う","え","お",
				"か","き","く","け","こ",
				"さ","し","す","せ","そ",
				"た","ち","つ","て","と",
				"な","に","ぬ","ね","の",
				"は","ひ","ふ","ふ","へ",
				"ま","み","む","め","も",
				"や","ゆ","よ",
				"ら","り","る","れ","ろ",
				"わ","ゐ","ゑ","を",
				"ん",
				"いぇ",
				"し","ち","つ",
				"ふぁ","ふぃ","ふぇ","ふぉ",
				"ぁ","ぃ","ぅ","ぇ","ぉ",
				"う゛ぁ","う゛ぃ","う゛","う゛ぇ","う゛ぉ",
				"くぁ","くぃ","くぇ","くぉ",
				"が","ぎ","ぐ","げ","ご",
				"ざ","じ","じ","ず","ぜ","ぞ",
				"だ","ぢ","づ","で","ど",
				"ほ","ば","び","ぶ","べ","ぼ",
				"ぱ","ぴ","ぷ","ぺ","ぽ",
				"じゃ","じゅ","じょ",
				"きゃ","きゅ","きょ",
				"ぎゃ","ぎゅ","ぎょ",
				"しゃ","しゅ","しょ",
				"しゃ","しゅ","しょ",
				"じゃ","じゅ","じょ",
				"ちゃ","ちゅ","ちょ",
				"ぢゃ","ぢゅ","ぢょ",
				"ちゃ","ちゅ","ちょ",
				"にゃ","にゅ","にょ",
				"ひゃ","ひゅ","ひょ",
				"びゃ","びゅ","びょ",
				"ぴゃ","ぴゅ","ぴょ",
				"みゃ","みゅ","みょ",
				"りゃ","りゅ","りょ",
				"しぇ","じぇ","しぇ","じぇ",
				"ちぇ","ちぇ",
				"つぁ","つぇ","つぉ",
				"てぃ","でぃ","でゅ",
				"ヵ","ヶ","っ",
				"ゃ","ゅ","ょ","ゎ",
				"うぃ","うぃ","うぇ","うぇ","うぉ",
				"う゛ゅ","つぃ",
				"くぁ","くぃ","くぇ","くぉ","ぐぁ",
				"じゃ","じゅ","じょ",
				"ちゃ","ちゅ","ちょ",
				"てぃ","でぃ","てゅ",
				"とぅ","どぅ",
				"ふぁ","ふぃ","ふぇ","ふぉ",
				"ふゅ","ふゅ",
				"んb","んc","んd","んf","んg","んh","んj","んk","んl","んm","んp","んq","んr","んs","んt","んv","んw","んx","んz",
				"っb","っc","っd","っf","っg","っh","っj","っk","っl","っm","っp","っq","っr","っs","っt","っv","っw","っx","っy","っz");
	var roma = new Array(	"a","i","u","e","o",
				"ka","ki","ku","ke","ko",
				"sa","si","su","se","so",
				"ta","ti","tu","te","to",
				"na","ni","nu","ne","no",
				"ha","hi","hu","fu","he",
				"ma","mi","mu","me","mo",
				"ya","yu","yo",
				"ra","ri","ru","re","ro",
				"wa","wyi","wye","wo",
				"nn",
				"ye",
				"shi","chi","tsu",
				"fa","fi","fe","fo",
				"xa","xi","xu","xe","xo",
				"va","vi","vu","ve","vo",
				"qa","qi","qe","qo",
				"ga","gi","gu","ge","go",
				"za","zi","ji","zu","ze","zo",
				"da","di","du","de","do",
				"ho","ba","bi","bu","be","bo",
				"pa","pi","pu","pe","po",
				"ja","ju","jo",
				"kya","kyu","kyo",
				"gya","gyu","gyo",
				"sya","syu","syo",
				"sha","shu","sho",
				"zya","zyu","zyo",
				"tya","tyu","tyo",
				"dya","dyu","dyo",
				"cha","chu","cho",
				"nya","nyu","nyo",
				"hya","hyu","hyo",
				"bya","byu","byo",
				"pya","pyu","pyo",
				"mya","myu","myo",
				"rya","ryu","ryo",
				"sye","she","zye","je",
				"tye","che",
				"tsa","tse","tso",
				"thi","dhi","dhu",
				"xka","xke","xtu",
				"xya","xyu","xyo","xwa",
				"whi","wi","whe","we","who",
				"vyu","tsi",
				"kwa","kwi","kwe","kwo","gwa",
				"jya","jyu","jyo",
				"cya","cyu","cyo",
				"thi","dhi","thu",
				"twu","dwu",
				"hwa","hwi","hwe","hwo",
				"fyu","hwyu",
				"nb","nc","nd","nf","ng","nh","nj","nk","nl","nm","np","nq","nr","ns","nt","nv","nw","nx","nz",
				"bb","cc","dd","ff","gg","hh","jj","kk","ll","mm","pp","qq","rr","ss","tt","vv","ww","xx","yy","zz");
	
	// カタカナとひらがなの判別
	if(flag_kana == 2) {
		kana = hirakana;
	}
	
	// Firefoxとオペラ以外の挙動
	function Fkana(formObj,thisObj,kanaObjId,keyCode) {
		if(ua.indexOf("FIREFOX") == -1 && ua.indexOf("OPERA") == -1) {
			var kanaObj = formObj.elements[kanaObjId];
			if(thisObj.value == "")
				kanaObj.value = "";
			if(keyCode > 64 && keyCode < 91) {
				kanaObj.value = kanaObj.value + alphabet[keyCode - 65];
				for(i=roma.length;i > -1;i--) {
					kanaObj.value = kanaObj.value.replace(roma[i],kana[i]);
				}
			}
			else if(keyCode == 8) {
				if(thisObj.value.length <= kanaObj.value.length) {
					kanaObj.value = kanaObj.value.substring(0,kanaObj.value.length - 1);
				}
			}
			else if(keyCode == 45) {
				kanaObj.value = kanaObj.value + "-";
				for(i=roma.length;i > -1;i--) {
					kanaObj.value = kanaObj.value.replace(roma[i],kana[i]);
				}
			}
			else if(keyCode == 109 || keyCode == 189) {
				kanaObj.value = kanaObj.value + "-";
				for(i=roma.length;i > -1;i--) {
					kanaObj.value = kanaObj.value.replace(roma[i],kana[i]);
				}
			}
			var nbsp = thisObj.value.substring(thisObj.value.length - 1,thisObj.value.length);
			if(nbsp == " " || nbsp == "　") {
				kanaObj.value += " ";
				kanaObj.value = kanaObj.value.replace("  "," ");
			}
			return false;
		}
	}
	function loopWatchTimer(fname,fkana) {
		setKANA(fname,fkana);
		kanatimer = setTimeout("loopWatchTimer('"+fname+"','"+fkana+"')",30);
	}
	
	// Firefoxとオペラの挙動
	function setKANA(nameId,kanaId) {
		var d = document;
		var newVal = d.getElementById(nameId).value;
		if(baseVal == newVal)
			return;
		if(newVal == "") {
			d.getElementById(kanaId).value="";
			baseVal = "";
			return;
		}
		var addVal = newVal;
		for(var i=baseVal.length;i>=0;i--) {
			if (newVal.substr(0,i) == baseVal.substr(0,i)) {
				addVal = newVal.substr(i);break;
			}
		}
		baseVal = newVal;
		var addruby = addVal.replace(/[^ 　ぁあ-んァーア-ン]/g, "");
		if(addruby == "")
			return;
		addruby = exchangeKana(addruby);
		d.getElementById(kanaId).value += addruby;
	}
	function exchangeKana(val) {
		var txt,arr = [];
		for(i=0;i<val.length;i++) {
			txt = val.charCodeAt(i);
			// カタカナとひらがなの判別
			if(flag_kana == 1) {
				// カタカナに変換
				arr[i] = (0x3041 <= txt && txt <= 0x3096) ? txt + 0x0060 : txt;
			}else {
				// ひらがなに変換
				arr[i] = (0x30A1 <= txt && txt <= 0x30F6) ? txt - 0x0060 : txt;
			}
		}
		return String.fromCharCode.apply(null,arr);
	}
	
	// ラベル関連
	function labelclick() {
		if(document.forms["fmail"]) {
			var obj = document.forms["fmail"];
			for(i=0;i<obj.length;i++) {
				if(obj.elements[i].type == "radio" || obj.elements[i].type == "checkbox") {
					var id = obj.elements[i].id + "_label";
					if(obj.elements[i].checked) {
						// true
						if(document.getElementById(id))
							document.getElementById(id).className = "fmail_label_enabled";
					}
					else {
						// false
						if(document.getElementById(id))
							document.getElementById(id).className = "fmail_label_disabled";
					}
				}
			}
		}
	}
	
	//prototype.jsとのコンフリクト回避
	//----------------------------
	//(function($) {
	//	//処理
	//})(jQuery);
	//----------------------------
	//を記述
	(function($) {
		function startupFmail() {
			if(document.forms["fmail"]) {
				var formObj = document.forms["fmail"];
				$("input.fmail").focus(function() {
					fmailf(this);
				});
				$("textarea.fmail").focus(function() {
					fmailf(this);
				});
				$("input.fmail").blur(function() {
					fmailb(this);
				});
				$("textarea.fmail").blur(function() {
					fmailb(this);
				});
				$("select.fmail").focus(function() {
					fmailf(this);
				});
				$("input.fmail").click(function() {
					labelclick();
				});
				$("label.fmail").click(function() {
					labelclick();
				});
				
				
				// 初期フォーカス
				//document.getElementById("fmail").elements[0].focus();
				
				for(i=0;i<formObj.length;i++) {
					if(exampleObj[formObj.elements[i].id] != undefined && formObj.elements[i].value == "") {
						formObj.elements[i].value = exampleObj[formObj.elements[i].id];
						formObj.elements[i].style.color = example_color;
					}
				}
				if(elementsetObj) {
					for(i=0;i<elementsetObj.length;i++) {
						if(elementsetObj[i] != undefined && document.getElementById(elementsetObj[i])) {
							if(document.getElementById(elementsetObj[i]).type == "select-one") {
								if(postvalueObj[elementsetObj[i]] != undefined)
									document.getElementById(elementsetObj[i]).value = postvalueObj[elementsetObj[i]];
							}
							else if(document.getElementById(elementsetObj[i]).type == "radio" || document.getElementById(elementsetObj[i]).type == "checkbox") {
								if(postvalueObj[elementsetObj[i]] == document.getElementById(elementsetObj[i]).value)
									document.getElementById(elementsetObj[i]).checked = true;
							}
						}
					}
				}
				labelclick();
			}
		}
		$(document).ready(startupFmail);
	})(jQuery);
	
	// 添付ファイルのキャンセル
	function del(str_id) {
		var nHit1 = ua.indexOf("MSIE");
		var nHit2 = ua.indexOf("OPERA");
		
		if((nHit1 == -1) && (nHit2 == -1)){
			// IE・OPERA以外
			document.getElementById(str_id).value = "";
		}else{
			// IE・OPERA
			document.getElementById(str_id).outerHTML = document.getElementById(str_id).outerHTML;
		}
	}
	
	
	// メールアドレスの半角化
	function mailadjust(str_id) {
		var single_char = new Array('0','1','2','3','4','5','6','7','8','9','-','-','-','-','-','-','-','@','.',',',':','_',
																'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
																'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z');
		var double_char = new Array('０','１','２','３','４','５','６','７','８','９','－','-', '－', 'ー', '―', 'ｰ', '‐','＠','．','，','：','＿',
																'ａ','ｂ','ｃ','ｄ','ｅ','ｆ','ｇ','ｈ','ｉ','ｊ','ｋ','ｌ','ｍ','ｎ','ｏ','ｐ','ｑ','ｒ','ｓ','ｔ','ｕ','ｖ','ｗ','ｘ','ｙ','ｚ',
																'Ａ','Ｂ','Ｃ','Ｄ','Ｅ','Ｆ','Ｇ','Ｈ','Ｉ','Ｊ','Ｋ','Ｌ','Ｍ','Ｎ','Ｏ','Ｐ','Ｑ','Ｒ','Ｓ','Ｔ','Ｕ','Ｖ','Ｗ','Ｘ','Ｙ','Ｚ');
		var ptn = '';
		
		// 半角化
		for(i=0;i<single_char.length;i++) {
			var temp = new Array();
			temp = document.getElementById(str_id).value.split(double_char[i]);
			document.getElementById(str_id).value = temp.join(single_char[i]);
		}
		ptn = document.getElementById(str_id).value;
		
		// 不要テキスト抹消
		var dummy = '';
		work = ptn.replace(/[^0-9|a-z|A-Z|\-|@|\.|,|:|_]+/g,"");
		
		// 値を返す
		document.getElementById(str_id).value = work;
	}
	
	
	// 住所の全角化
	function addradjust(str_id) {
		var single_char = new Array('0','1','2','3','4','5','6','7','8','9','-','ｰ','@','.',',',':','+','*','/',
																'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
																'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
																'ｧ','ｨ','ｩ','ｪ','ｫ',
																'ｯ',
																'ｬ','ｭ','ｮ',
																'ｳﾞ',
																'ｶﾞ','ｷﾞ','ｸﾞ','ｹﾞ','ｺﾞ',
																'ｻﾞ','ｼﾞ','ｽﾞ','ｾﾞ','ｿﾞ',
																'ﾀﾞ','ﾁﾞ','ﾂﾞ','ﾃﾞ','ﾄﾞ',
																'ﾊﾞ','ﾋﾞ','ﾌﾞ','ﾍﾞ','ﾎﾞ',
																'ﾊﾟ','ﾋﾟ','ﾌﾟ','ﾍﾟ','ﾎﾟ',
																'ｱ','ｲ','ｳ','ｴ','ｵ',
																'ｶ','ｷ','ｸ','ｹ','ｺ',
																'ｻ','ｼ','ｽ','ｾ','ｿ',
																'ﾀ','ﾁ','ﾂ','ﾃ','ﾄ',
																'ﾅ','ﾆ','ﾇ','ﾈ','ﾉ',
																'ﾊ','ﾋ','ﾌ','ﾌ','ﾍ',
																'ﾏ','ﾐ','ﾑ','ﾒ','ﾓ',
																'ﾔ','ﾕ','ﾖ',
																'ﾗ','ﾘ','ﾙ','ﾚ','ﾛ',
																'ﾜ','ｦ','ﾝ','ﾟ');
		var double_char = new Array('０','１','２','３','４','５','６','７','８','９','－','ー','＠','．','，','：','＋','＊','／',
																'ａ','ｂ','ｃ','ｄ','ｅ','ｆ','ｇ','ｈ','ｉ','ｊ','ｋ','ｌ','ｍ','ｎ','ｏ','ｐ','ｑ','ｒ','ｓ','ｔ','ｕ','ｖ','ｗ','ｘ','ｙ','ｚ',
																'Ａ','Ｂ','Ｃ','Ｄ','Ｅ','Ｆ','Ｇ','Ｈ','Ｉ','Ｊ','Ｋ','Ｌ','Ｍ','Ｎ','Ｏ','Ｐ','Ｑ','Ｒ','Ｓ','Ｔ','Ｕ','Ｖ','Ｗ','Ｘ','Ｙ','Ｚ',
																'ァ','ィ','ゥ','ェ','ォ',
																'ッ',
																'ャ','ュ','ョ',
																'ヴ',
																'ガ','ギ','グ','ゲ','ゴ',
																'ザ','ジ','ズ','ゼ','ゾ',
																'ダ','ヂ','ヅ','デ','ド',
																'バ','ビ','ブ','ベ','ボ',
																'パ','ピ','プ','ペ','ポ',
																'ア','イ','ウ','エ','オ',
																'カ','キ','ク','ケ','コ',
																'サ','シ','ス','セ','ソ',
																'タ','チ','ツ','テ','ト',
																'ナ','ニ','ヌ','ネ','ノ',
																'ハ','ヒ','フ','フ','ヘ',
																'マ','ミ','ム','メ','モ',
																'ヤ','ユ','ヨ',
																'ラ','リ','ル','レ','ロ',
																'ワ','ヲ','ン','゜');
		var ptn = '';
		
		// 半角化
		for(i=0;i<double_char.length;i++) {
			var temp = new Array();
			temp = document.getElementById(str_id).value.split(single_char[i]);
			document.getElementById(str_id).value = temp.join(double_char[i]);
		}
		ptn = document.getElementById(str_id).value;
		
		// 値を返す
		document.getElementById(str_id).value = ptn;
	}
	
	
	
	// カナの全角化
	function hankana2zenkana(str_id) {
		var single_char = new Array(' ','-','ｰ','.',
																'ｧ','ｨ','ｩ','ｪ','ｫ',
																'ｯ',
																'ｬ','ｭ','ｮ',
																'ｳﾞ',
																'ｶﾞ','ｷﾞ','ｸﾞ','ｹﾞ','ｺﾞ',
																'ｻﾞ','ｼﾞ','ｽﾞ','ｾﾞ','ｿﾞ',
																'ﾀﾞ','ﾁﾞ','ﾂﾞ','ﾃﾞ','ﾄﾞ',
																'ﾊﾞ','ﾋﾞ','ﾌﾞ','ﾍﾞ','ﾎﾞ',
																'ﾊﾟ','ﾋﾟ','ﾌﾟ','ﾍﾟ','ﾎﾟ',
																'ｱ','ｲ','ｳ','ｴ','ｵ',
																'ｶ','ｷ','ｸ','ｹ','ｺ',
																'ｻ','ｼ','ｽ','ｾ','ｿ',
																'ﾀ','ﾁ','ﾂ','ﾃ','ﾄ',
																'ﾅ','ﾆ','ﾇ','ﾈ','ﾉ',
																'ﾊ','ﾋ','ﾌ','ﾌ','ﾍ',
																'ﾏ','ﾐ','ﾑ','ﾒ','ﾓ',
																'ﾔ','ﾕ','ﾖ',
																'ﾗ','ﾘ','ﾙ','ﾚ','ﾛ',
																'ﾜ','ｦ','ﾝ','ﾟ');
		var double_char = new Array('　','－','ー','．',
																'ァ','ィ','ゥ','ェ','ォ',
																'ッ',
																'ャ','ュ','ョ',
																'ヴ',
																'ガ','ギ','グ','ゲ','ゴ',
																'ザ','ジ','ズ','ゼ','ゾ',
																'ダ','ヂ','ヅ','デ','ド',
																'バ','ビ','ブ','ベ','ボ',
																'パ','ピ','プ','ペ','ポ',
																'ア','イ','ウ','エ','オ',
																'カ','キ','ク','ケ','コ',
																'サ','シ','ス','セ','ソ',
																'タ','チ','ツ','テ','ト',
																'ナ','ニ','ヌ','ネ','ノ',
																'ハ','ヒ','フ','フ','ヘ',
																'マ','ミ','ム','メ','モ',
																'ヤ','ユ','ヨ',
																'ラ','リ','ル','レ','ロ',
																'ワ','ヲ','ン','゜');
		var ptn = '';
		
		// 半角化
		for(i=0;i<double_char.length;i++) {
			var temp = new Array();
			temp = document.getElementById(str_id).value.split(single_char[i]);
			document.getElementById(str_id).value = temp.join(double_char[i]);
		}
		ptn = document.getElementById(str_id).value;
		
		//カタカナ以外の抹消
		var ptn = new String(ptn).replace(/[^ァ-ヶ|ー|－|　]/g, "");
		
		// 値を返す
		document.getElementById(str_id).value = ptn;
	}
	
	
	
	// 数字の半角化
	function numadjust(str_id) {
		var single_char = new Array('0','1','2','3','4','5','6','7','8','9','-',"-","-","-","-","-","-","+",".",",");
		var double_char = new Array('０','１','２','３','４','５','６','７','８','９','－',"-","－","ー","―","ｰ","‐","＋","．","，");
		var ptn = '';
		
		// 半角化
		for(i=0;i<single_char.length;i++) {
			var temp = new Array();
			temp = document.getElementById(str_id).value.split(double_char[i]);
			document.getElementById(str_id).value = temp.join(single_char[i]);
		}
		ptn = document.getElementById(str_id).value;
		
		// 不要テキスト抹消
		var dummy = '';
		work = ptn.replace(/[^0-9|\-|\+|.|,]+/g,"");
		
		// 値を返す
		document.getElementById(str_id).value = work;
	}
	
	
	// 桁区切り
	function delimit(str_id) {
		this.numadjust(str_id);
		var yen = document.getElementById(str_id).value;
		var num = new String(yen).replace(/[^0-9|\-|.]/g, "");
		while(num != (num = num.replace(/^(-?\d+)(\d{3})/, "$1,$2")));
		document.getElementById(str_id).value = num;
	}
	
	
	jQuery(function($){
		// 必須項目のチェック
		must_item_checker();
		
		// 必須チェック
		$("input,select,textarea").on("click check keydown change", function(){
			must_item_checker(); // 必須項目残り数の更新
			
			// 必須即時チェック
			str = $(this).attr("class");
			if (str.match(/fmail/i) && str.match(/must/i) && !$(this).val()) {
				// 必須即時エラー表示
				$(this).parent("td, dd").addClass("fmail_error_line");
				$(this).parent("td, dd").prev("th, dt").addClass("fmail_error_line");
				// スペーサー等のネスト対応
				$(this).parent().parent("td, dd").addClass("fmail_error_line");
				$(this).parent().parent("td, dd").prev("th, dt").addClass("fmail_error_line");
				if ( $(this).next('span').attr('class') != 'fmail_error' ) {
					if ($(this).parent('td, dd').parent('tr, dl').attr('class') == 'zipcode size_1') {
						$(this).after('<span class="fmail_error" style="position: absolute; display: inline-block; margin-left: 80px;">未入力です。</span>');
					} else {
						$(this).after('<span class="fmail_error" style="display: inline-block; margin-top: 5px;">未入力です。</span>');
					}
				}
			} else if ($(this).attr("class") == 'postcode') {
				// 処理をスルーする
			} else {
				// 入力されたので解除
				$(this).parent("td, dd").removeClass("fmail_error_line");
				$(this).parent("td, dd").prev("th, dt").removeClass("fmail_error_line");
				// スペーサー等のネスト対応
				$(this).parent().parent("td, dd").removeClass("fmail_error_line");
				$(this).parent().parent("td, dd").prev("th, dt").removeClass("fmail_error_line");
				if ( $(this).next('span').attr('class') == 'fmail_error' ) {
					$(this).next('span').remove();
				}
			}
		});
		
		// 必須チェック（チェックボックス用）
		$("input:checkbox").on("change", function(){
			must_item_checker(); // 必須項目残り数の更新
			
			// 必須即時チェック
			str = $(this).attr("class");
			if (str.match(/fmail/i) && str.match(/must/i) && $(this).attr("type") == 'checkbox') {
				var checkbox_nm = $(this).attr("name");
				var flag_checkbox=[];
				$('[name="' + checkbox_nm + '"]:checked').each(function(){
					flag_checkbox.push($(this).val());
				});
				if (flag_checkbox.length) {
					// 入力されたので解除
					$(this).parent().parent().parent().parent("td, dd").removeClass("fmail_error_line");
					$(this).parent().parent().parent().parent("td, dd").prev("th, dt").removeClass("fmail_error_line");
					$(this).parent().parent().parent().next('span').remove();
				} else {
					// 必須即時エラー表示
					$(this).parent().parent().parent().parent("td, dd").addClass("fmail_error_line");
					$(this).parent().parent().parent().parent("td, dd").prev("th, dt").addClass("fmail_error_line");
					$(this).parent().parent().parent().after('<span class="fmail_error" style="display: inline-block; margin-top: 5px;">未入力です。</span>');
				}
			}
		});
		
		// 必須項目残り数の更新
		function must_item_checker() {
			var must_num = 0;
			var must_num_ckbox = 0;
			var work = '';
			// 添付ファイルのみclass割り当てが違うので、「,」をつけてor条件判断
			$(".fmail.must, .fmail_file.must").each( function() {
				// チェックボックス分カウント
				if ($(this).attr("type") == 'checkbox' || $(this).attr("type") == 'radio') {
					var checkbox_nm = $(this).attr("name");
					var flag_checkbox=[];
					$('[name="' + checkbox_nm + '"]:checked').each(function(){
						flag_checkbox.push($(this).val());
					});
					if (flag_checkbox.length == 0) {
						if( work == checkbox_nm ){
						} else {
							work = checkbox_nm;
							must_num_ckbox ++;
						}
					}
				} else if ($(this).attr("type") == 'file' && this.files[0] == null) {
					// ファイル添付有無
					must_num ++;
				} else if (!$(this).val()) {
					// 他カウント
					must_num ++;
				} else if($(this).css("color") == 'rgb(153, 153, 153)') {
					must_num ++;
				} else {
					// 入力されたので解除
					$(this).parent("td, dd").removeClass("fmail_error_line");
					$(this).parent("td, dd").prev("th, dt").removeClass("fmail_error_line");
				}
			});
			
			must_num += must_num_ckbox;
			
			$(".caution_mustchecker").text(must_num);
		}
		
		
		
		
		
		
//		// ページ移動前アラート
//		
//		// URLを取得して「?]で分割「&」でも分割
//		var url = location.href;
//		params = url.split("?");
//		
//		// パラメータがついている場合のみ処理
//		if (params[1]) {
//			paramms = params[1].split("&");
//		}
//		
//		$(window).on('beforeunload', function() {
//			// パラメータ用の配列を用意
//			var paramArray = [];
//			
//			// パラメータがついている場合のみ処理
//			if(params[1]){
//				// 配列にパラメータを格納
//				for ( i = 0; i < paramms.length; i++ ) {
//					neet = paramms[i].split("=");
//					paramArray.push(neet[0]);
//					paramArray[neet[0]] = neet[1];
//				}
//			}
//			
//			// 入力画面のみ必須未入力時に表示
//			if ( paramArray["mode"] != "confirm" && paramArray["mode"] != "thanks") {
//				// 1以上の場合、アラート
//				if ($(".caution_mustchecker").text() > 0) {
//					return 'お問い合わせが完了していません。';
//				}
//			}
//		});
		
		// 郵便番号記号とスペーサー
		if (($(".zipcode input[type=text]").val() && $(".zipcode input[type=text]").val() != '例）123-4567') || ($(".zipcode input[type=tel]").val() && $(".zipcode input[type=tel]").val() != '例）123-4567')) {
			$("input.zipcode_item").val('');
			$("input.zipcode_spacer").val('');
		} else {
			$("input.zipcode_item").val('');
			$("input.zipcode_spacer").val('');
		}
		
		// 郵便番号記号とスペーサー
		$(".zipcode input[type=text], .zipcode input[type=tel]").change(function(){
			if (($(".zipcode input[type=text]").val() && $(".zipcode input[type=text]").val() != '例）123-4567') || ($(".zipcode input[type=tel]").val() && $(".zipcode input[type=tel]").val() != '例）123-4567')) {
				$("input.zipcode_item").val('');
				$("input.zipcode_spacer").val('');
			} else {
				$("input.zipcode_item").val('');
				$("input.zipcode_spacer").val('');
			}
		});
		
		
		// マンション名等スペーサー
		if ($(".subaddr input:text").val()) {
			$("input.subaddr_spacer").val('');
		} else {
			$("input.subaddr_spacer").val('');
		}
		
		// マンション名等スペーサー
		$(".subaddr input:text").change(function(){
			if ($(".subaddr input:text").val()) {
				$("input.subaddr_spacer").val('');
			} else {
				$("input.subaddr_spacer").val('');
			}
		});
		
		// スペーサー枠でエラーを枠ごと配色する場合
		$(".fmail_error").parent("td, dd").addClass("fmail_error_line");
		$(".fmail_error_line").prev("th, dt").addClass("fmail_error_line");
		
		
		// スマホエレメント変更
		sp_ele();
		
		// ウィンドウサイズ変更時
		$(window).resize(function() {
			// スマホエレメント変更
			sp_ele();
		});
		
		// スマホエレメント変換
		function sp_ele() {
			if( $(window).width() <= 768) {
				$("input.smaph_tel").attr("type","tel");
				$("input.smaph_email").attr("type","email");
				$("input.smaph_number").attr("type","number");
				$("input.smaph_url").attr("type","url");
			} else {
				$("input.smaph_tel").attr("type","text");
				$("input.smaph_email").attr("type","text");
				$("input.smaph_number").attr("type","text");
				$("input.smaph_url").attr("type","text");
			}
		}
		
	});
	
//-->
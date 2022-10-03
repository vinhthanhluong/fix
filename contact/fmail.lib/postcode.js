<!--
	// 郵便番号から住所を求めるjs
	
	//以下がフォームのHTMLから見たCGIまでのパス
	var getpostcode_cgi = "fmail.postcode.cgi?";
	
	var postcode_form_Id = "";
	var postcode_ELM = "";
	var feedback_govm = "";
	var feedback_city = "";
	var feedback_town = "";
	function postcode_getQuery(){
		if ((httpObj.readyState == 4) && (httpObj.status == 200)) {
			var obj = document.forms[postcode_form_Id];
			var getAddress = decodeURI(httpObj.responseText);
			var getAddressGroup = new Array();
			getAddressGroup = getAddress.split(",");
			if(getAddressGroup.length == 3){
				//都道府県 getAddressGroup[0];
				//市区町村 getAddressGroup[1];
				//丁目番地 getAddressGroup[2];
				obj.elements[feedback_govm].value = getAddressGroup[0];
				obj.elements[feedback_city].value = getAddressGroup[1] + getAddressGroup[2];
				//市区町村と丁目番地を合成した都合で下記コメントアウト
				//obj.elements[feedback_city].value = getAddressGroup[1];
				//obj.elements[feedback_town].value = getAddressGroup[2];
				obj.elements[feedback_govm].style.color = enabled_color;
				obj.elements[feedback_city].style.color = enabled_color;
				//obj.elements[feedback_town].style.color = enabled_color;
			}
		}
	}
	
	//市区町村と丁目番地を合成した都合で下記コメントアウト
	//function mfpc(formId,postcodeELM,fb_govm,fb_city,fb_town){
	function mfpc(formId,postcodeELM,fb_govm,fb_city){
		var obj = document.forms[formId];
		postcode_form_Id = formId;
		postcode_ELM = postcodeELM;
		feedback_govm = fb_govm;
		feedback_city = fb_city;
		//feedback_town = fb_town;
		var border = new Array("-", "－", "ー", "―", "ｰ", "‐");
		var postcode = obj.elements[postcodeELM].value;
		var single_char = new Array('0','1','2','3','4','5','6','7','8','9','-',"-","-","-","-","-","-");
		var double_char = new Array('０','１','２','３','４','５','６','７','８','９','－',"-", "－", "ー", "―", "ｰ", "‐");
		for(i=0;i<single_char.length;i++){
			var temp = new Array();
			temp = obj.elements[postcodeELM].value.split(double_char[i]);
			obj.elements[postcodeELM].value = temp.join(single_char[i]);
		}
		var postdata = obj.elements[postcodeELM].value;
		for(var i = 0; i < border.length; i++){
			var temp = new Array();
			temp = postdata.split(border[i]);
			postdata = temp.join("");
		}
		if(postdata != ""){
			httpObj = createXMLHttpRequest();
			httpObj.onreadystatechange = postcode_getQuery;
			httpObj.open("GET",getpostcode_cgi+encodeURI(postdata),true);
			httpObj.send(null);
		}
		return false;
	}
	function createXMLHttp() {
		try {
			return new ActiveXObject ("Microsoft.XMLHTTP");
		}catch(e){
			try {
				return new XMLHttpRequest();
			}catch(e) {
				return null;
			}
		}
		return null;
	}
	function createXMLHttpRequest(){
		var XMLhttpObject = null;
		try{
			XMLhttpObject = new XMLHttpRequest();
		}
		catch(e){
			try{
				XMLhttpObject = new ActiveXObject("Msxml2.XMLHTTP");
			}
			catch(e){
				try{
					XMLhttpObject = new ActiveXObject("Microsoft.XMLHTTP");
				}
				catch(e){
					return null;
				}
			}
		}
		return XMLhttpObject;
	}
	
	//郵便番号正規化
	function zipadjust(str_id){
		var single_char = new Array('0','1','2','3','4','5','6','7','8','9','-',"-","-","-","-","-","-");
		var double_char = new Array('０','１','２','３','４','５','６','７','８','９','－',"-", "－", "ー", "―", "ｰ", "‐");
		var ptn = '';
		
		//半角化
		for(i=0;i<single_char.length;i++){
			var temp = new Array();
			temp = document.getElementById(str_id).value.split(double_char[i]);
			document.getElementById(str_id).value = temp.join(single_char[i]);
		}
		ptn = document.getElementById(str_id).value;
		
		//不要テキスト抹消
		var dummy = '';
		dummy = ptn.replace(/[^0-9]+/g,"");
		
		//ハイフンを代入
		var work = '';
		for(i=0;i<dummy.length;i++){
			if(i == 2){
				work += dummy.substr(i,1) + '-';
			}else{
				work += dummy.substr(i,1);
			}
		}
		
		
		document.getElementById(str_id).value = work;
	}
//-->
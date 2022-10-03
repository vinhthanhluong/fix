<!--
	var qtm_posObj = new Object();
	function checkUserEdit(obj,msg){
		var errorMSG = "";
		if(obj.elements["postcode_data"].value == ""){
			errorMSG = "更新ファイルが選択されていません";
		}
		else {
			var mfp_fileTypes = new Array();
			mfp_fileTypes = obj.elements["postcode_data"].value.split(".");
			var mfp_fileType = mfp_fileTypes[mfp_fileTypes.length - 1].toLowerCase();
			if(mfp_fileType != "csv" && mfp_fileType != "zip"){
				errorMSG = "ファイルはCSV形式またはZIP形式のファイルしか選択できません";
			}
		}
		
		if(errorMSG == ""){
			if(confirm("更新してもよろしいですか？")){
				twex_fullscreenObject();
				return true;
			}
			else
				return false;
		}
		else{
			alert(errorMSG);
			return false;
		}
	}
	function statdisp(){
		if(appObject['querys']["stat"] != undefined){
			if(document.getElementById(appObject['querys']["stat"])){
				document.getElementById(appObject['querys']["stat"]).style.display = "block";
				document.getElementById(appObject['querys']["stat"]).innerHTML = "";
				if(appObject['querys']["statmsg"] != undefined && appObject['querys']["statmsg"] != ""){
					document.getElementById(appObject['querys']["stat"]).innerHTML = decodeURI(appObject['querys']["statmsg"]);
				}
				if(document.getElementById(appObject['querys']["stat"]).innerHTML != ""){
					document.getElementById(appObject['querys']["stat"]).innerHTML += "<br />";
				}
				if(appObject['querys']["error"] != undefined && appObject['querys']["error"] != ""){
					document.getElementById(appObject['querys']["stat"]).innerHTML += decodeURI(appObject['querys']["error"]);
				}
			}
		}
	}
	function add_element_value() {
		objId = 'body';
		qtm_pos(objId);
		var obj = document.getElementById(objId);
		qtm_posObj.end = qtm_posObj.start;
		qtm_posObj.body = "<" + document.getElementById('add_elements_value_list').value + ">";
		qtm_feedback(obj);
	}
	function qtm_feedback(obj){
		qtm_posObj.first = obj.value.substring(0,qtm_posObj.start);
		qtm_posObj.last = obj.value.substring(qtm_posObj.end,obj.value.length);
		obj.value = qtm_posObj.first + qtm_posObj.body + qtm_posObj.last;
		obj.value = qtm_posObj.first + qtm_posObj.body + qtm_posObj.last;
		var endfocus = qtm_posObj.first + qtm_posObj.body;
		endfocus = endfocus.length;
		if (obj.createTextRange) {
			if(navigator.userAgent.indexOf("MSIE") > -1)endfocus-=1;
			var range = obj.createTextRange();
			range.move('character',endfocus+1);
			range.select();
		}
		else if (obj.setSelectionRange) {
			obj.setSelectionRange(endfocus,endfocus);
		}
	}
	function qtm_pos(objId){
		var obj = document.getElementById(objId);
		obj.focus();
		qtm_posObj.body = "";
		if(navigator.userAgent.indexOf("MSIE") > -1){
			//IE
			var range = document.selection.createRange();
			var clone = range.duplicate();
			clone.moveToElementText(obj);
			clone.setEndPoint('EndToEnd',range);
			qtm_posObj.start = clone.text.length - range.text.length;
			qtm_posObj.end = clone.text.length - range.text.length + range.text.length;
		}
		else {
			//NOT IE
			qtm_posObj.start = obj.selectionStart;
			qtm_posObj.end = obj.selectionEnd;
		}
		if(qtm_posObj.start != qtm_posObj.end){
			qtm_posObj.body = obj.value.substring(qtm_posObj.start,qtm_posObj.end);
		}
	}
	var loading_image = '<img src="images/fullscreen_loading.gif" id="loading_proccess_image" width="40" height="40" />';
	var twex_body = document['CSS1Compat' == document.compatMode ? 'documentElement' : 'body'];
	var twex_flag = 1;
	document.write("<style type=\"text/css\">");
	document.write('div#twex {');
	document.write('	margin: 0px;');
	document.write('	overflow: hidden;');
	document.write('	z-index: 100;');
	document.write('	position: absolute;');
	document.write('	top: 0;');
	document.write('	left: 0;');
	document.write('	visibility: hidden;');
	document.write('	text-align: center;background-color: #000000;filter: alpha(opacity=60);-moz-opacity: 0.60;-khtml-opacity: 0.60;opacity: 0.60;');
	document.write('}img#loading_proccess_image {position: absolute;}');
	document.write('</style>');
	function twex_fullscreenObject(){
		twex_hideObject();
		var twexHTML;
		twexHTML = loading_image;
		if(document.getElementsByTagName('BODY').length==0)
			document.write('<body>');
		var element = document.createElement('div');
		element.id = "twex";
		element.innerHTML = twexHTML;
		var objBody = document.getElementsByTagName("body").item(0);
		objBody.appendChild(element);
		
		twex_resize();
		if(document.getElementById('twex'))
			document.getElementById('twex').style.visibility = "inherit";
	}
	function twex_resize(){
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
					//IE7
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
			nWidth = window.innerWidth;
			nHeight = window.innerHeight;
			nTop = document.body.scrollTop  || document.documentElement.scrollTop;
			nLeft = document.body.scrollLeft || document.documentElement.scrollLeft;
		}
		
		var lTop = (nHeight - 40) / 2;
		var lLeft = (nWidth - 40) / 2;
		
		if(document.getElementById('twex')){
			document.getElementById('twex').style.width = nWidth + "px";
			document.getElementById('twex').style.height = nHeight + "px";
			document.getElementById('twex').style.top = nTop + "px";
			document.getElementById('twex').style.left = nLeft + "px";
			document.getElementById('loading_proccess_image').style.top = lTop + "px";
			document.getElementById('loading_proccess_image').style.left = lLeft + "px";
		}
	}
	// ---------------------------------------------------
	function twex_closefullscreenObject(){
		if(document.getElementById('twex')){
			document.getElementById('twex').style.visibility = "hidden";
			document.getElementById('twex').style.width = "1px";
			document.getElementById('twex').style.display = "none";
		}
		twex_showObject();
	}

	// ---------------------------------------------------
	function twex_showObject(){
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
	
	// ---------------------------------------------------
	function twex_hideObject(){
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
	//window.onscroll = twex_closefullscreenObject;
	//window.onresize = twex_resize;
	appObject['onload'].push("statdisp()");
	var d = document;
	d.preloadImage = new Image;
	d.preloadImage.src = "images/fullscreen_loading.gif";
//-->
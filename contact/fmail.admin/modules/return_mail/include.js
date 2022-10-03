<!--
	var qtm_posObj = new Object();
	function checkUserEdit(obj,msg){
		var errorMSG = "";
		if(obj.elements["return_mail_name"].value == ""){
			errorMSG = "条件名が入力されていません";
		}
		if(errorMSG == "" && (confirm(msg+"してもよろしいですか？"))){
			return true;
		}
		else{
			alert(errorMSG);
			return false;
		}
	}
	function change_return_mail_type(obj){
		if(obj.value == 1)
			show_hide('return_mail_if',0);
		else
			show_hide('return_mail_if',1);
	}
	function statdisp(){
		if(appObject['querys']["stat"] != undefined){
			if(document.getElementById("stat"))
				document.getElementById("stat").style.display = "block";
		}
		if(document.getElementById('return_mail_type'))
			change_return_mail_type(document.getElementById('return_mail_type'));
	}
	function delete_confirm(getUrl,getId){
		var confirmMSG = "自動返信条件を削除してもよろしいですか？";
		if(confirm(confirmMSG)){
			location.href = getUrl;
		}
		else{
			return false;
		}
	}
	function textnolimit(){
		document.getElementById('text_min').value = 0;
		document.getElementById('text_max').value = 1024 * 1024;
	}
	function change_element_type(obj){
		var d = window.document;
		if(obj.value != ""){
			d.getElementById('return_mail_value').length = 0;
			objLength = 0;
			for(i=0;i<d.getElementById('hidden_selected_items').length;i++){
				if(d.getElementById('hidden_selected_items').options[i].value == obj.value){
					d.getElementById('return_mail_value').length = objLength + 1;
					d.getElementById('return_mail_value').options[objLength].value = d.getElementById('hidden_selected_items').options[i].text;
					d.getElementById('return_mail_value').options[objLength].text = d.getElementById('hidden_selected_items').options[i].text;
					objLength++;
				}
			}
		}
	}
	function show_hide(objId,flag){
		var d = window.document;
		if(flag){
			d.getElementById(objId).style.display = 'block';
		}
		else {
			d.getElementById(objId).style.display = 'none';
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
	function oftt(obj){
		obj.style.height = "300px";
	}
	function obtt(obj){
		obj.style.height = "100px";
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
	//追加
	function add_element_value_subject() {
		objId = 'subject';
		qtm_pos_subject(objId);
		var obj = document.getElementById(objId);
		qtm_posObj.end = qtm_posObj.start;
		qtm_posObj.subject = "<" + document.getElementById('add_elements_value_list_subject').value + ">";
		qtm_feedback_subject(obj);
	}
	//追加
	function qtm_feedback_subject(obj){
		qtm_posObj.first = obj.value.substring(0,qtm_posObj.start);
		qtm_posObj.last = obj.value.substring(qtm_posObj.end,obj.value.length);
		obj.value = qtm_posObj.first + qtm_posObj.subject + qtm_posObj.last;
		obj.value = qtm_posObj.first + qtm_posObj.subject + qtm_posObj.last;
		var endfocus = qtm_posObj.first + qtm_posObj.subject;
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
	//追加
	function qtm_pos_subject(objId){
		var obj = document.getElementById(objId);
		obj.focus();
		qtm_posObj.subject = "";
		if(navigator.userAgent.indexOf("MSIE") > -1){
			//IE（textareaの場合）
			//var range = document.selection.createRange();
			//var clone = range.duplicate();
			//clone.moveToElementText(obj);
			//clone.setEndPoint('EndToEnd',range);
			//qtm_posObj.start = clone.text.length - range.text.length;
			//qtm_posObj.end = clone.text.length - range.text.length + range.text.length;
			
			//IE（追加：textarea以外の場合）
				var range = document.selection.createRange();
				var eleRange = obj.createTextRange();
				eleRange.setEndPoint('EndToStart', range);
				qtm_posObj.start = eleRange.text.length;

				eleRange = obj.createTextRange();
				eleRange.setEndPoint('EndToEnd', range);
				qtm_posObj.end = eleRange.text.length;
			
		}
		else {
			//NOT IE
			qtm_posObj.start = obj.selectionStart;
			qtm_posObj.end = obj.selectionEnd;
		}
		if(qtm_posObj.start != qtm_posObj.end){
			qtm_posObj.subject = obj.value.substring(qtm_posObj.start,qtm_posObj.end);
		}
	}
	appObject['onload'].push("statdisp()");
//-->
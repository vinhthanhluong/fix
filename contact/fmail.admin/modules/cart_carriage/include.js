<!--
	function checkUserEdit(obj,msg){
		var errorMSG = "";
		if(errorMSG == ""){
			return true;
		}
		else{
			alert(errorMSG);
			return false;
		}
	}
	function statdisp(){
		if(appObject['querys']["stat"] != undefined){
			if(document.getElementById("stat"))
				document.getElementById("stat").style.display = "block";
		}
	}
	
	
	
	var qtm_posObj = new Object();
	function add_element_value() {
		objId = 'mailform_sender_address_name';
		qtm_pos(objId);
		var obj = document.getElementById(objId);
		qtm_posObj.end = qtm_posObj.start;
		//qtm_posObj.body = "<" + document.getElementById('add_elements_value_list').value + ">";
		qtm_posObj.body = document.getElementById('add_elements_value_list').value;
		qtm_feedback(obj);
	}
	function qtm_feedback(obj){
		//qtm_posObj.first = obj.value.substring(0,qtm_posObj.start);
		qtm_posObj.first = "";
		//qtm_posObj.last = obj.value.substring(qtm_posObj.end,obj.value.length);
		qtm_posObj.last = "";
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
			qtm_posObj.body = obj.value.substring(qtm_posObj.start,qtm_posObj.end);
		}
	}
	
	function num_adjust(str_id) {
		var str = document.getElementById(str_id).value;
		var str = str.replace(/[^0-9|\n]+/g,"");
		document.getElementById(str_id).value = str;
	}
	
	
	appObject['onload'].push("statdisp()");
//-->
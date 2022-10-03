<!--
	jQuery(function($){
		// 条件指定時の表示・非表示
		if(!$("#conditional_element").val()) {
			$("#conditional_if").hide();
		}
	});
	
	

	function checkUserEdit(obj,msg){
		var errorMSG = "";
		checkboxCreated();
		if(obj.elements["must_name"].value == ""){
			errorMSG = "条件名が入力されていません";
		}
		if(obj.elements["conditional_element"].value == "" && obj.elements["conditional_type"].value == '0'){
			errorMSG = "条件項目が入力されていません";
		}
		if(obj.elements["conditional_value"].value == "" && obj.elements["conditional_type"].value == '0'){
			errorMSG = "条件値が入力されていません";
		}
		if(errorMSG == ""){
			if(confirm(msg+"してもよろしいですか？"))
				return true;
			else
				return false;
		}
		else{
			alert(errorMSG);
			return false;
		}
	}
	function change_conditional_type(obj){
		if(obj.value == 1){
			show_hide('conditional_if',0);
			document.getElementById('conditional_element').value = "";
			document.getElementById('conditional_value').selected = false;
			document.getElementById('hidden_selected_items').selected = false;
		}else{
			show_hide('conditional_if',1);
		}
	}
	function statdisp(){
		if(document.getElementById('conditional_type'))
			change_conditional_type(document.getElementById('conditional_type'));
	}
	function delete_confirm(getUrl,getId){
		var confirmMSG = "送信条件を削除してもよろしいですか？";
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
	// 条件指定
	function change_element_type(obj){
		var d = window.document;
		if(obj.value != ""){
			d.getElementById('conditional_value').length = 0;
			objLength = 0;
			for(i=0;i<d.getElementById('hidden_selected_items').length;i++){
				if(d.getElementById('hidden_selected_items').options[i].value == obj.value){
					d.getElementById('conditional_value').length = objLength + 1;
					d.getElementById('conditional_value').options[objLength].value = d.getElementById('hidden_selected_items').options[i].text;
					d.getElementById('conditional_value').options[objLength].text = d.getElementById('hidden_selected_items').options[i].text;
					objLength++;
				}
			}
		}
	}
	
	function show_hide(objId,flag){
		var d = window.document;
		if(flag){
			d.getElementById(objId).style.display = 'table';
		}
		else {
			d.getElementById(objId).style.display = 'none';
		}
	}
	function checkboxCreated(){
		var mustList = new Array();
		var obj = new Object();
		obj = document.forms["user_add"];
		for(i=0;i<obj.length;i++){
			if(obj.elements[i].type == "checkbox"){
				if(obj.elements[i].checked){
					var val = "";
					var selectedValElements = "val" + obj.elements[i].value;
					if(obj.elements[selectedValElements]){
						val = obj.elements[selectedValElements].value;
					}
					else {
						val = 1;
					}
					var addpram = obj.elements[i].value + "=" + val;
					mustList.push(addpram);
				}
			}
		}
		obj.elements["must_elements"].value = mustList.join("&");
	}
	
	
	appObject['onload'].push("statdisp()");
//-->
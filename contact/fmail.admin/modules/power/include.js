<!--
	function checkUserEdit(obj,msg){
		var errorMSG = "";
		if(obj.elements["form_power_id"].value == "")
			errorMSG += "・IDが空欄です\n";
		if(obj.elements["form_display_name"].value == "")
			errorMSG += "・表示名が空欄です\n";
		
		if(errorMSG == ""){
			if(confirm("権限を"+msg+"してよろしいですか？")){
				return true;
			}
			else{
				return false;
			}
		}
		else{
			alert(errorMSG);
			return false;
		}
	}
	function delete_confirm(getUrl,getId){
		var confirmMSG = "権限「" + getId + "」を削除してもよろしいですか？";
		if(confirm(confirmMSG)){
			location.href = getUrl;
		}
		else{
			return false;
		}
	}
//-->
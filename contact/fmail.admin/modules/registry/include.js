<!--
	function checkUserEdit(obj,msg){
		var errorMSG = "";
		if(obj.elements["form_registry_id"].value == "")
			errorMSG += "・ハッシュIDが空欄です\n";
		if(obj.elements["form_registry_value"].value == "")
			errorMSG += "・値が空欄です\n";
		if(obj.elements["form_display_name"].value == "")
			errorMSG += "・表示名が空欄です\n";
		
		if(errorMSG == ""){
			if(confirm("レジストリを"+msg+"してよろしいですか？")){
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
		var confirmMSG = "エントリ「" + getId + "」を削除してもよろしいですか？";
		if(confirm(confirmMSG)){
			location.href = getUrl;
		}
		else{
			return false;
		}
	}
//-->
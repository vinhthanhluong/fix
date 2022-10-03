<!--
	function checkUserEdit(obj,msg){
		var errorMSG = "";
		if(obj.elements["form_user_id"].value == "")
			errorMSG += "・ユーザIDが空欄です\n";
		if(obj.elements["form_user_password"].value == "")
			errorMSG += "・ユーザパスワードが空欄です\n";
		if(obj.elements["form_display_name"].value == "")
			errorMSG += "・表示名が空欄です\n";
		
		if(errorMSG == ""){
			if(confirm("管理ユーザを"+msg+"してよろしいですか？")){
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
	function random_password(){
		var chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
		var chars_length = chars.length - 1;
		var passwd = "";
		for(i=0;i<9;i++){
			var getKey = Math.floor(Math.random() * chars_length);
			passwd += chars.substring(getKey,getKey+1);
		}
		document.forms["user_add"].elements["form_user_password"].value = passwd;
	}
	function delete_confirm(getUrl,getId){
		var confirmMSG = "アカウント「" + getId + "」を削除してもよろしいですか？";
		if(confirm(confirmMSG)){
			location.href = getUrl;
		}
		else{
			return false;
		}
	}
//-->
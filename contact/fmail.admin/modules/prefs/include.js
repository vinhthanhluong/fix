<!--
	function checkUserEdit(obj,msg){
		var errorMSG = "";
		if(obj.elements["form_user_password"].value != ""){
			if(obj.elements["form_user_password"].value.length < 8)
				errorMSG += "パスワードは8文字以上の英数で入力してください\n";
			else if(obj.elements["form_user_password"].value != obj.elements["form_user_password_confirm"].value)
				errorMSG += "パスワードと確認用のパスワードが違います\n";
		}else{
			errorMSG += "パスワードと確認用のパスワードを入力してください\n";
		}
		//if(obj.elements["form_display_name"].value == "")
		//	errorMSG += "お名前が空欄です\n";
		//if(obj.elements["form_user_email"].value == "")
		//	errorMSG += "メールアドレスが空欄です\n";
		
		if(errorMSG == ""){
			if(confirm("登録情報を更新してもよろしいですか？")){
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
//-->
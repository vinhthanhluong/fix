<!--
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
	function install_confirm(getUrl,getId){
		var confirmMSG = "「" + getId + "」モジュールをインストールしてもよろしいですか？";
		if(confirm(confirmMSG)){
			location.href = getUrl;
		}
		else{
			return false;
		}
	}
	function uninstall_confirm(getUrl,getId){
		var confirmMSG = "「" + getId + "」モジュールをアンインストールしてもよろしいですか？";
		if(confirm(confirmMSG)){
			location.href = getUrl;
		}
		else{
			return false;
		}
	}
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
	function setPowers(obj) {
		if(obj.value == "null"){
			for(i=0;i<obj.length;i++){
				if(obj.options[i].value != "null"){
					obj.options[i].selected = false;
				}
			}
		}
	}
	function checkPowers(obj,msg){
		var errorMSG = "";
		var setVals = new Array();
		var alluser_flag = 1;
		for(i=0;i<obj.elements["powers"].length;i++){
			if((obj.elements["powers"].options[i].selected) && obj.elements["powers"].options[i].value != "null"){
				setVals.push(obj.elements["powers"].options[i].value)
			}
			else if((obj.elements["powers"].options[i].selected) && obj.elements["powers"].options[i].value == "null"){
				alluser_flag = 0;
				obj.elements["post_powers"].value = "null";
			}
		}
		if(alluser_flag){
			obj.elements["post_powers"].value = setVals.join(",");
		}
		if(obj.elements["post_powers"].value == ""){
			obj.elements["post_powers"].value = "null";
		}
		if(errorMSG == ""){
			if(confirm("アクセス権を"+msg+"してよろしいですか？")){
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
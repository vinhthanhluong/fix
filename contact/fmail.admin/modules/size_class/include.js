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
	
	function dataadjust(str_id) {
		var ptn = document.getElementById(str_id).value;
				
		// 不要テキスト抹消
		if (ptn != 'auto') {
			var work = ptn.replace(/[^0-9]/g,"");
			if (work) {
				work = work + 'px';
			}
			// 値を返す
			document.getElementById(str_id).value = work;
		}
	}
	
	appObject['onload'].push("statdisp()");
//-->
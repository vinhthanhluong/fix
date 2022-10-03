<!--
	function checkUserEdit(obj,msg){
		var errorMSG = "";
		if(obj.elements["note_title"].value == "")
			errorMSG += "・ページ名が空欄です\n";
		if(obj.elements["note_body"].value == "")
			errorMSG += "・ページが空欄です\n";
		
		if(errorMSG == ""){
			return true;
		}
		else{
			alert(errorMSG);
			return false;
		}
	}
	function delete_confirm(getUrl,getId){
		var confirmMSG = "ページ「" + getId + "」を削除してもよろしいですか？";
		if(confirm(confirmMSG)){
			location.href = getUrl;
		}
		else{
			return false;
		}
	}
	function settextarea(){
		if(document.getElementById('note_body')){
			document.getElementById('note_body').style.height = (appConf['contents'].height - 190) + "px";
		}
	}
	appObject['onload'].push("settextarea()");
	$(window).resize(settextarea);
	
	// date picker
	$(document).ready(function(){
		$('.formlog_search').datepicker({
			dateFormat: "yy-m-d",
			yearRange: "c-5:c+0",
			changeMonth: true,
			changeYear: true
		});
		
		$("div.tabs li").click(function(){
			var class_name = $(this).attr("class");
			$("div.tabs ~ div").fadeOut("fast",function(){
				$("div#" + class_name).fadeIn(function(){
				});
			});
		});
	});
	
//-->
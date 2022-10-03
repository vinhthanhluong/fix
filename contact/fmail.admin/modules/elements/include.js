<!--
	//
	var jsLibNames = new Array("実装済イベント","自動フリガナ","郵便番号からの住所入力","数字の半角化","半角数字（3桁区切り）","住所の全角化","メールアドレスの半角化","カタカナの全角化");
	var jsLibFuncs = new Array("",
								"onkeyup=\"Fkana(this.form,this,'フリガナエレメントのID',event.keyCode)\" onfocus=\"kWatch(this,'フリガナエレメントのID')\"",
								"onclick=\"mfpc(this.form.id,'郵便番号エレメントのID','都道府県エレメントのID','市区町村エレメントのID','丁目番地エレメントのID');\"",
								"onchange=\"numadjust(this.id);\"",
								"onchange=\"delimit(this.id);\"",
								"onchange=\"addradjust(this.id);\"",
								"onchange=\"mailadjust(this.id);\"",
								"onchange=\"hankana2zenkana(this.id);\"");
	
	// add 2010-01-24
	function charexp(obj){
		var before = ('(',')');
		var after = ('（','）');
		// 記号の全角化
		obj.value = obj.value.replace(/([\!-\/])/g,function (char){ return String.fromCharCode(char.charCodeAt(0) + 65248)}).replace(/”/g, "\"").replace(/'/g, "’");
		obj.value = obj.value.replace(/([\;-\@])/g,function (char){ return String.fromCharCode(char.charCodeAt(0) + 65248)}).replace(/\\/g, "￥");
		obj.value = obj.value.replace(/([\[-\`])/g,function (char){ return String.fromCharCode(char.charCodeAt(0) + 65248)}).replace(/`/g, "‘");
		obj.value = obj.value.replace(/([\{-\~])/g,function (char){ return String.fromCharCode(char.charCodeAt(0) + 65248)}).replace(/＜－br－＞/g, '<-br->');
	}
	// add 2010-01-24
	
	function display_elements_list(){
		document.getElementById("button_element_list_field").style.display = "none";
		document.getElementById("elements_id_list_select_field").style.display = "block";
	}
	function get_elements_id_list_select(gval) {
		document.getElementById("elements_id_list_select_value").value = gval;
	}
	function select_delete_check(str){
		document.getElementById('flag_delete').value = str;
	}
	function gosort() {
		if(document.getElementById('flag_delete').value == 'del'){
			if(confirm("選択中の項目　を削除してもよろしいですか？"))
				return true;
			else
				return false;
		}else{
			if(confirm("「項目の並べ替え」を実行してもよろしいですか？"))
				return true;
			else
				return false;
		}
	}
	function checkUserEdit(obj,msg){
		var errorMSG = "";
		if(obj.elements["name"].value == ""){
			errorMSG = "項目名が入力されていません";
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
	function statdisp(){
		if(appObject['querys']["stat"] != undefined){
			if(document.getElementById("stat"))
				document.getElementById("stat").style.display = "block";
		}
		if(document.getElementById('element_type'))
			change_element_type();
		if(document.getElementById('jslibt')){
			document.getElementById('jslibt').length = jsLibNames.length;
			for(i=0;i<jsLibNames.length;i++){
				document.getElementById('jslibt').options[i].text = jsLibNames[i];
				document.getElementById('jslibt').options[i].value = jsLibFuncs[i];
			}
		}
		systemDispTag();
	}
	function systemDispTag(){
		if(document.getElementById('system_disp_false')){
			if(document.getElementById('system_disp_false').checked){
				document.getElementById('system_disp_false_html').style.display = 'block';
				var ptag = "";
				var element_type = document.getElementById('element_type').value;
				var element_id = document.getElementById('id_example').value;
				var smartphone_element_type = document.getElementById('smartphone_element_type').value;
				if(element_type == "text" && smartphone_element_type){
					document.getElementById('system_disp_false_html').value = '<input type="text_' + smartphone_element_type + '" name="'+element_id+'" id="'+element_id+'" class="fmail" value="[['+element_id+']]" />[['+element_id+'_error]]';
				}
				else if(element_type == "text"){
					document.getElementById('system_disp_false_html').value = '<input type="text" name="'+element_id+'" id="'+element_id+'" class="fmail" value="[['+element_id+']]" />[['+element_id+'_error]]';
				}
				else if(element_type == "textarea") {
					document.getElementById('system_disp_false_html').value = '<textarea name="'+element_id+'" id="'+element_id+'" class="fmail">[['+element_id+']]</textarea>[['+element_id+'_error]]';
				}
				else if(element_type == "select") {
					// fix 2009-07-23 update
					document.getElementById('system_disp_false_html').value = '<select name="'+element_id+'" id="'+element_id+'" class="fmail">';
					var optGroupFlag = 0;
					var prevOptGroup = "";
					var option_element_values = document.getElementById("element_valus").value.split("\n");
					var option_element_text = document.getElementById("element_text").value.split("\n");
					for(i=0;i<option_element_values.length;i++){
						var option_element_optgroup = option_element_text[i].split('::');
						var elementText = option_element_optgroup[0];
						var optGroup = option_element_optgroup[1];
						if(!(optGroupFlag) && optGroup != undefined && prevOptGroup == ""){
							document.getElementById('system_disp_false_html').value += '<optgroup label="'+optGroup+'">';
							optGroupFlag = 1;
						}
						else if(optGroup != undefined && prevOptGroup != optGroup){
							document.getElementById('system_disp_false_html').value += '</optgroup><optgroup label="'+optGroup+'">';
							optGroupFlag = 1;
						}
						document.getElementById('system_disp_false_html').value += '<option value="'+option_element_values[i]+'">'+elementText+'</option>';
						prevOptGroup = optGroup;
					}
					if(optGroupFlag){
						document.getElementById('system_disp_false_html').value += "</optgroup>";
					}
					document.getElementById('system_disp_false_html').value += '</select>[['+element_id+'_error]]';
				}
				else if(element_type == "radio" || element_type == "checkbox"){
					var insertTag = "";
					var option_element_values = document.getElementById("element_valus").value.split("\n");
					var option_element_text = document.getElementById("element_text").value.split("\n");
					
					insertTag = '[['+element_id+'_error]]<ol class="fmail_' + element_type + '_list clearfix">';
					for(i=0;i<option_element_values.length;i++){
						num = i + 1;
						if(num < 10) num = "0"+num;
						insertTag += '<li><label id="'+element_id+'_'+num+'_label" for="'+element_id+'_'+num+'" class="fmail_label">';
						insertTag += '<input type="'+element_type+'" name="'+element_id+'" id="'+element_id+'_'+num+'" class="fmail" value="'+option_element_values[i]+'" /> ';
						insertTag += option_element_text[i];
						insertTag += '</label></li>';
					}
					insertTag += '</ol>';
					document.getElementById('system_disp_false_html').value = insertTag;
				}
				else if(element_type == "file") {
					document.getElementById('system_disp_false_html').value = '<input type="file" name="'+element_id+'" id="'+element_id+'" class="fmail_file" /><input type="button" value="キャンセル" class="ffcancel" onclick="del(\''+element_id+'\');" onkeypress="del(\''+element_id+'\');" />[['+element_id+'_error]]';
				}
				else if(element_type == "hidden") {
					document.getElementById('system_disp_false_html').value = '<input type="hidden" name="'+element_id+'" id="'+element_id+'" class="fmail" value="[['+element_id+']]" />[['+element_id+'_error]]';
				}
				else {
					
				}
			}
			else {
				document.getElementById('system_disp_false_html').style.display = 'none';
			}
		}
	}
	function jslibChange(val){
		if(val != "")
			prompt('以下のコードをコピーしてご利用ください',val);
	}
	function delete_confirm(getUrl,getId){
		var confirmMSG = "項目「" + getId + "」を削除してもよろしいですか？";
		if(confirm(confirmMSG)){
			location.href = getUrl;
		}
		else{
			return false;
		}
	}
	function copy_confirm(getUrl,getId){
		var confirmMSG = "項目「" + getId + "」を複製してもよろしいですか？";
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
	function change_element_type(){
		val = document.getElementById('element_type').value;
		if(val == "text"){
			show_hide('smartphone_check',1);		// スマホアクセス時のtype属性
			show_hide('req_icon',1);						// 必須アイコン・ORアイコン
			show_hide('joielement',0);					// 連結指定
			show_hide('standard_sys_disp',1);		// システム非表示
			show_hide('standard_conf_disp',1);	// 確認画面非表示
			show_hide('standard_mail_disp',1);	// 本文非表示
			show_hide('standard_err',1);				// エラー表示
			show_hide('standard',1);						// イベント属性・HTMLタグ・
			show_hide('id_disp',1);							// ID属性
			show_hide('addclass_disp',1);				// addClass
			show_hide('size_class',1);					// サイズ属性
			show_hide('value_check_type',1);		// チェックタイプ
			show_hide('text_format',1);					// 入力例・文字数制限
			show_hide('text_only',1);						// マッチングタグ
			show_hide('val_only',1);						// 初期値
			show_hide('textarea_only',0);				// 高さ属性・横幅属性・初期値
			show_hide('selectvals_format',0);		// 選択値
			show_hide('filetype_only',0);				// 対応ファイル・ファイルサイズ
		}
		else if(val == "textarea"){
			show_hide('smartphone_check',0);
			show_hide('req_icon',1);
			show_hide('joielement',0);
			show_hide('standard_sys_disp',1);
			show_hide('standard_conf_disp',1);	// 確認画面非表示
			show_hide('standard_mail_disp',1);	// 本文非表示
			show_hide('standard_err',1);
			show_hide('standard',1);
			show_hide('id_disp',1);
			show_hide('addclass_disp',1);				// addClass
			show_hide('size_class',1);
			show_hide('value_check_type',1);
			show_hide('text_format',1);
			show_hide('text_only',0);
			show_hide('val_only',0);
			show_hide('textarea_only',1);
			show_hide('selectvals_format',0);
			show_hide('filetype_only',0);
		}
		else if(val == "select" || val == "radio" || val == "checkbox"){
			show_hide('smartphone_check',0);
			show_hide('req_icon',1);
			show_hide('joielement',0);
			show_hide('standard_sys_disp',1);
			show_hide('standard_conf_disp',1);	// 確認画面非表示
			show_hide('standard_mail_disp',1);	// 本文非表示
			show_hide('standard_err',1);
			show_hide('standard',1);
			show_hide('id_disp',1);
			show_hide('addclass_disp',1);				// addClass
			show_hide('size_class',1);
			show_hide('value_check_type',0);
			show_hide('text_format',0);
			show_hide('text_only',0);
			show_hide('val_only',0);
			show_hide('textarea_only',0);
			show_hide('selectvals_format',1);
			show_hide('filetype_only',0);
		}
		else if(val == "file"){
			show_hide('smartphone_check',0);
			show_hide('req_icon',1);
			show_hide('joielement',0);
			show_hide('standard_sys_disp',1);
			show_hide('standard_conf_disp',1);	// 確認画面非表示
			show_hide('standard_mail_disp',1);	// 本文非表示
			show_hide('standard_err',1);
			show_hide('standard',1);
			show_hide('id_disp',1);
			show_hide('addclass_disp',1);				// addClass
			show_hide('size_class',1);
			show_hide('value_check_type',0);
			show_hide('text_format',0);
			show_hide('text_only',0);
			show_hide('val_only',0);
			show_hide('textarea_only',0);
			show_hide('selectvals_format',0);
			show_hide('filetype_only',1);
		}
		else if(val == "join"){
			show_hide('smartphone_check',0);
			show_hide('req_icon',0);
			show_hide('joielement',1);
			show_hide('standard_sys_disp',0);
			show_hide('standard_conf_disp',0);	// 確認画面非表示
			show_hide('standard_mail_disp',0);	// 本文非表示
			show_hide('standard_err',0);
			show_hide('standard',0);
			show_hide('id_disp',0);
			show_hide('addclass_disp',0);				// addClass
			show_hide('size_class',0);
			show_hide('value_check_type',1);
			show_hide('text_format',0);
			show_hide('text_only',0);
			show_hide('val_only',0);
			show_hide('textarea_only',0);
			show_hide('selectvals_format',0);
			show_hide('filetype_only',0);
		}
		else if(val == "spacer"){
			show_hide('smartphone_check',0);
			show_hide('req_icon',1);
			show_hide('joielement',0);
			show_hide('standard_sys_disp',1);
			show_hide('standard_conf_disp',0);	// 確認画面非表示
			show_hide('standard_mail_disp',0);	// 本文非表示
			show_hide('standard_err',1);
			show_hide('standard',1);
			show_hide('id_disp',1);
			show_hide('addclass_disp',1);				// addClass
			show_hide('size_class',1);
			show_hide('value_check_type',0);
			show_hide('text_format',0);
			show_hide('text_only',0);
			show_hide('val_only',0);
			show_hide('textarea_only',0);
			show_hide('selectvals_format',0);
			show_hide('filetype_only',0);
			// 090818fix com.synck
			document.getElementById("html_example").value = "";
			//
		}
		else if(val == "hidden"){
			show_hide('smartphone_check',0);
			show_hide('req_icon',0);
			show_hide('joielement',0);
			show_hide('standard_sys_disp',1);
			show_hide('standard_conf_disp',1);	// 確認画面非表示
			show_hide('standard_mail_disp',1);	// 本文非表示
			show_hide('standard_err',1);
			show_hide('standard',0);
			show_hide('id_disp',1);
			show_hide('addclass_disp',0);				// addClass
			show_hide('size_class',0);
			show_hide('value_check_type',0);
			show_hide('text_format',0);
			show_hide('text_only',0);
			show_hide('val_only',1);
			show_hide('textarea_only',0);
			show_hide('selectvals_format',0);
			show_hide('filetype_only',0);
		}
		else {
			show_hide('smartphone_check',0);
			show_hide('req_icon',0);
			show_hide('joielement',0);
			show_hide('standard_sys_disp',0);
			show_hide('standard_conf_disp',0);	// 確認画面非表示
			show_hide('standard_mail_disp',0);	// 本文非表示
			show_hide('standard_err',0);
			show_hide('standard',0);
			show_hide('id_disp',0);
			show_hide('addclass_disp',0);				// addClass
			show_hide('size_class',0);
			show_hide('value_check_type',0);
			show_hide('text_format',0);
			show_hide('text_only',0);
			show_hide('val_only',0);
			show_hide('textarea_only',0);
			show_hide('selectvals_format',0);
			show_hide('filetype_only',0);
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
	var qtm_posObj = new Object();
	function add_element_value() {
		objId = 'type_of_element';
		qtm_pos(objId);
		var obj = document.getElementById(objId);
		//var obj = document.forms["user_add"].elements["type_of_element"];
		var listObj = document.forms["user_add"].elements["add_elements_value_list"];
		qtm_posObj.end = qtm_posObj.start;
		//qtm_posObj.body = "<join id=\"" + document.getElementById('add_elements_value_list').value + "\" name=\""+document.getElementById('add_elements_value_list').text+"\" />";
		qtm_posObj.body = "<join id=\"" + listObj.options[listObj.selectedIndex].value + "\" name=\""+listObj.options[listObj.selectedIndex].text+"\" />";
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
	appObject['onload'].push("statdisp()");
//-->
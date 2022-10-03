<!--
	function cart_logformat(selectdata){
		targetdata = selectdata.split("-");
		targetdata = targetdata[0] + '年' + targetdata[1] + '月';
		if(confirm("[ 商品カート履歴データ初期化　再確認 ]\n\n\n" + targetdata + " の初期化を実行しますか？\n\n\n※初期化後、データ復旧は出来ません。事前のＣＳＶダウンロードを推奨します。")){
			location.href = 'index.cgi?m=cart_logview&a=format&v=' + selectdata;
		}
	}
	
	function cartselect_save(obj,rd) {
		location.href = 'index.cgi?m=cart_logview&a=dateselect&v=' + obj.value + '&r=' + rd;
	}
//-->
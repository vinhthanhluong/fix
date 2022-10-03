<!--
function updateOrientation() {
	//回転角度を検出
	switch(window.orientation) {
		//横向きを判定
		case 90:
		case -90:
		document.getElementById("viewport").setAttribute('content','device-width=' + screen.height + ',width=' + screen.height + ',initial-scale=1.0,maximum-scale=1.0, user-scalable=0');
		document.getElementById("fmailbody").setAttribute('class','yoko');
		break;
		
		//縦向きを判定
		case 0:
		case 180:
		default:
		document.getElementById("viewport").setAttribute('content','device-width=' + screen.width + ',width=' + screen.width + ',initial-scale=1.0,maximum-scale=1.0, user-scalable=0');
		document.getElementById("fmailbody").setAttribute('class','tate');
		break;
	}
}
//-->
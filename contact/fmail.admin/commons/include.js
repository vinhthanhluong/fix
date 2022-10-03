<!--
//Interface Functions
function over(obj){
	obj.className = 'over';
}
function out(obj){
	obj.className = '';
}
function logtout(){
	if(confirm("May You logout ?")){
		location.href = '?logout';
	}
}
//Macromedia Dreamweaver Basic Functions
	function MM_swapImgRestore() {
	//v3.0
	  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
	}
	
	function MM_preloadImages() {
	//v3.0
	  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
	    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
	    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
	}
	
	function MM_findObj(n, d) {
	//v4.01
	  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
	    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
	  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
	  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
	  if(!x && d.getElementById) x=d.getElementById(n); return x;
	}
	
	function MM_swapImage() {
	//v3.0
	  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
	   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
	}
//end of feeld


//Page Top smoothed scroll Functions
	var Mac = navigator.appVersion.indexOf('Mac',0) != -1;
	var Win = navigator.appVersion.indexOf('Win',0) != -1;
	var IE  = navigator.appName.indexOf("Microsoft Internet Explorer",0) != -1;
	var NN  = navigator.appName.indexOf("Netscape",0) != -1;
	var Moz = navigator.userAgent.indexOf("Gecko") != -1;
	var Vmajor = parseInt(navigator.appVersion); // ex. 3
	var Vminor = parseFloat(navigator.appVersion); // ex. 3.01
	
	var MacIE4 = ((Mac && navigator.appVersion.indexOf('MSIE 4.',0) != -1));
	var MacIE3 = ((Mac && navigator.appVersion.indexOf('MSIE 3.',0) != -1));
	
	function getScrollLeft() {
		if ((navigator.appName.indexOf("Microsoft Internet Explorer",0) != -1)) {
			return document.body.scrollLeft;
		}
		else if (window.pageXOffset) {
			return window.pageXOffset;
		}
		else {
			return 0;
		}
	}
	
	function getScrollTop() {
		if ((navigator.appName.indexOf("Microsoft Internet Explorer",0) != -1)) {
			return document.body.scrollTop;
		}
		else if (window.pageYOffset) {
			return window.pageYOffset;
		}
		else {
			return 0;
		}
	}
	
	var pageScrollTimer;
	function pageScroll(toX,toY,frms,cuX,cuY) { // 020314
	 if (pageScrollTimer) clearTimeout(pageScrollTimer);
	 if (!toX || toX < 0) toX = 0;
	 if (!toY || toY < 0) toY = 0;
	 if (!cuX) cuX = 0 + getScrollLeft();
	 if (!cuY) cuY = 0 + getScrollTop();
	 if (!frms) frms = 6;
	
	 if (toY > cuY && toY > (getAnchorPosObj('end','enddiv').y) - getInnerSize().height) toY = (getAnchorPosObj('end','enddiv').y - getInnerSize().height) + 1;
	 cuX += (toX - getScrollLeft()) / frms; if (cuX < 0) cuX = 0;
	 cuY += (toY - getScrollTop()) / frms;  if (cuY < 0) cuY = 0;
	 var posX = Math.floor(cuX);
	 var posY = Math.floor(cuY);
	 window.scrollTo(posX, posY);
	
	 if (posX != toX || posY != toY) {
	  pageScrollTimer = setTimeout("pageScroll("+toX+","+toY+","+frms+","+cuX+","+cuY+")",16);
	 }
	}
	
	function jumpToPageTop() {
	  pageScroll(0,0,5);
	}
//end of feeld

function loadFlash(url,width,height){
	var myDate = new Date();
	var time = myDate.getTime();
	url = url + "?timer=" + time;
	document.write('<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=5,0,0,0" width="'+width+'" height="'+height+'">');
	document.write('<param name="movie" value="'+url+'">');
	document.write('<param name="quality" value="high">');
	document.write('<embed src="'+url+'" quality="high" pluginspage="http://www.macromedia.com/jp/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash" type="application/x-shockwave-flash" width="'+width+'" height="'+height+'">');
	document.write('</embed>');
	document.write('</object>');
}
function WppSEPlay(sename){
	var str;
	var url = 'images/'+sename+'.swf';
	var width = 1;
	var height = 1;
	str = '<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=5,0,0,0" width="'+width+'" height="'+height+'">';
	str += '<param name="movie" value="'+url+'">';
	str += '<param name="quality" value="high">';
	str += '<embed src="'+url+'" quality="high" pluginspage="http://www.macromedia.com/jp/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash" type="application/x-shockwave-flash" width="'+width+'" height="'+height+'">';
	str += '</embed>';
	str += '</object>';
	return str;
}
var appConf = new Object();
appConf['contents'] = new Object();
var appObject = new Object();
appObject['onload'] = new Array();
appObject['querys'] = new Object();
function resizeElements(){
	if(1){
		//navigator.appVersion.indexOf("Safari") == 0 && navigator.appVersion.indexOf("Mobile") == 0
		var nWidth, nHeight, nTop, nLeft;
		var ua = navigator.userAgent;
		var nHit = ua.indexOf("MSIE");
		var bIE = (nHit >=  0);
		var bVer6 = (bIE && ua.substr(nHit+5, 1) == "6");
		var bStd = (document.compatMode && document.compatMode=="CSS1Compat");
		if (bIE) {
			if (bVer6 && bStd) {
				nWidth = document.documentElement.clientWidth;
				nHeight = document.documentElement.clientHeight;
				nTop = document.documentElement.scrollTop;
				nLeft = document.documentElement.scrollLeft;
			}
			else {
				if(typeof document.body.style.maxHeight != "undefined") {
					//IE7
					nWidth = document.documentElement.clientWidth;
					nHeight = document.documentElement.clientHeight;
					nTop = document.documentElement.scrollTop;
					nLeft = document.documentElement.scrollLeft;
				}
				else {
					nWidth = document.body.clientWidth;
					nHeight = document.body.clientHeight;
					nTop = document.body.scrollTop;
					nLeft = document.body.scrollLeft;
				}
			}
		}
		else {
			nWidth = window.innerWidth;
			nHeight = window.innerHeight;
			nTop = document.body.scrollTop  || document.documentElement.scrollTop;
			nLeft = document.body.scrollLeft || document.documentElement.scrollLeft;
		}
		if(nHeight < 640){
			nHeight = 640;
		}
		document.getElementById("footer").style.top = (nHeight-131)+"px";
		document.getElementById("sidebar").style.height = (nHeight-130)+"px";
		document.getElementById("contents").style.height = (nHeight-130)+"px";
		document.getElementById("contents").style.width = (nWidth-217)+"px";
		document.getElementById("contentsbody").style.height = (nHeight-186)+"px";
		document.getElementById("contentsbody").style.width = (nWidth-217)+"px";
		document.getElementById("inbox").style.width = (nWidth-237)+"px";
		appConf["contents"].width = nWidth-200;
		appConf["contents"].height = nHeight-130;
	}
}
function setQuery(){
	var querys = new Array();
	var query = new Array();
	var str = location.search;
	str = str.substring(1,str.length);
	querys = str.split("&");
	for(i=0;i<querys.length;i++){
		query = querys[i].split("=");
		appObject['querys'][query[0]] = query[1];
	}
}
setQuery();

window.onload = function(){
	resizeElements();
	var tagObjects = document.getElementsByTagName("a");
	for(i=0;i < tagObjects.length;i++) {
		if(tagObjects[i].className == "module" && location.href.split("?")[1] == tagObjects[i].href.split("?")[1] && location.href.split("?")[1] == ""){
			tagObjects[i].className = "module_active";
		}
		else if(tagObjects[i].className == "module" && location.href.indexOf(tagObjects[i].href) > -1 && tagObjects[i].href.split("?")[1] != ""){
			tagObjects[i].className = "module_active";
		}
	}
	for(i=0;i < appObject['onload'].length;i++){
		setTimeout(appObject['onload'][i],0);
	}
}

$(window).resize(resizeElements);
//-->
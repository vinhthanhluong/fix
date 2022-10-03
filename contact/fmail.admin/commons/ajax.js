<!--
//////////////////////////////////////////////
	var ajaxObj = new Object();
	function loadComplate() {
		MM_swapImage('loading','','images/spacer.gif',1);
	}
	function post_module(){
		MM_swapImage('loading','','images/loading.gif',1);
		httpObj = createXMLHttpRequest();
		httpObj.onreadystatechange = get_module;
		httpObj.open("GET","index.cgi?ajax=1&m="+ajaxObj.m+"&"+ajaxObj.query,true);
		httpObj.send(null);
		return false;
	}
	function get_module(){
		if ((httpObj.readyState == 4) && (httpObj.status == 200)) {
			ajaxObj.get = httpObj.responseText;
			setTimeout(loadComplate,1000);
			resizeElements();
			if(ajaxObj.callback){
				setTimeout(ajaxObj.callback,200);
			}
		}
	}
	function createXMLHttp() {
		try {
			return new ActiveXObject ("Microsoft.XMLHTTP");
		}catch(e){
			try {
				return new XMLHttpRequest();
			}catch(e) {
				return null;
			}
		}
		return null;
	}
	function createXMLHttpRequest(){
		var XMLhttpObject = null;
		try{
			XMLhttpObject = new XMLHttpRequest();
		}
		catch(e){
			try{
				XMLhttpObject = new ActiveXObject("Msxml2.XMLHTTP");
			}
			catch(e){
				try{
					XMLhttpObject = new ActiveXObject("Microsoft.XMLHTTP");
				}
				catch(e){
					return null;
				}
			}
		}
		return XMLhttpObject;
	}
//////////////////////////////////////////////
//-->
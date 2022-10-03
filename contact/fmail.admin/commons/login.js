<!--
	function windowresize(){
		document.getElementById('user_id').focus(); // オートフォーカス
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
				if (typeof document.body.style.maxHeight != "undefined") {
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
		leftp = (nWidth - 460) / 2;
		ntopp = (nHeight - 200) / 2;
		if(document.all){
			document.all("wrapper").style.top = ntopp + "px";
			document.all("wrapper").style.left = leftp + "px";
			document.all("loginframe").style.top = ntopp + "px";
			document.all("loginframe").style.left = leftp + "px";
		}
		else if(document.getElementById){
			document.getElementById("wrapper").style.top = ntopp + "px";
			document.getElementById("wrapper").style.left = leftp + "px";
			document.getElementById("loginframe").style.top = ntopp + "px";
			document.getElementById("loginframe").style.left = leftp + "px";
		}
	}
	window.onload = windowresize;
	window.onresize = windowresize;
//-->
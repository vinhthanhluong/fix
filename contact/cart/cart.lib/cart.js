<!--
function pnumsave(obj,order) {
	obj.value = obj.value.replace(/[Ａ-Ｚａ-ｚ０-９]/g,function(s){return String.fromCharCode(s.charCodeAt(0)-0xFEE0)});
	obj.value = obj.value.replace(/[^0-9]/g,"");
	location.href = 'index.cgi?m=n&n=' + obj.value + "&o=" + order;
}
// -->

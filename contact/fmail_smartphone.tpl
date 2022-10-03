<!DOCTYPE html>
<html lang="ja">
	<head>
		<meta charset="utf-8">
		<meta id="viewport" name="viewport" content="width=device-width">
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta http-equiv="Content-Style-Type" content="text/css" />
		
		<title>Fmail | <!--%%fmail-printable-area-title%%--></title>
		<link rel="stylesheet" href="./smaph/commons/_include.css" type="text/css" />
		<meta name="Description" content="fmail <!--%%fmail-printable-area-ver%%-->" />
		
		<!-- [ Fmail Include Files ] -->
		<link rel="stylesheet" href="./smaph/fmail.lib/fmail.css" type="text/css" />
		<link rel="stylesheet" href="./smaph/fmail.lib/smoothness/jquery-ui-1.10.1.custom.css" type="text/css">
		<script type="text/javascript" src="./fmail.lib/jquery_reader.js" charset="utf-8"></script>
		<script type="text/javascript" src="./fmail.lib/jquery-ui-1.10.1.custom.js" charset="utf-8"></script>
		<script type="text/javascript" src="./fmail.lib/jquery_autoKana.js" charset="utf-8"></script>
		<script type="text/javascript" src="./fmail.postcode.cgi?js" charset="utf-8"></script>
		<script type="text/javascript" src="./smaph/fmail.lib/fmail.js" charset="utf-8"></script>
		<script type="text/javascript" src="./fmail.lib/fmail.formlog.js" charset="utf-8"></script>
		<script type="text/javascript" src="./smaph/fmail.lib/smaph.js" charset="utf-8"></script>
		<script type="text/javascript" src="./fmail.lib/gcalendar-holidays.js" charset="utf-8"></script>
		<script type="text/javascript" src="./smaph/fmail.lib/datepicker.js" charset="utf-8"></script>
		<!-- [ Fmail Include Files EOF ] -->
		
		<script>
			$(document).ready(function(){
				$.fn.autoKana('#en1240790859', '#en1240790885', {katakana:true});
			});
		</script>
		
	</head>
	<body id="fmailbody" onload="updateOrientation()" Onorientationchange="updateOrientation()">
		<div id="header">
			<h1 id="title">fmail <!--%%fmail-printable-area-ver%%--></h1>
			<span>FREESALE MAILFORM SYSTEM VERSION <!--%%fmail-printable-area-ver%%--></span>
		</div>
		<div id="container">
			<div id="contents">
				<!--%%fmail-invisible-contents-start%%-->
					これはスマフォ用テンプレートです。<br />
					入力画面のみ出力
				<!--%%fmail-invisible-contents-end%%-->
				
				<!--%%fmail-printable-area-error%%-->
				<!--%%fmail-printable-area-body%%-->
			</div>
		</div>
		<div id="footer">
			<span>Copyright&copy; 2009 All Rights Reserved.</span>
		</div>
		
		
		<!--%%fmail-invisible-contents-start%%-->
			入力画面のみ出力
		<!--%%fmail-invisible-contents-end%%-->
		
		<!--%%fmail-error-contents-start%%-->
			エラー画面のみ出力
		<!--%%fmail-error-contents-end%%-->
		
		<!--%%fmail-confirm-contents-start%%-->
			確認画面画面のみ出力
		<!--%%fmail-confirm-contents-end%%-->
		
		<!--%%fmail-thanks-contents-start%%-->
			送信完了画面のみ出力<br />
			値引継したい場合、<span class="fmail_caution">&lt;ID名&gt;</span>と記述。<br />
			分類→<en1248700237><br />
			<br />
			引継した値をURLエンコードする場合は、IDを&lt;<span class="fmail_caution">urlenc_</span>ID名&gt;と記述。<br />
			分類→<urlenc_en1248700237><br />
			<br />
			URLエンコードは例えば、GA解析の仮想URLなどで活用します。（送信完了画面で、ソースをご確認ください）<br />
			<span class="fmail_caution">設置事例ですので、本番実装時は、これらの記載は削除しておいてください。</span><br />
			
<script type="text/javascript">
	var _gaq = _gaq || [];
	_gaq.push(['_setAccount', 'UA-XXXXX-X']);
	_gaq.push(['_trackPageview', '/contact/index.cgi?mode=thanks&pattern=<urlenc_en1248700237>']);
	
	(function() {
		var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
		ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
		var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
	})();
</script>
		<!--%%fmail-thanks-contents-end%%-->
		
	</body>
</html>
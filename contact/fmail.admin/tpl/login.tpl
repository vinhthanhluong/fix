<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
		<meta http-equiv="Content-Style-Type" content="text/css" />
		<title><!--WebSiteAdmin-Title--></title>
		<meta name="revisit_after" content="7 days" />
		<meta name="robots" content="ALL" />
		<meta http-equiv="pragma" content="no-cache" />
		<link rel="index" href="index.cgi" />
		<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
		<link rel="stylesheet" href="commons/login.css" type="text/css" />
		<script type="text/javascript" src="../fmail.lib/jquery-1.10.2.min.js"></script>
		<script type="text/javascript" src="commons/login.js"></script>
		<meta name="Keywords" content="tasklogs" />
		<meta name="Description" content="tasklogs" />
	</head>
	<body>
		<div id="wrapper">
			<form id="login" name="login" method="post" action="?m=<!--m-->">
				<input type="text" name="login_user_id" id="user_id" value="<!--user_id-->" />
				<input type="password" name="login_user_password" id="user_password" />
				<input type="submit" value="" id="button" />
				<div id="msg"><!--WebSiteAdmin-Warning--></div>
			</form>
		</div>
		<div id="loginframe"></div>
	</body>
</html>

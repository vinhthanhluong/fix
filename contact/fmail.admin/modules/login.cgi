###############################################################################
# Administrated Screen Global Menu Functions
###############################################################################
$loginframe = <<"EOF";
<table id="login" cellpadding="0" cellspacing="20" background="images/loginframe.gif">
	<tr>
		<td align="right" valign="bottom">
			<div style="width: 330px;height: 130px;text-align: left;">
				<p><!--WebSiteAdmin-Warning--></p>
				<form name="login" method="POST" action="?">
					<table cellspacing="5" cellpadding="0" style="margin-top: 20px;">
						<tr>
							<td align="right">USER ID</td>
							<td colspan="2"><input name="user_id" type="text" id="user_id" value="${user_id}" style="ime-mode: disabled;width: 100%;"></td>
						</tr>
						<tr>
							<td align="right">PASSWORD</td>
							<td><input name="user_password" type="password" id="user_password" style="ime-mode: disabled;"></td>
							<td><input type="submit" name="Submit" value="LOGIN"></td>
						</tr>
					</table>
				</form>
			</div>
		</td>
	</tr>
</table>
EOF

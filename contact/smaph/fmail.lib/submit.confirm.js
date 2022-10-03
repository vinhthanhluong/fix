<!--
//標準ボタン利用時
//document.write('<input type="button" id="submit_confirm" value="確認画面へ進む" class="default_button" onclick="fmail_sending(this.form)" onkeypress="fmail_sending(this.form)" />');
//画像ボタン利用時
document.write('<input type="button" id="submit_confirm" class="submit_confirm_button" value="" title="確認画面へ進む" onclick="fmail_sending(this.form)" onkeypress="fmail_sending(this.form)" />');
//モバイルで邪魔にならないようperl側で処理
//document.write('<div id="mailfrom_hidden_object"><input type="submit" /></div>');
//-->
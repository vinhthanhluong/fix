#!/usr/bin/perl --

use CGI;
use Jcode;
use File::Find;

# perl 5.8.1以降のみ（エラーになる場合は、コピー関連処理をなくす）（メールログを作る時にバックアップ複製を作る場合に利用）
$flag_copy_mod = 1; # 1=使用 / 0=未使用
if($flag_copy_mod){
	use File::Copy;
}
use CGI::Cookie;

# Perl 5.8以降のみ利用可（完了画面での値引継でURLエンコードを使う場合に利用）
$flag_p58 = 1; # 1=使用 / 0=未使用

# 完了画面で入力値をURLエンコード反映する際に利用
if($flag_p58) {
	require './fmail.admin/commons/uriescape.cgi';
}
require './fmail.admin/commons/conf.cgi';
require './fmail.lib.cgi';
require './fmail.admin/commons/mimew.pl';
require './fmail.admin/commons/registry.cgi';

# 古い入力画面用のセッションデータ削除 1 日間保持
&sesclear('./fmail.admin/datas/sessions_files/');

#モバイルでのアクセスの場合の切り分けフラグ。登録されているモバイルブラウザの数だけループ
$flag_mua = 0;
for($mua=0;@MOBILE_USER_AGENT>$mua;$mua++){
	if($ENV{'HTTP_USER_AGENT'} =~ /$MOBILE_USER_AGENT[$mua]/){
		#モバイルの機種に合致したので、フラグON
		$flag_mua = 1;
	}
}

#添付ファイルの可否（有り=1 無し=0）
if($reg{'attached_method'} && $flag_mua == 0){
	$enctype = ' enctype="multipart/form-data"';
}
else {
	$enctype = '';
}

$attached_files_dir = './fmail.admin/datas/attached_files/';
$sessions_files_dir = './fmail.admin/datas/sessions_files/';
&GET;
*getSes = GetCookie($ENV{'HTTP_COOKIE'});
if($_GET{'ses'} ne $null){
	$session = $_GET{'ses'};
}
elsif($getSes{'session'} eq $null || index($getSes{'session'},'/') > -1){
	$session = &createId;
}
else {
	$session = $getSes{'session'};
}

if(&device){
	$sesQuery = "&ses=${session}";
}

$send_token = $sessions_files_dir . $session . '_token.cgi';

@mailform_env = &loadfile('./fmail.admin/datas/modules/mailform_env/mailform_env.dat');
$mailform_env = join("\n",@mailform_env);
($mailform_flag,$expires_start,$expires_end,$limit,$serials,$thanks_page,$sendmail_path,$logsave,$cart_in_element,$cart_logsave,$form_logsave,$form_logsave_period,$send_mode,$attached_mode,$display_mode,$logdata_path,$cart_logdata_path,$mailform_sender_address_name,$mailform_sender_address,$mail_method,$thanks_message,$title_mailform,$title_confirm,$title_error,$title_thanks,$mail_dustclear,$mail_dustclear_zero,$client_info,$site_url,$table_style,$th_style,$td_style,$separate_before,$separate_after,$flag_afiri,$afiri1_tag,$afiri2_tag,$afiri3_tag,$afiri4_tag,$afiri5_tag,$flag_smartphone_tpl,$flag_futurephone_tpl,$setlang,$spamcheck,$domaincheck,$encheck,$txtchange) = split(/\n/,$mailform_env);

@elements = &loadfile('./fmail.admin/datas/modules/elements/elements.dat');
@must = &loadfile('./fmail.admin/datas/modules/must_conditional/must_conditional.dat');

#スマートフォンでのアクセスの場合の切り分けフラグ。登録されているブラウザの数だけループ
$flag_smartphone = 0;
if($flag_smartphone_tpl == 1){
	for($smartphone=0;@SMARTPHONE_USER_AGENT>$smartphone;$smartphone++){
		if($ENV{'HTTP_USER_AGENT'} =~ /$SMARTPHONE_USER_AGENT[$smartphone]/){
			#スマートフォンの機種に合致したので、フラグON
			$flag_smartphone = 1;
		}
	}
}
# 無条件で、デバイスチェックを行う
for($smartphone=0;@SMARTPHONE_USER_AGENT>$smartphone;$smartphone++){
	if($ENV{'HTTP_USER_AGENT'} =~ /$SMARTPHONE_USER_AGENT[$smartphone]/){
		#スマートフォンの機種に合致したので、フラグON
		$flag_smartphone_custom = 1;
	}
}


#フューチャーフォンでのアクセスの場合の切り分けフラグ。登録されているブラウザの数だけループ
$flag_futurephone = 0;
if($flag_futurephone_tpl == 1){
	for($futurephone=0;@MOBILE_USER_AGENT>$futurephone;$futurephone++){
		if($ENV{'HTTP_USER_AGENT'} =~ /$MOBILE_USER_AGENT[$futurephone]/){
			#スマートフォンの機種に合致したので、フラグON
			$flag_futurephone = 1;
		}
	}
}

if($flag_smartphone) {
	# スマホ
	$tpl = './fmail_smartphone.tpl';
} elsif($flag_futurephone) {
	# ガラケー
	$tpl = './fmail_mobile.tpl';
} else {
	# スマフォ以外
	$tpl = './fmail.tpl';
}

$tpl_symbol_title = '<!--%%fmail-printable-area-title%%-->';
$tpl_symbol_title_body = '<!--%%fmail-printable-area-title-body%%-->';
$tpl_symbol_body = '<!--%%fmail-printable-area-body%%-->';
$tpl_symbol_error = '<!--%%fmail-printable-area-error%%-->';
$tpl_symbol_ver = '<!--%%fmail-printable-area-ver%%-->';
if(-f $tpl){
	@html = &loadfile($tpl);
	$html = join("\n",@html);
}

if($_GET{'mode'} eq "send" && -f $send_token){
	if (!$redirect) {
		# unlink "${sessions_files_dir}${session}\.cgi"; # 完了ページへのデータ引継に利用
		unlink $send_token;
		@return_mail_set = &loadfile('./fmail.admin/datas/modules/return_mail/return_mail.dat');
		
		# 通し番号
		&serials();
		
		# POSTデータ取得
		$q = new CGI;
		
		# ログ出力用の配列
		@csv_fields = ($stmp,$session,$serial_number);
		
		# ログ出力用のフラグ
		$flag_log_write = 0;
		
		# 自動返信メール条件が複数存在する場合があるので、先読み
		%getElementById = ();
		for($cnt=0;$cnt<@elements;$cnt++){
			($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt]);
			#項目名の改行処理
			$name =~ s/&lt;-br-&gt;//g;
			
			if($element_type ne "spacer"){
				$elementname = "en${elements_id}";
				@values = $q->param($elementname);
				$values = join("\n",@values);
				$getElementById{$elements_id} = $values;
			}
		}
		
		for($cnt_rmail=0;$cnt_rmail<@return_mail_set;$cnt_rmail++){
			($return_mail_id,$return_mail_type,$return_mail_name,$return_mail_element,$return_mail_value,$return_mail_flag,$return_mail_from,$return_mail_sender,$return_mail_subject,$return_mail_serials,$return_mail_email_field,$return_mail_body) = split(/\t/,$return_mail_set[$cnt_rmail]);
			$return_mail_body =~ s/<br \/>/\n/g;
			
			# 自動返信に通し番号を付ける
			if($return_mail_serials) {
				$mark_serials = '[' . $serial_number . '] ';
			}
			$return_mail_subject = $mark_serials . $return_mail_subject;
			
			if($return_mail_type){
				@logdata = split(/\n/,$logdata);
				$return_values = "";
				%getElementById = ();
				if($mail_method eq "html"){
					$return_mail_body =~ s/&quot;/\"/g;
					$return_mail_body =~ s/\&lt;/</g;
					$return_mail_body =~ s/\&gt;/>/g;
					$return_mail_body =~ s/<br \/>/<br>/g;
				}
				
				##joinエレメントを抽出
				@join_elements = grep(/\tjoin\t/,@elements);
				%join_elements = ();
				%join_values = ();
				for($cnt=0;$cnt<@join_elements;$cnt++){
					($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$join_elements[$cnt]);
					$elementname = "en${elements_id}";
					@values = $q->param($elementname);
					$values = join("\n",@values);
					$safe = 100;
					$empty_str = '';			#入力された値を集める
					while($safe > 0 && $type_of_element =~ /&lt;join id\=\"(.*?)\" name=\"(.*?)\" \/&gt;/){
						$join_id = $1;
						$joinelementname = "en${join_id}";
						@values = $q->param($joinelementname);
						$values = join("\n",@values);

						$empty_str = $empty_str  . $judge_value{$join_id};			#入力された値を集める

						$join_elements{$join_id} = 1;
						$type_of_element =~ s/&lt;join id\=\"$join_id\" name=\"$2\" \/&gt;/$values/g;
						$safe--;
					}
					if(!$empty_str){			#入力された値を集めた結果、空白の場合
						$type_of_element = $empty_str;
					}

					$type_of_element =~ s/<br \/>/\n/g;
					$join_values{$elements_id} = $type_of_element;
					
					#件名置換
					$return_mail_subject =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}/g;
				}
				
				$attcnt = 1;# 複数添付ファイル用カウンタ
				for($cnt=0;$cnt<@elements;$cnt++){
					($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt]);
					
					#項目名の改行処理
					$name =~ s/&lt;-br-&gt;//g;
					
					if($element_type ne "spacer"){
						$elementname = "en${elements_id}";
						@values = $q->param($elementname);
						$values = join("\n",@values);
						
						# ログデータ蓄積（複数個所でため込む為、フラグ管理）
						if(!$flag_log_write && !$log_hidden) {
							$values =~ s/\t/ /g;
							push @csv_fields,$values;
						}
						
						$getElementById{$elements_id} = $values;
						if($join_values{$elements_id}){
							$values = $join_values{$elements_id};
						}
						$crr = "";
						if(index($values,"\n") > 1){
							$crr = "\n";
						}
						if($element_type eq "file" && $values ne $null){
							$save_file_name = "${attached_files_dir}${session}_${elementname}\.cgi";
							if(-f $save_file_name){
								$binary = &mfp_LoadFile($save_file_name);
								# ファイル名の通し番号置き換え
								# 添え字に-1を指定すると下番地（逆順）から取得してくれる
								#$values;
								@filename_extension = split(/\./,$values);
								$values = "$serial\_$attcnt\.$filename_extension[-1]";
								$attcnt ++;
								
								push @file_paths,$values;
								push @file_datas,$binary;
								push @unlinkpath,$save_file_name;
							}
						}
						
						
						if(!$join_elements{$elements_id}){
							# メール本文が非表示になっているものは除外する
							if(!$return_hidden){
								#未入力項目の除外処理 $mail_dustclear=1　「0」除外 $mail_dustclear_zero=1
								#各パターンが入っているので分岐は多い目
								#除外処理が入っていない
								if(!($mail_dustclear) && !($mail_dustclear_zero)){
									if($mail_method eq "html"){
										$return_values .= "<tr><th valign=\"top\" $th_style>${name}</th><td $td_style>${values}</td></tr>\n";
									} else {
										$return_values .= "\n$separate_before${name}$separate_after${crr}${values}${crr}";
									}
								}else{
									#未入力項目の除外処理 $mail_dustclear=1
									if($mail_dustclear && !($mail_dustclear_zero) && $values ne $null){
										if($mail_method eq "html"){
											$return_values .= "<tr><th valign=\"top\" $th_style>${name}</th><td $td_style>${values}</td></tr>\n";
										} else {
											$return_values .= "\n$separate_before${name}$separate_after${crr}${values}${crr}";
										}
										
									#「0」または、「0個」除外 $mail_dustclear_zero=1
									}elsif(!($mail_dustclear) && $mail_dustclear_zero && $values ne '0' && $values ne '0個'){
										if($mail_method eq "html"){
											$return_values .= "<tr><th valign=\"top\" $th_style>${name}</th><td $td_style>${values}</td></tr>\n";
										} else {
											$return_values .= "\n$separate_before${name}$separate_after${crr}${values}${crr}";
										}
										
									#未入力項目の除外処理 $mail_dustclear=1　「0」または、「0個」除外 $mail_dustclear_zero=1
									}elsif($mail_dustclear && $mail_dustclear_zero && $values ne $null && $values ne '0' && $values ne '0個'){
										if($mail_method eq "html"){
											$return_values .= "<tr><th valign=\"top\" $th_style>${name}</th><td $td_style>${values}</td></tr>\n";
										} else {
											$return_values .= "\n$separate_before${name}$separate_after${crr}${values}${crr}";
										}
									}
								}
							}
							#if(!($mail_dustclear) || (($mail_dustclear) && $values ne $null)){
							#	if($mail_method eq "html"){
							#		$return_values .= "<tr><th valign=\"top\">${name}</th><td>${values}</td></tr>";
							#	}
							#	else {
							#		$return_values .= "\n\[ ${name} \] ${crr}${values}${crr}";
							#	}
							#}
							
						}
						if($mail_method eq "html"){
							$return_mail_body =~ s/<${elements_id}>/$values/g;
						}
						else {
							$return_mail_body =~ s/&lt;${elements_id}&gt;/$values/g;
						}
						if($return_mail_email_field eq $elements_id){
							$return_mail_email_address = $values[0];
						}
					}
					#件名置換
					$return_mail_subject =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}/g;
				}
				
				## ENV proccess
				my($user_agent) = $ENV{'HTTP_USER_AGENT'};
				$user_agent =~ s/\t/ /g;
				$user_agent =~ s/\n/ /g;
				$hostname = &gethostname;
				@env_fields = ($hostname,$ENV{'REMOTE_ADDR'},$user_agent,$ENV{'HTTP_REFERER'});
				
				# ログデータ蓄積（複数個所でため込む為、フラグ管理）
				if(!$flag_log_write) {
					push @csv_fields,@env_fields;
				}
				
				# ログ蓄積完了フラグ
				$flag_log_wite = 1;
				
				## to admin send proccess
				if($mail_method eq "html"){
					$admin_mail_body = "<table class=\"mailform\" cellpadding=\"0\" cellspacing=\"0\" $table_style>\n";
					$admin_mail_body .= "<tr><th valign=\"top\" $th_style>ホスト名</th><td $td_style>" . $hostname . "</td></tr>\n";
					$admin_mail_body .= "<tr><th valign=\"top\" $th_style>IPアドレス</th><td $td_style>" . $ENV{'REMOTE_ADDR'} . "</td></tr>\n";
					$admin_mail_body .= "<tr><th valign=\"top\" $th_style>ブラウザ\/OS</th><td $td_style>" . $ENV{'HTTP_USER_AGENT'} . "</td></tr>\n";
					#追加
					$admin_mail_body .= "<tr><th valign=\"top\" $th_style>送信元URL</th><td $td_style>" . $ENV{'HTTP_REFERER'} . "</td></tr>\n";
					$admin_mail_body .= "<tr><th valign=\"top\" $th_style>バージョン</th><td $td_style>" . $reg{'version'} . "</td></tr></table>\n";
					$env_data = $admin_mail_body;
					#$stmp . "\n" . $return_values . $admin_mail_body;
				}
				else {
					$admin_mail_body = "\n\n$separate_beforeホスト名$separate_after" . $hostname . "\n";
					$admin_mail_body .= "$separate_before"."IPアドレス$separate_after" . $ENV{'REMOTE_ADDR'} . "\n";
					$admin_mail_body .= "$separate_beforeブラウザ\/OS$separate_after" . $ENV{'HTTP_USER_AGENT'} . "\n";
					#追加
					$admin_mail_body .= "$separate_before送信元アドレス$separate_after" . $ENV{'HTTP_REFERER'} . "\n";
					$admin_mail_body .= "$separate_beforeバージョン$separate_after" . $reg{'version'} . "\n";
					$env_data = $admin_mail_body;
					#$stmp . "\n" . $return_values . $admin_mail_body;
				}
				
				## send proccess
				if($mail_method eq "html"){
					$return_values = "<table class=\"mailform\" cellpadding=\"0\" cellspacing=\"0\" $table_style>${return_values}</table>\n";
				}
				
				#本文反映用アフィリタグの設定
				$timestamp = $stmp;
				$timestamp =~ s/-//g;
				$timestamp =~ s/://g;
				$timestamp =~ s/ //g;
				$afiri_uniq_id = "$getSes{'session'}$serial";
				
				if(($return_mail_flag) && $return_mail_email_address ne $null){
					## return mail proccess
					if($mail_method eq "html"){
						$return_mail_body =~ s/<serial>/$serial/g;
						$return_mail_body =~ s/<resbody>/$return_values/g;
						$return_mail_body =~ s/<stmp>/$stmp/g;
						$return_mail_body =~ s/<env>/$env_data/g;
						#追加
						$return_mail_body =~ s/<site_url>/$site_url/g;
						$client_info =~ s/<br \/>/<br>/g;
						$return_mail_body =~ s/<client_info>/$client_info/g;
						$return_mail_body =~ s/<afiri_uniq_id>/$afiri_uniq_id/g;
					}
					else {
						$return_mail_body =~ s/&lt;serial&gt;/$serial/g;
						$return_mail_body =~ s/&lt;resbody&gt;/$return_values/g;
						$return_mail_body =~ s/&lt;stmp&gt;/$stmp/g;
						$return_mail_body =~ s/&lt;env&gt;/$env_data/g;
						#追加
						$return_mail_body =~ s/&lt;site_url&gt;/$site_url/g;
						$client_info =~ s/<br \/>/\n/g;
						$return_mail_body =~ s/&lt;client_info&gt;/$client_info/g;
						$return_mail_body =~ s/&lt;afiri_uniq_id&gt;/$afiri_uniq_id/g;
					}
					# 機種依存文字サニタイズ
					if ($txtchange) {
						$return_mail_subject = &sanitizing_str($return_mail_subject);
						$return_mail_sender = &sanitizing_str($return_mail_sender);
						$return_mail_body = &sanitizing_str($return_mail_body);
					}
					# 多言語対応
					if($charset ne 'utf8'){
						# 多言語対応でない
						$return_mail_subject = &sanitizing_str2($return_mail_subject);
						$return_mail_sender = &sanitizing_str2($return_mail_sender);
						$return_mail_body = &sanitizing_str2($return_mail_body);
					}
					
					# 多言語対応
					use MIME::Base64;
					#$setlang = ja or utf8;
					# 言語設定
					$charset = $setlang;
					
					# 多言語対応
					if($charset ne 'utf8'){
						# 多言語対応でない
						$return_mail_body = &encodeJIS($return_mail_body);
						$return_mail_subject = &encodeJIS($return_mail_subject);
						$return_mail_sender = &encodeJIS($return_mail_sender);
						$return_mail_sender = "${return_mail_sender} <${return_mail_from}>";
						$return_mail_sender = Jcode->new($return_mail_sender)->mime_encode;
						$return_mail_subject = Jcode->new($return_mail_subject)->mime_encode;
					}else{
						# 多言語対応
						if($flag_p58) {
							$return_mail_body = &line1000Bytes($return_mail_body); # 強制改行回避
						} else {
							$return_mail_body = $return_mail_body;
						}
						$return_mail_subject = "=?UTF-8?B?" . encode_base64($return_mail_subject) . '?=';
						$return_mail_subject =~ s/\n//ig;
						$return_mail_sender = "=?UTF-8?B?" . encode_base64(${return_mail_sender}) . '?=' . "<${return_mail_from}>";
						$return_mail_sender =~ s/\n//ig;
					}
					
					# -----------------------------------------------
					# 書き込み用データチェック
					$csv_fields = join("\t",@csv_fields);
					$csv_fields =~ s/\r\n/<br \/>/g;
					$csv_fields =~ s/\n/<br \/>/g;
					$csv_fields =~ s/\r//g;
					if (!$csv_fields) {
						&error("エラーが発生しました。画面を戻って画面更新後、再度送信してください");
					}
					# -----------------------------------------------
					
					&sendmail($return_mail_email_address,$null,$null,$return_mail_from,$return_mail_sender,$return_mail_subject,$return_mail_body);
				}
			}
			else {
				# 条件で送信
				@values = split(/\n/,$getElementById{$return_mail_element});
				if(1 == grep(/^${return_mail_value}$/,@values)){
					
					@logdata = split(/\n/,$logdata);
					$return_values = "";
					%getElementById = ();
					if($mail_method eq "html"){
						$return_mail_body =~ s/&quot;/\"/g;
						$return_mail_body =~ s/\&lt;/</g;
						$return_mail_body =~ s/\&gt;/>/g;
						$return_mail_body =~ s/<br \/>/<br>/g;
					}
					
					##joinエレメントを抽出
					@join_elements = grep(/\tjoin\t/,@elements);
					%join_elements = ();
					%join_values = ();
					for($cnt=0;$cnt<@join_elements;$cnt++){
						($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$join_elements[$cnt]);
						$elementname = "en${elements_id}";
						@values = $q->param($elementname);
						$values = join("\n",@values);
						$safe = 100;
						$empty_str = '';			#入力された値を集める
						while($safe > 0 && $type_of_element =~ /&lt;join id\=\"(.*?)\" name=\"(.*?)\" \/&gt;/){
							$join_id = $1;
							$joinelementname = "en${join_id}";
							@values = $q->param($joinelementname);
							$values = join("\n",@values);

							$empty_str = $empty_str  . $judge_value{$join_id};			#入力された値を集める

							$join_elements{$join_id} = 1;
							$type_of_element =~ s/&lt;join id\=\"$join_id\" name=\"$2\" \/&gt;/$values/g;
							$safe--;
						}
						if(!$empty_str){			#入力された値を集めた結果、空白の場合
							$type_of_element = $empty_str;
						}

						$type_of_element =~ s/<br \/>/\n/g;
						$join_values{$elements_id} = $type_of_element;
						
						#件名置換
						$return_mail_subject =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}/g;
					}
					
					$attcnt = 1;# 複数添付ファイル用カウンタ
					for($cnt=0;$cnt<@elements;$cnt++){
						($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt]);
						
						#項目名の改行処理
						$name =~ s/&lt;-br-&gt;//g;
						
						if($element_type ne "spacer"){
							$elementname = "en${elements_id}";
							@values = $q->param($elementname);
							$values = join("\n",@values);
							
							# ログデータ蓄積（複数個所でため込む為、フラグ管理）
							if(!$flag_log_write) {
								$values =~ s/\t/ /g;
								push @csv_fields,$values;
							}
							
							$getElementById{$elements_id} = $values;
							if($join_values{$elements_id}){
								$values = $join_values{$elements_id};
							}
							$crr = "";
							if(index($values,"\n") > 1){
								$crr = "\n";
							}
							if($element_type eq "file" && $values ne $null){
								$save_file_name = "${attached_files_dir}${session}_${elementname}\.cgi";
								if(-f $save_file_name){
									$binary = &mfp_LoadFile($save_file_name);
									# ファイル名の通し番号置き換え
									# 添え字に-1を指定すると下番地（逆順）から取得してくれる
									#$values;
									@filename_extension = split(/\./,$values);
									$values = "$serial\_$attcnt\.$filename_extension[-1]";
									$attcnt ++;
									
									push @file_paths,$values;
									push @file_datas,$binary;
									push @unlinkpath,$save_file_name;
								}
							}
							if(!$join_elements{$elements_id}){
								# メール本文が非表示になっているものは除外する
								if(!$return_hidden){
									#未入力項目の除外処理 $mail_dustclear=1　「0」除外 $mail_dustclear_zero=1
									#各パターンが入っているので分岐は多い目
									#除外処理が入っていない
									if(!($mail_dustclear) && !($mail_dustclear_zero)){
										if($mail_method eq "html"){
											$return_values .= "<tr><th valign=\"top\" $th_style>${name}</th><td $td_style>${values}</td></tr>\n";
										} else {
											$return_values .= "\n$separate_before${name}$separate_after${crr}${values}${crr}";
										}
									}else{
										#未入力項目の除外処理 $mail_dustclear=1
										if($mail_dustclear && !($mail_dustclear_zero) && $values ne $null){
											if($mail_method eq "html"){
												$return_values .= "<tr><th valign=\"top\" $th_style>${name}</th><td $td_style>${values}</td></tr>\n";
											} else {
												$return_values .= "\n$separate_before${name}$separate_after${crr}${values}${crr}";
											}
											
										#「0」または、「0個」除外 $mail_dustclear_zero=1
										}elsif(!($mail_dustclear) && $mail_dustclear_zero && $values ne '0' && $values ne '0個'){
											if($mail_method eq "html"){
												$return_values .= "<tr><th valign=\"top\" $th_style>${name}</th><td $td_style>${values}</td></tr>\n";
											} else {
												$return_values .= "\n$separate_before${name}$separate_after${crr}${values}${crr}";
											}
											
										#未入力項目の除外処理 $mail_dustclear=1　「0」または、「0個」除外 $mail_dustclear_zero=1
										}elsif($mail_dustclear && $mail_dustclear_zero && $values ne $null && $values ne '0' && $values ne '0個'){
											if($mail_method eq "html"){
												$return_values .= "<tr><th valign=\"top\" $th_style>${name}</th><td $td_style>${values}</td></tr>\n";
											} else {
												$return_values .= "\n$separate_before${name}$separate_after${crr}${values}${crr}";
											}
										}
									}
								}
								#if(!($mail_dustclear) || (($mail_dustclear) && $values ne $null)){
								#	if($mail_method eq "html"){
								#		$return_values .= "<tr><th valign=\"top\">${name}</th><td>${values}</td></tr>";
								#	}
								#	else {
								#		$return_values .= "\n\[ ${name} \] ${crr}${values}${crr}";
								#	}
								#}
								
							}
							if($mail_method eq "html"){
								$return_mail_body =~ s/<${elements_id}>/$values/g;
							}
							else {
								$return_mail_body =~ s/&lt;${elements_id}&gt;/$values/g;
							}
							if($return_mail_email_field eq $elements_id){
								$return_mail_email_address = $values[0];
							}
						}
						#件名置換
						$return_mail_subject =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}/g;
					}
					
					## ENV proccess
					my($user_agent) = $ENV{'HTTP_USER_AGENT'};
					$user_agent =~ s/\t/ /g;
					$user_agent =~ s/\n/ /g;
					$hostname = &gethostname;
					@env_fields = ($hostname,$ENV{'REMOTE_ADDR'},$user_agent,$ENV{'HTTP_REFERER'});
					
					# ログデータ蓄積（複数個所でため込む為、フラグ管理）
					if(!$flag_log_write) {
						push @csv_fields,@env_fields;
					}
					
					# ログ蓄積完了フラグ
					$flag_log_write = 1;
					
					## to admin send proccess
					if($mail_method eq "html"){
						$admin_mail_body = "<table class=\"mailform\" cellpadding=\"0\" cellspacing=\"0\" $table_style>\n";
						$admin_mail_body .= "<tr><th valign=\"top\" $th_style>ホスト名</th><td $td_style>" . $hostname . "</td></tr>\n";
						$admin_mail_body .= "<tr><th valign=\"top\" $th_style>IPアドレス</th><td $td_style>" . $ENV{'REMOTE_ADDR'} . "</td></tr>\n";
						$admin_mail_body .= "<tr><th valign=\"top\" $th_style>ブラウザ\/OS</th><td $td_style>" . $ENV{'HTTP_USER_AGENT'} . "</td></tr>\n";
						#追加
						$admin_mail_body .= "<tr><th valign=\"top\" $th_style>送信元URL</th><td $td_style>" . $ENV{'HTTP_REFERER'} . "</td></tr>\n";
						$admin_mail_body .= "<tr><th valign=\"top\" $th_style>バージョン</th><td $td_style>" . $reg{'version'} . "</td></tr></table>\n";
						$env_data = $admin_mail_body;
						#$stmp . "\n" . $return_values . $admin_mail_body;
					}
					else {
						$admin_mail_body = "\n\n$separate_beforeホスト名$separate_after" . $hostname . "\n";
						$admin_mail_body .= "$separate_before"."IPアドレス$separate_after" . $ENV{'REMOTE_ADDR'} . "\n";
						$admin_mail_body .= "$separate_beforeブラウザ\/OS$separate_after" . $ENV{'HTTP_USER_AGENT'} . "\n";
						#追加
						$admin_mail_body .= "$separate_before送信元アドレス$separate_after" . $ENV{'HTTP_REFERER'} . "\n";
						$admin_mail_body .= "$separate_beforeバージョン$separate_after" . $reg{'version'} . "\n";
						$env_data = $admin_mail_body;
						#$stmp . "\n" . $return_values . $admin_mail_body;
					}
					
					## send proccess
					if($mail_method eq "html"){
						$return_values = "<table class=\"mailform\" cellpadding=\"0\" cellspacing=\"0\" $table_style>${return_values}</table>\n";
					}
					
					#本文反映用アフィリタグの設定
					$timestamp = $stmp;
					$timestamp =~ s/-//g;
					$timestamp =~ s/://g;
					$timestamp =~ s/ //g;
					$afiri_uniq_id = "$getSes{'session'}$serial";
					
					if(($return_mail_flag) && $return_mail_email_address ne $null){
						## return mail proccess
						if($mail_method eq "html"){
							$return_mail_body =~ s/<serial>/$serial/g;
							$return_mail_body =~ s/<resbody>/$return_values/g;
							$return_mail_body =~ s/<stmp>/$stmp/g;
							$return_mail_body =~ s/<env>/$env_data/g;
							#追加
							$return_mail_body =~ s/<site_url>/$site_url/g;
							$client_info =~ s/<br \/>/<br>/g;
							$return_mail_body =~ s/<client_info>/$client_info/g;
							$return_mail_body =~ s/<afiri_uniq_id>/$afiri_uniq_id/g;
						}
						else {
							$return_mail_body =~ s/&lt;serial&gt;/$serial/g;
							$return_mail_body =~ s/&lt;resbody&gt;/$return_values/g;
							$return_mail_body =~ s/&lt;stmp&gt;/$stmp/g;
							$return_mail_body =~ s/&lt;env&gt;/$env_data/g;
							#追加
							$return_mail_body =~ s/&lt;site_url&gt;/$site_url/g;
							$client_info =~ s/<br \/>/\n/g;
							$return_mail_body =~ s/&lt;client_info&gt;/$client_info/g;
							$return_mail_body =~ s/&lt;afiri_uniq_id&gt;/$afiri_uniq_id/g;
						}
						# 機種依存文字サニタイズ
						if ($txtchange) {
							$return_mail_subject = &sanitizing_str($return_mail_subject);
							$return_mail_sender = &sanitizing_str($return_mail_sender);
							$return_mail_body = &sanitizing_str($return_mail_body);
						}
						# 多言語対応
						if($charset ne 'utf8'){
							# 多言語対応でない
							$return_mail_subject = &sanitizing_str2($return_mail_subject);
							$return_mail_sender = &sanitizing_str2($return_mail_sender);
							$return_mail_body = &sanitizing_str2($return_mail_body);
						}
						
						# 多言語対応
						use MIME::Base64;
						#$setlang = ja or utf8;
						# 言語設定
						$charset = $setlang;
						
						# 多言語対応
						if($charset ne 'utf8'){
							# 多言語対応でない
							$return_mail_body = &encodeJIS($return_mail_body);
							$return_mail_subject = &encodeJIS($return_mail_subject);
							$return_mail_sender = &encodeJIS($return_mail_sender);
							$return_mail_sender = "${return_mail_sender} <${return_mail_from}>";
							$return_mail_sender = Jcode->new($return_mail_sender)->mime_encode;
							$return_mail_subject = Jcode->new($return_mail_subject)->mime_encode;
						}else{
							# 多言語対応
							if($flag_p58) {
								$return_mail_body = &line1000Bytes($return_mail_body); # 強制改行回避
							} else {
								$return_mail_body = $return_mail_body;
							}
							$return_mail_subject = "=?UTF-8?B?" . encode_base64($return_mail_subject) . '?=';
							$return_mail_subject =~ s/\n//ig;
							$return_mail_sender = "=?UTF-8?B?" . encode_base64(${return_mail_sender}) . '?=' . "<${return_mail_from}>";
							$return_mail_sender =~ s/\n//ig;
						}
						
						# -----------------------------------------------
						# 書き込み用データチェック
						$csv_fields = join("\t",@csv_fields);
						$csv_fields =~ s/\r\n/<br \/>/g;
						$csv_fields =~ s/\n/<br \/>/g;
						$csv_fields =~ s/\r//g;
						if (!$csv_fields) {
							&error("エラーが発生しました。画面を戻って再度送信してください");
						}
						# -----------------------------------------------
						
						&sendmail($return_mail_email_address,$null,$null,$return_mail_from,$return_mail_sender,$return_mail_subject,$return_mail_body);
					}
				}# 条件値で送信
			}# if 条件
		}# for
		
			# -------------------------
			# 本番ログデータ
			$cartstmp = sprintf("%04d-%02d",$year,$mon);
			# エラーログデータ
			$error_logdata_path = './fmail.admin/datas/maillog/errorLog/error_logdata-' . $cartstmp . '.cgi';
			# 書き込みデータの精査
			$csv_fields = join("\t",@csv_fields);
			$csv_fields =~ s/\r\n/<br \/>/g;
			$csv_fields =~ s/\n/<br \/>/g;
			$csv_fields =~ s/\r//g;
			# エラーログ
			@err_file_arr = split(/\//,__FILE__);
			$error_csv_fields = "$err_file_arr[-2]/$err_file_arr[-1]\t" . __LINE__ . "行目\t自動返信管理者宛送信の間\t$serial\t" . $csv_fields;
			&mfp_SaveAddLine($error_logdata_path,$error_csv_fields);
			# -------------------------

		if(!($send_mode)){
			$admin_mail_body = $stmp . "メールフォームよりメールが届きました\n\n&lt;message&gt;\n\n";
		}
		@send_conditional = &loadfile('./fmail.admin/datas/modules/send_conditional/send_conditional.dat');
		for($cnt=0;$cnt<@send_conditional;$cnt++){
			$send_mail_body = $admin_mail_body;
			($send_conditional_id,$send_conditional_type,$send_conditional_name,$send_conditional_element,$send_conditional_value,$send_mailaddress,$send_numname,$send_subject,$send_body,$send_note,$cc,$bcc) = split(/\t/,$send_conditional[$cnt]);
			if($send_conditional_type){
				#HTMLメール
				if($mail_method eq "html"){
					$send_body =~ s/&quot;/\"/g;
					$send_body =~ s/\&lt;/</g;
					$send_body =~ s/\&gt;/>/g;
					$send_body =~ s/<br \/>/<br>/g;
					$send_body =~ s/<serial>/$serial/g;
					$send_body =~ s/<resbody>/$return_values/g;
					$send_body =~ s/<stmp>/$stmp/g;
					$send_body =~ s/<env>/$env_data/g;
					#追加
					$send_body =~ s/<site_url>/$site_url/g;
					$client_info =~ s/<br \/>/<br>/g;
					$send_body =~ s/<client_info>/$client_info/g;
					$send_body =~ s/<afiri_uniq_id>/$afiri_uniq_id/g;
					for($cnt=0;$cnt<@elements;$cnt++){
						($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt]);
						if($join_values{$elements_id}){
							$send_body =~ s/<${elements_id}>/$join_values{$elements_id}/g;
							#件名置換
							$send_subject =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}/g;
							#クライアント宛の送信元の置換（セキュア上良くないので、基本は使わない）
							$mailform_sender_address =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}/g;
							$mailform_sender_address_name =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}　様/g;
						}
						else {
							$send_body =~ s/<${elements_id}>/$getElementById{$elements_id}/g;
							#件名置換
							$send_subject =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}/g;
							#クライアント宛の送信元の置換（セキュア上良くないので、基本は使わない）
							$mailform_sender_address =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}/g;
							$mailform_sender_address_name =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}　様/g;
						}
						# 入力値を反映させる
						if($send_mailaddress =~ /$elements_id/){
							$send_mailaddress_work = "";
							@send_mailaddress_arr = split(/,/,$send_mailaddress);
							for($send_mailaddress_cnt=0; $send_mailaddress_cnt<@send_mailaddress_arr; $send_mailaddress_cnt++){
								if($send_mailaddress_arr[$send_mailaddress_cnt] =~ /$elements_id/){
									$send_mailaddress_arr[$send_mailaddress_cnt] =~ s/$send_mailaddress_arr[$send_mailaddress_cnt]/$getElementById{$elements_id}/g;
									$send_mailaddress_work .= "$send_mailaddress_arr[$send_mailaddress_cnt],";
								}else{
									$send_mailaddress_work .= "$send_mailaddress_arr[$send_mailaddress_cnt],";
								}
							}
							$send_mailaddress = $send_mailaddress_work;
						}
						# 入力値を反映させる
						if($cc =~ /$elements_id/){
							$cc_work = "";
							@cc_arr = split(/,/,$cc);
							for($cc_cnt=0; $cc_cnt<@cc_arr; $cc_cnt++){
								if($cc_arr[$cc_cnt] =~ /$elements_id/){
									$cc_arr[$cc_cnt] =~ s/$cc_arr[$cc_cnt]/$getElementById{$elements_id}/g;
									$cc_work .= "$cc_arr[$cc_cnt],";
								}else{
									$cc_work .= "$cc_arr[$cc_cnt],";
								}
							}
							$cc = $cc_work;
						}
						# 入力値を反映させる
						if($bcc =~ /$elements_id/){
							$bcc_work = "";
							@bcc_arr = split(/,/,$bcc);
							for($bcc_cnt=0; $bcc_cnt<@bcc_arr; $bcc_cnt++){
								if($bcc_arr[$bcc_cnt] =~ /$elements_id/){
									$bcc_arr[$bcc_cnt] =~ s/$bcc_arr[$bcc_cnt]/$getElementById{$elements_id}/g;
									$bcc_work .= "$bcc_arr[$bcc_cnt],";
								}else{
									$bcc_work .= "$bcc_arr[$bcc_cnt],";
								}
							}
							$bcc = $bcc_work;
						}
					}
				}
				else {
					#テキストメール
					$send_body =~ s/<br \/>/\n/g;
					$send_body =~ s/&lt;serial&gt;/$serial/g;
					$send_body =~ s/&lt;resbody&gt;/$return_values/g;
					$send_body =~ s/&lt;stmp&gt;/$stmp/g;
					$send_body =~ s/&lt;env&gt;/$env_data/g;
					#追加
					$send_body =~ s/&lt;site_url&gt;/$site_url/g;
					$client_info =~ s/<br \/>/\n/g;
					$send_body =~ s/&lt;client_info&gt;/$client_info/g;
					$send_body =~ s/&lt;afiri_uniq_id&gt;/$afiri_uniq_id/g;
					for($cnt=0;$cnt<@elements;$cnt++){
						($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt]);
						if($join_values{$elements_id}){
							$send_body =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}/g;
							#件名置換
							$send_subject =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}/g;
							#クライアント宛の送信元の置換（セキュア上良くないので、基本は使わない）
							$mailform_sender_address =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}/g;
							$mailform_sender_address_name =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}　様/g;
						}
						else {
							$send_body =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}/g;
							#件名置換
							$send_subject =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}/g;
							#クライアント宛の送信元の置換（セキュア上良くないので、基本は使わない）
							$mailform_sender_address =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}/g;
							$mailform_sender_address_name =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}　様/g;
						}
						# 入力値を反映させる
						if($send_mailaddress =~ /$elements_id/){
							$send_mailaddress_work = "";
							@send_mailaddress_arr = split(/,/,$send_mailaddress);
							for($send_mailaddress_cnt=0; $send_mailaddress_cnt<@send_mailaddress_arr; $send_mailaddress_cnt++){
								if($send_mailaddress_arr[$send_mailaddress_cnt] =~ /$elements_id/){
									$send_mailaddress_arr[$send_mailaddress_cnt] =~ s/$send_mailaddress_arr[$send_mailaddress_cnt]/$getElementById{$elements_id}/g;
									$send_mailaddress_work .= "$send_mailaddress_arr[$send_mailaddress_cnt],";
								}else{
									$send_mailaddress_work .= "$send_mailaddress_arr[$send_mailaddress_cnt],";
								}
							}
							$send_mailaddress = $send_mailaddress_work;
						}
						# 入力値を反映させる
						if($cc =~ /$elements_id/){
							$cc_work = "";
							@cc_arr = split(/,/,$cc);
							for($cc_cnt=0; $cc_cnt<@cc_arr; $cc_cnt++){
								if($cc_arr[$cc_cnt] =~ /$elements_id/){
									$cc_arr[$cc_cnt] =~ s/$cc_arr[$cc_cnt]/$getElementById{$elements_id}/g;
									$cc_work .= "$cc_arr[$cc_cnt],";
								}else{
									$cc_work .= "$cc_arr[$cc_cnt],";
								}
							}
							$cc = $cc_work;
						}
						# 入力値を反映させる
						if($bcc =~ /$elements_id/){
							$bcc_work = "";
							@bcc_arr = split(/,/,$bcc);
							for($bcc_cnt=0; $bcc_cnt<@bcc_arr; $bcc_cnt++){
								if($bcc_arr[$bcc_cnt] =~ /$elements_id/){
									$bcc_arr[$bcc_cnt] =~ s/$bcc_arr[$bcc_cnt]/$getElementById{$elements_id}/g;
									$bcc_work .= "$bcc_arr[$bcc_cnt],";
								}else{
									$bcc_work .= "$bcc_arr[$bcc_cnt],";
								}
							}
							$bcc = $bcc_work;
						}
					}
				}
				
				#汚染チェック 件名
				$send_subject =~ s/\@/＠/g;
				$send_subject =~ s/\./．/g;
				$send_subject =~ s/\+/＋/g;
				$send_subject =~ s/\-/－/g;
				$send_subject =~ s/\:/：/g;
				$send_subject =~ s/\;/；/g;
				$send_subject =~ s/\|/｜/g;
				$send_subject =~ s/\n//g;
				$send_subject =~ s/\r//g;
				
				#汚染チェック 送信元
				$mailform_sender_address =~ s/\;/；/g;
				$mailform_sender_address =~ s/\n//g;
				$mailform_sender_address =~ s/\r//g;
				
				#汚染チェック 送信元
				$mailform_sender_address_name =~ s/\;/；/g;
				$mailform_sender_address_name =~ s/\n//g;
				$mailform_sender_address_name =~ s/\r//g;
				
				# 機種依存文字サニタイズ
				if ($txtchange) {
					$send_subject = &sanitizing_str($send_subject);
					$mailform_sender_address_name = &sanitizing_str($mailform_sender_address_name);
					$send_body = &sanitizing_str($send_body);
				}
				# 多言語対応
				if($charset ne 'utf8'){
					# 多言語対応しない
					$send_subject = &sanitizing_str2($send_subject);
					$mailform_sender_address_name = &sanitizing_str2($mailform_sender_address_name);
					$send_body = &sanitizing_str2($send_body);
				}
				
				# 多言語対応
				if($charset ne 'utf8'){
					# 多言語対応しない
					$mailform_sender_address_from = "$mailform_sender_address_name <$mailform_sender_address>";
					#一端utf8からsjisに変換し、その後にjisに変換しないと、utf8からjisの場合、一部文字化ける
					Jcode::convert(\$mailform_sender_address_from,"sjis","utf8");
					$mailform_sender_address_from = &encodeJIS($mailform_sender_address_from);
					$mailform_sender_address_from = Jcode->new($mailform_sender_address_from)->mime_encode;
				}else{
					# 多言語対応
					$mailform_sender_address_from = "=?UTF-8?B?" . encode_base64(${mailform_sender_address_name}) . '?=' . "<$mailform_sender_address>";
					$mailform_sender_address_from =~ s/\n//ig;
				}
				
				
				# 多言語対応
				if($charset ne 'utf8'){
					# 多言語対応でない
					$send_mail_body = &encodeJIS($send_body);
				}else{
					# 多言語対応
					if($flag_p58) {
						$send_mail_body = &line1000Bytes($send_body); # 強制改行前処理
					} else {
						$send_mail_body = $send_body;
					}
				}
				
				# シリアル番号名の挿入
				$admin_subject_serial =~ s/<-numname->/$send_numname/g;
				
	#			#一端utf8からsjisに変換し、その後にjisに変換しないと、utf8からjisの場合、一部文字化ける
	#			Jcode::convert(\$send_subject,"sjis","utf8");
				# 多言語対応
				if($charset ne 'utf8'){
					# 多言語対応でない
					$send_subject = &encodeJIS($admin_subject_serial . $send_subject);
					$send_subject = Jcode->new($send_subject)->mime_encode;
				}else{
					# 多言語対応
					$send_subject = "=?UTF-8?B?" . encode_base64($admin_subject_serial . $send_subject) . '?=';
					$send_subject =~ s/\n//ig;
				}
				
				if(@file_paths > 0 && !($attached_mode)){
					sendAttachMail($mailform_sender_address_from,$send_mailaddress,$cc,$bcc, $send_subject, $send_mail_body, @file_datas, @file_paths);
				}
				else {
					&sendmail($send_mailaddress,$cc,$bcc,$mailform_sender_address,$mailform_sender_address_from,$send_subject,$send_mail_body);
				}
			}
			else {
				# 条件で送信
				@values = split(/\n/,$getElementById{$send_conditional_element});
				if(1 == grep(/^${send_conditional_value}$/,@values)){
					$send_body =~ s/<br \/>/\n/g;
					$send_body =~ s/&lt;serial&gt;/$serial/g;
					$send_body =~ s/&lt;resbody&gt;/$return_values/g;
					$send_body =~ s/&lt;stmp&gt;/$stmp/g;
					$send_body =~ s/&lt;env&gt;/$env_data/g;
					#追加
					$send_body =~ s/&lt;site_url&gt;/$site_url/g;
					$client_info =~ s/<br \/>/\n/g;
					$send_body =~ s/&lt;client_info&gt;/$client_info/g;
					$send_body =~ s/&lt;afiri_uniq_id&gt;/$afiri_uniq_id/g;
					for($cnt2=0;$cnt2<@elements;$cnt2++){
						($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt2]);
						if($join_values{$elements_id}){
							$send_body =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}/g;
							#件名置換
							$send_subject =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}/g;
							#クライアント宛の送信元の置換（セキュア上良くないので、基本は使わない）
							$mailform_sender_address =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}/g;
							$mailform_sender_address_name =~ s/&lt;${elements_id}&gt;/$join_values{$elements_id}　様/g;
						}
						else {
							$send_body =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}/g;
							#件名置換
							$send_subject =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}/g;
							#クライアント宛の送信元の置換（セキュア上良くないので、基本は使わない）
							$mailform_sender_address =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}/g;
							$mailform_sender_address_name =~ s/&lt;${elements_id}&gt;/$getElementById{$elements_id}　様/g;
						}
						# 入力値を反映させる
						if($send_mailaddress =~ /$elements_id/){
							$send_mailaddress_work = "";
							@send_mailaddress_arr = split(/,/,$send_mailaddress);
							for($send_mailaddress_cnt=0; $send_mailaddress_cnt<@send_mailaddress_arr; $send_mailaddress_cnt++){
								if($send_mailaddress_arr[$send_mailaddress_cnt] =~ /$elements_id/){
									$send_mailaddress_arr[$send_mailaddress_cnt] =~ s/$send_mailaddress_arr[$send_mailaddress_cnt]/$getElementById{$elements_id}/g;
									$send_mailaddress_work .= "$send_mailaddress_arr[$send_mailaddress_cnt],";
								}else{
									$send_mailaddress_work .= "$send_mailaddress_arr[$send_mailaddress_cnt],";
								}
							}
							$send_mailaddress = $send_mailaddress_work;
						}
						# 入力値を反映させる
						if($cc =~ /$elements_id/){
							$cc_work = "";
							@cc_arr = split(/,/,$cc);
							for($cc_cnt=0; $cc_cnt<@cc_arr; $cc_cnt++){
								if($cc_arr[$cc_cnt] =~ /$elements_id/){
									$cc_arr[$cc_cnt] =~ s/$cc_arr[$cc_cnt]/$getElementById{$elements_id}/g;
									$cc_work .= "$cc_arr[$cc_cnt],";
								}else{
									$cc_work .= "$cc_arr[$cc_cnt],";
								}
							}
							$cc = $cc_work;
						}
						# 入力値を反映させる
						if($bcc =~ /$elements_id/){
							$bcc_work = "";
							@bcc_arr = split(/,/,$bcc);
							for($bcc_cnt=0; $bcc_cnt<@bcc_arr; $bcc_cnt++){
								if($bcc_arr[$bcc_cnt] =~ /$elements_id/){
									$bcc_arr[$bcc_cnt] =~ s/$bcc_arr[$bcc_cnt]/$getElementById{$elements_id}/g;
									$bcc_work .= "$bcc_arr[$bcc_cnt],";
								}else{
									$bcc_work .= "$bcc_arr[$bcc_cnt],";
								}
							}
							$bcc = $bcc_work;
						}
					}
					
					#汚染チェック 件名
					$send_subject =~ s/\@/＠/g;
					$send_subject =~ s/\./．/g;
					$send_subject =~ s/\+/＋/g;
					$send_subject =~ s/\-/－/g;
					$send_subject =~ s/\:/：/g;
					$send_subject =~ s/\;/；/g;
					$send_subject =~ s/\|/｜/g;
					$send_subject =~ s/\n//g;
					$send_subject =~ s/\r//g;
					
					#汚染チェック 送信元
					$mailform_sender_address =~ s/\;/；/g;
					$mailform_sender_address =~ s/\n//g;
					$mailform_sender_address =~ s/\r//g;
					
					#汚染チェック 送信元
					$mailform_sender_address_name =~ s/\;/；/g;
					$mailform_sender_address_name =~ s/\n//g;
					$mailform_sender_address_name =~ s/\r//g;
					
					# 機種依存文字サニタイズ
					if ($txtchange) {
						$mailform_sender_address_name = &sanitizing_str($mailform_sender_address_name);
						$send_subject = &sanitizing_str($send_subject);
						$send_body = &sanitizing_str($send_body);
					}
					# 多言語対応
					if($charset ne 'utf8'){
						# 多言語対応でない
						$mailform_sender_address_name = &sanitizing_str2($mailform_sender_address_name);
						$send_subject = &sanitizing_str2($send_subject);
						$send_body = &sanitizing_str2($send_body);
					}
					
					# 多言語対応
					if($charset ne 'utf8'){
						# 多言語対応でない
						$mailform_sender_address_from = "$mailform_sender_address_name <$mailform_sender_address>";
						#一端utf8からsjisに変換し、その後にjisに変換しないと、utf8からjisの場合、一部文字化ける
						Jcode::convert(\$mailform_sender_address_from,"sjis","utf8");
						$mailform_sender_address_from = &encodeJIS($mailform_sender_address_from);
						$mailform_sender_address_from = Jcode->new($mailform_sender_address_from)->mime_encode;
					}else{
						# 多言語対応
						$mailform_sender_address_from = "=?UTF-8?B?" . encode_base64($mailform_sender_address_name) . '?=' . "<$mailform_sender_address>";
						$mailform_sender_address_from =~ s/\n//ig;
					}
					
					#$send_mail_body =~ s/&lt;message&gt;/$send_body/g;
					$send_mail_body = $send_body;
					
					
					# 多言語対応
					if($charset ne 'utf8'){
						# 多言語対応でない
						$send_mail_body = &encodeJIS($send_mail_body);
					} else {
						if($flag_p58) {
							$send_mail_body = &line1000Bytes($send_mail_body); # 強制改行前処理
						} else {
							$send_mail_body = $send_mail_body;
						}
					}
					
					# シリアル番号名の挿入
					$admin_subject_serial =~ s/<-numname->/$send_numname/g;
					
	#				#一端utf8からsjisに変換し、その後にjisに変換しないと、utf8からjisの場合、一部文字化ける
	#				Jcode::convert(\$send_subject,"sjis","utf8");
					# 多言語対応
					if($charset ne 'utf8'){
						# 多言語対応でない
						$send_subject = &encodeJIS($admin_subject_serial . $send_subject);
						$send_subject = Jcode->new($send_subject)->mime_encode;
					}else{
						# 多言語対応
						$send_subject = "=?UTF-8?B?" . encode_base64($admin_subject_serial . $send_subject) . '?=';
						$send_subject =~ s/\n//ig;
					}
					if(@file_paths > 0 && !($attached_mode)){
						sendAttachMail($mailform_sender_address_from,$send_mailaddress,$cc,$bcc, $send_subject, $send_mail_body, @file_datas, @file_paths);
					}
					else {
						&sendmail($send_mailaddress,$cc,$bcc,$mailform_sender_address,$mailform_sender_address_from,$send_subject,$send_mail_body);
					}
				}
			}
		}
		
		
		
		# ----------------------------------------------------------------
		## mail log save proccess
		# ----------------------------------------------------------------
		if($logsave){
			# 本番ログデータ
			$cartstmp = sprintf("%04d-%02d",$year,$mon);
			
			if($logdata_path eq $null){
				$logdata_path = './fmail.admin/datas/maillog/mail_logdata' . '-' . $cartstmp . '.cgi';
			} else {
				$logdata_path = $logdata_path . 'mail_logdata' . '-' . $cartstmp . '.cgi';
			}
			# バックアップデータ
			$logdata_bu_path = $logdata_path . '.backup';
			
			# エラーログデータ
			$error_logdata_path = './fmail.admin/datas/maillog/errorLog/error_logdata-' . $cartstmp . '.cgi';
			
			# save判定用フラグ初期化
			$flag_savelog = 1;
			
			# 書き込みデータの精査
			$csv_fields = join("\t",@csv_fields);
			$csv_fields =~ s/\r\n/<br \/>/g;
			$csv_fields =~ s/\n/<br \/>/g;
			$csv_fields =~ s/\r//g;
			if($flag_copy_mod) {
				# Copyモジュールを使う場合
				while($flag_savelog == 1){
					# 保存前容量のチェック
					# 本番ファイル
					$logdata_capacity = -s $logdata_path;
					# BUファイル
					$logdata_bu_capacity = -s $logdata_bu_path;
					
					# 本番とBUファイル容量比較
					if($logdata_capacity < $logdata_bu_capacity){
						# 本番ファイルが壊れている可能性あり
						copy($logdata_bu_path, $logdata_path);
						
						# エラーログ
						@err_file_arr = split(/\//,__FILE__);
						$error_csv_fields = "$err_file_arr[-2]/$err_file_arr[-1]\t" . __LINE__ . "行目\t本番ファイル破損の復旧\t$serial";
						&mfp_SaveAddLine($error_logdata_path,$error_csv_fields);
						
					}elsif($logdata_capacity > $logdata_bu_capacity){
						# BUファイルが壊れている可能性あり
						copy($logdata_path, $logdata_bu_path);
						
						# エラーログ
						@err_file_arr = split(/\//,__FILE__);
						$error_csv_fields = "$err_file_arr[-2]/$err_file_arr[-1]\t" . __LINE__ . "行目\tBUファイル破損の復旧\t$serial";
						&mfp_SaveAddLine($error_logdata_path,$error_csv_fields);
						
					}
					# ここまでで、本番＝BUとなっている
					
					$logdata_capacity = '';
					$logdata_after_capacity = '';
					
					# 保存前容量のチェック
					# 本番ファイル
					$logdata_capacity = -s $logdata_path;
					
					# 本番ファイル保存
					&mfp_SaveAddLine($logdata_path,$csv_fields);
					
					# 本番ファイル保存後容量のチェック
					$logdata_after_capacity = -s $logdata_path;
					
					# 本番ファイル保存前と保存後の容量を比較
					if($logdata_capacity < $logdata_after_capacity){
						# 保存後の方が容量大。正常保存と判断。バックアップデータを作成。
						copy($logdata_path, $logdata_bu_path);
						# 正常保存なので、ループエンドさせる為、フラグを折る
						$flag_savelog = 9;
						
						# エラーログ
						@err_file_arr = split(/\//,__FILE__);
						$error_csv_fields = "$err_file_arr[-2]/$err_file_arr[-1]\t" . __LINE__ . "行目\t追書込正常保存\t$serial";
						&mfp_SaveAddLine($error_logdata_path,$error_csv_fields);
						
					}else{
						# 保存後の方が容量小。保存失敗と判断。バックアップデータから復旧。
						copy($logdata_bu_path, $logdata_path);
						
						# エラーログ
						@err_file_arr = split(/\//,__FILE__);
						$error_csv_fields = "$err_file_arr[-2]/$err_file_arr[-1]\t" . __LINE__ . "行目\tロールバック（本番 $logdata_after_capacity byte）\t$serial\t" . $csv_fields;
						&mfp_SaveAddLine($error_logdata_path,$error_csv_fields);
						
						# whileに戻ってもう一度処理のやり直し
					}
				}
			} else {
				# Copyモジュールを使わない場合
				# 本番ファイル保存
				&mfp_SaveAddLine($logdata_path,$csv_fields);
			}
			chmod 0644, "$logdata_bu_path";
		}
		
		
		
		# ----------------------------------------------------------------
		## cart log save proccess
		# ----------------------------------------------------------------
		# Cartitems Temporary Data
		$temp_file_cartitems = './cart/cart.admin/datas/cart.items/';
		
		# セッションチェック
			
		#-- Get the whole Cookie --#
		my %cookies = fetch CGI::Cookie;

		#-- Gets the value of the Cookie --#
		if(exists $cookies{'socket'}){
			$cookies_value = $cookies{'socket'}->value; #値
			$cookies_expires = $cookies{'socket'}->expires; #賞味期限
			$cookies_domain  = $cookies{'socket'}->domain;  #有効なドメイン
			$cookies_path = $cookies{'socket'}->path; #有効なパス
		}
		
		$cartitems_file = $temp_file_cartitems . $cookies_value . '.cgi';
		
		
		if($cart_logsave){
			# 本番ログデータ
			$cartstmp = sprintf("%04d-%02d",$year,$mon);
			
			if($cart_logdata_path eq $null){
				$cart_logdata_path = './fmail.admin/datas/cartlog/cart_logdata' . '-' . $cartstmp . '.cgi';
			} else {
				$cart_logdata_path = $cart_logdata_path . 'cart_logdata' . '-' . $cartstmp . '.cgi';
			}
			
			# バックアップデータ
			$logdata_bu_path = $cart_logdata_path . '.backup';
			
			
			open(CART,"<$cartitems_file");
				while($cart_table = <CART>) {
					# カート内データの整形
					$cart_table =~ s/\r//g;
					$cart_table =~ s/\n//g;
					@cart_table_arr = split(/,/,$cart_table);
					
					# save判定用フラグ初期化
					$flag_savelog = 1;
					
					# 書き込みデータの精査
					$csv_fields = "$cookies_value\t";
					$csv_fields .= join("\t",@cart_table_arr);
					$csv_fields .= "\t";
					$csv_fields .= join("\t",@csv_fields);
					$csv_fields =~ s/\r\n/<br \/>/g;
					$csv_fields =~ s/\n/<br \/>/g;
					$csv_fields =~ s/\r//g;
					
					if($flag_copy_mod) {
						# Copyモジュールを使う場合
						while($flag_savelog == 1){
							# 保存前容量のチェック
							# 本番ファイル
							$logdata_capacity = -s $cart_logdata_path;
							# BUファイル
							$logdata_bu_capacity = -s $logdata_bu_path;
							
							# 本番とBUファイル容量比較
							if($logdata_capacity < $logdata_bu_capacity){
								# 本番ファイルが壊れている可能性あり
								copy($logdata_bu_path, $cart_logdata_path);
							}elsif($logdata_capacity > $logdata_bu_capacity){
								# BUファイルが壊れている可能性あり
								copy($cart_logdata_path, $logdata_bu_path);
							}
							# ここまでで、本番＝BUとなっている
							
							
							# 保存前容量のチェック
							# 本番ファイル
							$logdata_capacity = -s $cart_logdata_path;
							
							# 本番ファイル保存
							&mfp_SaveAddLine($cart_logdata_path,$csv_fields);
							
							# 本番ファイル保存後容量のチェック
							$logdata_after_capacity = -s $cart_logdata_path;
							
							# 本番ファイル保存前と保存後の容量を比較
							if($logdata_capacity < $logdata_after_capacity){
								# 保存後の方が容量大。正常保存と判断。バックアップデータを作成。
								copy($cart_logdata_path, $logdata_bu_path);
								# 正常保存なので、ループエンドさせる為、フラグを折る
								$flag_savelog = 9;
							}else{
								# 保存後の方が容量小。保存失敗と判断。バックアップデータから復旧。
								copy($logdata_bu_path, $cart_logdata_path);
							}
						}
					} else {
						# Copyモジュールを使わない場合
						# 本番ファイル保存
						&mfp_SaveAddLine($cart_logdata_path,$csv_fields);
					}
					chmod 0644, "$logdata_bu_path";
				}
			close(CART);
		}
		
		
		
		
		## att delete prrocess
		if(!$attached_mode){
			for($cnt=0;$cnt<@unlinkpath;$cnt++){
				unlink $unlinkpath[$cnt];
			}
		}
		
		if($thanks_page ne $null){
			$redirect = $thanks_page;
		}
		else {
			# カートデータの削除
			&cart_del;
			
			# 完了ページへのリダイレクト
			$redirect = 'index.cgi?mode=thanks' . $sesQuery;
		}
		#$session = "";
	}
}
elsif($_GET{'mode'} eq "thanks"){
	#送信完了画面
	
	# ダイレクトにbackパラメータURLにアクセスされた場合に、入力ページへリダイレクトする--------------------
	# 直前URL取得（パラメータ付）
	my @ref_url_arr = split(/\//,$ENV{'HTTP_REFERER'});
	# 現在URL取得（パラメータ付）
	my $q = CGI->new();
	my @now_url_arr = split(/\//,$q->url);
	
	# 直前ページが、同じ階層かを確認
	# 直前ページが、index.cgiか
	if ($ref_url_arr[-1] eq 'index.cgi?mode=confirm') {
		# 直前ページFmailフォルダと現在Fmailフォルダが違う場合は、入力ページへ
		if ($ref_url_arr[-2] ne $now_url_arr[-2]) {
			print "Location: ./\n\n";
		}
	} else {
		print "Location: ./\n\n";
	}
	# -------------------------------------------------------------------------------------------------------
	
	
	
	$title = $title_thanks;
	$title_body = '<span id="fmail_title_thanks">' . $title_thanks . '</span>';
	$contents = "<div id=\"fmail_thankspage\">${thanks_message}</div>";
		#HTML装飾を許可にしている。不要ならコメントアウト
		$contents =~ s/&lt;/</g;
		$contents =~ s/&gt;/>/g;
	#トップへ戻るボタン追加
	if($site_url){
		$contents .= "\n\n<p class=\"site_top\"><a href=\"$site_url\">トップページへ</a></p>\n\n";
	}
	#アフィリエイトタグ追加
	if($flag_afiri){
		$afiri1_tag =~ s/&lt;/</g;
		$afiri1_tag =~ s/&gt;/>/g;
		$afiri2_tag =~ s/&lt;/</g;
		$afiri2_tag =~ s/&gt;/>/g;
		$afiri3_tag =~ s/&lt;/</g;
		$afiri3_tag =~ s/&gt;/>/g;
		$afiri4_tag =~ s/&lt;/</g;
		$afiri4_tag =~ s/&gt;/>/g;
		$afiri5_tag =~ s/&lt;/</g;
		$afiri5_tag =~ s/&gt;/>/g;
#		$contents .= "$afiri1_tag\n$afiri2_tag\n$afiri3_tag\n$afiri4_tag\n$afiri5_tag\n";
		$html =~ s/\$afiri1_tag/$afiri1_tag/g;
		$html =~ s/\$afiri2_tag/$afiri2_tag/g;
		$html =~ s/\$afiri3_tag/$afiri3_tag/g;
		$html =~ s/\$afiri4_tag/$afiri4_tag/g;
		$html =~ s/\$afiri5_tag/$afiri5_tag/g;
	}
	
	# 引継セッションデータ読み込み
	@getsession = &WppLoadLine(${sessions_files_dir} . ${session} . '.cgi');
	# セッションデータ削除
	unlink "${sessions_files_dir}${session}\.cgi";
	# 引継データの置換
	for($i=0; @getsession>$i; $i++) {
		@getsession_arr = split(/=/,$getsession[$i]);
		# URLエンコード表示
		if($flag_p58) {
			$encodedata = uri_escape($getsession_arr[1]);
			$contents =~ s/<urlenc_$getsession_arr[0]>/$encodedata/g; # アフィリエイト
			$html =~ s/<urlenc_$getsession_arr[0]>/$encodedata <urlenc_$getsession_arr[0]>/g; # 他全て
		}
		# プレーン表示
		$contents =~ s/<$getsession_arr[0]>/$getsession_arr[1]/g; # アフィリエイト
		$html =~ s/<$getsession_arr[0]>/$getsession_arr[1] <$getsession_arr[0]>/g; # 他全て
	}
	# 無駄コードの削除
	for($i=0; @getsession>$i; $i++) {
		@getsession_arr = split(/=/,$getsession[$i]);
		# URLエンコード表示
		if($flag_p58) {
			$encodedata = uri_escape($getsession_arr[1]);
			$html =~ s/ <urlenc_$getsession_arr[0]>//g; # 他全て
		}
		# プレーン表示
		$html =~ s/ <$getsession_arr[0]>//g; # 他全て
	}

}
elsif($_GET{'mode'} eq "confirm"){
	#確認画面
	unlink $send_token;
	##create session
	$q = new CGI;
	@session_data = ();
	%judge_value = ();
	%filetype_error = ();
	%filetype_name = ();
	$file_error_flag = 0;
	
	%sanitizing_error = ();
	$sanitizing_error_flag = 0;
	%sanitizing_value = ();
	
	##match pref
	@match_elements = ();
	%match_elements_vals = ();
	@names = $q->param;
	for($cnt=0;$cnt<@names;$cnt++){
		$name = $names[$cnt];
		if(index($name,'_match') > -1){
			push @match_elements,$name;
			$match_elements_vals{$name} = $q->param($names[$cnt]);
			push @session_data,"${name}=$match_elements_vals{$name}";
			$matchObj .= "<input type=\"hidden\" name=\"${name}\" value=\"$match_elements_vals{$name}\" \/>";
		}
	}
	$spam_flag = 1;
	$en_flag = 1;
	$link_spam_flag = 0;
	for($cnt=0;$cnt<@elements;$cnt++){
		($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt]);
		$elementname = "en${elements_id}";
		
		if($element_type ne "file"){
			@values = $q->param($elementname);
			$judge_value{$elements_id} = join('<-sp->',@values);
			for($i=0;$i<@values;$i++){
				## sanitizing
				if($element_type eq "text" || $element_type eq "textarea"){
					# 住所のみ正規化を外す
					if($check_type ne "addr"){
						if ($txtchange) {
							$values[$i] = &sanitizing_str($values[$i]);
						}
					}
					# 全文数字のみ確認
					if(!($values[$i] !~ /[\x80-\xff]/)){
						$en_flag = 0;
					}
					# スパムフィルタ
					if($values[$i] =~ /\[\/url\]/si){
						$link_spam_flag = 1;
					}
					# スパムフィルタ
					if($values[$i] =~ /\[\/link\]/si){
						$link_spam_flag = 1;
					}
					if($check_type ne "none" && $values[$i] ne $null){
						if($check_type eq "digit" && $values[$i] =~ /[^0-9.\-]/){
							$sanitizing_error{$elements_id} = "数字以外の文字が含まれています。<br />";
							push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
							$sanitizing_error_flag = 1;
						}
						if($check_type eq "demilit" && $values[$i] =~ /[^0-9.,\-]/){
							$sanitizing_error{$elements_id} = "数字以外の文字が含まれています。<br />";
							push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
							$sanitizing_error_flag = 1;
						}
						if($check_type eq "alphabet" && $values[$i] =~ /[^a-zA-Z]/){
							$sanitizing_error{$elements_id} = "半角英字以外の文字が含まれています。<br />";
							push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
							$sanitizing_error_flag = 1;
						}
						if($check_type eq "digitandalphabet" && $values[$i] =~ /[^a-zA-Z0-9]/){
							$sanitizing_error{$elements_id} = "半角英数字以外の文字が含まれています。<br />";
							push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
							$sanitizing_error_flag = 1;
						}
						if($check_type eq "mobilephone"){
							$tmp = $values[$i];
							$tmp =~ s/\-//g;
							$c = length($tmp);
							if($tmp =~ /[^0-9]/){
								$sanitizing_error{$elements_id} = "数字以外の文字が含まれています。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
							elsif($c != 11){
								$sanitizing_error{$elements_id} = "電話番号の桁数に誤りがあります。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
							else {
								$mobilephone[0] = substr($tmp, 0, 3);
								$mobilephone[1] = substr($tmp, 3, 4);
								$mobilephone[2] = substr($tmp, 7, 4);
								$values[$i] = join('-',@mobilephone);
							}
						}
						if($check_type eq "postcode"){
							$tmp = $values[$i];
							$tmp =~ s/\-//g;
							$c = length($tmp);
							if($tmp =~ /[^0-9]/){
								$sanitizing_error{$elements_id} = "数字以外の文字が含まれています。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
							elsif($c > 7){
								$sanitizing_error{$elements_id} = "郵便番号の桁数に誤りがあります。７桁以内で入力してください。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
							else {
								@mobilephone =();
								$mobilephone[0] = substr($tmp, 0, 3);
								if($c > 3){
									$mobilephone[1] = substr($tmp, 3, 4);
									$values[$i] = join('-',@mobilephone);
								}
							}
						}
						if($check_type eq "telephone"){
							$tmp = $values[$i];
							$tmp =~ s/\-//g;
							$tmp =~ s/\+//g;
							$c = length($tmp);
							if($tmp =~ /[^0-9]/){
								$sanitizing_error{$elements_id} = "数字以外の文字が含まれています。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
							elsif($c != 11 && $c != 10){
								# 固定電話だけでなく、携帯電話の入力も踏まえて、10桁と11桁を許可する
								$sanitizing_error{$elements_id} = "電話番号の桁数に誤りがあります。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
#							elsif(split(/\-/,$values[$i]) != 3){
#								$sanitizing_error{$elements_id} = "電話番号はハイフンで区切って入力してください。<br />";
#								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
#								$sanitizing_error_flag = 1;
#							}
						}
						#追加
						if($check_type eq "fax"){
							$tmp = $values[$i];
							$tmp =~ s/\-//g;
							$tmp =~ s/\+//g;
							$c = length($tmp);
							if($tmp =~ /[^0-9]/){
								$sanitizing_error{$elements_id} = "数字以外の文字が含まれています。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
							elsif($c != 10){
								$sanitizing_error{$elements_id} = "FAX番号の桁数に誤りがあります。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
#							elsif(split(/\-/,$values[$i]) != 3){
#								$sanitizing_error{$elements_id} = "FAX番号はハイフンで区切って入力してください。<br />";
#								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
#								$sanitizing_error_flag = 1;
#							}
						}
						if($check_type eq "mail"){
							if($values[$i] =~ /[^a-zA-Z0-9\.\@\-\_\+]/){
								$sanitizing_error{$elements_id} = "メールアドレスで使えない文字が含まれています。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
							elsif(split(/\@/,$values[$i]) != 2){
								$sanitizing_error{$elements_id} = "メールアドレスに誤りがあります。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
							elsif(!($values[$i] =~ /^([a-zA-Z0-9\.\-\/_]{1,})@([a-zA-Z0-9\.\-\/_]{1,})\.([a-zA-Z0-9\.\-\/_]{1,})$/)){
								$sanitizing_error{$elements_id} = "メールアドレスに誤りがあります。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
						}
						if($check_type eq "url"){
							$tmp = $values[$i];
							$c = length($tmp);
							if($tmp !~ /^http:\/\/.+/ && $tmp !~ /^https:\/\/.+/ ){
								$sanitizing_error{$elements_id} = "URLに誤りがあります。<br />";
								push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
								$sanitizing_error_flag = 1;
							}
						}
						if($check_type eq "addr" && $values[$i] =~ /[a-zA-Z0-9|-]/){
							$sanitizing_error{$elements_id} = "全て全角で入力してください。<br />";
							push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
							$sanitizing_error_flag = 1;
						}
					}
					$c = $values[$i];
					$c =~ s/[\r\n\s]//g; 
					
					if($flag_p58) {
						# perl5.8以降のみ
						$textsize = length(decode('utf-8', $c));
					} else {
						$textsize = length($c);
					}
					if(($text_min > $textsize && $text_min ne $null) || ($textsize > $text_max && $text_max ne $null)){
						$sanitizing_error{$elements_id} = "現在$textsize文字です。文字数は${text_min}文字から${text_max}文字の範囲で入力してください。<br />";
						push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
						$sanitizing_error_flag = 1;
					}
					
					## matching proccess
					$match_hash = $elementname . '_match';
					if(1 == grep(/^${match_hash}$/ig,@match_elements)){
						if($match_elements_vals{$match_hash} ne $values[$i]){
							$sanitizing_error{$elements_id} = "入力内容が確認用の内容と異なっています。<br />";
							push @session_data,"en${elements_id}_error=" . $sanitizing_error{$elements_id};
							push @session_data,"en${elements_id}_match=" . $match_elements_vals{$match_hash};
							$sanitizing_error_flag = 1;
						}
					}
					
					$sanitizing_value{$elements_id} = $values[$i];
				}
				$values[$i] =~ s/\=/<eq>/g;
				$values[$i] =~ s/\&/<amp>/g;
				$values[$i] =~ s/\n/<-br->/g;
				push @session_data,"en${elements_id}=${values[$i]}";
			}
		}
		else {
			if($q->param($elementname) ne $null){
				@enabled_filetypes = split(/\,/,$enable_filetypes);
				my $fH = $q->upload($elementname);
				@filenames = split(/\\/,$fH);
				$filename = $filenames[-1];
				@filetypes = split /\./,$filename;
				$filetype = $filetypes[-1];
				$save_file_name = "${attached_files_dir}${session}_${elementname}\.cgi";
				$file_bytes = 0;
				open (OUT, ">$save_file_name");
				binmode (OUT);
				while(read($fH, $buffer, 1024)){
					print OUT $buffer;
					$file_bytes += 1024;
				}
				close (OUT);
				close ($fH) if ($CGI::OS ne 'UNIX');
				chmod 0600, $save_file_name;
				$file_bytes = $file_bytes / 1024;
				if(1 == grep(/^${filetype}$/ig,@enabled_filetypes)){
					if(($filesize_min > $file_bytes && $filesize_min ne $null) || ($file_bytes > $filesize_max && $filesize_max ne $null)){
						unlink $save_file_name;
						$filetype_error{$elements_id} = "ファイルサイズは${filesize_min}KBから${filesize_max}KBの範囲で選択してください。<br />";
						push @session_data,"en${elements_id}_error=" . $filetype_error{$elements_id};
						$file_error_flag = 1;
					}
					else {
						$judge_value{$elements_id} = $fH;
						push @session_data,"en${elements_id}=${filename}";
						$filetype_name{$elementname} = $filename;
					}
				}
				else {
					unlink $save_file_name;
					$filetype_error{$elements_id} = "対応していないファイルが選択されています。<br />";
					push @session_data,"en${elements_id}_error=" . $filetype_error{$elements_id};
					$file_error_flag = 1;
				}
			}
		}
		## text format check
	}
	
	##must check
	$send_flag = 0;
	$error_code = "";
	@errorCounters = ();
	$flag_case_result = 0;
	for($cnt=0;$cnt<@must;$cnt++){
#		($conditional_id,$must_name,$error_message,$must_elements,$note) = split(/\t/,$must[$cnt]);
		($conditional_id,$must_name,$error_message,$must_elements,$note,$flag_case,$case_elements_id,$case_value) = split(/\t/,$must[$cnt]);
		@must_elements = split(/\&/,$must_elements);
		$must_flag = 1;
		$errorCounter = 0;
		# 条件による必須の変更
		# n個の条件指定を確認し、未合致の場合、すべて送信が適用される。
		# 条件指定に一度でも合致したら、他の条件はスルーさせる
		if($flag_case_result == 0){
			if($flag_case == 0){
				# 条件指定
				# 条件指定した値と、合致している時に適用
				if($case_value eq $judge_value{$case_elements_id}){
					for($i=0;$i<@must_elements;$i++){
						($elements_id,$elements_value) = split(/\=/,$must_elements[$i]);
						if($elements_value ne $null){
							# 条件指定の値と当該項目の値を比較
							if($elements_value eq "1" && $judge_value{$elements_id} eq $null){
								$must_flag = 0;
								$error_code = $conditional_id;
								$errorCounter++;
							}
							elsif($elements_value eq "1" && $judge_value{$elements_id} ne $null){
								
							}
							elsif($judge_value{$elements_id} ne $null) {
								@values = split(/<-sp->/,$judge_value{$elements_id});
								if(1 != grep(/^${elements_value}$/,@values)){
									$must_flag = 0;
									$error_code = $conditional_id;
									$errorCounter++;
								}
							}
							else {
								$must_flag = 0;
								$error_code = $conditional_id;
								$errorCounter++;
							}
						}
					}
					push @errorCounters,"${conditional_id}\t${errorCounter}";
					if($must_flag){
						$send_flag++;
					}
					# 条件指定で一致しているので、以降の処理は無視する為のフラグ
					$flag_case_result = 1;
				}
			}else{
				# すべて送信
				for($i=0;$i<@must_elements;$i++){
					($elements_id,$elements_value) = split(/\=/,$must_elements[$i]);
					if($elements_value ne $null){
						if($elements_value eq "1" && $judge_value{$elements_id} eq $null){
							$must_flag = 0;
							$error_code = $conditional_id;
							$errorCounter++;
						}
						elsif($elements_value eq "1" && $judge_value{$elements_id} ne $null){
							
						}
						elsif($judge_value{$elements_id} ne $null) {
							@values = split(/<-sp->/,$judge_value{$elements_id});
							if(1 != grep(/^${elements_value}$/,@values)){
								$must_flag = 0;
								$error_code = $conditional_id;
								$errorCounter++;
							}
						}
						else {
							$must_flag = 0;
							$error_code = $conditional_id;
							$errorCounter++;
						}
					}
				}
				push @errorCounters,"${conditional_id}\t${errorCounter}";
				if($must_flag){
					$send_flag++;
				}
			}
		}
	}
	
	## file error & format error
	if($file_error_flag){
		$send_flag = 0;
		$error_code = "";
	}
	if($sanitizing_error_flag){
		$send_flag = 0;
		$error_code = "";
	}
	
	## spam check
	if($spamcheck){
		# スパムチェック
		if($link_spam_flag){
			$send_flag = 0;
			push @session_data,"spam_error=スパム対策のため\[\/link\]や\[\/url\]が含まれる送信はできません。";
		}
	}
	## en check
	if($encheck){
		# 全文英数チェック
		if($en_flag){
			$send_flag = 0;
			push @session_data,"spam_error=すべての入力項目が英数で入力されています。";
		}
	}
	## domain check
	if($domaincheck){
		# ドメインチェック
		$http_host = $ENV{'HTTP_HOST'};
		$referer = $ENV{'HTTP_REFERER'};
		if($referer !~ /$http_host/){
			$send_flag = 0;
			push @session_data,"spam_error=別ホストからのリクエストの為、送信はできません。";
		}
	}
	
	if($send_flag > 0){
		$title = $title_confirm;
		$title_body = '<span id="fmail_title_confirm">' . $title_confirm . '</span>';
		#モバイル判定
		if(!$flag_mua && !$flag_smartphone){
			$contents = "\n<table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" class=\"mailform\" summary=\"mailform main\">\n";
		}
		
		##joinエレメントを抽出
		@join_elements = grep(/\tjoin\t/,@elements);
		%join_elements = ();
		%join_values = ();
		for($cnt=0;$cnt<@join_elements;$cnt++){
			($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$join_elements[$cnt]);
			$safe = 100;
			$empty_str = '';			#入力された値を集める
			while($safe > 0 && $type_of_element =~ /&lt;join id\=\"(.*?)\" name=\"(.*?)\" \/&gt;/){
				$join_id = $1;
				$join_elements{$join_id} = 1;
				$judge_value{$join_id} =~ s/\"/&quot;/g;
				$judge_value{$join_id} =~ s/</\&lt;/g;
				$judge_value{$join_id} =~ s/>/\&gt;/g;
				@values = split(/&lt;-sp-&gt;/,$judge_value{$join_id});
				$judge_value{$join_id} = join("\n",@values);

				$empty_str = $empty_str  . $judge_value{$join_id};			#入力された値を集める

				$type_of_element =~ s/&lt;join id\=\"$join_id\" name=\"$2\" \/&gt;/$judge_value{$join_id}/g;
				$safe--;
			}
			if(!$empty_str){			#入力された値を集めた結果、空白の場合
				$type_of_element = $empty_str;
			}
			
			$join_values{$elements_id} = $type_of_element;
		}
		
		$q = new CGI;
		@session_data = ();
		for($cnt=0;$cnt<@elements;$cnt++){
			($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt]);
			$elementname = "en${elements_id}";
			@values = $q->param($elementname);
			
			
			#項目名の改行処理
			$name =~ s/&lt\;-br-&gt\;/<br \/>/g;
			
			
			if($filetype_name{$elementname}){
				$values[0] = $filetype_name{$elementname};
			}
			if($sanitizing_value{$elements_id}){
				$values[0] = $sanitizing_value{$elements_id};
			}
			for($i=0;$i<@values;$i++){
				$sesval = $values[$i];
				$values[$i] =~ s/\"/&quot;/g;
				$values[$i] =~ s/</\&lt;/g;
				$values[$i] =~ s/>/\&gt;/g;
				$hiddenObj .= "<input type=\"hidden\" name=\"en${elements_id}\" value=\"${values[$i]}\" />";
				$sesval =~ s/\=/<eq>/g;
				$sesval =~ s/\&/<amp>/g;
				push @session_data,"en${elements_id}=${sesval}";
			}
			# 連結項目が存在しているか、もしくは、「0」である場合
			if($join_values{$elements_id} || $join_values{$elements_id} eq '0'){
				$values[0] = $join_values{$elements_id};
				$join_values{$elements_id} =~ s/<br \/>/\n/g;
				$hiddenObj .= "<input type=\"hidden\" name=\"en${elements_id}\" value=\"$join_values{$elements_id}\" />";
			}
			$value = join('<br />',@values);
			$value =~ s/\n/<br \/>/g;
			if(!$join_elements{$elements_id} && $element_type ne "spacer"){
				#モバイル判定
				if($flag_mua){
					#ファイル添付判定
					if($element_type ne 'file'){
						if($fmail_item_color){
							$fmail_item_color = "";
							$fmail_item_color_inline = "";
						}else{
							$fmail_item_color = " fmail_item_color";
							$fmail_item_color_inline = " bgcolor=\"#def\"";
						}
						if($mail_dustclear && $mail_dustclear_zero) {
							# 確認画面で非表示は除外 & 未入力項目非表示＆0値非表示
							if(!$confirm_hidden && ${value}) {
								$contents .= "<div class=\"fmail_item$fmail_item_color\">\n";
								$contents .= "<b>${name}</b><br>\n";
								$contents .= "${value}&nbsp;<br>\n<br>\n";
								$contents .= "</div>\n";
							}
						} elsif ($mail_dustclear){
							# 確認画面で非表示は除外 & 未入力項目非表示のみ
							if(!$confirm_hidden && (${value} || ${value} eq '0')) {
								$contents .= "<div class=\"fmail_item$fmail_item_color\">\n";
								$contents .= "<b>${name}</b><br>\n";
								$contents .= "${value}&nbsp;<br>\n<br>\n";
								$contents .= "</div>\n";
							}
						} elsif($mail_dustclear_zero) {
							# 確認画面で非表示は除外 & 0値非表示のみ
							if(!$confirm_hidden && (${value} ne '0')) {
								$contents .= "<div class=\"fmail_item$fmail_item_color\">\n";
								$contents .= "<b>${name}</b><br>\n";
								$contents .= "${value}&nbsp;<br>\n<br>\n";
								$contents .= "</div>\n";
							}
						} else {
							# 確認画面で非表示
							if(!$confirm_hidden) {
								# 全て表示
								$contents .= "<div class=\"fmail_item$fmail_item_color\">\n";
								$contents .= "<b>${name}</b><br>\n";
								$contents .= "${value}&nbsp;<br>\n<br>\n";
								$contents .= "</div>\n";
							}
						}
					}
				#スマホ判定
				}elsif($flag_smartphone){
					#ファイル添付判定
					if($element_type ne 'file'){
						if($fmail_item_color){
							$fmail_item_color = "";
						}else{
							$fmail_item_color = " fmail_item_color";
						}
						if($mail_dustclear && $mail_dustclear_zero) {
							# 確認画面で非表示は除外 & 未入力項目非表示＆0値非表示
							if(!$confirm_hidden && ${value}) {
								$contents .= "<div class=\"fmail_item$fmail_item_color\">\n";
								$contents .= "<p class=\"fmail_item_name\"><b>${name}</b></p>\n";
								$contents .= "<p class=\"fmail_item_value\">${value}</p>\n";
								$contents .= "</div>\n";
							}
						} elsif ($mail_dustclear){
							# 確認画面で非表示は除外 & 未入力項目非表示のみ
							if(!$confirm_hidden && (${value} || ${value} eq '0')) {
								$contents .= "<div class=\"fmail_item$fmail_item_color\">\n";
								$contents .= "<p class=\"fmail_item_name\"><b>${name}</b></p>\n";
								$contents .= "<p class=\"fmail_item_value\">${value}</p>\n";
								$contents .= "</div>\n";
							}
						} elsif($mail_dustclear_zero) {
							# 確認画面で非表示は除外 & 0値非表示のみ
							if(!$confirm_hidden && (${value} ne '0')) {
								$contents .= "<div class=\"fmail_item$fmail_item_color\">\n";
								$contents .= "<p class=\"fmail_item_name\"><b>${name}</b></p>\n";
								$contents .= "<p class=\"fmail_item_value\">${value}</p>\n";
								$contents .= "</div>\n";
							}
						} else {
							# 確認画面で非表示
							if(!$confirm_hidden) {
								# 全て表示
								$contents .= "<div class=\"fmail_item$fmail_item_color\">\n";
								$contents .= "<p class=\"fmail_item_name\"><b>${name}</b></p>\n";
								$contents .= "<p class=\"fmail_item_value\">${value}</p>\n";
								$contents .= "</div>\n";
							}
						}
					}
				}else{
					if($mail_dustclear && $mail_dustclear_zero) {
						# 確認画面で非表示は除外 & 未入力項目非表示＆0値非表示
						if(!$confirm_hidden && ${value}) {
							$contents .= "<tr>\n";
							$contents .= "<th>${name}</th>\n";
							$contents .= "<td>${value}&nbsp;</td>\n";
							$contents .= "</tr>\n";
						}
					} elsif ($mail_dustclear){
						# 確認画面で非表示は除外 & 未入力項目非表示のみ
						if(!$confirm_hidden && (${value} || ${value} eq '0')) {
							$contents .= "<tr>\n";
							$contents .= "<th>${name}</th>\n";
							$contents .= "<td>${value}&nbsp;</td>\n";
							$contents .= "</tr>\n";
						}
					} elsif($mail_dustclear_zero) {
						# 確認画面で非表示は除外 & 0値非表示のみ
						if(!$confirm_hidden && (${value} ne '0')) {
							$contents .= "<tr>\n";
							$contents .= "<th>${name}</th>\n";
							$contents .= "<td>${value}&nbsp;</td>\n";
							$contents .= "</tr>\n";
						}
					} else {
						# 確認画面で非表示
						if(!$confirm_hidden) {
							# 全て表示
							$contents .= "<tr>\n";
							$contents .= "<th>${name}</th>\n";
							$contents .= "<td>${value}&nbsp;</td>\n";
							$contents .= "</tr>\n";
						}
					}
				}
			}
		}
		$contents .= "</table>\n";
		$contents .= "<div class=\"button clearfix\">\n";
		
		#モバイルアクセスでJSが使えるかを判定
		$contents .= "<script type=\"text/javascript\"><!--document.write('\$JsOperationFlag');--></script>\n";
		if($contents =~ /\$JsOperationFlag/){
			$contents =~ s/<script type="text\/javascript"><!--document.write\('\$JsOperationFlag'\);--><\/script>\n//g;
			#js利用可能
			$flag_js = 1;
		}else{
			#js利用不可能
			$flag_js = 0;
		}
		
		# 確認画面でのボタンの並び ------------------------------------------
		# モバイルアクセス時 --------------
		if($flag_mua == 1){
			# 送信ボタン
			$contents .= "<form id=\"fmail_submit\" class=\"fmail_submit\" method=\"post\" action=\"index.cgi?mode=send${sesQuery}\">\n";
			$contents .= "<div class=\"hiddenObj\">";
			
			if($flag_js){
				#JS利用可能の場合
				$contents .= "<script type=\"text/javascript\" src=\"./mobile/fmail.lib/submit.send.js\"></script>\n";
				$contents .= "<noscript><p><input type=\"submit\" id=\"submit_send\" value=\"送信\" /></p></noscript>\n";
			}else{
				#JS利用不可能の場合
				$contents .= "<noscript><p><input type=\"submit\" id=\"submit_send\" value=\"送信\" /></p></noscript>\n";
			}
			$contents .= "${hiddenObj}</div>\n";
			$contents .= "</form>\n";
			
			# 戻るボタン
			$contents .= "<form id=\"fmail_cancel\" class=\"fmail_cancel\" method=\"post\" action=\"index.cgi?mode=back\">\n";
			$contents .= "<div class=\"hiddenObj\">";
			if($flag_js){
				#JS利用可能の場合
				$contents .= "<script type=\"text/javascript\" src=\"./mobile/fmail.lib/submit.cancel.js\"></script>\n";
				$contents .= "<noscript><p><input type=\"submit\" id=\"submit_cancel\" value=\"前のページへ\" /></p></noscript>";
			}else{
				#JS利用不可能の場合
				$contents .= "<noscript><p><input type=\"submit\" id=\"submit_cancel\" value=\"前のページへ\" /></p></noscript>";
			}
			$contents .= "${hiddenObj}${matchObj}</div>\n";
			$contents .= "</form>\n";
			
		# スマートフォンアクセス時 --------------
		}elsif($flag_smartphone == 1){
			# 送信ボタン
			$contents .= "<form id=\"fmail_submit\" class=\"fmail_submit\" method=\"post\" action=\"index.cgi?mode=send${sesQuery}\">\n";
			$contents .= "<div class=\"hiddenObj\">";
			$contents .= "<script type=\"text/javascript\" src=\"./smaph/fmail.lib/submit.send.js\"></script>\n";
			$contents .= "<noscript><p><input type=\"submit\" id=\"submit_send\" value=\"送信\" /></p></noscript>\n";
			$contents .= "${hiddenObj}</div>\n";
			$contents .= "</form>\n";
			
			# 戻るボタン
			$contents .= "<form id=\"fmail_cancel\" class=\"fmail_cancel\" method=\"post\" action=\"index.cgi?mode=back\">\n";
			$contents .= "<div class=\"hiddenObj\">";
			$contents .= "<script type=\"text/javascript\" src=\"./smaph/fmail.lib/submit.cancel.js\"></script>\n";
			$contents .= "<noscript><p><input type=\"submit\" id=\"submit_cancel\" value=\"前のページへ\" /></p></noscript>";
			$contents .= "${hiddenObj}${matchObj}</div>\n";
			$contents .= "</form>\n";
			
		# PCアクセス時 --------------
		}else{
			# 戻るボタン
			$contents .= "<form id=\"fmail_cancel\" class=\"fmail_cancel\" method=\"post\" action=\"index.cgi?mode=back\">\n";
			$contents .= "<div class=\"hiddenObj\">";
			$contents .= "<script type=\"text/javascript\" src=\"./fmail.lib/submit.cancel.js\"></script>\n";
			$contents .= "<noscript><p><input type=\"submit\" id=\"submit_cancel\" value=\"前のページへ\" /></p></noscript>";
			$contents .= "${hiddenObj}${matchObj}</div>\n";
			$contents .= "</form>\n";
			
			# 送信ボタン
			$contents .= "<form id=\"fmail_submit\" class=\"fmail_submit\" method=\"post\" action=\"index.cgi?mode=send${sesQuery}\">\n";
			$contents .= "<div class=\"hiddenObj\">";
			$contents .= "<script type=\"text/javascript\" src=\"./fmail.lib/submit.send.js\"></script>\n";
			$contents .= "<noscript><p><input type=\"submit\" id=\"submit_send\" value=\"送信\" /></p></noscript>\n";
			$contents .= "${hiddenObj}</div>\n";
			$contents .= "</form>\n";
		}
		
		$contents .= "</div>\n";
		&WppSaveLine("${sessions_files_dir}${session}_token\.cgi",$null);
		# 完了ページへの引継用
		# タブ区切りで生成
		$session_work = join("\t", @session_data);
		&WppSaveLine("${sessions_files_dir}${session}\.cgi",$session_work);
	}
	else {
		@errorCounters = sort { (split(/\t/,$a))[1] <=> (split(/\t/,$b))[1]} @errorCounters;
		($error_code,$errorCounter) = split(/\t/,$errorCounters[0]);
		if($file_error_flag){
			$error_code = "";
		}
		else {
			push @session_data,"code=" . $error_code;
		}
		$session_data = join('&',@session_data);
		&WppSaveLine("${sessions_files_dir}${session}\.cgi",$session_data);
		$redirect = 'index.cgi?mode=error' . $sesQuery;
	}
}
else {
	#エラー出力処理
	unlink $send_token;
	$scriptObj = "\n<script type=\"text/javascript\">\n<!--\nvar exampleObj = new Array();\nvar postvalueObj = new Array();\nvar elementsetObj = new Array();\n";## fix / keep selectObj 090723
#	$scriptObj = "\n<script type=\"text/javascript\">\n\nvar exampleObj = new Array();\nvar postvalueObj = new Array();\nvar elementsetObj = new Array();\n";## fix / keep selectObj 090723
	$contents = "\n<form id=\"fmail\" method=\"post\" action=\"index.cgi?mode=confirm${sesQuery}\"${enctype} onsubmit=\"return falsesubmit(this)\">\n";
	if(($display_mode eq "table") && $flag_mua != 1 && $flag_smartphone != 1){
		$contents .= "<table border=\"0\" cellspacing=\"0\" cellpadding=\"0\" class=\"mailform\" summary=\"mailform main\">\n";
	}
	%getElement = ();
	%errorElements = ();
	$false_elements = join("\n",@elements);
	if($_GET{'mode'} eq "error"){
		# ダイレクトにエラーパラメータURLにアクセスされた場合に、入力ページへリダイレクトする--------------------
		# 直前URL取得（パラメータ付）
		my @ref_url_arr = split(/\//,$ENV{'HTTP_REFERER'});
		# 現在URL取得（パラメータ付）
		my $q = CGI->new();
		my @now_url_arr = split(/\//,$q->url);
		
		## 直前ページが、同じ階層かを確認
		## 直前ページが、index.cgiか
		#if ($ref_url_arr[-1] eq 'index.cgi' || $ref_url_arr[-1] eq 'index.cgi?mode=confirm') {
		#	# 直前ページFmailフォルダと現在Fmailフォルダが違う場合は、入力ページへ
		#	if ($ref_url_arr[-2] ne $now_url_arr[-2]) {
		#		print "Location: ./\n\n";
		#	}
		## 直前ページが、index.cgi?mode=errorか
		#} elsif ($ref_url_arr[-1] eq "index.cgi?mode=error") {
		#	# 直前ページFmailフォルダと現在Fmailフォルダが違う場合は、入力ページへ
		#	if ($ref_url_arr[-2] ne $now_url_arr[-2]) {
		#		print "Location: ./\n\n";
		#	}
		## 直前ページフォルダと現在ページフォルダが違うなら、入力ページへ
		#} elsif ($ref_url_arr[-2] ne $now_url_arr[-2]) {
		#	print "Location: ./\n\n";
		#}
		# -------------------------------------------------------------------------------------------------------
		
		$title = $title_error;
		$title_body = '<span id="fmail_title_error">' . $title_error . '</span>';
		## セッション情報の復元
		@getsession = &loadfile($sessions_files_dir . $session . '.cgi');
		$getsession = join("\n",@getsession);
		@getsession = split(/\&/,$getsession);
		for($cnt=0;$cnt<@getsession;$cnt++){
			($name,$value) = split(/\=/,$getsession[$cnt]);
			$value =~ s/<amp>/\&/g;
			$value =~ s/<eq>/\=/g;
			$getElement{$name} .= $value . '<-sp->';
			$false_elements =~ s/\[\[${name}\]\]/$value/g;
			if($name eq "code"){
				$error_code = $value;
			}
			elsif($name eq "spam_error"){
				$spam_error = $value;
			}
		}
		
		## エラーエレメントの解析
		@must = grep(/^${error_code}\t/,@must);
		($conditional_id,$must_name,$error_message,$must_elements,$note) = split(/\t/,$must[0]);
		@must_elements = split(/\&/,$must_elements);
		for($i=0;$i<@must_elements;$i++){
			($elements_id,$elements_value) = split(/\=/,$must_elements[$i]);
			$elements_id = "en" . $elements_id;
			@values = split(/<-sp->/,$getElement{$elements_id});
			if($elements_value ne $null){
				if($elements_value eq "1" && $values[0] eq $null){
					$errorElements{$elements_id} = 1;
					$errorElementsMSG{$elements_id} = 'が未入力または未選択です。<br />';
					
					# フォームログ
					&FormLog($elements_id);
				}
				elsif($elements_value eq "1" && $values[0] ne $null){
					
				}
				elsif($values[0] ne $null) {
					if(1 != grep(/^${elements_value}$/,@values)){
						#$errorElements{$elements_id} = 1;
					}
				}
				else {
					$errorElements{$elements_id} = 1;
					$errorElementsMSG{$elements_id} = 'が未入力または未選択です。<br />';
					
					# フォームログ
					&FormLog($elements_id);
				}
			}
		}
		for($cnt=0;$cnt<@elements;$cnt++){
			($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt]);
			$elementname = "en${elements_id}";
			if($errorElementsMSG{$elementname} ne $null){
				if($element_error_message) {
					$errorElementsMSG{$elementname} = '<span class="fmail_error">' . $element_error_message . '</span>';
				} else {
					$errorElementsMSG{$elementname} = '<span class="fmail_error">' . $name . $errorElementsMSG{$elementname} . '</span>';
				}
			}
			$false_elements =~ s/\[\[${elementname}_error\]\]/$errorElementsMSG{$elementname}/g;
			$false_elements =~ s/\[\[${elementname}_match\]\]//g;
			$false_elements =~ s/\[\[${elementname}\]\]//g;
		}
	}
	else {
		# mode=confirm画面からのmode=back
				
		# ダイレクトにbackパラメータURLにアクセスされた場合に、入力ページへリダイレクトする--------------------
		if($_GET{'mode'} eq "back"){
			# 直前URL取得（パラメータ付）
			my @ref_url_arr = split(/\//,$ENV{'HTTP_REFERER'});
			# 現在URL取得（パラメータ付）
			my $q = CGI->new();
			my @now_url_arr = split(/\//,$q->url);
			
			# 直前ページが、同じ階層かを確認
			# 直前ページが、index.cgiか
			if ($ref_url_arr[-1] eq 'index.cgi?mode=confirm') {
				# 直前ページFmailフォルダと現在Fmailフォルダが違う場合は、入力ページへ
				if ($ref_url_arr[-2] ne $now_url_arr[-2]) {
					print "Location: ./\n\n";
				}
			} else {
				print "Location: ./\n\n";
			}
		}
		# -------------------------------------------------------------------------------------------------------

		
		
		
		$title = $title_mailform;
		$title_body = '<span id="fmail_title_default">' . $title_mailform . '</span>';
		$q = new CGI;
		for($cnt=0;$cnt<@elements;$cnt++){
			($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt]);
			$elementname = "en${elements_id}";
			$matchelementname = "en${elements_id}_match";
			$errorelementname = "en${elements_id}_error";
			@values = $q->param($elementname);
			$matchvalues = $q->param($matchelementname);
			$getElement{$elementname} = join('<-sp->',@values);
			if($values[0] ne $null){
				$values[0] =~ s/\n//g;
				$false_elements =~ s/\[\[${elementname}\]\]/$values[0]/g;
			}
			else {
				$default_value =~ s/\n//g;
				$false_elements =~ s/\[\[${elementname}\]\]/$default_value/g;
			}
			
			$false_elements =~ s/\[\[${matchelementname}\]\]/$matchvalues/g;
			$false_elements =~ s/\[\[${errorelementname}\]\]//g;
		}
	}
	
	@elements = split(/\n/,$false_elements);
	
	#入力画面での項目出力等
	for($cnt=0;$cnt<@elements;$cnt++){
		($elements_id,$num,$name,$type_of_element,$html_size,$html_rows,$html_cols,$html_id,$element_type,$check_type,$on_event,$html_tag_free,$text_min,$text_max,$enable_filetypes,$filesize_min,$filesize_max,$checked_min,$checked_max,$element_valus,$element_text,$html_example,$note,$element_error_message,$must_disp,$default_value,$system_disp_false,$html_tag_free_top,$elements_class,$smartphone_elements_type,$confirm_hidden,$return_hidden,$or_disp,$log_hidden) = split(/\t/,$elements[$cnt]);
		$elementname = "en${elements_id}";
		$scriptObj .= "elementsetObj.push('en${elements_id}');\n"; ## fix / keep selectObj 090723
		@values = split(/<-sp->/,$getElement{$elementname});
		
		#項目名の改行処理
		$name =~ s/&lt\;-br-&gt\;/<br \/>/g;
		
		$classname = "";
		$disp_error_message = "";
		$musticon = ' must'; # 必須用クラス名
		# 追加クラス名設定
		if(${elements_class}) {
			$add_class = "${elements_class}";
		}
		if($must_disp) {
			# 必須アイコン登録している場合
			$eclass = " class=\"fmail$musticon smaph_$smartphone_elements_type\"";
			$eclass_file = " class=\"fmail_file$musticon\"";
		} else {
			$eclass = " class=\"fmail smaph_$smartphone_elements_type\"";
			$eclass_file = " class=\"fmail_file\"";
		}
		
		$must_icontag = "";
		#モバイル対応
		if($must_disp && $flag_mua){
			$must_icontag =<<"			EOD";
			<font color="red"><b><span id="fmail_must_$elementname" class="fmail_must">※</span></b></font>
			EOD
		}elsif($or_disp && $flag_mua){
			$must_icontag =<<"			EOD";
			<font color="red"><b><span id="fmail_or_$elementname" class="fmail_or">※</span></b></font>
			EOD
		}elsif($must_disp){
			$must_icontag =<<"			EOD";
			<div id="fmail_must_$elementname" class="fmail_must">※</div>
			EOD
		}elsif($or_disp){
			$must_icontag =<<"			EOD";
			<div id="fmail_or_$elementname" class="fmail_or">※</div>
			EOD
		}
		
		# musticon初期化
		$musticon = "";
		
		if($errorElements{$elementname}){
			$classname = " class=\"fmail_error_line\"";
			if($element_error_message ne $null){
				$disp_error_message = "<span class=\"fmail_error\">${element_error_message}</span>";
			}
			else {
				if($element_type eq "text" || $element_type eq "textarea"){
					$disp_error_message = "<span class=\"fmail_error\">${name}が未入力です。<br /></span>";
				}
				elsif($element_type eq "checkbox" || $element_type eq "radio"){
					$disp_error_message = "<span class=\"fmail_error\">${name}がチェックされていません。<br /></span>";
				}
				else {
					$disp_error_message = "<span class=\"fmail_error\">${name}が選択されていません。<br /></span>";
				}
			}
			#必須エラーがある場合にフラグを立てる。
			$flag_musterror = 1;
		}
		$error_element_name_hash = $elementname . "_error";
		if($getElement{$error_element_name_hash}){
			$classname = " class=\"fmail_error_line\"";
			@errors = split(/<-sp->/,$getElement{$error_element_name_hash});
			$disp_error_message = "<span class=\"fmail_error\">${errors[0]}</span>";
		}
		if($on_event ne $null){
			$on_event = " ${on_event} ";
		}
		if($html_rows ne $null){
			$html_rows = " rows=\"${html_rows}\"";
		}
		if($html_cols ne $null){
			$html_cols = " cols=\"${html_cols}\"";
		}
		if($html_example ne $null){
			#$html_example = "<span class=\"fmail_example\">${html_example}</span>";
			$html_example =~ s/\n//g;
			$html_example =~ s/\r//g;
			$html_example =~ s/<-br->/\n/g;
			$scriptObj .= "exampleObj\['en${elements_id}'\] = \"${html_example}\";\n";
		}
		if($note ne $null){
			$note = "<p class=\"fmail_note\">${note}</p>";
		}
		# HTMLタグ後
		if($html_tag_free ne $null){
			$html_tag_free =~ s/<br \/>/\n/g;
			$html_tag_free =~ s/<-br->/\n/g;
			$html_tag_free =~ s/&lt;/</g;
			$html_tag_free =~ s/&gt;/>/g;
		}
		# HTMLタグ前
		if($html_tag_free_top ne $null){
			$html_tag_free_top =~ s/<br \/>/\n/g;
			$html_tag_free_top =~ s/<-br->/\n/g;
			$html_tag_free_top =~ s/&lt;/</g;
			$html_tag_free_top =~ s/&gt;/>/g;
		}
		
		# エスケープ処理
		if($element_type eq "text" || $element_type eq "hidden" || $element_type eq "textarea") {
			$values[0] =~ s/\"/&quot;/g;
			$values[0] =~ s/</\&lt;/g;
			$values[0] =~ s/>/\&gt;/g;
		}
		
		$display_element_flag = 1;
		if($element_type eq "text"){
			if($values[0] eq $null){
				$values[0] = $default_value;
			}
			if($smartphone_elements_type && $flag_smartphone == 1) {
				# スマホでtype指定がある場合
				$text_format = $smartphone_elements_type;
				# メールアドレスの再確認用対策
				${html_tag_free_top} =~ s/type="text"/type="$smartphone_elements_type"/;
				${html_tag_free} =~ s/type="text"/type="$smartphone_elements_type"/;
			} else {
				# アクセスユーザーのエージェントが元々指定されているデバイスなら変換
				if ($flag_smartphone_custom) {
					$text_format = $smartphone_elements_type;
					${html_tag_free_top} =~ s/type="text"/type="$smartphone_elements_type"/;
					${html_tag_free} =~ s/type="text"/type="$smartphone_elements_type"/;
				} else {
					$text_format = 'text';
				}
			}
			$elementtag = "${disp_error_message}${html_tag_free_top}<input type=\"$text_format\" name=\"en${elements_id}\" id=\"en${elements_id}\"${eclass} value=\"${values[0]}\"${on_event} />${note}\n";
		}
		elsif($element_type eq "hidden"){
			if($values[0] eq $null){
				$default_value =~ s/<br \/>/\n/g;
				$values[0] = $default_value;
			}
			$default_value =~ s/<br \/>/\n/g;
			$elementtag = "${disp_error_message}${html_tag_free_top}<input type=\"hidden\" name=\"en${elements_id}\" id=\"en${elements_id}\"${eclass} value=\"${values[0]}\"${on_event} />${note}\n";
		}
		elsif($element_type eq "textarea"){
			if($values[0] eq $null){
				$default_value =~ s/<br \/>/\n/g;
				$values[0] = $default_value;
			}
			$values[0] =~ s/<-br->/\n/g;
			$elementtag = "${disp_error_message}${html_tag_free_top}<textarea name=\"en${elements_id}\" id=\"en${elements_id}\"${eclass}${html_rows}${html_cols}${on_event}>${values[0]}</textarea>${note}\n";
		}
		elsif($element_type eq "select"){
			$elementtag = "${disp_error_message}\n";
			$elementtag .= "${html_tag_free_top}<select name=\"en${elements_id}\" id=\"en${elements_id}\"${eclass}${on_event}>\n";
			@element_values = split(/<br \/>/,$element_valus);
			@element_text = split(/<br \/>/,$element_text);
			$optGroupFlag = 0;
			$prevOptGroup = "";
			for($i=0;$i<@element_values;$i++){
				($elementText,$optGroup) = split(/\:\:/,$element_text[$i]);
				#追加
				@element_work = split(/::/,$element_values[$i]);
				if($element_work[1] eq "selected"){
					$selected = " selected=\"selected\"";
				}else{
					$selected = "";
				}
				$element_values[$i] = $element_work[0];
				if(1 == grep(/^$element_values[$i]$/,@values)){
					#$selected = " selected";
					$scriptObj .= "postvalueObj\['en${elements_id}'\] = \"${element_values[$i]}\";\n"; ## fix / keep selectObj 090723
				}
				else {
					#$selected = "";
				}
				if(!($optGroupFlag) && $optGroup ne $null && $prevOptGroup eq $null){
					$elementtag .= "<optgroup label=\"${optGroup}\">\n";
					$optGroupFlag = 1;
				}
				elsif($optGroup ne $null && $prevOptGroup ne $optGroup){
					$elementtag .= "</optgroup>\n<optgroup label=\"${optGroup}\">\n";
					$optGroupFlag = 1;
				}
				$elementtag .= "<option value=\"${element_values[$i]}\"${selected}>${elementText}</option>\n";
				$prevOptGroup = $optGroup;
			}
			if($optGroupFlag){
				$elementtag .= "</optgroup>\n";
			}
			$elementtag .= "</select>\n";
		}
		elsif($element_type eq "radio" || $element_type eq "checkbox"){
			$elementtag = "${disp_error_message}\n";
			@element_values = split(/<br \/>/,$element_valus);
			@element_text = split(/<br \/>/,$element_text);
			
			#リストタグ判定
			if(!$flag_mua){
				#PC・スマートフォン
				$elementtag .= "${html_tag_free_top}<ol class=\"fmail_${element_type}_list clearfix\">\n";
			}else{
				#フィーチャーフォン
				$elementtag .= "${html_tag_free_top}<p class=\"fmail_${element_type}_list clearfix\">\n";
			}
			
			for($i=0;$i<@element_values;$i++){
				$inum = sprintf("%02d",$i+1);
				$scriptObj .= "elementsetObj.push('en${elements_id}_${inum}');\n"; ## fix / keep selectObj 090818
				#追加
				#if(1 == grep(/^$element_values[$i]$/,@values)){
				#通常入力とエラー時の吐き出し分岐
				if(($_GET{'mode'} ne "error") && ($_GET{'mode'} ne "back")){
					@element_work = split(/::/,$element_values[$i]);
					if($element_work[1] eq "checked"){
						$checked = " checked=\"checked\"";
					}
					else {
						$checked = "";
					}
					$element_values[$i] = $element_work[0];
				}
				
				## fix / keep radio&checkboxObj 090818
				$element_values[$i] =~ s/::checked//;
				if(1 == grep(/^$element_values[$i]$/,@values)){
					$scriptObj .= "postvalueObj\['en${elements_id}_${inum}'\] = \"${element_values[$i]}\";\n";
				}
				##
				
				#リストタグ判定
				if(!$flag_mua){
					#PC・スマートフォン　リストタグあり
					$elementtag .= "<li><label id=\"en${elements_id}_${inum}_label\" for=\"en${elements_id}_${inum}\" class=\"fmail_label\"><input type=\"${element_type}\" name=\"en${elements_id}\" id=\"en${elements_id}_${inum}\"${eclass}${on_event} value=\"${element_values[$i]}\"${checked} /> ${element_text[$i]}</label></li>\n";
				}else{
					#フィーチャーフォン　リストタグなし
					$elementtag .= "<input type=\"${element_type}\" name=\"en${elements_id}\" id=\"en${elements_id}_${inum}\" class=\"radiocheckbox\" value=\"${element_values[$i]}\"${checked} /> ${element_text[$i]}<br>\n";
				}
			}
			#リストタグ判定
			if(!$flag_mua){
				#PC・スマートフォン
				$elementtag .= "</ol>\n";
			}else{
				#フィーチャーフォン
				$elementtag .= "</p>\n";
			}
		}
		elsif($element_type eq "file"){
			$save_file_name = "${attached_files_dir}${session}_${elementname}";
			unlink $save_file_name;
			$error_element_name_hash = $elementname . "_error";
			if($getElement{$error_element_name_hash}){
				@errors = split(/<-sp->/,$getElement{$error_element_name_hash});
				$disp_error_message = "<span class=\"fmail_error\">${errors[0]}</span>";
			}
#			if($ENV{'HTTP_USER_AGENT'} !~ /IE/ && $ENV{'HTTP_USER_AGENT'} !~ /Opera/) {
#				# IE以外（ただしOperaは何やってもダメ）
#				$elementtag = "${disp_error_message}${html_tag_free_top}<input type=\"file\" name=\"en${elements_id}\" id=\"en${elements_id}\"${eclass_file}${html_id}${size}${on_event} /><input type=\"button\" value=\"キャンセル\" class=\"ffcancel\" onclick=\"del('en${elements_id}')\;\" onkeypress=\"del('en${elements_id}')\;\" /> ${html_example}${note}\n";
#			}else{
#				# IEのみ
#				$elementtag = "${disp_error_message}${html_tag_free_top}<input type=\"file\" name=\"en${elements_id}\" id=\"en${elements_id}\"${eclass_file}${html_id}${size}${on_event} /> ${html_example}${note}\n";
#			}
			# ブラウザの判定はJS側で行う。
			$elementtag = "${disp_error_message}${html_tag_free_top}<input type=\"file\" name=\"en${elements_id}\" id=\"en${elements_id}\"${eclass_file}${html_id}${size}${on_event} /><input type=\"button\" value=\"キャンセル\" class=\"ffcancel\" onclick=\"del('en${elements_id}')\;\" onkeypress=\"del('en${elements_id}')\;\" /> ${html_example}${note}\n";
		}
		elsif($element_type eq "spacer"){
			#追加
			${html_tag_free_top} =~ s/::checked"/" checked="checked"/g;
			${html_tag_free_top} =~ s/::selected"/" selected="selected"/g;
			${html_tag_free} =~ s/::checked"/" checked="checked"/g;
			${html_tag_free} =~ s/::selected"/" selected="selected"/g;
			${html_tag_free_top} =~ s/数字以外の文字が含まれています。/<span class="fmail_error">数字以外の文字が含まれています。<\/span>/g;
			${html_tag_free} =~ s/数字以外の文字が含まれています。/<span class="fmail_error">数字以外の文字が含まれています。<\/span>/g;
			${html_tag_free_top} =~ s/半角英字以外の文字が含まれています。/<span class="fmail_error">半角英字以外の文字が含まれています。<\/span>/g;
			${html_tag_free} =~ s/半角英字以外の文字が含まれています。/<span class="fmail_error">半角英字以外の文字が含まれています。<\/span>/g;
			${html_tag_free_top} =~ s/半角英数字以外の文字が含まれています。/<span class="fmail_error">半角英数字以外の文字が含まれています。<\/span>/g;
			${html_tag_free} =~ s/半角英数字以外の文字が含まれています。/<span class="fmail_error">半角英数字以外の文字が含まれています。<\/span>/g;
			${html_tag_free_top} =~ s/電話番号の桁数に誤りがあります。/<span class="fmail_error">電話番号の桁数に誤りがあります。<\/span>/g;
			${html_tag_free} =~ s/電話番号の桁数に誤りがあります。/<span class="fmail_error">電話番号の桁数に誤りがあります。<\/span>/g;
			${html_tag_free_top} =~ s/郵便番号の桁数に誤りがあります。７桁以内で入力してください。/<span class="fmail_error">郵便番号の桁数に誤りがあります。７桁以内で入力してください。<\/span>/g;
			${html_tag_free} =~ s/郵便番号の桁数に誤りがあります。７桁以内で入力してください。/<span class="fmail_error">郵便番号の桁数に誤りがあります。７桁以内で入力してください。<\/span>/g;
#			${html_tag_free_top} =~ s/電話番号はハイフンで区切って入力してください。/<span class="fmail_error">電話番号はハイフンで区切って入力してください。<\/span>/g;
#			${html_tag_free} =~ s/電話番号はハイフンで区切って入力してください。/<span class="fmail_error">電話番号はハイフンで区切って入力してください。<\/span>/g;
			${html_tag_free_top} =~ s/FAX番号の桁数に誤りがあります。/<span class="fmail_error">FAX番号の桁数に誤りがあります。<\/span>/g;
			${html_tag_free} =~ s/FAX番号の桁数に誤りがあります。/<span class="fmail_error">FAX番号の桁数に誤りがあります。<\/span>/g;
#			${html_tag_free_top} =~ s/FAX番号はハイフンで区切って入力してください。/<span class="fmail_error">FAX番号はハイフンで区切って入力してください。<\/span>/g;
#			${html_tag_free} =~ s/FAX番号はハイフンで区切って入力してください。/<span class="fmail_error">FAX番号はハイフンで区切って入力してください。<\/span>/g;
			${html_tag_free_top} =~ s/メールアドレスで使えない文字が含まれています。/<span class="fmail_error">メールアドレスで使えない文字が含まれています。<\/span>/g;
			${html_tag_free} =~ s/メールアドレスで使えない文字が含まれています。/<span class="fmail_error">メールアドレスで使えない文字が含まれています。<\/span>/g;
			${html_tag_free_top} =~ s/メールアドレスに誤りがあります。/<span class="fmail_error">メールアドレスに誤りがあります。<\/span>/g;
			${html_tag_free} =~ s/メールアドレスに誤りがあります。/<span class="fmail_error">メールアドレスに誤りがあります。<\/span>/g;
			${html_tag_free_top} =~ s/対応していないファイルが選択されています。/<span class="fmail_error">対応していないファイルが選択されています。<\/span>/g;
			${html_tag_free} =~ s/対応していないファイルが選択されています。/<span class="fmail_error">対応していないファイルが選択されています。<\/span>/g;
			
			if($flag_smartphone == 1) {
				# スマホなのでtyp属性を調整
				${html_tag_free_top} =~ s/type="text_/type="/g;
				${html_tag_free} =~ s/type="text_/type="/g;
			} else {
				# スマホ以外なので、最短マッチ
				${html_tag_free_top} =~ s/type="text_.+?"/type="text"/g;
				${html_tag_free} =~ s/type="text_.+?"/type="text"/g;
			}
			
			$elementtag = "${disp_error_message}${html_tag_free_top}${html_example}${note}\n";
			
			#リストタグ判定 フィーチャーフォンのみ置換
			if($flag_mua){
				#フィーチャーフォン　リストタグなし
				# HTMLタグ（前）
				$elementtag =~ s/<ol /<p /g;
				$elementtag =~ s/<\/ol>/<\/p>/g;
				$elementtag =~ s/<li>//g;
				$elementtag =~ s/<\/li>/<br>/g;
				$elementtag =~ s/<label.+?>//g; #spacerに貼り付けられるコードは一行に全部入っているので、最短マッチングを繰り返すように置換
				$elementtag =~ s/<\/label>//g;
				$elementtag =~ s/(type="radio".+?)(class="fmail")/$1class="radiocheckbox"/g; #必要箇所のみ置換
				$elementtag =~ s/(type="checkbox".+?)(class="fmail")/$1class="radiocheckbox"/g; #必要箇所のみ置換
				
				# HTMLタグ（後）
				${html_tag_free} =~ s/<ol /<p /g;
				${html_tag_free} =~ s/<\/ol>/<\/p>/g;
				${html_tag_free} =~ s/<li>//g;
				${html_tag_free} =~ s/<\/li>/<br>/g;
				${html_tag_free} =~ s/<label.+?>//g; #spacerに貼り付けられるコードは一行に全部入っているので、最短マッチングを繰り返すように置換
				${html_tag_free} =~ s/<\/label>//g;
				${html_tag_free} =~ s/(type="radio".+?)(class="fmail")/$1class="radiocheckbox"/g; #必要箇所のみ置換
				${html_tag_free} =~ s/(type="checkbox".+?)(class="fmail")/$1class="radiocheckbox"/g; #必要箇所のみ置換
			}
		}
		else {
			$display_element_flag = 0;
		}
		if($system_disp_false){
			$display_element_flag = 0;
		}
		#隠しデータかどうかの判断
		if($element_type ne "hidden"){
			#隠しデータでない場合
			if($display_element_flag){
				#モバイルアクセスの場合
				if($flag_mua == 1){
					#モバイルの場合、添付できないので、処理上は除外
					if(${elementtag} !~ /type="file"/){
						if($fmail_item_color){
							$fmail_item_color = "";
							$fmail_item_color_inline = "";
						}else{
							$fmail_item_color = " fmail_item_color";
							$fmail_item_color_inline = " bgcolor=\"#def\"";
						}
						$contents .= "<div id=\"p_en${elements_id}\" class=\"fmail_item$fmail_item_color\">\n";
						$contents .= "<span${classname} id=\"h_en${elements_id}\"><b>${must_icontag}${name}</b></span><br>\n";
						$contents .= "<span${classname} id=\"d_en${elements_id}\">${elementtag}${html_tag_free}</span><br>\n<br>\n";
						$contents .= "</div>\n";
					}
				#スマホアクセスの場合
				}elsif($flag_smartphone == 1){
					#スマホの場合、添付できないので、処理上は除外
#					if(${elementtag} !~ /type="file"/){
						if($fmail_item_color){
							$fmail_item_color = "";
						}else{
							$fmail_item_color = " fmail_item_color";
						}
						# Classが追加されている場合
						if($add_class) {
							$add_class = qq| $add_class|;
						}
						# Errorの場合
						if(${classname}) {
							${classname}  = ' fmail_error_line';
						}
						$contents .= "<div id=\"p_en${elements_id}\" class=\"fmail_item$fmail_item_color$add_class${classname}\">\n";
						$contents .= "<p id=\"h_en${elements_id}\" class=\"fmail_item_name\"><b>${name}</b>${must_icontag}</p>\n";
						$contents .= "<p id=\"d_en${elements_id}\" class=\"fmail_item_value\">${elementtag}${html_tag_free}</p>\n";
						$contents .= "</div>\n";
#					}
				#talbe定義の場合
				}elsif($display_mode eq "table"){
					# Classが追加されている場合
					if($add_class) {
						$add_class = qq|class="$add_class $html_size"|;
					} else {
						$add_class = qq|class="$html_size"|;
					}
					$contents .= "<tr id=\"r_en${elements_id}\" $add_class>\n";
					$contents .= "<th${classname} id=\"h_en${elements_id}\"><span class=\"name\">${name}</span>${must_icontag}</th>\n";
					$contents .= "<td${classname} id=\"d_en${elements_id}\">${elementtag}${html_tag_free}</td>\n";
					$contents .= "</tr>\n";
				}#dl定義の場合
				else {
					# Classが追加されている場合
					if($add_class) {
						$add_class = qq| $add_class $html_size|;
					} else {
						$add_class = qq| $html_size|;
					}
					$contents .= "<dl class=\"mailform$add_class\" id=\"r_en${elements_id}\">\n";
					$contents .= "<dt${classname} id=\"h_en${elements_id}\"><span class=\"name\">${name}</span>${must_icontag}</dt>\n";
					$contents .= "<dd${classname} id=\"d_en${elements_id}\">${elementtag}${html_tag_free}</dd>\n";
					$contents .= "</dl>\n";
				}
			}
			# musticonとadd_class初期化
			$add_class = "";
		}else{
			#隠しデータの場合
			if($display_element_flag){
				#モバイルアクセスの場合
				if($flag_mua == 1 || $flag_smartphone == 1){
					$contents .= "${elementtag}";
				#talbe定義の場合
				}elsif($display_mode eq "table"){
					$contents .= "${elementtag}";
				}#dl定義の場合
				else {
					$contents .= "${elementtag}";
				}
			}
		}
	}
	
	#エラー時にページTOPへ表示する文言
	if(($error_message ne $null) && ($flag_musterror == 1)){
		$error = '<div class="fmail_error_message">' . $error_message . '</div>';
	}
	elsif($spam_error ne $null){
		$error = '<div class="fmail_error_message">' . $spam_error . '</div>';
	}
	elsif($error_message ne $null){
		$error = '<div class="fmail_error_message">' . $error_message . '</div>';
	}
	
	#モバイルアクセスでJSが使えるかを判定
	$contents .= "<script type=\"text/javascript\"><!--document.write('\$JsOperationFlag');--></script>\n";
	if($contents =~ /\$JsOperationFlag/){
		$contents =~ s/<script type="text\/javascript"><!--document.write\('\$JsOperationFlag'\);--><\/script>\n//g;
		#js利用可能
		$flag_js = 1;
	}else{
		#js利用不可能
		$flag_js = 0;
	}
	
	#モバイルアクセスの場合
	if($flag_mua == 1){
		if($flag_js){
			#JS利用可能の場合
			$contents .= "<p class=\"button\">\n";
			$contents .= "<script type=\"text/javascript\" src=\"./mobile/fmail.lib/submit.confirm.js\"></script>\n";
			$contents .= "</p>\n";
			$contents .= "<noscript><p><input type=\"submit\" id=\"submit_confirm\" value=\"確認画面へ進む\" /></p></noscript>\n";
		}else{
			#JS利用不可能の場合
			$contents .= "<noscript><p><input type=\"submit\" id=\"submit_confirm\" value=\"確認画面へ進む\" /></p></noscript>\n";
		}
	#スマートフォンアクセスの場合
	}elsif($flag_smartphone == 1){
		if($flag_js){
			#JS利用可能の場合
			$contents .= "<p class=\"button\">\n";
			$contents .= "<script type=\"text/javascript\" src=\"./smaph/fmail.lib/submit.confirm.js\"></script>\n";
			$contents .= "</p>\n";
			$contents .= "<noscript><p><input type=\"submit\" id=\"submit_confirm\" value=\"確認画面へ進む\" /></p></noscript>\n";
		}else{
			#JS利用不可能の場合
			$contents .= "<noscript><p><input type=\"submit\" id=\"submit_confirm\" value=\"確認画面へ進む\" /></p></noscript>\n";
		}
	#talbe定義の場合
	}elsif($display_mode eq "table"){
		$contents .= "</table>\n";
		$contents .= "<p class=\"button\">\n";
		$contents .= "<script type=\"text/javascript\" src=\"./fmail.lib/submit.confirm.js\"></script>\n";
		$contents .= "<script type=\"text/javascript\">\n<!--\n";
		$contents .= "document.write('<div id=\"mailfrom_hidden_object\"><input type=\"submit\" /></div>')\;\n";
		$contents .= "//-->\n</script>\n";
		$contents .= "</p>\n";
		$contents .= "<noscript><p><input type=\"submit\" id=\"submit_confirm\" value=\"確認画面へ進む\" /></p></noscript>\n";
	}#dl定義の場合
	else {
		$contents .= "<dl class=\"mailform\">\n";
		$contents .= "<dt>&nbsp;</dt>\n";
		$contents .= "<dd>\n";
		$contents .= "<script type=\"text/javascript\" src=\"./fmail.lib/submit.confirm.js\"></script>\n";
		$contents .= "<noscript><p><input type=\"submit\" id=\"submit_confirm\" value=\"確認画面へ進む\" /></p></noscript>\n";
		$contents .= "<script type=\"text/javascript\">\n<!--\n";
		$contents .= "document.write('<div id=\"mailfrom_hidden_object\"><input type=\"submit\" /></div>')\;\n";
		$contents .= "//-->\n</script>\n";
		$contents .= "</dd>\n";
		$contents .= "</dl>\n";
	}
	$contents .= "</form>\n";
	$scriptObj .= "-->\n</script>\n";
#	$scriptObj .= "\n</script>\n";
	$contents .= $scriptObj;
	unlink "${sessions_files_dir}${session}\.cgi";
}

## ケース1
#$cookie_path = $ENV{'SCRIPT_NAME'};
#@cookie_path = split(/\//,$cookie_path);
#$cookie_path[-1] = "";
#$cookie_path = join('/',@cookie_path);

## ケース2
#my $q = CGI->new();
#$cookie_path = $q->url();
##Preview-Server or not
##iCLUSTAの別サーバーのみ環境変数 HTTP_X_FUJITSUBO_PROXY が用意されており、別サーバーのFQDNがセットされている
#if ($ENV{'HTTP_X_FUJITSUBO_PROXY'}) {
#	$cookie_path =~ s/^http[s]?\:\/\///i;
#} else {
#	$cookie_path =~ s/^http[s]?\:\/\/.*?\///i;
#}
#$cookie_path = '/' . $cookie_path;

# ケース3
my $q = CGI->new();
$cookie_path = $q->self_url();
#Preview-Server or not
#iCLUSTAの別サーバーのみ環境変数 HTTP_X_FUJITSUBO_PROXY が用意されており、別サーバーのFQDNがセットされている
if ($ENV{'HTTP_X_FUJITSUBO_PROXY'}) {
	$cookie_path =~ s/^http[s]?\:\/\///i;
} else {
	$cookie_path =~ s/^http[s]?\:\/\/.*?\///i;
}
$cookie_path = '/' . $cookie_path;
#仕上げにファイル名を削除
$cookie_path =~ s/^([^\?]+\/).*$/$1/i;
if($redirect){
	print "Location: ${redirect}\n";
	print "Set-Cookie: session=${session}; path=${cookie_path}; \n\n";
}
else {
	$html =~ s/$tpl_symbol_title/$title/ig;
	$html =~ s/$tpl_symbol_title_body/$title_body/ig;
	$html =~ s/$tpl_symbol_body/$contents/ig;
	$html =~ s/$tpl_symbol_error/$error/ig;
	$html =~ s/$tpl_symbol_ver/$reg{'version'}/ig;
	
	# 完了ページ表示時にIDの再発行を実施
	if($_GET{'mode'} eq 'thanks'){
		${session} = &createId;
	}
	
	print "Pragma: no-cache\n";
	print "Cache-Control: no-cache\n";
	print "Content-type: text/html; charset=UTF-8\n";
	print "Set-Cookie: session=${session}; path=${cookie_path};\n\n";
	
	#追加プログラム---------------------------------------------------------------------
	#入力・確認・完了　各画面での表示非表示部分の切り分け処理（テンプレ依存）
	
	# 追加CSS
	@size_classes = &loadfile('./fmail.admin/datas/modules/size_class/size_class.dat');
	$add_csses = join("\n",@size_classes);
	($size_1_w,$size_1_h,$size_2_w,$size_2_h,$size_3_w,$size_3_h,$size_4_w,$size_4_h,$size_5_w,$size_5_h,$size_6_w,$size_6_h,$size_7_w,$size_7_h,$size_8_w,$size_8_h,$size_9_w,$size_9_h,$size_10_w,$size_10_h) = split(/\n/,$add_csses);

	$add_css =<<"	EOD";
<style type="text/css">
<!--
	#fmail .size_1 input, #fmail .size_1 select, #fmail .size_1 textarea {	width: $size_1_w;	height: $size_1_h;}
	#fmail .size_2 input, #fmail .size_2 select, #fmail .size_2 textarea {	width: $size_2_w;	height: $size_2_h;}
	#fmail .size_3 input, #fmail .size_3 select, #fmail .size_3 textarea {	width: $size_3_w;	height: $size_3_h;}
	#fmail .size_4 input, #fmail .size_4 select, #fmail .size_4 textarea {	width: $size_4_w;	height: $size_4_h;}
	#fmail .size_5 input, #fmail .size_5 select, #fmail .size_5 textarea {	width: $size_5_w;	height: $size_5_h;}
	#fmail .size_6 input, #fmail .size_6 select, #fmail .size_6 textarea {	width: $size_6_w;	height: $size_6_h;}
	#fmail .size_7 input, #fmail .size_7 select, #fmail .size_7 textarea {	width: $size_7_w;	height: $size_7_h;}
	#fmail .size_8 input, #fmail .size_8 select, #fmail .size_8 textarea {	width: $size_8_w;	height: $size_8_h;}
	#fmail .size_9 input, #fmail .size_9 select, #fmail .size_9 textarea {	width: $size_9_w;	height: $size_9_h;}
	#fmail .size_10 input, #fmail .size_10 select, #fmail .size_10 textarea {	width: $size_10_w;	height: $size_10_h;}
-->
</style>
	EOD
	
	$html =~ s/<!--%%fmail-addcss%%-->/$add_css/;
	
	#エラー画面での処理部分----------------------------------
	if($_GET{'mode'} eq 'error'){
		$invisible = 0;
		$invisible_confirm = 0;
		$invisible_thanks = 0;
		
		$html_work = $html;
		@html_work2 = split(/\n/,$html_work);
		for($i=0;@html_work2>$i;$i++){
			#入力画面以降表示させない部分----------------------------------
			if($html_work2[$i] =~ /<!--%%fmail-invisible-contents-start%%-->/){
				#見えない箇所開始
				$invisible = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-invisible-contents-end%%-->/){
				#見えない箇所終了
				$invisible = 9;
			}
			
			#確認画面で非表示させる部分----------------------------------
			#確認画面用
			if($html_work2[$i] =~ /<!--%%fmail-confirm-contents-start%%-->/){
				#見えない箇所開始
				$invisible_confirm = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-confirm-contents-end%%-->/){
				#見えない箇所終了
				$invisible_confirm = 9;
			}
			#送信完了用
			if($html_work2[$i] =~ /<!--%%fmail-thanks-contents-start%%-->/){
				#見えない箇所開始
				$invisible_thanks = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-thanks-contents-end%%-->/){
				#見えない箇所終了
				$invisible_thanks = 9;
			}
			
			if($invisible ne '1' && $invisible_confirm ne '1' && $invisible_thanks ne '1'){
					print "$html_work2[$i]\n";
			}
		}
		
	#確認画面での処理部分----------------------------------
	}elsif($_GET{'mode'} eq 'confirm'){
		$invisible = 0;
		$invisible_error = 0;
		$invisible_thanks = 0;
		
		$html_work = $html;
		@html_work2 = split(/\n/,$html_work);
		for($i=0;@html_work2>$i;$i++){
			#入力画面以降表示させない部分----------------------------------
			if($html_work2[$i] =~ /<!--%%fmail-invisible-contents-start%%-->/){
				#見えない箇所開始
				$invisible = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-invisible-contents-end%%-->/){
				#見えない箇所終了
				$invisible = 9;
			}
			
			#確認画面で非表示させる部分----------------------------------
			#エラー表示用
			if($html_work2[$i] =~ /<!--%%fmail-error-contents-start%%-->/){
				#見えない箇所開始
				$invisible_error = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-error-contents-end%%-->/){
				#見えない箇所終了
				$invisible_error = 9;
			}
			#送信完了用
			if($html_work2[$i] =~ /<!--%%fmail-thanks-contents-start%%-->/){
				#見えない箇所開始
				$invisible_thanks = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-thanks-contents-end%%-->/){
				#見えない箇所終了
				$invisible_thanks = 9;
			}
			
			if($invisible ne '1' && $invisible_error ne '1' && $invisible_thanks ne '1'){
					print "$html_work2[$i]\n";
			}
		}
		
		# フォームログ
		&FormLog;
	#送信完了画面での処理----------------------------------
	}elsif($_GET{'mode'} eq 'thanks'){
		$invisible = 0;
		$invisible_error = 0;
		$invisible_confirm = 0;
		
		$html_work = $html;
		@html_work2 = split(/\n/,$html_work);
		
		&serials_read;
		
		for($i=0;@html_work2>$i;$i++){
			#入力画面以降表示させない部分----------------------------------
			if($html_work2[$i] =~ /<!--%%fmail-invisible-contents-start%%-->/){
				#見えない箇所開始
				$invisible = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-invisible-contents-end%%-->/){
				#見えない箇所終了
				$invisible = 9;
			}
			
			#送信完了画面で表示させる部分----------------------------------
			#エラー画面用
			if($html_work2[$i] =~ /<!--%%fmail-error-contents-start%%-->/){
				#見える箇所開始
				$invisible_error = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-error-contents-end%%-->/){
				#見える箇所終了
				$invisible_error = 9;
			}
			#確認画面用
			if($html_work2[$i] =~ /<!--%%fmail-confirm-contents-start%%-->/){
				#見える箇所開始
				$invisible_confirm = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-confirm-contents-end%%-->/){
				#見える箇所終了
				$invisible_confirm = 9;
			}
			
			if($invisible ne '1' && $invisible_error ne '1' && $invisible_confirm ne '1'){
				#完了画面で出すアフィリエイトタグ対応のスタンパーの置換
				$timestamp = $stmp;
				$timestamp =~ s/-//g;
				$timestamp =~ s/://g;
				$timestamp =~ s/ //g;
				$afiri_uniq_id = "$getSes{'session'}$serial";
				$html_work2[$i] =~ s/<afiri_uniq_id>/$afiri_uniq_id/g;
				
				print "$html_work2[$i]\n";
			}
		}
		
		# フォームログ
		&FormLog;
	}else{
		
		#入力画面で非表示にする部分----------------------------------
		#エラー表示用
		$invisible_error = 0;
		#確認画面用
		$invisible_confirm = 0;
		#送信完了画面用
		$invisible_thanks = 0;
		
		$html_work = $html;
		@html_work2 = split(/\n/,$html_work);
		for($i=0;@html_work2>$i;$i++){
			#エラー画面
			if($html_work2[$i] =~ /<!--%%fmail-error-contents-start%%-->/){
				#見えない箇所開始
				$invisible_error = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-error-contents-end%%-->/){
				#見える箇所終了
				$invisible_error = 9;
			}
			
			#確認画面
			if($html_work2[$i] =~ /<!--%%fmail-confirm-contents-start%%-->/){
				#見えない箇所開始
				$invisible_confirm = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-confirm-contents-end%%-->/){
				#見える箇所終了
				$invisible_confirm = 9;
			}
			
			#送信完了画面
			if($html_work2[$i] =~ /<!--%%fmail-thanks-contents-start%%-->/){
				#見えない箇所開始
				$invisible_thanks = 1;
			}
			if($html_work2[$i] =~ /<!--%%fmail-thanks-contents-end%%-->/){
				#見える箇所終了
				$invisible_thanks = 9;
			}
			
			if($invisible_error ne '1' && $invisible_confirm ne '1' && $invisible_thanks ne '1'){
				print "$html_work2[$i]\n";
			}
		}
		
		#送信完了画面で表示させる部分----------------------------------
		
		# フォームログ
		&FormLog;
	}
	#追加プログラム---------------------------------------------------------------------
	#元のソース
	#print $html;
}
exit;
sub GET {
	$buffer = $ENV{'QUERY_STRING'};
	@pairs = split(/&/, $buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$name =~ tr/+/ /;
		$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$_GET{$name} = $value;
	}
}
sub escape {
	my($str) = @_;
	$str =~ s/\&/&quot;/g;
	$str =~ s/</\&lt;/g;
	$str =~ s/>/\&gt;/g;
	$str =~ s/\n/<br \/>/g;
	return $str;
}
sub syslog {
	my($str) = @_;
	&WppSaveAddLine('debug.txt',$str);
}

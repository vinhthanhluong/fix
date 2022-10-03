#!/usr/bin/perl --

use CGI::Carp qw(fatalsToBrowser);
use CGI;
use Digest::MD5 qw(md5_hex);
require './commons/conf.cgi';
require './commons/cgi-lib.pl';
require '../fmail.lib.cgi';
require $registry;
&getform;
use lib qw(./);
use lib qw(../);
use Jcode;

# コピーモジュールが使えない場合は、「0」
$flag_copy_mod = 1; # 1=使用 / 0=未使用
if($flag_copy_mod){
	use File::Copy;
}


$attached_method = $reg{'attached_method'};

$buffer = $ENV{'QUERY_STRING'};
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$name =~ tr/+/ /;
	$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$value =~ s/\,/\./g;
	$form{$name} = $value;
}

if(&loginCheck){
	require "commons/modulelist.cgi";
	require "commons/power.cgi";
	$module_path = './modules/' . $form{'m'} . '/include.cgi';
	$module_conf_path = "${dir_datas}modules\/$form{'m'}\.cgi";
	$module_action_path = "./modules/$form{'m'}/action.$form{'a'}.cgi";
	if(-f $module_path){
		
	}
	else{
		$form{'m'} = 'home';
	}
	if(-f $module_conf_path){
		require $module_conf_path;
	}
	if(-f $module_path){
		require $module_path;
	}
	if(-f $module_action_path){
		require $module_action_path;
	}
	else {
		require "./modules/$form{'m'}/default.cgi";
	}
	if($flag{'ajax'}){
		
	}
	else {
		$include_path = "./modules/" . $form{'m'} . '/include.js';
		if(-f $include_path){
			$include_tag .= "<script type=\"text/javascript\" src=\"modules/" . $form{'m'} . "/include.js\"></script>";
		}
		$include_path = "./modules/" . $form{'m'} . '/include.css';
		if(-f $include_path){
			$include_tag .= "<link rel=\"stylesheet\" href=\"modules/" . $form{'m'} . "/include.css\" type=\"text/css\" />";
		}
		&display();
		
	}

	require './modules/global_menu.cgi';
	$html =~ s/$sp_topheader/$globalmenu/ig;
	$html =~ s/<!--module_list-->/$module_list/ig;
	$html =~ s/$sp_include/$include_tag/ig;
}
else{
	if($flag{'ajax'}){
		$html = "SESSION ERROR";
	}
	else {
		$html = &loadhtml('login','ログイン画面',$loginframe);
		$html =~ s/<!--user_id-->/$form{'login_user_id'}/ig;
		$html =~ s/<!--WebSiteAdmin-Warning-->/$warning_message/ig;
		$html =~ s/<!--m-->/$form{'m'}/ig;
	}
}

if($redirect){
	#print "Location: $reg{'SERVER_PROTOCOL'}://${this_url}index.cgi${redirect}\n\n";
	if($redirect eq "zip"){
		print "Location: zip.php\n\n";
	}
	else {
		print "Location: index.cgi${redirect}\n\n";
	}
}
else {
#		$cookie_path = $ENV{'SCRIPT_NAME'};
#		@cookie_path = split(/\//,$cookie_path);
#		$cookie_path[-1] = "";
#		$cookie_path = join('/',@cookie_path);
	my $q = CGI->new();
	$cookie_path = $q->url();
	#Preview-Server or not
	#iCLUSTAの別サーバーのみ環境変数 HTTP_X_FUJITSUBO_PROXY が用意されており、別サーバーのFQDNがセットされている
	if ($ENV{'HTTP_X_FUJITSUBO_PROXY'}) {
		$cookie_path =~ s/^http[s]?\:\/\///i;
	} else {
		$cookie_path =~ s/^http[s]?\:\/\/.*?\///i;
	}
	$cookie_path = '/' . $cookie_path;
	#iCLUSTA対応用として、仕上げにファイル名を削除
	$cookie_path =~ s/index.cgi//i;
	
	
	print "Pragma: no-cache\n";
	print "Cache-Control: no-cache\n";
	print "Content-type: text/html; charset=UTF-8\n";
	#print "Set-Cookie: session_id=${session_id}; path=${cookie_path}; expires=Mon, 30 Dec 2020 23:59:59 GMT\n\n";
	print "Set-Cookie: session_id=${session_id}; path=${cookie_path}; \n\n";
	print $html;
}
exit;
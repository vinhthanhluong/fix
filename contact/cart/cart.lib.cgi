use CGI::Cookie;
use File::Find;

#----------------------------------------------------------------------------------------
#  Initial Setting
#----------------------------------------------------------------------------------------
# Time units (truncated after the decimal point)
$hour_stamp = int(time / 3600);

# Time the session authorization
$hour_limit = 4;

# Session file
$ses_file = './cart.admin/datas/sessions/';

# Lock directory for session files
$ses_lockdir = './cart.admin/datas/sessions/lock_';


#----------------------------------------------------------------------------------------
#  Set session
#----------------------------------------------------------------------------------------
sub set_session {
	# Generating the hash key
	$hashid = &createId;

	# Cookies set
	$cookie = &set_cookie;

	# Synthesis of the session file name
	$ses_set_file = $ses_file . $hashid . '.cgi';

	# File locking
	&file_lock($ses_lockdir . $hashid);

	# Creating a session file
	open(SES,">$ses_set_file");
		print SES "$hour_stamp";
	close(SES);

	# Release file lock
	&file_unlock($ses_lockdir . $hashid);

	print "$cookie\n";

}


#------------------------------------------------
#  Issue of the session ID
#------------------------------------------------
sub createId {

	@alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9");
	# Number of digits
	$digit = 10;
	$hash_char = "";
	for($cnt=0;$cnt<$digit;$cnt++){
		my($randno) = int(rand @alphabet);
		$hash_char .= $alphabet[$randno];
	}
	$hash_char = time . $hash_char;
	return $hash_char;
}


#------------------------------------------------
#  Cookies set
#------------------------------------------------
sub set_cookie {

	my $cookie = 'Set-Cookie: ';
	$cookie .= "socket=$hashid\;";
	# Is valid until the browser is closed
	#$cookie .= "expires=\;";
	$cookie .= "path=/";

	return $cookie;

}


#----------------------------------------------------------------------------------------
#  File locking
#----------------------------------------------------------------------------------------
sub file_lock {

	# Read the file name
	my $param = $_[0];

	# Binding of the lock directory name
	my $lockdir_combine = $param . '/';

	# If the file directory of cleaning lock is not released in error
	if(-e $lockdir_combine) {
		# If the file exists, Decision to remove them by date
		
		# Set time limit (5 minutes)
		my $limit_time = 60 * 5;
		
		# Last updated directory of lock acquisition
		my @stats = stat($lockdir_combine);
		my $judge_time = time - $stats[9];
		
		# If you exceed the time limit is directory delete the file lock
		if($judge_time > $limit_time){
			# Delete directory
			rmdir($lockdir_combine);
		}
	}

	# Flag for failure to unlock
	my $flag_locking = 1;

	for (my $i = 0; $i <= 10; $i++) {
		if (mkdir($lockdir_combine, 0755)) {
			# Success
			$flag_locking = 0;
			last;
		} else {
			# Failure
			# Wait a second re-trial
			sleep(1);
		}
	}

	if($flag_locking){
		&error('書き込みエラー　：　しばらく経ってから、再度実行してください。');
	}

}

#----------------------------------------------------------------------------------------
#  Unlock files
#----------------------------------------------------------------------------------------
sub file_unlock {
	# Parameter acquisition
	my $param = $_[0];

	# Binding of the lock directory name
	my $lockdir_combine = $param . '/';

	# Delete directory
	rmdir($lockdir_combine);
}


#----------------------------------------------------------------------------------------
#  Check session
#----------------------------------------------------------------------------------------
sub ses_check {
	
	# Delete old session files
	find(\&want_func, "$ses_file");
	
	# Delete the old file cart
	find(\&want_func, "$temp_file_cartitems");

	#-- Get the whole Cookie --#
	my %cookies = fetch CGI::Cookie;

	#-- Gets the value of the Cookie --#
	if(exists $cookies{'socket'}){
		$cookies_value = $cookies{'socket'}->value;
		$cookies_expires = $cookies{'socket'}->expires;
		$cookies_domain  = $cookies{'socket'}->domain;
		$cookies_path = $cookies{'socket'}->path;
	}
	
	# Synthesis session file name
	$ses_check_file .= $ses_file . $cookies_value . '.cgi';
	
	# Reading time in the session file
	open(SES,"<$ses_check_file");
		$ses_stamp = <SES>;
	close(SES);
	
	# Calculation of connection time
	$use_check = $hour_stamp - $ses_stamp;

	# Check connection time limit
	if($use_check > $hour_limit || $ses_stamp eq ''){
		# Redirect timeout
		#print "Location:../../index.cgi\n\n";
		# Re-create the time-out session
		$flag_session_make = 1;
	}
}



#----------------------------------------------------------------------------------------
#  Remove the old session files
#----------------------------------------------------------------------------------------
sub want_func{
	# cgi file extraction
	if($File::Find::name =~ /.cgi/){
		
		# Acquisition of property files
		@filestat = stat $_;
		
		# Update time (Calculated on an hourly basis)
		$mtime = int($filestat[9] / 3600);
		
		# Difference calculation update time of files
		$del_time = $hour_stamp - $mtime;
		
		# Time-out file
		if($del_time > $hour_limit){
			# Delete
			unlink $_;
		}
	}

}




#----------------------------------------------------------------------------------------
#  Acquisition of GET parameters
#----------------------------------------------------------------------------------------
sub get_param {
	# Retrieve GET parameters
	$query_string = $ENV{"QUERY_STRING"};
	@params = split(/&/, $query_string);

	# Question for code
	$param = $params[0];

	# GET parameter set to an associative array
	foreach $params(@params) {
		# The "variable name = value" Decompose at "="
		($name, $value) = split(/=/, $params);
		# Decode
		$value =~ tr/+/ /;
		$value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex( $1 ))/eg;
		# For later use, you assign to $ in {'name'}
		$in{$name} = $value;
	}
}




#------------------------------------------------
#  Referer set
#------------------------------------------------
sub set_referer {

	my $referer_cookie = 'Set-Cookie: ';
	$referer_cookie .= "referer=@_\;";
	# Is valid until the browser is closed
	#$referer_cookie .= "expires=\;";
	$referer_cookie .= "path=/";
	
	print "$referer_cookie\n";

}




#------------------------------------------------
#  Referer load
#------------------------------------------------
sub load_referer {
	#-- Get the whole Cookie --#
	my %referer_cookies = fetch CGI::Cookie;

	#-- Gets the value of the Cookie --#
	if(exists $referer_cookies{'referer'}){
		$referer_cookies_value = $referer_cookies{'referer'}->value;
		$referer_cookies_expires = $referer_cookies{'referer'}->expires;
		$referer_cookies_domain  = $referer_cookies{'referer'}->domain;
		$referer_cookies_path = $referer_cookies{'referer'}->path;
	}
	return $referer_cookies_value;

}





#----------------------------------------------------------------------------------------
#  Decimal Separator
#----------------------------------------------------------------------------------------
sub decimal_separator { 
my $num = shift; 
if ($num =~ /^[-+]?\d\d\d\d+/g) {
	for (my $i = pos($num) - 3, my $j = $num =~ /^[-+]/; $i > $j; $i -= 3) {
		substr($num, $i, 0) = ',';
	}
}
	return $num;
}







#----------------------------------------------------------------------------------------
#  エラーページ
#----------------------------------------------------------------------------------------
sub error {
# HTML宣言
print "Content-type: text/html\n\n";

# テンプレートファイルの読み込み
open(OUT,"<$cart_tmplate");
	while($tmp = <OUT>){
		
		if($tmp =~/<!-- Error Tag -->/){
			$tmp =~ s/<!-- Error Tag -->/@_/g;
		}
		
		# 通常データ
		$html .= $tmp;
		$html .= $ENV{'HTTP_COOKEI'};
		
	}
close(OUT);

# 画面表示
print $html;

exit;
}

#!/usr/bin/perl --

use CGI;
#use lib qw(../Jcode);
use Unicode::Japanese;
use Unicode::Japanese qw(unijp);

require '../fmail.admin/commons/conf.cgi';
require '../fmail.admin/commons/registry.cgi';
require 'cart.lib.cgi';

# -------------------------------------------- #
#  Initial Setting
# -------------------------------------------- #
# Script File
$script = 'index.cgi';

# Template File
$cart_tmplate = 'index.tpl';

# Fmail File
$fmail_script = '../index.cgi';

# Cartitems Temporary Data
$temp_file_cartitems = './cart.admin/datas/cart.items/';

# Cartitems File Lock Directory
$lockdir_cartitems = './cart.admin/datas/cart.items/lock_';

# Get Date
($sec,$min,$hour,$day,$mon,$year) = gmtime(time + 9 * 3600);$mon++;$year += 1900;
$date_stamp = sprintf("%04d%02d%02d",$year,$mon,$day);

# Specifies ID of Fmail
$current_data_path = '../fmail.admin/datas/modules/mailform_env/mailform_env.dat';
@current_data = &loadfile($current_data_path);
$current_data = join("\n",@current_data);
($flag,$expires_start,$expires_end,$limit,$serials,$thanks_page,$sendmail_path,$logsave,$cart_in_element,$cart_logsave,$form_logsave,$form_logsave_period,$send_mode,$attached_mode,$display_mode,$logdata_path,$cart_logdata_path,$mailform_sender_address_name,$mailform_sender_address,$mail_method,$thanks_message,$title_mailform,$title_confirm,$title_error,$title_thanks,$mail_dustclear,$mail_dustclear_zero,$client_info,$site_url,$table_style,$th_style,$td_style,$separate_before,$separate_after,$flag_afiri,$afiri1_tag,$afiri2_tag,$afiri3_tag,$afiri4_tag,$afiri5_tag,$flag_smartphone_tpl,$flag_futurephone_tpl,$setlang,$spamcheck,$domaincheck,$encheck) = split(/\n/,$current_data);
$post_name = 'en' . ${cart_in_element};

# Carriage Data Load
$cartcarriage_data_path = '../fmail.admin/datas/modules/cart_carriage/cart_carriage.dat';
@cartcarriage_data = &loadfile($cartcarriage_data_path);
$cartcarriage_data = join("\n",@cartcarriage_data);
($carriage_place,$carriage_price,$flag_free,$carriage_limit) = split(/\n/,$cartcarriage_data);
# Destination Split
@carriage_place_arr = split(/<br \/>/,$carriage_place);
@carriage_price_arr = split(/<br \/>/,$carriage_price);
for(my $i=0; @carriage_place_arr>$i; $i++) {
	$carriage_work = "$carriage_place_arr[$i]　$carriage_price_arr[$i]円";
	push(@carriage_arr,$carriage_work);
}

# Smartphone Judgement Flag
$flag_smartphone = 0;
if($flag_smartphone_tpl == 1){
	for($smartphone=0;@SMARTPHONE_USER_AGENT>$smartphone;$smartphone++){
		if($ENV{'HTTP_USER_AGENT'} =~ /$SMARTPHONE_USER_AGENT[$smartphone]/){
			# Determined Smartphone. Flag ON
			$flag_smartphone = 1;
		}
	}
}
# ハッシュIDの削除（ゴミデータ）
$hashid="";

# -------------------------------------------- #
#  The Main Routine
# -------------------------------------------- #
# Check the referrer
# URL of the current
my $filehash = CGI->new();
my $thisurl = $filehash->url;

if($thisurl !~ /$ENV{'HTTP_REFERER'}/) {
	&set_referer($ENV{'HTTP_REFERER'});
}
$referer_cookie = &load_referer;

# Check the session
&ses_check;

# Session is created if the deadline has passed or the file does not exist.
if($flag_session_make) {
	&set_session;
}

# Set the file name
if($hashid) {
	$ses_id = $hashid;
} else {
	$ses_id = $cookies_value;
}
$cartitems_file = $temp_file_cartitems . $ses_id . '.cgi';

# Get Data
$q = new CGI;
$mode = $q->param('mode');

# Get param get
&get_param;

if($mode eq 'cart_total') {
	# Confirm
	&confirm;
} elsif($in{'m'} eq 'd') {
	# Delete unnecessary data in the cart
	&cart_del;
} elsif($in{'m'} eq 'n') {
	# Quantity change
	&cart_pnum_save;
} else {
	# Cart page
	&cart_page;
}


# -------------------------------------------- #
#  Cart del
# -------------------------------------------- #
sub cart_del {
	
	# Set the temporary file name
	$temp_file_cartitems .= 'temp' . $ses_id . '.cgi';
	
	# File lock
	&file_lock($lockdir_cartitems . $ses_id);
	
	
	# Write to the file
	open(TMP,">$temp_file_cartitems");
		
		open(IN,"<$cartitems_file");
			
			while($data = <IN>) {
				@arr = split(/,/,$data);
				# Non-target data is not deleted
				if($in{'o'} ne $arr[0]) {
					print TMP "$data";
				}
			}
			
		close(IN);
		
	close(TMP);
	
	# Release file lock
	&file_unlock($lockdir_cartitems . $ses_id);
	
	rename($temp_file_cartitems,$cartitems_file);	
	
	# Redirect
	print "Location: ./\n\n";
}


# -------------------------------------------- #
#  Cart pnum save
# -------------------------------------------- #
sub cart_pnum_save {
	
	# Set the temporary file name
	$temp_file_cartitems .= 'temp' . $ses_id . '.cgi';
	
	# File lock
	&file_lock($lockdir_cartitems . $ses_id);
	
	
	# Write to the file
	open(TMP,">$temp_file_cartitems");
		
		open(IN,"<$cartitems_file");
			
			while($data = <IN>) {
				@arr = split(/,/,$data);
				# Non-target data is written
				if($in{'o'} ne $arr[0]) {
					print TMP "$data";
				} elsif($in{'o'} eq $arr[0]) {
					# Recalculate subtotal
					$subtotal = $arr[5] * $in{'n'};
					# orderid pcode pname pdetail1 pdetail2 pprice pnum subtotal
					print TMP "$arr[0],$arr[1],$arr[2],$arr[3],$arr[4],$arr[5],$in{'n'},$subtotal,\n";
				}
			}
			
		close(IN);
		
	close(TMP);
	
	# Release file lock
	&file_unlock($lockdir_cartitems . $ses_id);
	
	rename($temp_file_cartitems,$cartitems_file);
	
	# Redirect
	print "Location: ./\n\n";
}


# -------------------------------------------- #
#  Cart Page
# -------------------------------------------- #
sub cart_page {
	# Writing only if the POST data exists
	if($mode eq 'cart_in') {
		# Data set
		# Datas detail
		#--------------------------------------------------------------
		# pcode / pname / pdetail1 / pdetail2 / pprice / pnum / pnum_hidden
		#--------------------------------------------------------------
		$pcode = $q->param('pcode');
			$pcode =~ s/,/&cedil\;/g;
			$pcode =~ s/\n//g;
		$pname = $q->param('pname');
			$pname =~ s/,/&cedil\;/g;
			$pname =~ s/\n//g;
		$pdetail1 = $q->param('pdetail1');
			$pdetail1 =~ s/,/&cedil\;/g;
			$pdetail1 =~ s/\n//g;
		$pdetail2 = $q->param('pdetail2');
			$pdetail2 =~ s/,/&cedil\;/g;
			$pdetail2 =~ s/\n//g;
		$pprice = $q->param('pprice');
			$pprice = Unicode::Japanese->new($pprice)->z2h->get;
			$pprice =~ tr/0-9//cd;
		$pnum = $q->param('pnum');
			$pnum = Unicode::Japanese->new($pnum)->z2h->get;
			$pnum =~ tr/0-9//cd;
		
		# Set the temporary file name
		$temp_file_cartitems .= 'temp' . $ses_id . '.cgi';
		
		
		# Generating the hash key for the order record
		$order_id = 'od' . &createId;
		
		# File lock
		&file_lock($lockdir_cartitems . $ses_id);
		
		# Write to the file
		open(TMP,">$temp_file_cartitems");
			
			open(IN,"<$cartitems_file");
				
				while($data = <IN>) {
					@arr = split(/,/,$data);
					# Recalculate order quantity
					$pnum_after = $arr[6] + $pnum;
					if($pcode eq $arr[1] && $pname eq $arr[2] && $pdetail1 eq $arr[3] && $pdetail2 eq $arr[4] && $pprice eq $arr[5]) {
						# Recalculate subtotal
						$subtotal = $arr[5] * $pnum_after;
						# orderid pcode pname pdetail1 pdetail2 pprice pnum subtotal
						print TMP "$arr[0],$arr[1],$arr[2],$arr[3],$arr[4],$arr[5],$pnum_after,$subtotal,\n";
						$flag_wdata = 1;
					} else {
						print TMP "$data";
					}
				}
				
				# Add a record that if a duplicate record does not exist
				if($flag_wdata != 1 && $pcode && $pname && $pprice && $pnum) {
					# Recalcutlate subtotal
					$subtotal = $pprice * $pnum;
					# orderid pcode pname pdetail1 pdetail2 pprice pnum subtotal
					print TMP "$order_id,$pcode,$pname,$pdetail1,$pdetail2,$pprice,$pnum,$subtotal,\n";
				}
			
			close(IN);
			
		close(TMP);
		
		# Release file lock
		&file_unlock($lockdir_cartitems . $ses_id);
		
		rename($temp_file_cartitems,$cartitems_file);
	}
	
	
	
	# Screen display
	if(!$flag_smartphone) {
		# PC向け（スマフォの場合、構造が変わる）
		$cart_data =<<"		EOD";
				<h2 class="cart_total">カート詳細</h2>
				<form action="$script" method="POST" name="cart_total" class="cart_total">
					<fieldset>
						<table>
							<tr>
								<th class="t_code">商品コード</th>
								<th class="t_name">商品名</th>
								<th class="t_detail">商品詳細1</th>
								<th class="t_detail">商品詳細2</th>
								<th class="t_price">単価（税込）</th>
								<th class="t_num">個数</th>
								<th class="t_delete">削除</th>
							</tr>
		EOD
	} else {
		# スマフォ向け
		$cart_data =<<"		EOD";
				<h2 class="cart_total_sp">カート詳細</h2>
				<form action="$script" method="POST" class="cart_total_sp">
					<fieldset>
						<dl>
		EOD
	}
	
	# Write to the file
	open(IN,"<$cartitems_file");
	
	$j = 1;
	while($data = <IN>) {
		@arr = split(/,/,$data);
		@arr_num = split(/ /,$arr[7]);
		$pprice = &decimal_separator($arr[5]);
		# Data load
		if(!$flag_smartphone) {
			# PC向け
			$cart_data .=<<"			EOD";
							<tr>
								<td class="t_code">$arr[1]<input type="hidden" name="pcode_$j" value="$arr[1]" id="pcode_$j" /></td>
								<td class="t_name">$arr[2]<input type="hidden" name="pname_$j" value="$arr[2]" id="pname_$j" /></td>
								<td class="t_detail">$arr[3]<input type="hidden" name="pdetail1_$j" value="$arr[3]" id="pdetail1_$j" /></td>
								<td class="t_detail">$arr[4]<input type="hidden" name="pdetail2_$j" value="$arr[4]" id="pdetail2_$j" /></td>
								<td class="t_price">$pprice円<input type="hidden" name="pprice_$j" value="$arr[5]" id="pprice_$j" /></td>
								<td class="t_num">
			EOD
		} else {
			# スマフォ向け
			$cart_data .=<<"			EOD";
							<dt class="t_code">商品コード</dt>
							<dd class="t_code">$arr[1]<input type="hidden" name="pcode_$j" value="$arr[1]" id="pcode_$j" /></dd>
							
							<dt class="t_name">商品名</dt>
							<dd class="t_name">$arr[2]<input type="hidden" name="pname_$j" value="$arr[2]" id="pname_$j" /></dd>
							
							<dt class="t_detail">商品詳細1</dt>
							<dd class="t_detail">$arr[3]<input type="hidden" name="pdetail1_$j" value="$arr[3]" id="pdetail1_$j" /></dd>
							
							<dt class="t_detail">商品詳細2</dt>
							<dd class="t_detail">$arr[4]<input type="hidden" name="pdetail2_$j" value="$arr[4]" id="pdetail2_$j" /></dd>
							
							<dt class="t_price">単価（税込）</dt>
							<dd class="t_price">$pprice円<input type="hidden" name="pprice_$j" value="$arr[5]" id="pprice_$j" /></dd>
							
							<dt class="t_num">個数</dt>
							<dd class="t_num">
			EOD
		}
		
		
		# Order quantity
		$cart_data .=<<"		EOD";
									<input type="text" name="pnum_$j" value="$arr[6]" id="pnum_$j" onchange="pnumsave(this,'$arr[0]');" />
		EOD
		
		if(!$flag_smartphone) {
			# PC向け
			$cart_data .=<<"			EOD";
								</td>
								<td class="t_delete"><a href="index.cgi?m=d&o=$arr[0]"><img src="./images/item_delete.gif" alt="削除" class="item_delete"></a></td>
							</tr>
			EOD
		} else {
			# スマフォ向け
			$cart_data .=<<"			EOD";
							</dd>
							
							<dt class="t_delete">削除</dt>
							<dd class="t_delete"><a href="index.cgi?m=d&o=$arr[0]"><img src="./images/item_delete_sp.gif" alt="削除" class="item_delete"></a></dd>
							
			EOD
		}
		
		$j ++;
	}
	close(IN);
	
	
	if($flag_free) {
		$carriage_limit = &decimal_separator($carriage_limit);
		$carriage_comment = qq|<p class="carriage_comment">※ $carriage_limit 円以上のお買い上げで送料無料</p>|;
	}
	
	if(!$flag_smartphone) {
		# PC向け
		$cart_data .=<<"		EOD";
						</table>
						<table class="carriage">
							<tr>
								<th class="postal">郵送先地域</th>
								<td>
									<select name="carriage">
		EOD
		
		for(my $i=0; @carriage_arr>$i; $i++) {
			$cart_data .=<<"			EOD";
										<option value="$carriage_arr[$i]">$carriage_arr[$i]</option>
			EOD
		}
		
		$cart_data .=<<"		EOD";
									</select>
									$carriage_comment
								</td>
							<tr>
						</table>
						<input type="hidden" name="porder" value="$ses_id" id="porder" />
						<input type="hidden" name="mode" value="cart_total" />
						<p class="submit"><input type="submit" value="" class="submit" /></p>
						<p class="window_close"><img src="./images/cart_back_off.gif" alt="戻る" onclick="#JAVASCRIPTPAGEBACK"></p>
					</fieldset>
				</form>
		EOD
	} else {
		# スマフォ向け
		$cart_data .=<<"		EOD";
						</dl>
						<p class="carriage">
							<span class="postal">郵送先地域</span>
							<select name="carriage">
		EOD
		
		for(my $i=0; @carriage_arr>$i; $i++) {
			$cart_data .=<<"			EOD";
								<option value="$carriage_arr[$i]">$carriage_arr[$i]</option>
			EOD
		}
		
		$cart_data .=<<"		EOD";
							</select>
							$carriage_comment
						</p>
						<input type="hidden" name="porder" value="$ses_id" id="porder" />
						<input type="hidden" name="mode" value="cart_total" />
						<p class="submit"><input type="submit" value="" class="submit" /></p>
						<p class="window_close_sp"><img src="./images/cart_back_off.gif" alt="戻る" onclick="#JAVASCRIPTPAGEBACK"></p>
					</fieldset>
				</form>
		EOD
	}
	
	
	
	
	
	print "Content-type: text/html\n\n";
	
	$flag_confirm_disp = 0;
	
	# 直前ページデータが無い場合
	if(!$referer_cookie) {
		$referer_cookie = $ENV{'HTTP_REFERER'};
	}
	
	if(!$flag_smartphone) {
		# PC向け
		open(OUT,"<$cart_tmplate");
			while($html_data = <OUT>) {
				$html_data =~ s/<!-- Cart Tag -->/$cart_data/g;
				$html_data =~ s/#JAVASCRIPTPAGEBACK/locationhref('$referer_cookie')/g;
				
				# 確認画面用非表示
				if($html_data =~ /<!--%%fmail-cart-confirm-start%%-->/) {
					$flag_confirm_disp = 1;
				}
				if($html_data =~ /<!--%%fmail-cart-confirm-end%%-->/) {
					$flag_confirm_disp = 9;
				}
				
				if($flag_confirm_disp != 1) {
					$html .= $html_data;
				}
				
			}
		close(OUT);
	} else {
		# スマフォ向け
		open(OUT,"<$cart_tmplate");
			while($html_data = <OUT>) {
				$html_data =~ s/<!-- viewport -->/<meta id="viewport" name="viewport" content="width=device-width">/g;
				$html_data =~ s/<!-- Cart Tag -->/$cart_data/g;
				$html_data =~ s/#JAVASCRIPTPAGEBACK/locationhref('$referer_cookie')/g;
				
				# 確認画面用非表示
				if($html_data =~ /<!--%%fmail-cart-confirm-start%%-->/) {
					$flag_confirm_disp = 1;
				}
				if($html_data =~ /<!--%%fmail-cart-confirm-end%%-->/) {
					$flag_confirm_disp = 9;
				}
				
				if($flag_confirm_disp != 1) {
					$html .= $html_data;
				}
				
			}
		close(OUT);
	}
	
	print $html;
}


# -------------------------------------------- #
#  Confirm Page
# -------------------------------------------- #
sub confirm {
	# Get the value of name
	@names = $q->param;
	
	# Datas detail
	#--------------------------------------------------------------
	# pcode_x / pname_x / pdetail_x / pprice_x / pnum_x / mode
	#--------------------------------------------------------------
	
	# Order number check
	for(my $i=0; $i<@names; $i++) {
		@arr_names = split(/_/,$names[$i]);
		if($arr_names[1]) {
			$flag_order_last_number = $arr_names[1];
		}
	}
	
	# For display
	if(!$flag_smartphone) {
		# PC向け
		$for_disp =<<"		EOD";
	<h2 class="cart_confirm">確認画面</h2>
	<table class="cart_confirm">
		<tr>
			<th class="t_code">商品コード</th>
			<th class="t_name">商品名</th>
			<th class="t_detail">商品詳細1</th>
			<th class="t_detail">商品詳細2</th>
			<th class="t_price">単価（税込）</th>
			<th class="t_num">個数</th>
			<th class="t_subtotal">小計（税込）</th>
		</tr>
		EOD
	} else {
		# スマフォ向け
		$for_disp =<<"		EOD";
	<h2 class="cart_confirm_sp">確認画面</h2>
	<dl class="cart_confirm_sp">
		EOD
	}
	
	# Repeat number of orders
	$porder = $q->param("porder");
	$cart_post_data = 'お問い合わせ番号：　' . $porder ."\n";
	$cart_post_data .= "--------------------------------------\n";
	for(my $i=0; $i<$flag_order_last_number; $i++) {
		$x = $i + 1;
		$pcode = $q->param("pcode_$x");
		$pname = $q->param("pname_$x");
		$pdetail1 = $q->param("pdetail1_$x");
		$pdetail2 = $q->param("pdetail2_$x");
		$pprice = $q->param("pprice_$x");
		$pnum = $q->param("pnum_$x");
		# 数量サニタイズ
		$pnum = &sanitizing_num($pnum);
		$sub_total = $pprice * $pnum;
		
		$total += $sub_total;
		
		# Decimal separate
		$pprice = &decimal_separator($pprice);
		$pnum = &decimal_separator($pnum);
		$sub_total = &decimal_separator($sub_total);
		
		if(!$flag_smartphone) {
			# PC向け
			$for_disp .=<<"			EOD";
		<tr>
			<td class="t_code">$pcode</td>
			<td class="t_name">$pname</td>
			<td class="t_detail">$pdetail1</td>
			<td class="t_detail">$pdetail2</td>
			<td class="t_price">$pprice円</td>
			<td class="t_num">$pnum</td>
			<td class="t_subtotal">$sub_total円</td>
		</tr>
			EOD
		} else {
			# スマフォ向け
			$for_disp .=<<"			EOD";
		<dt class="t_code">商品コード</dt>
		<dd class="t_code">$pcode</dd>
		
		<dt class="t_name">商品名</dt>
		<dd class="t_name">$pname</dd>
		
		<dt class="t_detail">商品詳細1</dt>
		<dd class="t_detail">$pdetail1</dd>
		
		<dt class="t_detail">商品詳細2</dt>
		<dd class="t_detail">$pdetail2</dd>
		
		<dt class="t_price">単価（税込）</dt>
		<dd class="t_price">$pprice円</dd>
		
		<dt class="t_num">個数</dt>
		<dd class="t_num">$pnum</dd>
		
		<dt class="t_subtotal">小計（税込）</dt>
		<dd class="t_subtotal">$sub_total円</dd>
		
			EOD
		}
		
		# For send
		$pcode = 'コード：　' . $pcode ."\n";
		$pname = '商品名：　' . $pname ."\n";
		$pdetail1 = '詳細1：　' . $pdetail1 ."\n";
		$pdetail2 = '詳細2：　' . $pdetail2 ."\n";
		$pprice = '単価（税込）：　' . $pprice ."円\n";
		$pnum = '個数：　' . $pnum ."\n";
		$sub_total = '小計（税込）：　' . $sub_total ."円\n";
		
		$cart_post_data .= $pcode . $pname . $pdetail1 . $pdetail2 . $pprice . $pnum . $sub_total;
		$cart_post_data .= "--------------------------------------\n";
	}
	
	# Carriage Price
	$carriage_price = $q->param("carriage");
	@carriage_price_arr = split(/　/,$carriage_price);
	$carriage_price = $carriage_price_arr[-1];
	$carriage_price =~ s/円//g;
	$disp_carriage_price = &decimal_separator($carriage_price);
	
	
	# Carriage Price Check
	if($flag_free) {
		if($total >= $carriage_limit) {
			$total -= $carriage_price;
			$disp_carriage_price = 0;
		}
	}
	# For dispay total
	$total += $carriage_price;
	
	$total = &decimal_separator($total);
	
	# For send carriage
	$cart_post_data .= '送料（税込）：　' . $disp_carriage_price . '円' . "\n";
	
	# For send total
	$cart_post_data .= '合計（税込）：　' . $total . '円';
	
	if(!$flag_smartphone) {
		# PC向け
		$for_disp .=<<"		EOD";
	</table>
	<table class="total_carriage"><tr><td>送料（税込）：　$disp_carriage_price円</td></tr></table>
	<table class="total"><tr><td>合計（税込）：　$total円</td></tr></table>
		EOD
	} else {
		# スマフォ向け
		$for_disp .=<<"		EOD";
	</dl>
	<p class="total_carriage_sp">送料（税込）：<span class="disp_price">$disp_carriage_price円</span></p>
	<p class="total_sp">合計（税込）：<span class="disp_price">$total円</span></p>
		EOD
	}
	
	if(!$flag_smartphone) {
		# PC向け
		$confirm_data =<<"		EOD";
$for_disp
	
	<form action="$fmail_script" method="POST" class="cart_confirm">
		<fieldset>
			<textarea name="$post_name">$cart_post_data</textarea>
			<p class="submit"><input type="submit" value="" class="submit"></p>
			<p class="window_close"><img src="./images/cart_back_off.gif" alt="戻る" onclick="#JAVASCRIPTPAGEBACK"></p>
		</fieldset>
	</form>
		EOD
	} else {
		# スマフォ向け
		$confirm_data =<<"		EOD";
$for_disp
	
	<form action="$fmail_script" method="POST" class="cart_confirm_sp">
		<fieldset>
			<textarea name="$post_name">$cart_post_data</textarea>
			<p class="submit"><input type="submit" value="" class="submit"></p>
			<p class="window_close_sp"><img src="./images/cart_back_off.gif" alt="戻る" onclick="#JAVASCRIPTPAGEBACK"></p>
		</fieldset>
	</form>
		EOD
	}
	
	print "Content-type: text/html\n\n";
	
	$flag_detail_disp = 0;
	
	if(!$flag_smartphone) {
		# PC向け
		open(OUT,"<$cart_tmplate");
			while($html_data = <OUT>) {
				# Data Substitution
				$html_data =~ s/<!-- Cart Confirm Tag -->/$confirm_data/g;
				$html_data =~ s/#JAVASCRIPTPAGEBACK/javasscript:history.back()/g;
				
				# 詳細画面用非表示
				if($html_data =~ /<!--%%fmail-cart-detail-start%%-->/) {
					$flag_detail_disp = 1;
				}
				if($html_data =~ /<!--%%fmail-cart-detail-end%%-->/) {
					$flag_detail_disp = 9;
				}
				
				if($flag_detail_disp != 1) {
					$html .= $html_data;
				}
				
			}
		close(OUT);
	} else {
		# スマフォ向け
		open(OUT,"<$cart_tmplate");
			while($html_data = <OUT>) {
				$html_data =~ s/<!-- viewport -->/<meta id="viewport" name="viewport" content="width=device-width">/g;
				$html_data =~ s/<!-- Cart Confirm Tag -->/$confirm_data/g;
				$html_data =~ s/#JAVASCRIPTPAGEBACK/javasscript:history.back()/g;
				
				# 詳細画面用非表示
				if($html_data =~ /<!--%%fmail-cart-detail-start%%-->/) {
					$flag_detail_disp = 1;
				}
				if($html_data =~ /<!--%%fmail-cart-detail-end%%-->/) {
					$flag_detail_disp = 9;
				}
				
				if($flag_detail_disp != 1) {
					$html .= $html_data;
				}
				
			}
		close(OUT);
	}
	
	print $html;
}



# -------------------------------------------- #
#  Sanitize Setting
# -------------------------------------------- #
sub sanitizing_num {
	@con_befor_num = ('０','１','２','３','４','５','６','７','８','９');
	@con_after_num = ('0','1','2','3','4','5','6','7','8','9');
	
	my($str) = @_;
	for($i=0;$i<@con_befor_num;$i++){
		$str =~ s/${con_befor_num[$i]}/${con_after_num[$i]}/g;
	}
	return $str;
}

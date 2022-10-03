<?php

	$setting=unserialize(@file_get_contents(DATA_DIR.'/setting/overnotes.dat'));
	ini_set('mbstring.http_input', 'pass');
	parse_str($_SERVER['QUERY_STRING'],$_GET);
	$keyword=isset($_GET['k'])?trim($_GET['k']):'';
	$category=isset($_GET['c'])?trim($_GET['c']):'';
	$page=isset($_GET['p'])?trim($_GET['p']):'';
	$base_title = !empty($setting['title'])? $setting['title'] : 'OverNotes';

?><?php
	$contribute=get_contribute($contribute_id);
		$title=$contribute['title'];
	$category_id=$contribute['category'];
	$category_data=unserialize(@file_get_contents(DATA_DIR.'/category/'.$category_id.'.dat'));
	$category_name=$category_data['name'];
	$category_text=@$category_data['text'];
	$category_url=$category_data['id'];
	$field_id=$contribute['field'];
	$id=$contribute['id'];
	$field=get_field($field_id);
	$date=$contribute['public_begin_datetime'];
	$url=$contribute['url'].'/';

	foreach($field as $field_index=>$field_data){
		${$field_data['code'].'_Name'}=$field_data['name'];
		${$field_data['code'].'_Value'}=make_value(
		$field_data['name']
				,@$contribute['data'][$field_id][$field_index]
			,$field_data['type']
			,$id
			,$field_id
			,$field_index
		);
		if($field_data['type']=='image'){
			${$field_data['code'].'_Src'}=ROOT_URI.'/_data/contribute/images/'.@$contribute['data'][$field_id][$field_index];
		}
	}

?>
<?php
$current_category_id   = $category_id;
$current_category_name = $category_name;
?>
<?php
	$category_index=get_category_index();
	foreach($category_index as $rowid=>$id){
		$category_data=unserialize(@file_get_contents(DATA_DIR.'/category/'.$id.'.dat'));
		$category_url=$category_data['id'];
		$category_name=$category_data['name'];
		$category_text=@$category_data['text'];
		$category_id=$id;
		${'category'.$id.'_url'}=$category_data['id'];
		${'category'.$id.'_name'}=$category_data['name'];
		${'category'.$id.'_text'}=@$category_data['text'];
		$selected=(@$_GET['c']==$id?' selected="selected"':'');

?>
	<?php if( $current_category_id==$category_id ) $current_category_url = $category_url; ?>
<?php
	}
?>

<!Doctype html>
<html lang="ja">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="format-detection" content="telephone=no">
	<title><?php echo $title; ?>|<?php echo $current_category_name; ?>｜京都の外壁塗装・リフォームの「BANBA PAINT」</title>
	<?php
	if($keywords_Value){
?>
		<meta name="keywords" content="<?php echo $keywords_Value; ?>" />
		<?php
	}else{
?>
			<meta name="keywords" content="亀岡市,福知山市,外壁塗装,リフォーム,新着情報" />
	<?php
	}
?>
	<?php
	if($description_Value){
?>
		<meta name="description" content="<?php echo $description_Value; ?>" />
		<?php
	}else{
?>
			<meta name="description" content="京都亀岡市・福知山市を中心に外壁塗装・リフォームを行なっている「BANBA　PAINT」のインフォメーションページです。営業時間のお知らせから、現地調査やスタッフミーティングの様子、コラムまで、当社の活動状況やお役立ち情報を詳細にお伝えしております。当社へのご依頼やお問い合わせ、イベントへのご参加を検討される際にはぜひご活用ください。" />
	<?php
	}
?>
	<meta http-equiv="Content-Style-Type" content="text/css" />
	<meta http-equiv="Content-Script-Type" content="text/javascript" />
	<link rel="shortcut icon" href="../../images/favicon.ico" type="image/x-icon">
	<!-- CSS -->
	<link href="../../css/styles.css" rel="stylesheet" type="text/css" />
	<link href="../../css/responsive.css" rel="stylesheet" type="text/css" />
	<link href="../../css/under.css" rel="stylesheet" type="text/css" />
	<link href="../../css/under_responsive.css" rel="stylesheet" type="text/css" />

	<!-- Google Analytics start -->
	<!-- Google Analytics end -->
</head>

<body class="under">
	<div id="wrapper">
		<header id="header">
			<div class="header-wrapper">
				<h1>京都府亀岡市の外壁塗装会社「BANBA PAINT」からのお知らせ・お役立ちコラム</h1>
				<div class="header-main">
					<div class="logo">
						<a href="https://www.kabbanba.com/">
							<img src="../../images/logo.png" width="544" height="143" alt="BANBA PAINT">
						</a>
					</div>
					<div class="header-act">
						<div class="hamburger-btn">
							<div class="bar"></div>
						</div>
					</div>
				</div>
			</div>
		</header>
		<div class="header-menu ud-menu">
			<ul class="menu-list">
				<li class="dropdown">
					<span>
						基礎知識
						<span class="m-arrow"></span>
					</span>
					<ul class="sub-menu">
						<li>
							<a href="../../first/point.html">ご依頼に関するお悩み解消！①</a>
						</li>
						<li>
							<a href="../../first/price.html">ご依頼に関するお悩み解消！②</a>
						</li>
					</ul>
				</li>
				<li class="dropdown">
					<span href="#">
						サービスについて
						<span class="m-arrow"></span>
					</span>
					<ul class="sub-menu">
						<li>
							<a href="../../painting.html">塗装サービスメニュー</a>
						</li>
						<li>
							<a href="../../rain.html">雨漏り対策メニュー</a>
						</li>
						<li>
							<a href="../../reform.html">リフォームサービスメニュー</a>
						</li>
						<li>
							<a href="../../paint.html">使用する塗料の種類</a>
						</li>
						<li>
							<a href="../../price.html">料金案内</a>
						</li>
						<li>
							<a href="../../flow.html">お問い合わせから施工が完了するまで</a>
						</li>
						<li>
							<a href="../../maintenance.html">保証・アフターメンテナンス</a>
						</li>
					</ul>
				</li>
				<li class="dropdown">
					<span href="#">
						実績について
						<span class="m-arrow"></span>
					</span>
					<ul class="sub-menu">
						<li>
							<a href="../../works/">施工事例（一覧）</a>
						</li>
						<li>
							<a href="../../works/post-1">施工事例（詳細)</a>
						</li>
						<li>
							<a href="../../voice.html">お客様の喜びの声</a>
						</li>
					</ul>
				</li>
				<li class="dropdown">
					<span href="#">
						BANBA PAINTについて
						<span class="m-arrow"></span>
					</span>
					<ul class="sub-menu">
						<li>
							<a href="../../concept.html">BANBA PAINTの強み・魅力</a>
						</li>
						<li>
							<a href="../../goaisatsu.html">代表挨拶・スタッフ紹介・採用情報</a>
						</li>
						<li>
							<a href="../../faq.html">SDGsについて</a>
						</li>
						<li>
							<a href="../../company.html">会社案内・ショールーム紹介</a>
						</li>
						<li>
							<a href="../../contact/">お見積もり相談・お問い合わせフォーム</a>
						</li>

					</ul>
				</li>
				<li class="dropdown">
					<span href="#">
						インフォメーション
						<span class="m-arrow"></span>
					</span>
					<ul class="sub-menu">
						<li>
							<a href="../../news/">お知らせ・ブログ・イベント情報 (一覧)</a>
						</li>
						<li>
							<a href="../../news/post-1">お知らせ・ブログ・イベント情報 (詳細)</a>
						</li>
					</ul>
				</li>
			</ul>
			<p class="close-btn sp"><span>× CLOSE</span></p>
		</div>
		<div class="btn-fix sp">
			<ul class="fx-df">
				<li>
					<div class="fx-rt">
						<a href="../../contact?mode=tab2" class="fx-btn fx1">
							<span class="fx-w">
								<span class="fx-c">無料</span>
								<span class="fx-tt">資料請求</span>
							</span>
						</a>
						<div class="fx-phone">
							<a href="tel:0771246977" class="fx-number sweetlink">
								0771-24-6977
							</a>
							<p class="fx-text">
								【受付】9：00～18：00【定休】日曜日
							</p>
						</div>
					</div>
				</li>
				<li>
					<div class="fx-rt">
						<a href="../../contact?mode=tab1" class="fx-btn fx2">
							<span class="fx-w">
								<span class="fx-c">無料</span>
								<span class="fx-tt">お見積もり</span>
							</span>
						</a>
						<a href="../../contact?mode=tab1" class="fx-btn fx3">
							<span class="fx-w">
								<span class="fx-c">無料</span>
								<span class="fx-tt">お問い合わせ</span>
							</span>
						</a>
					</div>
				</li>
			</ul>
		</div>
		<!-- end #header-->
		<main id="main" class="main-under">
			<!-- top info = main visual -->
			<div id="mainvisual" class="under-visual udr-news-d">
				<div class="container">
					<div class="udr_fx_h2">
                        <div class="udr_box_h2">
                            <h2><span class="en">news</span><?php echo $title; ?></h2>
                        </div>
                        <p class="img sp">
                            <img src="../../images/udr_img_news_d01.jpg" alt="<?php echo $title; ?>">
                        </p>
                    </div>
				</div>
			</div>
			<!-- end #top_info -->

			<div id="content">
				<!-- topic path = breadcrumb -->
				<div id="topic-path">
					<ul class="topic-list">
						<li><a href="https://www.kabbanba.com/">ホーム</a></li>
						<li><a href="../"><?php echo $base_title; ?></a></li>
						<li><a href="../<?php echo $current_category_url; ?>"><?php echo $current_category_name; ?></a></li>
						<li><?php echo $title; ?></li>
					</ul>
				</div>
				<!-- end #topic_path -->

				<div class="section">
					<div class="news-detail">
						<h3 class="h3"> <?php echo $title; ?></h3>
						<div class="nwd-box">
							<?php
	if($img01_Value || $txt01_Value){
?>
								<div class="nwd-item">
									<?php
	if($img01_Value){
?>
										<p class="nwd-img">
											<img src="<?php echo $img01_Src; ?>" alt=" <?php echo $title; ?>">
										</p>
									<?php
	}
?>

									<?php
	if($txt01_Value){
?>
										<div class="nwd-desc">
											<?php echo $txt01_Value; ?>
										</div>
									<?php
	}
?>
								</div>
							<?php
	}
?>
							<?php
	if($img02_Value || $txt02_Value){
?>
								<div class="nwd-item">
									<?php
	if($img02_Value){
?>
										<p class="nwd-img">
											<img src="<?php echo $img02_Src; ?>" alt=" <?php echo $title; ?>">
										</p>
									<?php
	}
?>

									<?php
	if($txt02_Value){
?>
										<div class="nwd-desc">
											<?php echo $txt02_Value; ?>
										</div>
									<?php
	}
?>
								</div>
							<?php
	}
?>
							<?php
	if($img03_Value || $txt03_Value){
?>
								<div class="nwd-item">
									<?php
	if($img03_Value){
?>
										<p class="nwd-img">
											<img src="<?php echo $img03_Src; ?>" alt=" <?php echo $title; ?>">
										</p>
									<?php
	}
?>

									<?php
	if($txt03_Value){
?>
										<div class="nwd-desc">
											<?php echo $txt03_Value; ?>
										</div>
									<?php
	}
?>
								</div>
							<?php
	}
?>
							<?php
	if($img04_Value || $txt04_Value){
?>
								<div class="nwd-item">
									<?php
	if($img04_Value){
?>
										<p class="nwd-img">
											<img src="<?php echo $img04_Src; ?>" alt=" <?php echo $title; ?>">
										</p>
									<?php
	}
?>

									<?php
	if($txt04_Value){
?>
										<div class="nwd-desc">
											<?php echo $txt04_Value; ?>
										</div>
									<?php
	}
?>
								</div>
							<?php
	}
?>
							<?php
	if($img05_Value || $txt05_Value){
?>
								<div class="nwd-item">
									<?php
	if($img05_Value){
?>
										<p class="nwd-img">
											<img src="<?php echo $img05_Src; ?>" alt=" <?php echo $title; ?>">
										</p>
									<?php
	}
?>

									<?php
	if($txt05_Value){
?>
										<div class="nwd-desc">
											<?php echo $txt05_Value; ?>
										</div>
									<?php
	}
?>
								</div>
							<?php
	}
?>
							<?php
	if($img06_Value || $txt06_Value){
?>
								<div class="nwd-item">
									<?php
	if($img06_Value){
?>
										<p class="nwd-img">
											<img src="<?php echo $img06_Src; ?>" alt=" <?php echo $title; ?>">
										</p>
									<?php
	}
?>

									<?php
	if($txt06_Value){
?>
										<div class="nwd-desc">
											<?php echo $txt06_Value; ?>
										</div>
									<?php
	}
?>
								</div>
							<?php
	}
?>
							<?php
	if($img07_Value || $txt07_Value){
?>
								<div class="nwd-item">
									<?php
	if($img07_Value){
?>
										<p class="nwd-img">
											<img src="<?php echo $img07_Src; ?>" alt=" <?php echo $title; ?>">
										</p>
									<?php
	}
?>

									<?php
	if($txt07_Value){
?>
										<div class="nwd-desc">
											<?php echo $txt07_Value; ?>
										</div>
									<?php
	}
?>
								</div>
							<?php
	}
?>
							<?php
	if($img08_Value || $txt08_Value){
?>
								<div class="nwd-item">
									<?php
	if($img08_Value){
?>
										<p class="nwd-img">
											<img src="<?php echo $img08_Src; ?>" alt=" <?php echo $title; ?>">
										</p>
									<?php
	}
?>

									<?php
	if($txt08_Value){
?>
										<div class="nwd-desc">
											<?php echo $txt08_Value; ?>
										</div>
									<?php
	}
?>
								</div>
							<?php
	}
?>
							<?php
	if($img09_Value || $txt09_Value){
?>
								<div class="nwd-item">
									<?php
	if($img09_Value){
?>
										<p class="nwd-img">
											<img src="<?php echo $img09_Src; ?>" alt=" <?php echo $title; ?>">
										</p>
									<?php
	}
?>

									<?php
	if($txt09_Value){
?>
										<div class="nwd-desc">
											<?php echo $txt09_Value; ?>
										</div>
									<?php
	}
?>
								</div>
							<?php
	}
?>
							<?php
	if($img10_Value || $txt10_Value){
?>
								<div class="nwd-item">
									<?php
	if($img10_Value){
?>
										<p class="nwd-img">
											<img src="<?php echo $img10_Src; ?>" alt=" <?php echo $title; ?>">
										</p>
									<?php
	}
?>

									<?php
	if($txt10_Value){
?>
										<div class="nwd-desc">
											<?php echo $txt10_Value; ?>
										</div>
									<?php
	}
?>
								</div>
							<?php
	}
?>
						</div>
					</div>
				</div>

				<div class="section">
					<div class="btn_prev_next_sec clearfix">
						<?php $current_url = $url; ?>
						<?php
	$contribute_index=contribute_search(
		$current_category_id
		,''
		,''
		,''
		,''
		,''
	);
	$max_record_count=count($contribute_index);

?>
							<?php
	$local_index=0;
	foreach($contribute_index as $rowid=>$index){
		$contribute=unserialize(@file_get_contents(DATA_DIR.'/contribute/'.$index['id'].'.dat'));
		$title=$contribute['title'];
		$url=$contribute['url'].'/';
		$category_id=$index['category'];
		$category_data=unserialize(@file_get_contents(DATA_DIR.'/category/'.$category_id.'.dat'));
		$category_name=$category_data['name'];
		$category_text=@$category_data['text'];
		$field_id=$index['field'];
		$date=$index['public_begin_datetime'];
		$id=$index['id'];
		$field=get_field($field_id);

		foreach($field as $field_index=>$field_data){
			${$field_data['code'].'_Name'}=$field_data['name'];
			${$field_data['code'].'_Value'}=make_value(
		$field_data['name']
				,@$contribute['data'][$field_id][$field_index]
				,$field_data['type']
				,$id
				,$field_id
				,$field_index
			);
	
			if($field_data['type']=='image'){
				${$field_data['code'].'_Src'}=ROOT_URI.'/_data/contribute/images/'.@$contribute['data'][$field_id][$field_index];
			}
		}
		$local_index++;

?>
								<?php $pages[] = $url; ?>
							<?php
		foreach($field as $field_index=>$field_data){
			unset(${$field_data['code'].'_Name'});
			unset(${$field_data['code'].'_Value'});
			unset(${$field_data['code'].'_Src'});
		}
	}
?>
						
						<?php $current_page = array_search($current_url,$pages); ?>
						<ul class="btn_prev_next">
							<?php if($prev = @$pages[$current_page+1]): ?>
							<li class="prevPage"><a href="../<?php echo $prev ?>">&#8592; 前の記事へ</a></li>
							<?php endif; ?>
							<li class="centerPage"><a href="../<?php echo $current_category_url; ?>/">一覧に戻る</a></li>
							<?php if($next = @$pages[$current_page-1]): ?>
							<li class="nextPage"><a href="../<?php echo $next ?>">次の記事へ &#8594;</a></li>
							<?php endif ?>
						</ul>
					</div>
				</div>
			</div>
			<!-- end #content -->
		</main>
		<!-- end #main -->
		<footer id="footer">
			<div class="footer-top">
				<div class="container">
					<div class="ft-wrapper">
						<div class="ft-txt">
							<a href="https://www.kabbanba.com/" class="ft-logo">
								<img src="../../images/footer-logo.png" alt="BANBA PAINT">
							</a>
							<p class="ft-info">
								〒621-0814 <br>
								京都府亀岡市三宅町2丁目6番3号 <br>
								ル・シアル三宅B号室 <br>
							</p>
							<p class="ft-banner">
								<img src="../../images/ft-img01.jpg" alt="姉妹サイトバナー  ">
							</p>
						</div>
						<div class="ft-map">
							<div class="fmap">
								<iframe
									src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3268.027704567475!2d135.59031629999998!3d35.0060116!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000555d31e30689%3A0xbf73462894efa70b!2zKOagqilCQU5CQSBQQUlOVC_jg5Djg7Pjg5Djg5rjgqTjg7Pjg4g!5e0!3m2!1sja!2s!4v1663763539983!5m2!1sja!2s"
									width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"
									referrerpolicy="no-referrer-when-downgrade"></iframe>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="footer-bottom">
				<div class="container">
					<div class="fb-wrapper">
						<div class="fb-col col1">
							<ul class="fb-list">
								<li>
									<p class="fb-tt">基礎知識</p>
									<ul class="fb-sub">
										<li>
											<a href="../../first/point.html">
												ご依頼に関するお悩み解消！①
											</a>
										</li>
										<li>
											<a href="../../first/price.html">
												ご依頼に関するお悩み解消！②
											</a>
										</li>
									</ul>
								</li>
							</ul>
							<ul class="fb-list">
								<li>
									<p class="fb-tt">実績について</p>
									<ul class="fb-sub">
										<li>
											<a href="../../works/">
												施工事例
											</a>
										</li>
										<li>
											<a href="../../voice.html">
												お客様の喜びの声
											</a>
										</li>
									</ul>
								</li>
							</ul>
						</div>
						<div class="fb-col col2">
							<ul class="fb-list">
								<li>
									<p class="fb-tt">サービスについて</p>
									<ul class="fb-sub">
										<li>
											<a href="../../painting.html">
												塗装サービスメニュー
											</a>
										</li>
										<li>
											<a href="../../rain.html">
												雨漏り対策メニュー
											</a>
										</li>
										<li>
											<a href="../../reform.html">
												リフォームサービスメニュー
											</a>
										</li>
										<li>
											<a href="../../paint.html">
												使用する塗料の種類
											</a>
										</li>
										<li>
											<a href="../../price.html">
												料金案内
											</a>
										</li>
										<li>
											<a href="../../flow.html">
												お問い合わせから施工が完了するまで
											</a>
										</li>
										<li>
											<a href="../../maintenance.html">
												保証・アフターメンテナンス
											</a>
										</li>
									</ul>
								</li>
							</ul>
						</div>
						<div class="fb-col col3">
							<ul class="fb-list">
								<li>
									<p class="fb-tt">BANBA PAINTについて</p>
									<ul class="fb-sub">
										<li>
											<a href="../../concept.html">
												BANBA PAINTの強み・魅力
											</a>
										</li>
										<li>
											<a href="../../goaisatsu.html">
												代表挨拶・スタッフ紹介・採用情報
											</a>
										</li>
										<li>
											<a href="../../faq.html">
												よくあるご質問
											</a>
										</li>
										<li>
											<a href="../../faq.html">
												SDGsについて
											</a>
										</li>
										<li>
											<a href="../../company.html">
												会社案内・ショールーム紹介
											</a>
										</li>
									</ul>
								</li>
							</ul>
						</div>
						<div class="fb-col col4">
							<ul class="fb-list">
								<li>
									<p class="fb-tt">インフォメーション</p>
									<ul class="fb-sub">
										<li>
											<a href="../../news/cate_1">
												お知らせ
											</a>
										</li>
										<li>
											<a href="../../news/cate_2">
												ブログ
											</a>
										</li>
										<li>
											<a href="../../news/cate_3">
												イベント情報
											</a>
										</li>
									</ul>
								</li>
							</ul>
						</div>
					</div>
				</div>
			</div>
			<div class="copyright">Copyright &copy;BANBA PAINT. All Rights Reserved.</div>

			<div class="scroll-top"></div>
		</footer>
		<!-- end #footer -->
	</div>

	<!-- library -->
	<script src="../../js/libs/jquery.js" type="text/javascript"></script>
	<script src="../../js/libs/sweetlink/sweetlink.js" type="text/javascript"></script>
	<script src="../../js/libs/matchheight/matchHeight.js"></script>
	<script src="../../js/libs/slick/slick.js" type="text/javascript"></script>

	<!-- Modules -->
	<script src="../../js/modules/common.js" type="text/javascript"></script>

</body>

</html>
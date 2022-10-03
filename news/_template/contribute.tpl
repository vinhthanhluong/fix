<ONContribute id="$contribute_id"></ONContribute>
<?php
$current_category_id   = $category_id;
$current_category_name = $category_name;
?>
<ONCategory>
	<?php if( $current_category_id==$category_id ) $current_category_url = $category_url; ?>
</ONCategory>

<!Doctype html>
<html lang="ja">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="format-detection" content="telephone=no">
	<title>{=$title=}|{=$current_category_name=}｜京都の外壁塗装・リフォームの「BANBA PAINT」</title>
	<ONIf condition="$keywords_Value">
		<meta name="keywords" content="{=$keywords_Value=}" />
		<ONElse>
			<meta name="keywords" content="亀岡市,福知山市,外壁塗装,リフォーム,新着情報" />
	</ONIf>
	<ONIf condition="$description_Value">
		<meta name="description" content="{=$description_Value=}" />
		<ONElse>
			<meta name="description" content="京都亀岡市・福知山市を中心に外壁塗装・リフォームを行なっている「BANBA　PAINT」のインフォメーションページです。営業時間のお知らせから、現地調査やスタッフミーティングの様子、コラムまで、当社の活動状況やお役立ち情報を詳細にお伝えしております。当社へのご依頼やお問い合わせ、イベントへのご参加を検討される際にはぜひご活用ください。" />
	</ONIf>
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
	<script type="application/ld+json">
    {
        "@context": "http://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{
            "@type": "ListItem",
            "position": 1,
            "item": {
                "@id": "https://www.kabbanba.com/",
                "name": "京都亀岡市の外壁塗装・リフォームなら「BANBA PAINT」｜亀岡市・福知山市・上京・左京"
            }
        }, {
            "@type": "ListItem",
            "position": 2,
            "item": {
                "@id": "https://www.kabbanba.com/news/",
                "name": "新着情報＆コラム一覧｜京都亀岡市・福知山市の外壁塗装「BANBA PAINT」"
            }
        }, {
            "@type": "ListItem",
            "position": 3,
            "item": {
                "@id": "https://www.kabbanba.com/news/{=$url=}/",
                "name": "{=$title=}|{=$current_category_name=}｜京都の外壁塗装・リフォームの「BANBA PAINT」"
            }
        }]
    }
    </script>
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
							<a href="../../faq.html">よくあるご質問・SDGｓについて</a>
						</li>
						<li>
							<a href="../../company.html">会社案内</a>
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
                            <h2><span class="en">news</span>{=$title=}</h2>
                        </div>
                        <p class="img sp">
                            <img src="../../images/udr_img_news_d01.jpg" alt="{=$title=}">
                        </p>
                    </div>
				</div>
			</div>
			<!-- end #top_info -->

			<div id="content">
			 	<div class="ic-bg ibg1"></div>
                <div class="ic-bg ibg2"></div>
                <div class="ic-bg ibg3"></div>
                <div class="ic-bg ibg4"></div>
                <div class="ic-bg ibg5"></div>
                <div class="ic-bg ibg6"></div>
                <div class="ic-bg ibg7"></div>
                <div class="ic-bg ibg8"></div>
                <div class="ic-bg ibg9"></div>
                <div class="ic-bg ibg10"></div>
                <div class="ic-bg ibg11"></div>
				<!-- topic path = breadcrumb -->
				<div id="topic-path">
					<ul class="topic-list">
						<li><a href="https://www.kabbanba.com/">ホーム</a></li>
						<li><a href="../">{=$base_title=}</a></li>
						<li><a href="../{=$current_category_url=}">{=$current_category_name=}</a></li>
						<li>{=$title=}</li>
					</ul>
				</div>
				<!-- end #topic_path -->

				<div class="section">
					<div class="news-detail">
						<h3 class="h3"> {=$title=}</h3>
						<div class="nwd-box">
							<ONIf condition="$img01_Value || $txt01_Value">
								<div class="nwd-item">
									<ONIf condition="$img01_Value">
										<p class="nwd-img">
											<img src="{=$img01_Src=}" alt=" {=$title=}">
										</p>
									</ONIf>

									<ONIf condition="$txt01_Value">
										<div class="nwd-desc">
											{=$txt01_Value=}
										</div>
									</ONIf>
								</div>
							</ONIf>
							<ONIf condition="$img02_Value || $txt02_Value">
								<div class="nwd-item">
									<ONIf condition="$img02_Value">
										<p class="nwd-img">
											<img src="{=$img02_Src=}" alt=" {=$title=}">
										</p>
									</ONIf>

									<ONIf condition="$txt02_Value">
										<div class="nwd-desc">
											{=$txt02_Value=}
										</div>
									</ONIf>
								</div>
							</ONIf>
							<ONIf condition="$img03_Value || $txt03_Value">
								<div class="nwd-item">
									<ONIf condition="$img03_Value">
										<p class="nwd-img">
											<img src="{=$img03_Src=}" alt=" {=$title=}">
										</p>
									</ONIf>

									<ONIf condition="$txt03_Value">
										<div class="nwd-desc">
											{=$txt03_Value=}
										</div>
									</ONIf>
								</div>
							</ONIf>
							<ONIf condition="$img04_Value || $txt04_Value">
								<div class="nwd-item">
									<ONIf condition="$img04_Value">
										<p class="nwd-img">
											<img src="{=$img04_Src=}" alt=" {=$title=}">
										</p>
									</ONIf>

									<ONIf condition="$txt04_Value">
										<div class="nwd-desc">
											{=$txt04_Value=}
										</div>
									</ONIf>
								</div>
							</ONIf>
							<ONIf condition="$img05_Value || $txt05_Value">
								<div class="nwd-item">
									<ONIf condition="$img05_Value">
										<p class="nwd-img">
											<img src="{=$img05_Src=}" alt=" {=$title=}">
										</p>
									</ONIf>

									<ONIf condition="$txt05_Value">
										<div class="nwd-desc">
											{=$txt05_Value=}
										</div>
									</ONIf>
								</div>
							</ONIf>
							<ONIf condition="$img06_Value || $txt06_Value">
								<div class="nwd-item">
									<ONIf condition="$img06_Value">
										<p class="nwd-img">
											<img src="{=$img06_Src=}" alt=" {=$title=}">
										</p>
									</ONIf>

									<ONIf condition="$txt06_Value">
										<div class="nwd-desc">
											{=$txt06_Value=}
										</div>
									</ONIf>
								</div>
							</ONIf>
							<ONIf condition="$img07_Value || $txt07_Value">
								<div class="nwd-item">
									<ONIf condition="$img07_Value">
										<p class="nwd-img">
											<img src="{=$img07_Src=}" alt=" {=$title=}">
										</p>
									</ONIf>

									<ONIf condition="$txt07_Value">
										<div class="nwd-desc">
											{=$txt07_Value=}
										</div>
									</ONIf>
								</div>
							</ONIf>
							<ONIf condition="$img08_Value || $txt08_Value">
								<div class="nwd-item">
									<ONIf condition="$img08_Value">
										<p class="nwd-img">
											<img src="{=$img08_Src=}" alt=" {=$title=}">
										</p>
									</ONIf>

									<ONIf condition="$txt08_Value">
										<div class="nwd-desc">
											{=$txt08_Value=}
										</div>
									</ONIf>
								</div>
							</ONIf>
							<ONIf condition="$img09_Value || $txt09_Value">
								<div class="nwd-item">
									<ONIf condition="$img09_Value">
										<p class="nwd-img">
											<img src="{=$img09_Src=}" alt=" {=$title=}">
										</p>
									</ONIf>

									<ONIf condition="$txt09_Value">
										<div class="nwd-desc">
											{=$txt09_Value=}
										</div>
									</ONIf>
								</div>
							</ONIf>
							<ONIf condition="$img10_Value || $txt10_Value">
								<div class="nwd-item">
									<ONIf condition="$img10_Value">
										<p class="nwd-img">
											<img src="{=$img10_Src=}" alt=" {=$title=}">
										</p>
									</ONIf>

									<ONIf condition="$txt10_Value">
										<div class="nwd-desc">
											{=$txt10_Value=}
										</div>
									</ONIf>
								</div>
							</ONIf>
						</div>
					</div>
				</div>

				<div class="section">
					<div class="btn_prev_next_sec clearfix">
						<?php $current_url = $url; ?>
						<ONContributeSearch category="$current_category_id">
							<ONContributeFetch>
								<?php $pages[] = $url; ?>
							</ONContributeFetch>
						</ONContributeSearch>
						<?php $current_page = array_search($current_url,$pages); ?>
						<ul class="btn_prev_next">
							<?php if($prev = @$pages[$current_page+1]): ?>
							<li class="prevPage"><a href="../<?php echo $prev ?>">&#8592; 前の記事へ</a></li>
							<?php endif; ?>
							<li class="centerPage"><a href="../{=$current_category_url=}/">一覧に戻る</a></li>
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
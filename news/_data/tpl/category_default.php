<?php

	$setting=unserialize(@file_get_contents(DATA_DIR.'/setting/overnotes.dat'));
	ini_set('mbstring.http_input', 'pass');
	parse_str($_SERVER['QUERY_STRING'],$_GET);
	$keyword=isset($_GET['k'])?trim($_GET['k']):'';
	$category=isset($_GET['c'])?trim($_GET['c']):'';
	$page=isset($_GET['p'])?trim($_GET['p']):'';
	$base_title = !empty($setting['title'])? $setting['title'] : 'OverNotes';

?><!Doctype html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="format-detection" content="telephone=no">
    <title><?php echo $current_category_name; ?>｜京都亀岡市・福知山市の外壁塗装「BANBA PAINT」</title>
    <meta name="keywords" content="亀岡市,福知山市,外壁塗装,新着情報,イベント" />
    <meta name="description" content="京都の外壁塗装会社「BANBA PAINT」から皆さまへのお知らせや新着情報のご案内です。イベント情報から地域清掃といった日々の活動報告、現場の調査日報、施工コラムなど、これから塗装・リフォームをお考えの方に役立つ情報が満載です。亀岡市、福知山市、上京・左京エリアを中心に、京都で外壁塗装をご検討なら、ぜひ「BANBA PAINT」へ！" />
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
        <header id="header" class="--fix">
            <div class="header-wrapper">
                <h1>京都府亀岡市の外壁塗装会社「BANBA　PAINT」の新着情報やお役立ちコラム一覧です。</h1>
                <div class="header-main">
                    <div class="logo">
                        <a href="https://www.kabbanba.com/">
                            <img src="../../images/logo.png" width="544" height="143" alt="BANBA PAINT">
                        </a>
                    </div>
                    <div class="header-act">
                        <div class="header-info">
                            <div class="header-ih">
                                <p class="ih-tt">亀岡市・京都市で3冠達成！</p>
                                <p class="ih-img">
                                    <img src="../../images/header-img01.jpg" alt="亀岡市・京都市で3冠達成！">
                                </p>
                            </div>
                            <a href="#" class="header-ln">
                                <img src="../../images/header-img02.jpg" alt="亀岡市・京都市で3冠達成！">
                            </a>
                            <div class="header-phone">
                                <a href="tel:0771246977" onclick="gtag('event', 'tel', {'event_category': 'sp'});" class="phone-lk sweetlink">
                                    0771-24-6977
                                </a>
                                <p class="phone-text">
                                    【受付】9：00～18：00　【定休】日曜日
                                </p>
                                <p class="phone-text">
                                    <span>▲繋がらない場合は、ぜひLINEから</span>
                                    <!-- &#128073; -->
                                </p>
                            </div>
                            <div class="header-social">
                                <a href="#" target="_blank" class="social-lk">
                                    <img src="../../images/ic-line.png" alt="line">
                                </a>
                                <a href="https://instagram.com/stories/banbapaint_bpgram/2925461814060583948?igshid=YmMyMTA2M2Y=" target="_blank" class="social-lk">
                                    <img src="../../images/ic-ins.png" alt="instagram">
                                </a>
                            </div>
                        </div>
                        <div class="header-btn hdbtn-sp">
                            <a href="../../contact?mode=tab2" class="hd-btn">
                                <span class="hd-w">
                                    <span class="hbn-c">無料</span>
                                    <span class="hbn-tt">資料請求</span>
                                </span>
                            </a>
                            <a href="../../contact?mode=tab1" class="hd-btn">
                                <span class="hd-w">
                                    <span class="hbn-c">無料</span>
                                    <span class="hbn-tt">お見積もり</span>
                                </span>
                            </a>
                            <a href="../../contact?mode=tab1" class="hd-btn">
                                <span class="hd-w">
                                    <span class="hbn-c">無料</span>
                                    <span class="hbn-tt">お問い合わせ</span>
                                </span>
                            </a>
                        </div>
                        <div class="hamburger-btn">
                            <div class="bar"></div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <div class="btn-more pc">
            <a href="../../contact?mode=tab1">
                オンライン外壁診断
            </a>
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
            <div class="header-menu idx-menu --fixed">
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
                        <span href="../../#">
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
                        <span href="../../#">
                            実績について
                            <span class="m-arrow"></span>
                        </span>
                        <ul class="sub-menu">
                            <li>
                                <a href="../../works/">施工事例</a>
                            </li>
                            <li>
                                <a href="../../voice.html">お客様の喜びの声</a>
                            </li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <span href="../../#">
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
                        <span href="../../#">
                            インフォメーション
                            <span class="m-arrow"></span>
                        </span>
                        <ul class="sub-menu">
                            <li>
                                <a href="../../news/cate_1/">新着情報</a>
                            </li>
                            <li>
                                <a href="../../news/cate_2/">調査日報</a>
                            </li>
                            <li>
                                <a href="../../news/cate_4/">コラム</a>
                            </li>
                            <li>
                                <a href="../../news/cate_3/">イベント情報</a>
                            </li>
                        </ul>
                    </li>
                </ul>
                <p class="close-btn sp"><span>× CLOSE</span></p>
            </div>


            <!-- top info = main visual -->
            <div id="mainvisual" class="under-visual udr-news">
                <div class="container">
                    <div class="udr_fx_h2">
                        <div class="udr_box_h2">
                            <h2><span class="en">news</span><?php echo $current_category_name; ?></h2>
                        </div>
                        <p class="img sp">
                            <img src="../../images/udr_img_news01.jpg" alt="<?php echo $current_category_name; ?>">
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
                        <li><?php echo $current_category_name; ?></li>
                    </ul>
                </div>
                <!-- end #topic_path -->
                <div class="section">
                    <h3 class="h3">BANBA PAINTのイベント情報一覧</h3>
                    <p>京都・亀岡市、福知山市の外壁塗装会社「BANBA PAINT」のイベント情報を掲載しております。当社の新着情報や、地域清掃などの活動情報、ご依頼現場の調査日報や、外壁塗装やリフォームに関するお役立ちコラムも掲載しておりますので、ぜひご覧ください。</p>
                </div>
                <div class="section">
                    <div class="news">
                        <div class="news-wrapper">
                            <ul class="news-catalog">
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
                                    <li class="<?php if($current_category_id == $category_id) echo 'active'; ?>">
                                        <a href="../<?php echo $category_url; ?>" class="news-cata">
                                            <span><?php echo $category_name; ?></span>
                                        </a>
                                    </li>
                                <?php
	}
?>
                            </ul>
                            <?php $limitNum = 10 ?>
                            <?php
	$contribute_index=contribute_search(
		@$current_category_id
		,''
		,''
		,''
		,''
		,''
	);
	$max_record_count=count($contribute_index);

	$current_page=(@$_GET['p'])?(@$_GET['p']):1;
	$contribute_index=array_slice($contribute_index,($current_page-1)*$limitNum,$limitNum);
	$record_count=count($contribute_index)

?>
                                <div class="news-box">
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
                                        <div class="news-item">
                                            <?php
												$dates = explode("/", $date);
											?>
                                            <p class="news-date">
                                                <?php echo $dates[0]; ?>.<?php echo $dates[1]; ?>.<?php echo $dates[2]; ?>
                                            </p>
                                            <p class="news-cate ncate<?php echo $category_id; ?>">
                                                <span><?php echo $category_name; ?></span>
                                            </p>
                                            <p class="news-tt">
                                                <?php echo $title; ?>
                                                <!-- <?php echo mb_strimwidth($title, 0, 45, '…', 'UTF-8'); ?> -->
                                            </p>
                                            <a href="../<?php echo $url; ?>" class="lk-full"></a>
                                            <!-- <p class="img">
												<?php
	if($img1_Value){
?> <img src="<?php echo $img1_Src; ?>"
														alt="<?php echo $title; ?>">
													<?php
	}else{
?>
														<img src="../images/under_img01.jpg" alt="<?php echo $title; ?>">
												<?php
	}
?>
											</p>

											
											<div class="blog_list_news_ttl">
												<p class="cate cate<?php echo $category_id; ?>"><?php echo $category_name; ?></p>
												<p class="date"></p>
											</div>
											<p class="ttl"><?php echo mb_strimwidth($title, 0, 45, '…', 'UTF-8'); ?></p>
											<a href="<?php echo $url; ?>"></a> -->
                                        </div>
                                    <?php
		foreach($field as $field_index=>$field_data){
			unset(${$field_data['code'].'_Name'});
			unset(${$field_data['code'].'_Value'});
			unset(${$field_data['code'].'_Src'});
		}
	}
?>
                                </div>
                                <?php
	$page_count=(int)ceil($max_record_count/(float)$limitNum);
?>
                                    <?php
	if($max_record_count > $limitNum){
?>
                                        <ul class="pagination">
                                            <?php
	if($current_page <= 1){
?>
                                                <li class="disabled"><a href="#">&lt;&lt;</a></li>
                                                <?php
	}else{
?>
                                                    <li><a href="./?p=<?php echo $current_page-1; ?>">&lt;&lt;</a></li>
                                            <?php
	}
?>
                                            <?php
	$page_old=@$page;
	for($page=1;$page<=$page_count;$page++){
?>
                                                <?php
	if($current_page == $page){
?>
                                                    <li class="active"><a href="#"><?php echo $page; ?></a></li>
                                                    <?php
	}else{
?>
                                                        <li><a href="./?p=<?php echo $page; ?>"><?php echo $page; ?></a></li>
                                                <?php
	}
?>
                                            <?php
	}
$page=$page_old;
?>
                                            <?php
	if($current_page*$limitNum<$max_record_count){
?>
                                                <li><a href="./?p=<?php echo $current_page+1; ?>">&gt;&gt;</a></li>
                                                <?php
	}else{
?>
                                                    <li class="disabled"><a href="#">&gt;&gt;</a></li>
                                            <?php
	}
?>
                                        </ul>
                                    <?php
	}
?>
                                
                            
                        </div>
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
                            <!-- <p class="ft-banner">
                                <img src="../../images/ft-img01.jpg" alt="姉妹サイトバナー  ">
                            </p> -->
                        </div>
                        <div class="ft-map">
                            <div class="fmap">
                                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3268.027704567475!2d135.59031629999998!3d35.0060116!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6000555d31e30689%3A0xbf73462894efa70b!2zKOagqilCQU5CQSBQQUlOVC_jg5Djg7Pjg5Djg5rjgqTjg7Pjg4g!5e0!3m2!1sja!2s!4v1663763539983!5m2!1sja!2s" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
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
                                        <!-- <li>
                                            <a href="../../company.html">
                                                会社案内・ショールーム紹介
                                            </a>
                                        </li> -->
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
                                            <a href="../../news/cate_1">新着情報</a>
                                        </li>
                                        <li>
                                            <a href="../../news/cate_2">調査日報</a>
                                        </li>
                                        <li>
                                            <a href="../../news/cate_4">コラム</a>
                                        </li>
                                        <li>
                                            <a href="../../news/cate_3">イベント情報</a>
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
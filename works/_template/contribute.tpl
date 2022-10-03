<ONContribute id="$contribute_id"></ONContribute>
<?php
$current_category_id   = $category_id;
$current_category_name = $category_name;
?>
<ONCategory>
    <?php if( $current_category_id==$category_id ) $current_category_url = $category_url; ?>
</ONCategory>
<?xml version='1.0' encoding='UTF-8' ?>
<!Doctype html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="format-detection" content="telephone=no">
    <title>{=$title=}|実績詳細〜写真でみる施工事例〜｜京都の外壁塗装は「BANBA　PAINT」</title>
    <ONIf condition="$keywords_Value">
        <meta name="keywords" content="{=$keywords_Value=}" />
        <ONElse>
            <meta name="keywords" content="亀岡市,福知山市,外壁塗装,施工事例,実績" />
    </ONIf>
    <ONIf condition="$description_Value">
        <meta name="description" content="{=$description_Value=}" />
        <ONElse>
            <meta name="description" content="京都の「BANBA PAINT」の職人たちがこれまでに手掛けてきた施工実績をご確認いただけます。写真つきで詳しくご紹介しておりますので、亀岡市・福知山市・上京・左京エリアで外壁塗装をご検討中の方は、ぜひご参考ください。お客様の思い出がつまった大切な資産をお守りするため、常に誠心誠意施工させていただいております。事例写真には、細部までこだわりのつまったプロの仕事がたくさん収められています。ぜひ、しっかりとご確認ください。" />
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
                "@id": "https://www.kabbanba.com/works/",
                "name": "実績一覧〜施工事例〜｜京都亀岡の外壁塗装「BANBA　PAINT」"
            }
        }, {
            "@type": "ListItem",
            "position": 3,
            "item": {
                "@id": "https://www.kabbanba.com/works/{=$url=}/",
                "name": "{=$title=}|実績詳細〜写真でみる施工事例〜｜京都の外壁塗装は「BANBA　PAINT」"
            }
        }]
    }
    </script>
</head>

<body class="under">
    <div id="wrapper">
        <header id="header" class="--fix">
            <div class="header-wrapper">
                <h1>京都府亀岡市の外壁塗装会社「BANBA　PAINT」の施工事例を、写真つきで詳しくご紹介いたします。</h1>
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
            <div id="mainvisual" class="under-visual udr-works-d">
                <div class="container">
                    <div class="udr_fx_h2">
                        <div class="udr_box_h2">
                            <h2><span class="en">works</span>{=$title=}</h2>
                        </div>
                        <p class="img sp">
                            <img src="../../images/udr_img_works_d01.jpg" alt="{=$title=}">
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
                        <li><a href="../">実績について｜施工事例</a></li>
                        <li>{=$title=}</li>
                    </ul>
                </div>
                <!-- end #topic_path -->
                <div class="section">
                    <div class="under-bx">
                        <h3 class="h3">{=$title=}</h3>
                        <p>
                            京都亀岡市、福知山市の外壁塗装会社「BANBA PAINT」の施工事例です。施工前・施工後の状態や、工事中の様子を写真つきでご紹介いたします。
                        </p>
                        <p>
                            お客様の思い出がつまった大切な資産をお守りするため、外壁・内装のプロとして誠心誠意施工させていただきました。細部までこだわりのつまったプロの仕事を、ぜひご覧ください。
                        </p>
                    </div>
                </div>
                <div class="section">
                    <div class="works works-detail">
                        <ONIf condition="$img01_Value || $img02_Value">
                            <div class="wkd-box">
                                <ONIf condition="$img01_Value">
                                    <div class="wkd-item">
                                        <p class="wkd-tt">
                                            before
                                        </p>
                                        <p class="wkd-img">
                                            <img src="{=$img01_Src=}" alt="before">
                                        </p>
                                    </div>
                                </ONIf>
                                <ONIf condition="$img01_Value && $img02_Value">
                                    <div class="wkd-arrow">
                                        <span class="w-ar"></span>
                                    </div>
                                </ONIf>
                                <ONIf condition="$img02_Value">
                                    <div class="wkd-item">
                                        <p class="wkd-tt">
                                            after
                                        </p>
                                        <p class="wkd-img">
                                            <img src="{=$img02_Src=}" alt="after">
                                        </p>
                                    </div>
                                </ONIf>
                            </div>
                        </ONIf>
                        <ONIf condition="$td01_Value || td02_Value || td03_Value || td04_Value || td05_Value || td06_Value || td07_Value || td08_Value || td09_Value || td10_Value">
                            <table class="works-tbl table-black">
                                <tbody>
                                    <tr>
                                        <th class="w25">価格</th>
                                        <td class="w25 wk-price">{=$td01_Value=}</td>
                                        <th class="w25">地域</th>
                                        <td class="w25">{=$td02_Value=}</td>
                                    </tr>
                                    <tr>
                                        <th>坪数</th>
                                        <td>{=$td03_Value=}</td>
                                        <th>使用塗料</th>
                                        <td>{=$td04_Value=}</td>
                                    </tr>
                                    <tr>
                                        <th>お客様名</th>
                                        <td>{=$td05_Value=}</td>
                                        <th>工期</th>
                                        <td>{=$td06_Value=}</td>
                                    </tr>
                                    <tr>
                                        <th>塗装箇所</th>
                                        <td>{=$td07_Value=}</td>
                                        <th>その他工事</th>
                                        <td>{=$td08_Value=}</td>
                                    </tr>
                                    <tr>
                                        <th>築年数</th>
                                        <td>{=$td09_Value=}</td>
                                        <th>建物区分</th>
                                        <td>{=$td10_Value=}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </ONIf>
                        <ONIf condition="$img01_Value || $img02_Value || $img03_Value || $img04_Value || $img05_Value || $img06_Value || $img07_Value || $img08_Value || $img09_Value || $img10_Value">
                            <div class="wkd-slider">
                                <ul class="wkd-bg">
                                    <ONIf condition="$img02_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img02_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img03_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img03_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img04_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img04_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img05_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img05_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img06_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img06_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img07_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img07_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img08_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img08_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img09_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img09_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img10_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img10_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                </ul>
                                <ul class="wkd-sm">
                                    <ONIf condition="$img02_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img02_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img03_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img03_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img04_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img04_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img05_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img05_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img06_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img06_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img07_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img07_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img08_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img08_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img09_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img09_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                    <ONIf condition="$img10_Value">
                                        <li>
                                            <div class="wkd-sld">
                                                <img src="{=$img10_Src=}" alt="{=$title=}">
                                            </div>
                                        </li>
                                    </ONIf>
                                </ul>
                            </div>
                        </ONIf>
                        <ONIf condition="$ttl01_Value || $txt01_Value">
                            <div class="wkd-comment">
                                <ONIf condition="$ttl01_Value">
                                    <div class="udr_fx_point">
                                        <p class="udr_ttl_point">
                                            <span class="ico">
                                                <img src="../../images/udr_ico_point.png" alt="{=$ttl01_Value=}">
                                            </span>
                                            <span class="ttl">{=$ttl01_Value=}</span>
                                            <span class="sub">comment 1</span>
                                        </p>
                                    </div>
                                </ONIf>
                                <ONIf condition="$txt01_Value">
                                    <div class="wkd-desc">
                                        {=mb_strimwidth($txt01_Value, 0, 0, '…', 'UTF-8')=}
                                    </div>
                                </ONIf>
                            </div>
                        </ONIf>
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
                            <li class="centerPage"><a href="../">一覧に戻る</a></li>
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
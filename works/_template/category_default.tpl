<?xml version='1.0' encoding='UTF-8' ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>{=$current_category_name=}{=$base_title=}</title>
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<link  href="../_sys/css/sample.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="../_sys/js/jquery-1.8.2.min.js"></script>

</head>
<body id="inner" class="sub">
  <div id="wrapper">
		<div id="header">
				<h1>{=$base_title=}</h1>
				<p class="logo"><a href="../">{=$base_title=}</a></p>
		</div>
		
		<div id="gnav">
				<ul class="clearfix">
					<li><a href="../">Home</a></li>
					<li><a href="../search.php">検索</a></li>
				</ul>
		</div>
		
		<div id="main">
<?php
/**
 * OverNotes Loop Start -------------------------------->
 * 全体の変数設定
 */

//インデックス
$i   = 0;

//カラム数
$col = 2;

//表示件数　ページャーにも使われる
$limitNum=10;

//行のクラス
$row_class = 'row';

//列のクラス
$col_class = 'col';

?>
<?php /* --- ループクエリ --- */ ?>
<ONContributeSearch page="@$_GET['p']" limit="$limitNum" category="@$current_category_id">
	<?php /* ループ開始行 */ ?>
	<div class="{=$row_class=}">
	<?php /* ループ */ ?>
	<ONContributeFetch>
		<?php
		/* $urlのパッチ */
		$url = $current_category_id ? "../$url" : "./$url";
		?>
		<?php /* 行の挿入 */ ?>
		<ONIf condition="$i && $i % $col == 0">
	</div>
	<div class="{=$row_class=}">
		</ONIf>
		
		<div class="{=$col_class=}">
			…
			<a href="{=$url=}">リンク</a>
			…
		</div>
		<?php $i++ ?>
	</ONContributeFetch>
	</div>
</ONContributeSearch>

<?php /* --- ページャー --- */ ?>
<ONPagenation record_count="$max_record_count" limit="$limitNum">
	<?php /* ページャー表示条件：デフォルトでは全体件数が表示件数より上 */ ?>
	<ONIf condition="$max_record_count > $limitNum">
		<div class="pager">
			<p class="center">
				<ONIf condition="$current_page <= 1">
					<span class="nopage">&lt;&lt;</span>
				<ONElse>
					<a href="./?p={=$current_page-1=}">&lt;&lt;</a>
				</ONIf>
				
				<ONPagenationFetch>
					<ONIf condition="$current_page == $page">
						{=$page=}
					<ONElse>
						<a href="./?p={=$page=}">{=$page=}</a>
					</ONIf>
				</ONPagenationFetch>
				
				<ONIf condition="$current_page*$limitNum<$max_record_count">
					<a href="./?p={=$current_page+1=}">&gt;&gt;</a>
				<ONElse>
					<span class="nopage">&gt;&gt;</span>
				</ONIf>
			</p>
		</div>
	</ONIf>
</ONPagenation>

<?php
/**
 * <------------------------ OverNotes Loop End
 */
?>
			</div>
		</div>
	</div>
  <div id="footer">
    Copyright(c) 2012 FREESALE INC. All Right Reserved.
  </div>
</body>
</html>
<?php

	$setting=unserialize(@file_get_contents(DATA_DIR.'/setting/overnotes.dat'));
	ini_set('mbstring.http_input', 'pass');
	parse_str($_SERVER['QUERY_STRING'],$_GET);
	$keyword=isset($_GET['k'])?trim($_GET['k']):'';
	$category=isset($_GET['c'])?trim($_GET['c']):'';
	$page=isset($_GET['p'])?trim($_GET['p']):'';
	$base_title = !empty($setting['title'])? $setting['title'] : 'OverNotes';

?><?php echo "<?xml version='1.0' encoding='UTF-8' ?>\n" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title><?php echo $current_category_name; ?><?php echo $base_title; ?></title>
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<link  href="../_sys/css/sample.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="../_sys/js/jquery-1.8.2.min.js"></script>

</head>
<body id="inner" class="sub">
  <div id="wrapper">
		<div id="header">
				<h1><?php echo $base_title; ?></h1>
				<p class="logo"><a href="../"><?php echo $base_title; ?></a></p>
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
	<?php /* ループ開始行 */ ?>
	<div class="<?php echo $row_class; ?>">
	<?php /* ループ */ ?>
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
		<?php
		/* $urlのパッチ */
		$url = $current_category_id ? "../$url" : "./$url";
		?>
		<?php /* 行の挿入 */ ?>
		<?php
	if($i && $i % $col == 0){
?>
	</div>
	<div class="<?php echo $row_class; ?>">
		<?php
	}
?>
		
		<div class="<?php echo $col_class; ?>">
			…
			<a href="<?php echo $url; ?>">リンク</a>
			…
		</div>
		<?php $i++ ?>
	<?php
		foreach($field as $field_index=>$field_data){
			unset(${$field_data['code'].'_Name'});
			unset(${$field_data['code'].'_Value'});
			unset(${$field_data['code'].'_Src'});
		}
	}
?>
	</div>


<?php /* --- ページャー --- */ ?>
<?php
	$page_count=(int)ceil($max_record_count/(float)$limitNum);
?>
	<?php /* ページャー表示条件：デフォルトでは全体件数が表示件数より上 */ ?>
	<?php
	if($max_record_count > $limitNum){
?>
		<div class="pager">
			<p class="center">
				<?php
	if($current_page <= 1){
?>
					<span class="nopage">&lt;&lt;</span>
				<?php
	}else{
?>
					<a href="./?p=<?php echo $current_page-1; ?>">&lt;&lt;</a>
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
						<?php echo $page; ?>
					<?php
	}else{
?>
						<a href="./?p=<?php echo $page; ?>"><?php echo $page; ?></a>
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
					<a href="./?p=<?php echo $current_page+1; ?>">&gt;&gt;</a>
				<?php
	}else{
?>
					<span class="nopage">&gt;&gt;</span>
				<?php
	}
?>
			</p>
		</div>
	<?php
	}
?>


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
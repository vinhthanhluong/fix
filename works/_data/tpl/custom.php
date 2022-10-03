<?php

	$setting=unserialize(@file_get_contents(DATA_DIR.'/setting/overnotes.dat'));
	ini_set('mbstring.http_input', 'pass');
	parse_str($_SERVER['QUERY_STRING'],$_GET);
	$keyword=isset($_GET['k'])?trim($_GET['k']):'';
	$category=isset($_GET['c'])?trim($_GET['c']):'';
	$page=isset($_GET['p'])?trim($_GET['p']):'';
	$base_title = !empty($setting['title'])? $setting['title'] : 'OverNotes';

?><?php $limit = (!empty($_GET['limit']))? $_GET['limit']: 20; ?>
<?php
$data = array();
?>
<?php
	$contribute_index=contribute_search(
		@$_GET['cat']
		,''
		,''
		,@$_GET['order']
		,@$_GET['sort']
		,''
	);
	$max_record_count=count($contribute_index);

	$current_page=(@$_GET['p'])?(@$_GET['p']):1;
	$contribute_index=array_slice($contribute_index,($current_page-1)*@$limit,@$limit);
	$record_count=count($contribute_index)

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
<?php
$rec = array(
	"id"    => $id,
	"title" => $title,
	"url"   => $url,
	"date"  => $date,
	"category_id"   => $category_id,
	"category_name" => $category_name,
);
?>
<?php
	foreach($field as $field_index=>$field_data){
		$ONFieldName=$field_data['name'];
		if(@strlen(@$contribute['data'][$field_id][$field_index]) || @is_array(@$contribute['data'][$field_id][$field_index])){
			$ONFieldValue=make_value(
				$field_data['name']
				,@$contribute['data'][$field_id][$field_index]
				,$field_data['type']
				,$id
				,$field_id
				,$field_index
			);
			if($field_data['type']=='image'){
				$ONFieldSrc=ROOT_URI.'/_data/contribute/images/'.@$contribute['data'][$field_id][$field_index];
			}else{
				$ONFieldSrc='';
			}
		}else{
			$ONFieldValue='';
			$ONFieldSrc='';
		}

?>
<?php
$rec[ $field_data['code'] ] = $ONFieldValue;
?>
<?php
	}
?>
<?php
$data[] = $rec;
?>
<?php
		foreach($field as $field_index=>$field_data){
			unset(${$field_data['code'].'_Name'});
			unset(${$field_data['code'].'_Value'});
			unset(${$field_data['code'].'_Src'});
		}
	}
?>

<?php echo !empty( $_GET['callback'] ) ? htmlspecialchars($_GET['callback']) : 'callback' ?>(<?php echo json_encode(compact('data')) ?>);
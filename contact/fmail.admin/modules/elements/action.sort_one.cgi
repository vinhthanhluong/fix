###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################
# sort
for($cnt=0;$cnt<@current_data;$cnt++){
	@record = split(/\t/,$current_data[$cnt]);
	if($record[0] eq $form{'id'}){
		# ����UP�EDOWN�̔���
		if($form{'rank'} eq 'up'){
			# �O���R�[�h�����݂��邩�̃`�F�b�N
			if(@record_before){
				# ����UP---------------------------------------
				# �����R�[�h�̈ڂ��ς�
				$record_before[1] = $record[1];
				# �O���R�[�h���������ޏ���
				for($record_before_cnt=0; $record_before_cnt<@record_before; $record_before_cnt++){
					$current_data_remake_work .= "$record_before[$record_before_cnt]\t";
				}
				# ���ʏ���������̃��R�[�h�����݃f�[�^�̐���
				$current_data_remake .= "$current_data_remake_work\n";
				# �����p�ϐ��̏�����
				$current_data_remake_work = "";
				
				# �����R�[�h������������
				for($record_cnt=0; $record_cnt<@record;$record_cnt++){
					if($record_cnt == 1){
						# �����R�[�h�ɑO���R�[�h�̏��ʂ���
						$record_work .= "$num_before\t";
					}else{
						$record_work .= "$record[$record_cnt]\t";
					}
				}
				
				# ���ʏ���������̃��R�[�h�����݃f�[�^�̐���
				@record_before = split(/\t/,$record_work);
				# �����p�ϐ��̏�����
				$record_work = "";
				
				# ���ʃf�[�^�̂ݕʓr�i�[
				$num_before = $record_before[1];
			}else{
				# �O���R�[�h�����݂��Ȃ��i�܂�1���R�[�h�ځj�ꍇ�A���ʓ���ւ������̓X���[
				$current_data_remake .= $current_data[$cnt];
				# ���ʃR���g���[���ׁ̈A�����R�[�h�l�̕ێ�
				@record_before = @record;
				# ���ʃf�[�^�̂ݕʓr�i�[
				$num_before = $record[1];
			}
		}else{
			# ����DOWN-------------------------------------
			$flag_num_after = 1;
		}
		$record[1] = sprintf("%04d",$record[1]);
		
		# ���ʂ�������ꍇ�A�����R�[�h�Ɍ����R�[�h�������z��
		if($flag_num_after){
			# �O���R�[�h���������ݏ���
			for($record_before_cnt=0; $record_before_cnt<@record_before; $record_before_cnt++){
				$current_data_remake_work .= "$record_before[$record_before_cnt]\t";
			}
			# �O���R�[�h������
			$current_data_remake .= "$current_data_remake_work\n";
			# �ꎞ�ϐ��̏�����
			$current_data_remake_work = "";
			
			# �ۗ����R�[�h
			@record_before = split(/\t/,$current_data[$cnt]);
			# �\�[�g�ԍ���ی�i��ꃌ�R�[�h�̏ꍇ�A�O��f�[�^���Ȃ��̂ł����đ���j
			$num_before = $record[1];
		}
	}elsif($flag_num_after){
		# id�����v���Ȃ����A���ʂ�������Ώۃ��R�[�h�͂����ŏ�������
		# �O���R�[�h�̃\�[�g�ԍ��Ɍ����R�[�h�̃\�[�g�ԍ���}��
		$record_before[1] = $record[1];
		# �O���R�[�h���������ݏ���
		for($record_before_cnt=0; $record_before_cnt<@record_before; $record_before_cnt++){
			$record_before_work .= "$record_before[$record_before_cnt]\t";
		}
		# �O���R�[�h������
		$current_data_remake .= "$record_before_work\n";
		# �O���R�[�h�����p�ϐ�������
		$record_before_work = "";
		
		# �����R�[�h�̃\�[�g�ԍ��ɁA�O���R�[�h�̃\�[�g�ԍ��𔽉f
		$record[1] = $num_before;
		# �����R�[�h�̏�������
		for($cnt_record=0; $cnt_record<@record; $cnt_record++){
			$record_remake .= "$record[$cnt_record]\t";
		}
		@record_before = split(/\t/,$record_remake);
		
		# ���������Ȃ̂ŁA�t���O��������
		$flag_num_after = 0;
	}else{
		# ����h�c�ƈႤ�ꍇ-----------------------------
		# �O���R�[�h�����݂��邩�̃`�F�b�N
		if(@record_before){
			# �O���R�[�h�����݂���ꍇ�́A�O���R�[�h���������ޏ���
			for($record_before_cnt=0; $record_before_cnt<@record_before; $record_before_cnt++){
				$current_data_remake_work .= "$record_before[$record_before_cnt]\t";
			}
			# ���R�[�h�����݃f�[�^�̐���
			$current_data_remake .= "$current_data_remake_work\n";
			# �����p�ϐ��̏�����
			$current_data_remake_work = "";
		}
		
		# ���ʃR���g���[���ׁ̈A�����R�[�h�l�̕ێ�
		@record_before = @record;
		# ���ʃf�[�^�̂ݕʓr�i�[
		$num_before = $record[1];
	}
}

# �ŏI���R�[�h�����ݏ���
for($record_before_cnt=0; $record_before_cnt<@record_before; $record_before_cnt++){
	$record_before_work .= "$record_before[$record_before_cnt]\t";
}
# �ŏI���R�[�h������
$current_data_remake .= "$record_before_work\n";

@current_data = split(/\n/,$current_data_remake);
@current_data = sort { (split(/\t/,$b))[1] cmp (split(/\t/,$a))[1]} @current_data;
&savefile($current_data_path,@current_data);

$redirect = "?m=$form{'m'}";

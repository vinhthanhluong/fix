###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$current_data_path = "${dir_datas}modules/$form{'m'}/$form{'m'}\.dat";
@current_data = &loadfile($current_data_path);
@db_fields = ('size_1_w','size_1_h','size_2_w','size_2_h','size_3_w','size_3_h','size_4_w','size_4_h','size_5_w','size_5_h','size_6_w','size_6_h','size_7_w','size_7_h','size_8_w','size_8_h','size_9_w','size_9_h','size_10_w','size_10_h');

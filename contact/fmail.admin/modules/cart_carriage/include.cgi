###############################################################################
# Administrated Screen Users Editable Functions
###############################################################################

$current_data_path = "${dir_datas}modules/$form{'m'}/$form{'m'}\.dat";
@current_data = &loadfile($current_data_path);
@db_fields = ('carriage_place','carriage_price','flag_free','carriage_limit');

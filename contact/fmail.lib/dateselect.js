<!--
	// 年エレメントに表示する年数
	var dateselect_year_max = 5;
	
	// ○年からスタートさせる　※○年前から表示させると組み合わせるとバグるから注意
	// 未使用時は、「false」をセット。その場合は、本日日付からスタートします。
	//var year_start = 1900;
	var year_start = false;
	
	// ○年前から表示させる
	var dateselect_year_ajust = 0;
	
	// 初期状態で今日の日付を表示させる true or false
	var dateselect_today_default = true;
	
	//elements names
	var dateselect_yearElementsId = "en1242149347";
	var dateselect_monthElementsId = "en1242149316";
	var dateselect_dayElementsId = "en1242149357";
	var dateselect_calendars = new Array(0,31,28,31,30,31,30,31,31,30,31,30,31);
	var dateselect_monthName = new Array('1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月');
	var dateselect_weeksName = new Array('(日)','(月)','(火)','(水)','(木)','(金)','(土)');
	
	function dateselect_getWeek(year,month,day){
		year = parseInt(year);
		month = parseInt(month);
		day = parseInt(day);
		if(month == 1 || month == 2) {
			year--;
			month += 12;
		}
		week = Math.floor(year + Math.floor(year/4) - Math.floor(year/100) + Math.floor(year/400) + Math.floor((13 * month + 8) / 5) + day) % 7;
		return week;
	}
	function dateselect_bissextile(year,month){
		var dateselect_calendars = new Array(0,31,28,31,30,31,30,31,31,30,31,30,31);
		var cal_flag = 0;
		if(year % 100 == 0 || year % 4 != 0){
			if(year % 400 != 0){
				cal_flag = 0;
			}
			else{
				cal_flag = 1;
			}
		}
		else if(year % 4 == 0){
			cal_flag = 1;
		}
		else{
			cal_flag = 0;
		}
		dateselect_calendars[2] += cal_flag;
		return dateselect_calendars[month];
	}
	function dateselect_change(formId,yearEle,monthEle,dayEle){
		dateselect_yearElementsId = yearEle;
		dateselect_monthElementsId = monthEle;
		dateselect_dayElementsId = dayEle;
		yearObj = document.forms[formId].elements[dateselect_yearElementsId];
		monthObj = document.forms[formId].elements[dateselect_monthElementsId];
		dayObj = document.forms[formId].elements[dateselect_dayElementsId];
		var dateselect_year = yearObj.value;
		var dateselect_month = monthObj.value;
		var dateselect_day = dayObj.value;
		if(yearObj.value != ""){
			//day
			dateselect_week = dateselect_getWeek(dateselect_year,dateselect_month,1);
			dayObj.length = dateselect_bissextile(dateselect_year,dateselect_month);
			for(i=1;i<dayObj.length + 1;i++){
				var print_day = i;
				if(print_day < 10){
					print_day = "0" + i;
				}
				if(dateselect_week == 0){
					dayObj.options[i-1].style.backgroundColor = "#FFEEEE";
					dayObj.options[i-1].style.color = "#CC0000";
				}
				else if(dateselect_week == 6){
					dayObj.options[i-1].style.backgroundColor = "#EEEEFF";
					dayObj.options[i-1].style.color = "#0000CC";
				}
				else {
					dayObj.options[i-1].style.backgroundColor = "#FFFFFF";
					dayObj.options[i-1].style.color = "#000000";
				}
				dayObj.options[i-1].value = parseInt(i);
				dayObj.options[i-1].text = print_day + '日'+dateselect_weeksName[dateselect_week]+'';
				dateselect_week++;
				if(dateselect_week > 6){
					dateselect_week = 0;
				}
			}
		}
		else {
			yearObj.value = "";
			monthObj.value = "";
			dayObj.value = "";
		}
	}
	var dateselect_today = new Date();
	var dateselect_year = dateselect_today.getYear();
	var dateselect_month = dateselect_today.getMonth();
	var dateselect_day = dateselect_today.getDate();
	if (dateselect_year < 1900) dateselect_year += 1900;
	dateselect_year -= dateselect_year_ajust;
	
	//--------------------------------------------------------------
	//プラス日数調整箇所
	//--------------------------------------------------------------
	//足したい日数 MAXで一か月分
	plus = 0;
	
	//土日を営業日として換算しない Yes=1 No=0
	// つまり、1にすると土日は無視します。
	bisionly = 1;
	
	//閏年調査
	//グレゴリウス暦での閏年の決め方 
	//	1.閏年とは
	//		西暦年が4で割り切れる年は閏年（オリンピックのことは書いてない：作者注） 
	//	2.閏年の例外 
	//		上記、1であっても西暦年が100で割り切れる場合は、閏年としない。 
	//	3.閏年の例外の例外 
	//		上記、2であっても西暦年が400で割り切れる場合は、閏年。
	
	uru4 = dateselect_year % 4;
	uru100 = dateselect_year % 100;
	uru400 = dateselect_year % 400;
	flag_uru = 0;
	
	if(uru4 == 0){
		if(uru100 == 0){
			if(uru400 == 0){
				//閏年
				flag_uru = 1;
			}
		}else{
			//閏年
			flag_uru = 1;
		}
	}
	
	//月別日数セット
	if(flag_uru == 1){
		month_day = new Array(31,29,31,30,31,30,31,31,30,31,30,31);
	}else{
		month_day = new Array(31,28,31,30,31,30,31,31,30,31,30,31);
	}
	
	//曜日の算出
	youbi = dateselect_today.getDay();
	//加算日数は当日をカウントしないため1日プラス
	youbi ++;
	if(youbi > 6){
		youbi = 0;
	}
	
	//土日を挟む場合の処理
	//土日は営業日からはずすかどうかのチェック
	if(bisionly == 1){
		
		//dateselect_weekの中身は0～6の繰り返しで、日～土に対応している
		//曜日スカラの値移し替え
		dateselect_week_copy = youbi;
		
		//加算日数分ループ
		for(i=0;plus>i;i++){
			//曜日判定
			if((dateselect_week_copy == 0) || (dateselect_week_copy == 6)){
				//土日にあたるので加算
				plus += 1;
			}
			
			//曜日データの加算
			if(dateselect_week_copy == 6){
				dateselect_week_copy = 0;
			}else{
				dateselect_week_copy ++;
			}
		}
	}
	
	//残日数=(当日付け+加算日数)-月末日
	zan_day = (dateselect_day + plus) - month_day[dateselect_month];
	
	//翌月にずれるので、月を進める
	if(zan_day > 0){
		dateselect_month ++;
		dateselect_day = zan_day;
	}else{
		dateselect_day += plus;
	}
	
	//翌年にずれるので、年を進め、月を調整
	if(dateselect_month > 12){
		dateselect_year ++;
		dateselect_month = 1;
	}
	//--------------------------------------------------------------
	
	
	
	//year
	document.write('<select id="'+dateselect_yearElementsId+'" name="'+dateselect_yearElementsId+'" onchange="dateselect_change(this.form.id,'+"'"+dateselect_yearElementsId+"',"+"'"+dateselect_monthElementsId+"',"+"'"+dateselect_dayElementsId+"'"+')" style="padding: 2px\; font-size: 100%\;">');
	document.write('<option value=""></option>');
	
	//初年度設定---------------------------
	if(year_start != false){
		for(dateselect_year_start=year_start;dateselect_year>dateselect_year_start;dateselect_year_start++){
			var print_year_start = dateselect_year_start;
			document.write('<option value="'+print_year_start+'">'+print_year_start+'年</option>');
		}
	}
	//初年度設定---------------------------
	
	for(i=0;i<dateselect_year_max;i++){
		var print_year = dateselect_year + i;
		document.write('<option value="'+print_year+'">'+print_year+'年</option>');
	}
	document.write('</select>');
	document.getElementById(dateselect_yearElementsId).value = dateselect_year;
	
	//month
	document.write('<select id="'+dateselect_monthElementsId+'" name="'+dateselect_monthElementsId+'" onchange="dateselect_change(this.form.id,'+"'"+dateselect_yearElementsId+"',"+"'"+dateselect_monthElementsId+"',"+"'"+dateselect_dayElementsId+"'"+')" style="padding: 2px\; font-size: 100%\;">');
	document.write('<option value=""></option>');
	for(i=0;i<dateselect_monthName.length;i++){
		var print_month = 1 + i;
		if(i == dateselect_month){
			dateselect_selected = " selected";
		}
		else {
			dateselect_selected = "";
		}
		document.write('<option value="'+print_month+'"'+dateselect_selected+'>'+dateselect_monthName[i]+'</option>');
	}
	document.write('</select>');
	
	//day
	var dateselect_week = dateselect_getWeek(dateselect_year,dateselect_month+1,1);
	document.write('<select id="'+dateselect_dayElementsId+'" name="'+dateselect_dayElementsId+'" onchange="dateselect_change(this.form.id,'+"'"+dateselect_yearElementsId+"',"+"'"+dateselect_monthElementsId+"',"+"'"+dateselect_dayElementsId+"'"+')" style="padding: 2px\; font-size: 100%\;">');
	document.write('<option value=""></option>');
	for(i=1;i<dateselect_bissextile(dateselect_year,dateselect_month+1)+1;i++){
		if(i == dateselect_day){
			dateselect_selected = " selected";
		}
		else {
			dateselect_selected = "";
		}
		if(dateselect_week == 0){
			dateselect_font_style = ' style="color: #CC0000;background-color: #FFEEEE;"';
		}
		else if(dateselect_week == 6){
			dateselect_font_style = ' style="color: #0000CC;background-color: #EEEEFF;"';
		}
		else {
			dateselect_font_style = "";
		}
		var print_day = i;
		if(print_day < 10){
			print_day = "0" + i;
		}
		document.write('<option value="'+i+'"'+dateselect_selected+dateselect_font_style+'>'+print_day+'日'+dateselect_weeksName[dateselect_week]+'</option>');
		dateselect_week++;
		if(dateselect_week > 6){
			dateselect_week = 0;
		}
	}
	document.write('</select>');
	if(dateDefaultValue[dateselect_yearElementsId] != undefined && dateDefaultValue[dateselect_yearElementsId] != "")
		document.getElementById(dateselect_yearElementsId).value = dateDefaultValue[dateselect_yearElementsId];
	else if(dateselect_today_default)
		document.getElementById(dateselect_yearElementsId).value = dateselect_year;
	
	//falseの時は、初期値をヌルにする設定
	else if(!dateselect_today_default)
		document.getElementById(dateselect_yearElementsId).value = '';
	
	if(dateDefaultValue[dateselect_monthElementsId] != undefined && dateDefaultValue[dateselect_monthElementsId] != "")
		document.getElementById(dateselect_monthElementsId).value = dateDefaultValue[dateselect_monthElementsId];
	else if(dateselect_today_default)
		document.getElementById(dateselect_monthElementsId).value = (dateselect_month+1);
	
	//falseの時は、初期値をヌルにする設定
	else if(!dateselect_today_default)
		document.getElementById(dateselect_monthElementsId).value = '';
	
	if(dateDefaultValue[dateselect_dayElementsId] != undefined && dateDefaultValue[dateselect_dayElementsId] != "")
		document.getElementById(dateselect_dayElementsId).value = (dateDefaultValue[dateselect_dayElementsId]-1);
	else if(dateselect_today_default)
		document.getElementById(dateselect_dayElementsId).value = (dateselect_day-1);
	
	//falseの時は、初期値をヌルにする設定
	else if(!dateselect_today_default)
		document.getElementById(dateselect_dayElementsId).value = '';

	dateselect_change("fmail",dateselect_yearElementsId,dateselect_monthElementsId,dateselect_dayElementsId)
//-->
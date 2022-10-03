<!--
	//elements names
	var dateselect_dateElementsId = "en1331812811";
	
	// 表示期間
	var setdays = 100;
	
	// 表示開始日（0は当日、翌日からなら1とする）
	var start_day = 0;
	
	var dateselect_weeksName = new Array('(日)','(月)','(火)','(水)','(木)','(金)','(土)');
	
	
	
	
	
	// 祝日処理 ----------------------------------------------
	// 日付が指定されている祝日
	var DateHoliday = function( month, day ){
		this.month = month;
		this.day = day;
	};
	DateHoliday.prototype = {
		getHoliday:	function(year){
			return this.day;
		}
	};
	
	// ハッピーマンデー
	var MondayHoliday = function( month, week ){
		this.month = month;
		this.week = week;
		this.wday = 1;
	};
	MondayHoliday.prototype = {
		getHoliday: function(year){
			var firstWday = new Date(year,this.month-1,1).getDay();
			return 7*(this.week - ( (firstWday <= this.wday) ? 1 : 0 )) + ( this.wday - firstWday ) + 1; // 第this.week this.wday曜日
		}
	};
	
	// 春分・秋分の日
	var EquinoxHoliday = function( month ){
		this.month = month;
		if( this.month == 3 )
			this.offset = 20.8431;
		else if ( this.month == 9 )
			this.offset = 23.2488;
		else
			throw 'Not exists equinox day in '+month;
	};
	EquinoxHoliday.prototype = {
		getHoliday: function(year){
			return Math.floor(this.offset+0.242194*(year-1980)-Math.floor((year-1980)/4)); // 1980-2099に対応?
		}
	};
	
	var HolidayHelper = {
		holidayMap: {
			1: [new DateHoliday( 1, 1 ), new MondayHoliday( 1, 2 )],
			2: [new DateHoliday( 2, 11 )],
			3: [new EquinoxHoliday( 3 )],
			4: [new DateHoliday( 4, 29 )],
			5: [new DateHoliday( 5, 3 ), new DateHoliday( 5, 4 ), new DateHoliday( 5, 5 )],
			7: [new MondayHoliday( 7, 3 )], 
			9: [new MondayHoliday( 9, 3 ), new EquinoxHoliday( 9 )],
			10: [new MondayHoliday( 10, 2 )],
			11: [new DateHoliday( 11, 3 ), new DateHoliday( 11, 23 )],
			12: [new DateHoliday( 12, 23 )]
		},
		// 月をまたがる振替休日や国民の休日(昨日と翌日が国民の祝日である日)が存在しないことを前提とした処理
		getHolidays: function( year, month ){
			var holidays = this.holidayMap[month];
			if( !holidays )
				return {};
			var dayHash= {}
			var dateArray = []
			for( var i=0, len=holidays.length; i<len; i++ ){
				var day = holidays[i].getHoliday(year);
				dayHash[ day ] = true;
				dateArray.push( new Date(year,month-1,day) );
			}
			
			for( var i=0, len=dateArray.length; i<len; i++ ){
				var date = dateArray[i];
				var day = date.getDate();
				
				if( date.getDay() == 0 ){
					var cday = day+1;
					while( dayHash[cday] )	// 振替休日が祝日の場合、翌日へ
						cday++;
					dayHash[ cday ] = true;
				}
				// 国民の休日判定には、振替休日を考慮しない
				if( dayHash[day+2] && !dayHash[day+1] )
					dayHash[ day+1 ] = true;
			}
			return dayHash;
		},
		isHoliday : function( dateOrYear, month, day ){
			var year = day ? dateOrYear : dateOrYear.getFullYear();
			var month = day ? month : dateOrYear.getMonth()+1;
			var day = day || dateOrYear.getDate();
			
			return !! this.getHolidays( year, month )[ day ];
		}
	};
	
	// 数値から判定
	//aaa = HolidayHelper.isHoliday( 2014,4,29 );
	//祝日ならTrue
	// ------------------------------------------------
	
	
	
	
	
	
	// IE6～8だけ年調整
	if(navigator.userAgent.indexOf("MSIE 8") != -1 || navigator.userAgent.indexOf("MSIE 7") != -1 || navigator.userAgent.indexOf("MSIE 6") != -1){
		var yearplus = 0;
	}else{
		var yearplus = 1900;
	}
	
	
	document.write('<select name="' + dateselect_dateElementsId + '" id="' + dateselect_dateElementsId + '" style="padding: 2px\;">');
	
	for(i=start_day;i<setdays+start_day;i++){
		dateselect_today = new Date();
		dateselect_year = dateselect_today.getYear() + yearplus;
		dateselect_month = dateselect_today.getMonth() + 1;
		dateselect_day = dateselect_today.getDate();
		date = computeDate(dateselect_year, dateselect_month, dateselect_day, i);

		dateselect_year = date.getFullYear();
		dateselect_month = date.getMonth() + 1;
		dateselect_day = date.getDate();
		dateselect_week = dateselect_weeksName[date.getDay()];
		
		
		// 数値から判定
		judge = HolidayHelper.isHoliday( dateselect_year,dateselect_month,dateselect_day );
		
		if(judge) {
			// 祝日
			style = ' style="background: #FFAAAA;"';
			//style = ' style="background: #FFDDDD;" disabled'; // 選択不可能にする
		} else if(date.getDay() == 0){
			// 日曜日
			style = ' style="background: #FFAAAA;"';
			//style = ' style="background: #FFDDDD;" disabled'; // 選択不可能にする
		}else if(date.getDay() == 6){
			// 土曜日
			style = ' style="background: #AAAAFF;"';
			//style = ' style="background: #DDDDDD;" disabled'; // 選択不可能にする
		}else{
			// 平日
			style = '';
		}
		
		document.write('<option value="' + dateselect_year + '年' + dateselect_month + '月' + dateselect_day + '日' + dateselect_week + '"' + style + '>' + dateselect_year + '年' + dateselect_month + '月' + dateselect_day + '日' + dateselect_week + '</option>');
		
	}
	
	document.write('</select>');
	
	
	// 確認画面から戻ってきた時の代入
	if(dateDefaultValue[dateselect_dateElementsId] != undefined && dateDefaultValue[dateselect_dateElementsId] != "")
		document.getElementById(dateselect_dateElementsId).value = dateDefaultValue[dateselect_dateElementsId];
	
	
	
	function computeDate(year, month, day, addDays) {
		var dt = new Date(year, month - 1, day);
		var baseSec = dt.getTime();
		var addSec = addDays * 86400000;//日数 * 1日のミリ秒数
		var targetSec = baseSec + addSec;
		dt.setTime(targetSec);
		return dt;
	}

//-->
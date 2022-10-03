<!--
	// 祝日選択可能 1  /  選択不可能 0
	// この部分のカスタムは、gcalendar-holidays.js 169行目
	var flag_holiday = 1;
	
	// date picker
	$(document).ready(function(){
		// 日曜選択可否
		var SunEnd = 1; // 0なら選択不可能
		
		// 月曜選択可否
		var MonEnd = 1; // 0なら選択不可能
		
		// 火曜選択可否
		var TueEnd = 1; // 0なら選択不可能
		
		// 水曜選択可否
		var WedEnd = 1; // 0なら選択不可能
		
		// 木曜選択可否
		var ThuEnd = 1; // 0なら選択不可能
		
		// 金曜選択可否
		var FriEnd = 1; // 0なら選択不可能
		
		// 土曜選択可否
		var SatEnd = 1; // 0なら選択不可能
		
		// 休日特別指定
		// var holidays = [ '2014-4-30', '', '' ];
		 var holidays = [ '', '', '' ];
		
		// 週指定での判定（1～5の該当週の休日と平日で反転）
		var SunPoint = '0'; // 日曜
		var MonPoint = '0'; // 月曜
		var TuePoint = '0'; // 火曜
		var WedPoint = '0'; // 水曜
		var ThuPoint = '0'; // 木曜
		var FriPoint = '0'; // 金曜
		var SatPoint = '0'; // 土曜
		
		
		$('.datedata input').datepicker({
			showOn: "both", // button  にすると、トリガーがボタンのみになる
			buttonImage: "./images/mfp_calendar.gif",
			buttonImageOnly: false,
			buttonText: 'カレンダー',
			numberOfMonths: 1,
			dateFormat: "yy年m月d日(D)",
			yearRange: "c-5:c+0",
			minDate: 0, // 納期受付開始日
			//maxDate: "+2M +0D" // 納期受付終了日
			//changeMonth: true,
			//changeYear: true,
			//beforeShowDay: $.datepicker.noWeekends
			beforeShowDay: function(date) {
			
			
				// 休日特別指定
				for (var i = 0; i < holidays.length; i++) {
					var htime = Date.parse(holidays[i]);	// 祝日を 'YYYY-MM-DD' から time へ変換
					var holiday = new Date();
					holiday.setTime(htime);				 // 上記 time を Date へ設定
					
					// 祝日
					if (holiday.getYear() == date.getYear() &&
						holiday.getMonth() == date.getMonth() &&
						holiday.getDate() == date.getDate()) {
						return [true, 'special-holiday'];
					}
				}
				
				// 日曜日
				if (date.getDay() == 0) {
					// 第何週か
					judge = date.getDate();
					judge = (judge - 2) / 7;
					judge = Math.floor(judge); // 切り捨て
					judge = judge + 2;
					if( date.getDate() < 2) {
						judge = 1;
					}
					if (SunEnd) {
						if (judge == SunPoint) {
							return [false, 'gcal-sunday'];
						} else {
							return [true, 'gcal-sunday'];
						}
					} else {
						if (judge == SunPoint) {
							return [true, 'gcal-sunday'];
						} else {
							return [false, 'gcal-sunday'];
						}
					}
				}
				// 月曜日
				if (date.getDay() == 1) {
					// 第何週か
					judge = date.getDate();
					judge = (judge - 3) / 7;
					judge = Math.floor(judge); // 切り捨て
					judge = judge + 2;
					if( date.getDate() < 3) {
						judge = 1;
					}
					if (MonEnd) {
						if (judge == MonPoint) {
							return [false, ''];
						} else {
							return [true, ''];
						}
					} else {
						if (judge == MonPoint) {
							return [true, ''];
						} else {
							return [false, ''];
						}
					}
				}
				// 火曜日
				if (date.getDay() == 2) {
					// 第何週か
					judge = date.getDate();
					judge = (judge - 4) / 7;
					judge = Math.floor(judge); // 切り捨て
					judge = judge + 2;
					if( date.getDate() < 4) {
						judge = 1;
					}
					if (TueEnd) {
						if (judge == TuePoint) {
							return [false, ''];
						} else {
							return [true, ''];
						}
					} else {
						if (judge == TuePoint) {
							return [true, ''];
						} else {
							return [false, ''];
						}
					}
				}
				// 水曜日
				if (date.getDay() == 3) {
					// 第何週か
					judge = date.getDate();
					judge = (judge - 5) / 7;
					judge = Math.floor(judge); // 切り捨て
					judge = judge + 2;
					if( date.getDate() < 5) {
						judge = 1;
					}
					if (WedEnd) {
						if (judge == WedPoint) {
							return [false, ''];
						} else {
							return [true, ''];
						}
					} else {
						if (judge == WedPoint) {
							return [true, ''];
						} else {
							return [false, ''];
						}
					}
				}
				// 木曜日
				if (date.getDay() == 4) {
					// 第何週か
					judge = date.getDate();
					judge = (judge - 6) / 7;
					judge = Math.floor(judge); // 切り捨て
					judge = judge + 2;
					if( date.getDate() < 6) {
						judge = 1;
					}
					if (ThuEnd) {
						if (judge == ThuPoint) {
							return [false, ''];
						} else {
							return [true, ''];
						}
					} else {
						if (judge == ThuPoint) {
							return [true, ''];
						} else {
							return [false, ''];
						}
					}
				}
				// 金曜日
				if (date.getDay() == 5) {
					// 第何週か
					judge = date.getDate();
					judge = (judge - 7) / 7;
					judge = Math.floor(judge); // 切り捨て
					judge = judge + 2;
					if( date.getDate() < 7) {
						judge = 1;
					}
					if (FriEnd) {
						if (judge == FriPoint) {
							return [false, ''];
						} else {
							return [true, ''];
						}
					} else {
						if (judge == FriPoint) {
							return [true, ''];
						} else {
							return [false, ''];
						}
					}
				}
				// 土曜日
				if (date.getDay() == 6) {
					// 第何週か
					judge = date.getDate();
					judge = (judge - 1) / 7;
					judge = Math.floor(judge); // 切り捨て
					judge = judge + 1;
					if (SatEnd) {
						if (judge == SatPoint) {
							return [false, 'gcal-saturday'];
						} else {
							return [true, 'gcal-saturday'];
						}
					} else {
						if (judge == SatPoint) {
							return [true, 'gcal-saturday'];
						} else {
							return [false, 'gcal-saturday'];
						}
					}
				}
				// 平日
				return [true, ''];
			},
			onSelect: function(dateText, inst) {
				$("#date_val").val(dateText);
			}
		});
	});
	
//-->
<!--
	//time
	document.write('<li><div id="clock"></div></li>');
	document.write('<li><div id="notice"></div></li>');
	var dates = new Date();
	var current_time = Math.floor(dates.getTime() / 1000);
	function clock(){
		var clock_weeks = new Array("日","月","火","水","木","金","土");
		var clock_date = new Date();
		var clock_year = clock_date.getYear();
		if(clock_year < 2000) clock_year += 1900;
		var clock_month = clock_date.getMonth() + 1;
		var clock_day = clock_date.getDate();
		var clock_week= clock_date.getDay();
		var clock_hours = clock_date.getHours();
		var clock_minutes = clock_date.getMinutes();
		if(clock_month < 10)
			clock_month = "0" + clock_month;
		if(clock_day < 10)
			clock_day = "0" + clock_day;
		if(clock_hours < 10)
			clock_hours = "0" + clock_hours;
		if(clock_minutes < 10)
			clock_minutes = "0" + clock_minutes;
		document.getElementById('clock').innerHTML = clock_year + "年" + clock_month + "月" + clock_day + "日(" + clock_weeks[clock_week] + ") " + clock_hours + ":" + clock_minutes;
	}
	clock();
	setInterval(clock,60000);
//-->
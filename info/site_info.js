/////////
// SITE DATA
var siteInfo = {};

siteInfo["lafarge"] =
{
	title: "라파즈 한라시멘트 - 가행광산",
  photoYearArray:[2007,2008,2010,2013,2014,2015,2016], 
  demYearArray:[2007,2014,2015,2016],
	view: {
        destination : Cesium.Cartesian3.fromDegrees(128.96, 37.52, 3000.0),
        orientation : {
            heading : Cesium.Math.toRadians(10.0),
            pitch : Cesium.Math.toRadians(-35.0),
            roll : 0.0
        }
    },
	chg_type: [
		{text: "생태복원지역", action: function(){setWmsLayer({"theme":"restore"});}}
		,{text: "채광지역", action: function(){setWmsLayer({"theme":"dig"});}}
		,{text: "지형변화분석", action: function(){setWmsLayer({"theme":"dem_delta"});}}
		,{text: "차영상", action: function(){setWmsLayer({"theme":"photo_delta"});}}
	],
	period: [
		{text: "2015~2016", action: function(){setDem("dem_2016"); setWmsLayer({"year":2016,"photo":"photo"});}}
		,{text: "2014~2015", action: function(){setDem("dem_2015"); setWmsLayer({"year":2015,"photo":"photo"});}}
	],
	message: "광산 내의 각 지역을 선택하면 변화에 해당하는 토공량을 볼 수 있습니다."
}

siteInfo["dongyang"] =
{
	title: "동양시멘트 - 휴지광산",
  photoYearArray:[2014,2016], 
  demYearArray:[2014],
	view: {
        destination : Cesium.Cartesian3.fromDegrees(129.172, 37.385, 2000.0),
        orientation : {
            heading : Cesium.Math.toRadians(10.0),
            pitch : Cesium.Math.toRadians(-35.0),
            roll : 0.0
        }
	},
	chg_type: [
		{text: "종합비교", selected: true, action: function(){console.log("종합비교");}}
		,{text: "생태복원지역", action: function(){console.log("생태복원지역");}}
		,{text: "채광지역", action: function(){console.log("채광지역");}}
		,{text: "재해지역", action: function(){console.log("재해지역");}}
		,{text: "지형변화분석", action: function(){console.log("지형변화분석");}}
		,{text: "차영상", action: function(){console.log("차영상");}}
	],
	period: [
		{text: "2014~2015", action: function(){console.log("2014~2015");}}
		,{text: "2015~2016", action: function(){console.log("2015~2016");}}
	],
	message: "광산 내의 각 지역을 선택하면 변화에 해당하는 토공량을 볼 수 있습니다."
}

///////
// UI BOX FUNCTION
function runCmd(cmd, option) {
	if (cmd == undefined)
		return;
	
	try {
		console.log(cmd);
		var fun = eval(cmd);
		if (option == undefined) 
			fun();
		else
			fun(option);
	} catch(err) {
		console.error("[runCmd]"+err.message);
	}
}

var actionDic = {};
function showInfo(infoObj) {
	var htmlList = [];
	
	htmlList.push('<h1>');
	htmlList.push(infoObj.title);
	htmlList.push('</h1>');
	htmlList.push('<label for="chg_type">• 변화종류&nbsp;</label>');
	htmlList.push('<select name="chg_type" id="chg_type">');
	for (var i in infoObj.chg_type) {
		var item = infoObj.chg_type[i]; 
		var id = "chg_type_"+i;
		actionDic[id] = item.action;
		if (item.selected)
			htmlList.push('<option value="'+id+'" selected="selected">');
		else
			htmlList.push('<option value="'+id+'">');
		htmlList.push(item.text);
		htmlList.push('</option>');
	}
	htmlList.push('</select>');
	htmlList.push('<br/>');
	htmlList.push('<label for="period">• 비교시기&nbsp;</label>');
	htmlList.push('<select name="period" id="period">');
	for (var i in infoObj.period) {
		var item = infoObj.period[i]; 
		var id = "period_"+i;
		actionDic[id] = item.action;
		if (item.selected)
			htmlList.push('<option value="'+id+'" selected="selected">');
		else
			htmlList.push('<option value="'+id+'">');
		htmlList.push(item.text);
		htmlList.push('</option>');
	}
	htmlList.push('</select>');
	htmlList.push('<br/>');
	htmlList.push('<span>');
	htmlList.push(infoObj.message);
	htmlList.push('</span>');
	
	var ui_box = $(".ui-box");
	ui_box.hide();
	ui_box.html(htmlList.join(""));

	$( ".ui-box select" )
	  .change(function () {
		var id = $( this ).val();
		actionDic[id]();
	//});
	}).change();
	ui_box.show("drop", {}, 500);
	
	if (infoObj.view)
		viewer.camera.flyTo(infoObj.view);
}

function hideInfo() {
	$(".ui-box").hide();
}



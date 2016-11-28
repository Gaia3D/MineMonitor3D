/////////
// SITE DATA
var siteInfo = {};

siteInfo["lafarge"] =
{
	title: "라파즈 한라시멘트 - 가행광산",
	view: {
        destination : Cesium.Cartesian3.fromDegrees(128.96, 37.52, 3000.0),
        orientation : {
            heading : Cesium.Math.toRadians(10.0),
            pitch : Cesium.Math.toRadians(-35.0),
            roll : 0.0
        }
    },
  photoYearArray:[
    {year:2007,layer:"Sangji:2007_WGS84"},
    {year:2008,layer:"Sangji:2008_WGS84"},
    {year:2010,layer:"Sangji:2010_WGS84"},
    {year:2012,layer:"Sangji:2012_WGS84"},
    {year:2013,layer:"Sangji:2013_WGS84"},
    {year:2014,layer:"Sangji:2014_WGS84"},
    {year:2015,layer:"Sangji:2015_UAV_wgs84"},
    {year:2016,layer:"Sangji:2016_merge_WGS84"}
  ] 
  ,demYearArray:[
    {year:2007,layer:"dem_2007"},
    {year:2014,layer:"dem_2014"},
    {year:2015,layer:"dem_2015"},
    {year:2016,layer:"dem_2016"}
  ]
  ,photoDeltaArray: [
    {fromYear: 2016, toYear: 2015, layer:"Sangji:PhotoDeltaDelta_2016-2015"}
    ,{fromYear: 2015, toYear: 2014, layer:"Sangji:PhotoDeltaDelta_2015-2014"}
  ]
  ,negiArray: [
    {year: 2016, layer:"Sangji:restore_2016_2015"}
    ,{year: 2015, layer:"Sangji:restore_2015_2014"}
  ]
  ,demDeltaArray: [
    {fromYear: 2016, toYear: 2015, layer:"Sangji:DemDelta_2016-2015_5187"}
    ,{fromYear: 2015, toYear: 2007, layer:"Sangji:DemDelta_2015-2007_5187"}
  ]
  ,chgZoneArray: [
    {year: 2016, layer:"Sangji:restore_2016_2015"}
    ,{year: 2015, layer:"Sangji:dig_2015_2014"}
  ]
}

siteInfo["dongyang"] =
{
	title: "동양시멘트 - 휴지광산",
	view: {
        destination : Cesium.Cartesian3.fromDegrees(129.172, 37.385, 2000.0),
        orientation : {
            heading : Cesium.Math.toRadians(10.0),
            pitch : Cesium.Math.toRadians(-35.0),
            roll : 0.0
        }
	},
  photoYearArray:[
    {year:2008,layer:"Sangji:2008_dongyang_wgs84"},
    {year:2010,layer:"Sangji:2010_dongyang_WGS84"},
    {year:2012,layer:"Sangji:2012_dongyang_WGS84"}
  ], 
  demYearArray:[
    {year:2007,layer:"dem_2007"}
  ]
}

siteInfo["hyundai"] =
{
	title: "현대시멘트 - 가행광산",
	view: {
        destination : Cesium.Cartesian3.fromDegrees(128.360, 37.251, 1600.0),
        orientation : {
            heading : Cesium.Math.toRadians(356.2804),
            pitch : Cesium.Math.toRadians(-27.3142),
            roll : 0
        }
	},
  photoYearArray:[
    {year:2007,layer:"Sangji:Hyundai_2007_WGS84"},
    {year:2009,layer:"Sangji:Hyundai_2009_WGS84"},
    {year:2012,layer:"Sangji:Hyundai_2012_WGS84"}
  ], 
  demYearArray:[
    {year:2007,layer:"dem_2007"},
    {year:2014,layer:"dem_2014"},
    {year:2015,layer:"dem_2015"},
    {year:2016,layer:"dem_2016"}
  ]
}

siteInfo["asia"] =
{
	title: "아시아시멘트 - 가행광산",
	view: {
        destination : Cesium.Cartesian3.fromDegrees(128.301, 37.251, 1550),
        orientation : {
            heading : Cesium.Math.toRadians(21.6944),
            pitch : Cesium.Math.toRadians(-39.6105),
            roll : 0
        }
	},
  photoYearArray:[
    {year:2007,layer:"Sangji:Asia_2007_WGS84"},
    {year:2009,layer:"Sangji:Asia_2009_WGS84"},
    {year:2012,layer:"Sangji:Asia_2012_WGS84"}
  ], 
  demYearArray:[
    {year:2007,layer:"dem_2007"},
    {year:2014,layer:"dem_2014"},
    {year:2015,layer:"dem_2015"},
    {year:2016,layer:"dem_2016"}
  ]
}

siteInfo["ssangyoung"] =
{
	title: "쌍용시멘트 - 휴지광산",
	view: {
        destination : Cesium.Cartesian3.fromDegrees(129.170, 37.391, 1020.0),
        orientation : {
            heading : Cesium.Math.toRadians(344.583),
            pitch : Cesium.Math.toRadians(-37.049),
            roll : 0
        }
	},
  photoYearArray:[
    {year:2008,layer:"Sangji:SSangyoung_2008_WGS84"},
    {year:2009,layer:"Sangji:SSangyoung_2009_WGS84"},
    {year:2011,layer:"Sangji:SSangyoung_2011_WGS84"}
  ], 
  demYearArray:[
    {year:2007,layer:"dem_2007"},
    {year:2014,layer:"dem_2014"},
    {year:2015,layer:"dem_2015"},
    {year:2016,layer:"dem_2016"}
  ]
}

# -*- coding: utf-8 -*-
from osgeo import gdal
import osgeo.osr as osr
from gdalconst import *

# Enable GDAL/OGR exceptions
gdal.UseExceptions()


# example GDAL error handler function
def gdal_error_handler(err_class, err_num, err_msg):
    errtype = {
            gdal.CE_None: 'None',
            gdal.CE_Debug: 'Debug',
            gdal.CE_Warning: 'Warning',
            gdal.CE_Failure: 'Failure',
            gdal.CE_Fatal: 'Fatal'
    }
    err_msg = err_msg.replace('\n', ' ')
    err_class = errtype.get(err_class, 'None')
    print 'Error Number: %s' % err_num
    print 'Error Type: %s' % err_class
    print 'Error Message: %s' % err_msg

# install error handler
gdal.PushErrorHandler(gdal_error_handler)


def getRasterInfo(filePath):
    try:
        dataset = gdal.Open(filePath, GA_ReadOnly)
        wkt = dataset.GetProjection()
        srs = osr.SpatialReference()
        srs.ImportFromWkt(wkt)
        authoOrg = srs.GetAttrValue("AUTHORITY", 0)
        authoNo = srs.GetAttrValue("AUTHORITY", 1)
        geotransform = dataset.GetGeoTransform()
        infoObj = dict()
        infoObj['xSize'] = dataset.RasterXSize
        infoObj['ySize'] = dataset.RasterYSize
        infoObj['srs'] = "{}:{}".format(authoOrg, authoNo)
        if geotransform is not None:
            infoObj['xOrg'] = geotransform[0]
            infoObj['yOrg'] = geotransform[3]
            infoObj['xRes'] = geotransform[1]
            infoObj['yRes'] = geotransform[5]
            infoObj['xMin'] = min(geotransform[0], geotransform[0]+geotransform[1]*dataset.RasterXSize)
            infoObj['yMin'] = min(geotransform[3], geotransform[3]+geotransform[5]*dataset.RasterXSize)
            infoObj['xMax'] = max(geotransform[0], geotransform[0]+geotransform[1]*dataset.RasterXSize)
            infoObj['yMax'] = max(geotransform[3], geotransform[3]+geotransform[5]*dataset.RasterXSize)

        return infoObj
    except Exception as e:
        print "ERROR in getRasterInfo(", filePath, ')'
        print e
        return None
# -*- coding: utf-8 -*-

import os
from gdal_template import *

if __name__ == '__main__':
    DATA_FOLDER = r"C:\Temp\Lafarge"

    photo_list = dict()
    photo_list[2007] = "2007_WGS84.tif"
    photo_list[2008] = "2008_WGS84.tif"
    photo_list[2010] = "2010_WGS84.tif"
    photo_list[2012] = "2012_WGS84.tif"
    photo_list[2013] = "2013_WGS84.tif"
    photo_list[2014] = "2014_WGS84.tif"
    photo_list[2015] = "2015_UAV_wgs84.tif"
    photo_list[2016] = "2016_merge_WGS84.tif"

    years = photo_list.keys()
    years.sort()

    boundFilePath = os.path.join(DATA_FOLDER, "Bound.tif")
    boundInfo = getRasterInfo(boundFilePath)

    for i in range(len(years)):
        tempFileList = list()

        # 0. 파일정보 확인
        iYear = years[i]
        iName = photo_list[iYear]
        iFilePath = os.path.join(DATA_FOLDER, iName)
        iInfo = getRasterInfo(iFilePath)

        print '[I]:', iFilePath
        print iInfo

        tempPhotoPath = os.path.join(DATA_FOLDER, "temp_vari_{}.tif".format(iYear))
        cmdStr = 'gdal_translate -of "GTiff" -ot Float32 -outsize {} {} -projwin {} {} {} {} {} {}' \
            .format(boundInfo['xSize'], boundInfo['ySize'], boundInfo['xMin'], boundInfo['yMax'], boundInfo['xMax'], boundInfo['yMin'], iFilePath, tempPhotoPath)
        print cmdStr
        os.system(cmdStr)
        tempFileList.append(tempPhotoPath)

        # 그냥 하면 오류가 나서 여기서 멈춤.
        # regedit로 HKEY_CURRENT_USER\Software\Microsoft\Windows\Windows Error Reporting 의 DontShowUI 를 1로 설정하여 해결
        # 참고: http://gis.stackexchange.com/questions/101921/gdal-calc-works-but-i-get-a-python-error-at-the-end-of-each-process-that-prevent
        outFileName = r'{data_folder}\vari_{year}.tif'\
            .format(data_folder=DATA_FOLDER, year=iYear)
        # cmdStr = r'gdal_calc --calc "((B-A)/(B+A-C))*D" --format GTiff --type Float32 --overwrite ' \
        #          r'-A {src_file} --A_band 1 ' \
        #          r'-B {src_file} --B_band 2 ' \
        #          r'-C {src_file} --C_band 3 ' \
        #          r'-D {bound_file} ' \
        #          r'--outfile={out_name}'\
        #     .format(data_folder=DATA_FOLDER, src_file=tempPhotoPath, bound_file=boundFilePath, out_name=outFileName)
        cmdStr = r'gdal_calc --calc "((B-A)/(B+A-C))" --format GTiff --type Float32 --overwrite ' \
                 r'-A {src_file} --A_band 1 ' \
                 r'-B {src_file} --B_band 2 ' \
                 r'-C {src_file} --C_band 3 ' \
                 r'--outfile={out_name}'\
            .format(data_folder=DATA_FOLDER, src_file=tempPhotoPath, bound_file=boundFilePath, out_name=outFileName)
        print cmdStr
        os.system(cmdStr)

        # 불필요 파일 제거
        for tempFile in tempFileList:
            os.remove(tempFile)

        print

    exit(0)

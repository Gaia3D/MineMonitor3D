# -*- coding: utf-8 -*-

import os
from gdal_template import *


if __name__ == '__main__':
    DATA_FOLDER = r"C:\Temp\Lafarge"

    dem_list = dict()
    dem_list[2007] = "2007_join.tif"
    dem_list[2014] = "2014_DEM_fix.tif"
    dem_list[2015] = "2015_DEM_UAV_Cut.tif"
    dem_list[2016] = "2016_merge_dem_wgs84_fix.tif"

    years = dem_list.keys()
    years.sort()

    for i in range(len(years)):
        # 0. 파일정보 확인
        iYear = years[i]
        iName = dem_list[iYear]
        iFilePath = os.path.join(DATA_FOLDER, iName)
        iInfo = getRasterInfo(iFilePath)

        subYears = years[(i+1):]
        for j in range(len(subYears)):
            # 0. 파일정보 확인
            jYear = subYears[j]
            jName = dem_list[jYear]
            jFilePath = os.path.join(DATA_FOLDER, jName)
            jInfo = getRasterInfo(jFilePath)

            print '[I]:', iFilePath
            print iInfo
            print '[J]:', jFilePath
            print jInfo

            # 1. 범위 확인: 최대 최소 합성
            xMin = min(iInfo['xMin'], jInfo['xMin'])
            yMin = min(iInfo['yMin'], jInfo['yMin'])
            xMax = max(iInfo['xMax'], jInfo['xMax'])
            yMax = max(iInfo['yMax'], jInfo['yMax'])

            # 2. 해상도: 더 조밀한 해상도
            xRes = min(iInfo['xRes'], jInfo['xRes'])
            yRes = max(iInfo['yRes'], jInfo['yRes'])

            # 3. 해당 범위와 해상도 대상 변환
            iDem = os.path.join(DATA_FOLDER, "temp_{}.tif".format(iYear))
            cmdStr = 'gdal_translate -of "GTiff" -tr {} {} -projwin {} {} {} {} {} {}'\
                .format(xRes, yRes, xMin, yMax, xMax, yMin, iFilePath, iDem)
            print cmdStr
            os.system(cmdStr)

            jDem = os.path.join(DATA_FOLDER, "temp_{}.tif".format(jYear))
            cmdStr = 'gdal_translate -of "GTiff" -tr {} {} -projwin {} {} {} {} {} {}'\
                .format(xRes, yRes, xMin, yMax, xMax, yMin, jFilePath, jDem)
            print cmdStr
            os.system(cmdStr)

            # 4. 잔차 계산
            # 그냥 하면 오류가 나서 여기서 멈춤.
            # regedit로 HKEY_CURRENT_USER\Software\Microsoft\Windows\Windows Error Reporting 의 DontShowUI 를 1로 설정하여 해결
            # 참고: http://gis.stackexchange.com/questions/101921/gdal-calc-works-but-i-get-a-python-error-at-the-end-of-each-process-that-prevent
            cmdStr = r'gdal_calc --overwrite -A {data_folder}\temp_{a_year}.tif -B {data_folder}\\temp_{b_year}.tif ' \
                     '--outfile={data_folder}\dem_{a_year}-{b_year}.tif --calc="A-B"'\
                .format(data_folder=DATA_FOLDER, a_year=jYear, b_year=iYear)
            print cmdStr
            os.system(cmdStr)

            # 불필요 파일 제거
            os.remove(iDem)
            os.remove(jDem)

            print

# -*- coding: utf-8 -*-

import os
from gdal_template import *
from math import floor

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

    for i in range(len(years)):
        # 0. 파일정보 확인
        iYear = years[i]
        iName = photo_list[iYear]
        iFilePath = os.path.join(DATA_FOLDER, iName)
        iInfo = getRasterInfo(iFilePath)

        subYears = years[(i+1):]
        for j in range(len(subYears)):
            tempFileList = list()

            # 0. 파일정보 확인
            jYear = subYears[j]
            jName = photo_list[jYear]
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

            xSize = int((xMax - xMin) / xRes)
            ySize = int(abs((yMax - yMin) / yRes))

            # 3. 해당 범위와 해상도 대상 변환
            iPhoto = os.path.join(DATA_FOLDER, "temp_{}.tif".format(iYear))
            cmdStr = 'gdal_translate -of "GTiff" -outsize {} {} -projwin {} {} {} {} {} {}'\
                .format(xSize, ySize, xMin, yMax, xMax, yMin, iFilePath, iPhoto)
            print cmdStr
            os.system(cmdStr)
            tempFileList.append(iPhoto)

            jPhoto = os.path.join(DATA_FOLDER, "temp_{}.tif".format(jYear))
            cmdStr = 'gdal_translate -of "GTiff" -outsize {} {} -projwin {} {} {} {} {} {}'\
                .format(xSize, ySize, xMin, yMax, xMax, yMin, jFilePath, jPhoto)
            print cmdStr
            os.system(cmdStr)
            tempFileList.append(jPhoto)

            # 4. 밴드별 차영상 계산
            # 그냥 하면 오류가 나서 여기서 멈춤.
            # regedit로 HKEY_CURRENT_USER\Software\Microsoft\Windows\Windows Error Reporting 의 DontShowUI 를 1로 설정하여 해결
            # 참고: http://gis.stackexchange.com/questions/101921/gdal-calc-works-but-i-get-a-python-error-at-the-end-of-each-process-that-prevent
            for iBand in range(3):
                outFileName = r'{data_folder}\photo_band{band}_{a_year}-{b_year}.tif'\
                    .format(data_folder=DATA_FOLDER, a_year=jYear, b_year=iYear, band=(iBand+1))
                cmdStr = r'gdal_calc --calc "A-B" --format GTiff --type Byte ' \
                         r'-A {data_folder}\temp_{a_year}.tif --A_band {band} ' \
                         r'-B {data_folder}\\temp_{b_year}.tif --B_band {band} ' \
                         r'--outfile={out_name}'\
                    .format(data_folder=DATA_FOLDER, a_year=jYear, b_year=iYear, band=(iBand+1), out_name=outFileName)
                print cmdStr
                os.system(cmdStr)
                tempFileList.append(outFileName)

            # 5. RGB 합성위한 가상래스터 생성
            vrtFileName = r'{data_folder}\photo_{a_year}-{b_year}.vrt'\
                    .format(data_folder=DATA_FOLDER, a_year=jYear, b_year=iYear)
            cmdStr = r'gdalbuildvrt -separate {out_file} ' \
                     r'{data_folder}\photo_band1_{a_year}-{b_year}.tif ' \
                     r'{data_folder}\photo_band2_{a_year}-{b_year}.tif ' \
                     r'{data_folder}\photo_band3_{a_year}-{b_year}.tif'\
                .format(out_file=vrtFileName, data_folder=DATA_FOLDER, a_year=jYear, b_year=iYear)
            print cmdStr
            os.system(cmdStr)
            tempFileList.append(vrtFileName)

            # 6. 합성된 Tiff 생성
            finalFileName = r'{data_folder}\photo_{a_year}-{b_year}.tif'\
                    .format(data_folder=DATA_FOLDER, a_year=jYear, b_year=iYear)
            cmdStr = r'gdal_translate -of GTiff -ot Byte -co "TILED=YES" -a_srs "EPSG:4326" {src_file} {out_file}'\
                .format(out_file=finalFileName, src_file=vrtFileName)
            print cmdStr
            os.system(cmdStr)

            # 7. 속도 향상 위한 오버레이 생성
            cmdStr = r'gdaladdo -r average {} 2 4 8 16'.format(finalFileName)
            print cmdStr
            os.system(cmdStr)


            # 불필요 파일 제거
            for tempFile in tempFileList:
                os.remove(tempFile)

            print

    exit(0)

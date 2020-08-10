import geopandas as gpd
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from shapely.geometry import Polygon
import numpy as np
from shapely.geometry import Point
from geopy.distance import geodesic
from math import radians, cos, sin, asin, sqrt
import time
from dbfread import DBF
from pandas import DataFrame
import shapely


#Get the center of surbub area and caculate radius of suburb area



poly = gpd.read_file("/Users/zhangweichen/PycharmProjects/twitterproject/NSW_LOCALITY_POLYGON_shp.shp")
pol1 = gpd.read_file("/Users/zhangweichen/PycharmProjects/twitterproject/NSW_LOCALITY_POLYGON_shp.shp")
dbf =DBF("/Users/zhangweichen/PycharmProjects/twitterproject/NSW_LOCALITY_POLYGON_shp.dbf")
#pointdata = pd.read_csv('/Users/zhangweichen/PycharmProjects/twitterproject/points.csv')

poly.head()
bbox = pol1.bounds
bboxcsv = pd.DataFrame(bbox)
dbfdata = DataFrame(iter(dbf))

#print(bbox)
#print(poly)
#print(dbfdata)
#print(dbfdata[:])
#dbfdata.to_csv('/Users/zhangweichen/PycharmProjects/twitterproject/dbfdata.csv')
#bboxcsv.to_csv('/Users/zhangweichen/PycharmProjects/twitterproject/bboxcsv.csv')

# copy poly to new GeoDataFrame
points = poly.copy()


# change the geometry
points.geometry = points['geometry'].centroid
# same crs
points.crs = poly.crs
points.head()
#print(points)#中心点

#points.to_csv('/Users/zhangweichen/PycharmProjects/twitterproject/points.csv')



# print(poly)
centroid = pd.DataFrame({'points': points['geometry'],
                         'LC_PLY_PID': points['LC_PLY_PID']})
#centroid.to_csv('/Users/zhangweichen/PycharmProjects/twitterproject/centroid.csv')

#pointdata = pd.DataFrame(points)
#print(pointdata)
#pointdata.to_txt('/Users/zhangweichen/PycharmProjects/twitterproject/pointdata.txt')


###########分离经纬度###########
import re
#cendata = pd.DataFrame({'POINTS':centroid['points'],
#                       'LC_PLY_PID':centroid['LC_PLY_PID']})

pdata = pd.read_csv('/Users/zhangweichen/PycharmProjects/twitterproject/points.csv')
#searchdata = re.search(r'(^[0-9]+.[0-9]+$)\n(^\-[0-9]+.[0-9]+$)', pdata['geometry'][0])
#searchdata = re.findall(('\-?[0-9]+.[0-9]+'),pdata['geometry'][0])
#print(searchdata[0])
centindex = np.arange(4591)
latlondf = pd.DataFrame(columns=('index','lat','lon'), index=[])
#print(latlondf)
#latlondf_1 = pd.concat([pdata,latlondf],axis=0)
#print(latlondf_1)

#l = re.search(r'(^[0-9]+\.[0-9]+)\n(^\-[0-9]+\.[0-9]+)',pdata['geometry'][0])
#l1 = re.findall(('[0-9]+.[0-9]+' '$'),pdata['geometry'][0])
#l2 = re.findall(('\-.[0-9]+.[0-9]+'),pdata['geometry'][0])
#l = [pdata['geometry'][0]]
#print(l)
#ldata = re.findall(('\-?[0-9]+.[0-9]+'),l[0])
#l = re.findall(('\-?[0-9]+.[0-9]+'),pdata['geometry'][0])
#l1 = ldata[0]
#l2 = ldata[1]
#print(l1)
#print(l2)
#centrodf = pd.DataFrame({'LC_PLY_PID':pdata['LC_PLY_PID'],'lat':[],'lon':[]},index=centindex)
#print(centrodf)
for i in range(4591):
#for i in range(20):
#print(re.findall(('\-?[0-9]+.[0-9]+'),pdata['geometry'][i]))
#  searchdata = re.search(r'([0-9]+.[0-9]+)\n(^\-[0-9]+.[0-9]+)',pdata['geometry'][i])
#  searchdata = re.findall(('\-?[0-9]+.[0-9]+'),pdata['geometry'][i])
#  lat = searchdata.group(1)
#  lon = searchdata.group(0)
   l = [pdata['geometry'][i]]
#  print(l)
   ldata = re.findall(('\-?[0-9]+.[0-9]+'), l[0])
#  print(ldata)
#   l.clear()
#  l = re.findall(('\-?[0-9]+.[0-9]+'),pdata['geometry'][0])
   lon = ldata[0]
   lat = ldata[1]
#  print(lon)
#  print(lat)
   latlondf = latlondf.append(pd.DataFrame({'index':[i],'LC_PLY_PID': pdata['LC_PLY_PID'][i],'NSW_NAME':pdata['NSW_LOCA_2'][i],
                                             'lat': [lat],
                                             'lon': [lon]}),ignore_index=True)
#  ldata.clear()
   print(lat,lon)
#latlondf.dropna(axis=1,how='any')
#print(latlondf)
#latlondf.to_csv('/Users/zhangweichen/PycharmProjects/twitterproject/points.csv')



#for POINTS in cendata:
#    m = re.search(r'(\^[15]+/.[0-9]+\n$),(^/-[0-9]+/.[0-9]+$)',cendata[:1])
#    m = re.search(r'(/ ^ (0 | ([1 - 9]\d *))(\.\d +)?$),(/^[-](0|([1-9]\d*))(\.\d+)?$)',cendata[1:])
#     m = re.search(r'(/^\(.[0-9]+.\)&)',POINTS)
#     print(m)
#    lon = m.group(1)
#    lat = m.group(2)
#    print(lon,lat)

from shapely.geometry import Polygon


# data = pd.DataFrame({'LC_PLY_PID': poly['LC_PLY_PID'],
# 'geometry': poly['geometry']})

# print(poly)

# def point_to_geo(df, lon, lat):
#    df['geometry'] = gpd.GeoSeries(list(zip(df[lon], df[lat]))).apply(Point)  # 识别经纬度，转换点数据
#    df = gpd.GeoDataFrame(df)  # 转换Geodataframe格式
#    df.crs = {'init': 'epsg:4326'}  # 定义坐标系WGS84
#    del df[lon]
#    del df[lat]
#    return df

# poly = point_to_geo(poly, 'lon', 'lat')
# print(poly)
# print(geodesic((-32.873444,151.733446), (-32.899901,151.713572)).km)
# print(geodesic((-32.873444,151.713572), (-32.899901,151.733446)).km)
# dfbbox = pd.DataFrame(bbox)
# print(bbox.loc[0,'minx'])
# index = np.arange(0,4591)
# for n in range(4591):
#    Ldata = geodesic(((bbox.loc[n,'maxy']),(bbox.loc[n,'maxx'])),((bbox.loc[n,'miny']),(bbox.loc[n,'minx'])))
#    Wdata = geodesic(((bbox.loc[n,'maxy']),(bbox.loc[n,'minx'])),((bbox.loc[n,'miny']),(bbox.loc[n,'minx'])))
#    LWdata = pd.DataFrame({'L':Ldata,
#                   'W':Wdata},index=index)
#    n=n+1

# print(LWdata)
#def haversine(lon1, lat1, lon2, lat2):
#    """
#    Calculate the great circle distance between two points
#    on the earth (specified in decimal degrees)
#    """
    # convert decimal degrees to radians
#    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
#    dlon = lon2 - lon1
#    dlat = lat2 - lat1
#    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
#    c = 2 * asin(sqrt(a))
#    r = 3956  # Radius of earth in miles3956. Use 6371 for kilometers

#    return c * r


# print(haversine(151.733446, -32.873444, 151.713572, -32.899901))
#print(geodesic((-32.873444, 151.733446), (-32.899901, 151.713572)).km)
#print(geodesic((-32.873444, 151.713572), (-32.899901, 151.713572)).km)
#print(geodesic((bbox.loc[0, 'minx'], bbox.loc[0, 'maxy']), (bbox.loc[0, 'maxx'], bbox.loc[0, 'maxy'])).km)

#def haversine2(lon1, lat1, lon2, lat2):
#    dis = geodesic(lat1, lon1, lat2, lon2)
#    return dis
def geodistance(lng1,lat1,lng2,lat2):
#lng1,lat1,lng2,lat2 = (120.12802999999997,30.28708,115.86572000000001,28.7427)
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)]) # 经纬度转换成弧度
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance=2*asin(sqrt(a))*6371*1000 # 地球平均半径，6371km
    distance=round(distance/1000,3)
    return distance

LWdata = pd.DataFrame(columns=('index','L', 'W', 'Radius'), index=[])

# for n in range(4591):
#    Ldata = haversine((bbox.loc[n,'maxy']),(bbox.loc[n,'maxx']),(bbox.loc[n,'miny']),(bbox.loc[n,'minx']))
#    Wdata = haversine((bbox.loc[n,'maxy']),(bbox.loc[n,'minx']),(bbox.loc[n,'miny']),(bbox.loc[n,'minx']))
#   haversine()
#    Radius = Ldata-Wdata
#    LWdata= LWdata.append(pd.DataFrame({'L':[Ldata],
#                   'W':[Wdata],'Radius':[Radius]}),ignore_index=True)
# for n in range(4591):
#    Ldata = haversine((bbox.loc[n,'minx']),(bbox.loc[n,'maxy']),(bbox.loc[n,'maxx']),(bbox.loc[n,'maxy']))
#    Wdata = haversine((bbox.loc[n,'minx']),(bbox.loc[n,'miny']),(bbox.loc[n,'maxx']),(bbox.loc[n,'miny']))
#    Radius = Ldata-Wdata
#    LWdata= LWdata.append(pd.DataFrame({'L':[Ldata],
#                   'W':[Wdata],'Radius':[Radius]}),ignore_index=True)
###########################
for n in range(4591):
    Ldata = geodistance((bbox.loc[n, 'maxy']), (bbox.loc[n, 'maxx']), (bbox.loc[n, 'miny']), (bbox.loc[n, 'minx']))
    Wdata = geodistance((bbox.loc[n, 'maxy']), (bbox.loc[n, 'minx']), (bbox.loc[n, 'miny']), (bbox.loc[n, 'minx']))
    Radius =(((Ldata + Wdata)/2)/2)
    LWdata = LWdata.append(pd.DataFrame({'index':[n],'L': [Ldata],
                                         'W': [Wdata], 'Radius': [Radius]}), ignore_index=True)
#print(LWdata)
finaldata = pd.merge(latlondf, LWdata, how='left',on='index')
print(finaldata)
finaldata.to_csv("/Users/zhangweichen/PycharmProjects/twitterproject/finaldata.csv")
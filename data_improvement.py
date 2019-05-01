from datetime import datetime , time
import os
import glob
import pandas as pd
import csv
from math import sin, cos, sqrt, atan2, radians, asin


df=pd.read_csv("shortened.csv")

df['Latitude']=df['Latitude'].astype(float)
df['Longitude']=df['Longitude'].astype(float)

police = [{'lat': 41.85837259, 'lon': -87.62735617}, 
                {'lat': 41.80181109,  'lon': -87.63056018}, 
                {'lat': 41.76643089, 'lon': -87.60574786},
                {'lat': 41.70793329, 'lon': -87.56834912}, 
                {'lat': 41.69272336,  'lon': -87.60450587}, 
                {'lat': 41.75213684, 'lon': -87.64422891},
                {'lat': 41.77963154, 'lon': -87.66088702}, 
                {'lat': 41.77898719,  'lon': -87.70886382}, 
                {'lat': 41.83739443 , 'lon': -87.64640771},
                {'lat': 41.85668453, 'lon': -87.70838196}, 
                {'lat': 41.87358229,  'lon': -87.70548813}, 
                {'lat': 41.86297662, 'lon': -87.65697251},
                {'lat': 41.92110332, 'lon': -87.69745182}, 
                {'lat': 41.88008346,  'lon': -87.76819989}, 
                {'lat': 41.97409445 , 'lon': -87.76614884},
                {'lat': 41.96605342, 'lon': -87.72811456}, 
                {'lat': 41.90324165,  'lon': -87.64335214}, 
                {'lat': 41.94740046, 'lon': -87.65151202},
                {'lat': 41.94740046, 'lon': -87.65151202}, 
                {'lat': 41.97954951,  'lon': -87.69284451}, 
                {'lat': 41.69143478, 'lon': -87.66852039},
                {'lat': 41.99976348, 'lon': -87.67132429}, 
                {'lat': 41.91860889,  'lon': -87.76557448}, 
                {'lat': 41.83070169, 'lon': -87.62339535}]

def night_conv(x):
    x=datetime.strptime(x,'%m/%d/%Y %H:%M:%S %p').time()
    if x >= time(22,00) or x <= time(8,00):
        x=True
    else:
        x=False
    return(x)


def day_of_week(x):
    x=datetime.strptime(x,'%m/%d/%Y %H:%M:%S %p').weekday()
    return(x)

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

def closest(data,v):
    return min(police, key=lambda p: distance(v['Latitude'],v['Longitude'],p['lat'],p['lon']))

df['Night']=df['Date'].apply(night_conv)
df['dayofweek']=df['Date'].apply(day_of_week)
v=df[["Latitude","Longitude"]]
df["PolDis"] = ""
for index, row in v.iterrows():

    x = closest(police,row)
    t=distance(x['lat'],x['lon'],row['Latitude'],row['Longitude'])
    df['PolDis'].iloc[index]=t

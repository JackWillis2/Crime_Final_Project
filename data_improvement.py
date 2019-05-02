from datetime import datetime , time
import os
import glob
import pandas as pd
import csv
from math import sin, cos, sqrt
from sklearn.preprocessing import LabelEncoder
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

def whatmonth(x):
    x=datetime.strptime(x,'%m/%d/%Y %H:%M:%S %p').month
    return(x)

def whatday(x):
    x=datetime.strptime(x,'%m/%d/%Y %H:%M:%S %p').date()
    return(x)

def distance(lat1, lon1, lat2, lon2):
    return sqrt((lat1-lat2)**2+(lon1-lon2)**2)

def closest(data,la,lo):
    return min(police, key=lambda p: distance(la,lo,p['lat'],p['lon']))

df=pd.read_csv("shortened.csv")
df=df.head(n=100000)
df['Latitude']=df['Latitude'].astype(float)
df['Longitude']=df['Longitude'].astype(float)
#police station locations
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

df['Night']=df['Date'].apply(night_conv)
df['dayofweek']=df['Date'].apply(day_of_week)
df['Month']=df['Date'].apply(whatmonth)
df['day']=df['Date'].apply(whatday)
total_interactions=df[['ID','day']].groupby(['day']).count()
df=df.merge(total_interactions,left_on='day', right_on='day')
df["PolDis"] = 0
for index, row in df.iterrows():
    x = closest(police,row["Latitude"],row["Longitude"])
    df.loc[index, 'PolDis']=distance(x['lat'],x['lon'],row['Latitude'],row['Longitude'])*100
    print(index)



df.drop(['Unnamed: 0','Date','ID_x','Latitude', 'Longitude','day','Year'],axis=1,inplace=True)


le_type = LabelEncoder()

df['Primary Type'] = le_type.fit_transform(df['Primary Type'].astype(str))


le_Description = LabelEncoder()

df['Description'] = le_Description.fit_transform(df['Description'].astype(str))


le_arrest = LabelEncoder()
df['Arrest'] = le_arrest.fit_transform(df['Arrest'])


le_dom = LabelEncoder()
df['Domestic'] = le_dom.fit_transform(df['Domestic'])

le_loc = LabelEncoder()
df['Location Description'] = le_dom.fit_transform(df['Location Description'].astype(str))

le_fbi = LabelEncoder()

df['FBI Code'] = le_fbi.fit_transform(df['FBI Code'].astype(str))


le_night = LabelEncoder()
df['Night'] = le_night.fit_transform(df['Night'])


cols = list(df.columns.values)
cols.pop(cols.index('Arrest'))
df = df[['Arrest']+cols]
df=df.dropna()

df.to_csv("for_model.csv")
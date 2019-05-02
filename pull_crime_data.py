import os
import glob
import pandas as pd
import csv


df=pd.read_csv("Crimes_-_2001_to_present.csv")
print(df.head())
df.dropna(subset=["Location Description","Ward","Community Area","Latitude","Longitude","Police Districts"],inplace= True)
df=df[df.Year < 2004]
df=df[df.Year > 2002]
cols = [1,3,4,15,16,18,21,22,23,24,25,26]
df.drop(df.columns[cols],axis=1,inplace=True)

df.to_csv("shortened.csv")

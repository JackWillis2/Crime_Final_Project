import os
import glob
import pandas as pd
import csv


df=pd.read_csv("Crimes_-_2001_to_present.csv")
print(df.head())
df.dropna(subset=["Location Description","Ward","Community Area","Latitude","Longitude","Police Districts"],inplace= True)
df[df.Year < 2010]
cols = [1,3,4,15,16,18,21,22,23,24,25,26]
df.drop(df.columns[cols],axis=1,inplace=True)
p=df.head(n=1000)
p.to_csv("shortened.csv")

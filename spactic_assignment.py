# -*- coding: utf-8 -*-
"""spactic assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QqCyr92NIsbMkdgENe6mVXYCwrpJ1_yY
"""

# !pip install geopy
# !pip install Levenshtein

import pandas as pd
from geopy.distance import geodesic
from Levenshtein import distance

df = pd.read_csv('assignment_data.csv')

df['is_similar'] = 0   #To add new column

for i in range(len(df)-1):
  name1 = df.loc[i, "name"]
  lat1 = df.loc[i, "latitude"]
  long1 = df.loc[i, "longitude"]

  for j in range(i+1, len(df)):
    if df.loc[i, "is_similar"]==1 and df.loc[j, "is_similar"]==1:  #Extra check point to optimise
      continue

    name2 = df.loc[j, "name"]
    lat2 = df.loc[j, "latitude"]
    long2 = df.loc[j, "longitude"]

    lev_dis = distance(name1, name2)   # calculation of Levenshtein distance

    cordinate1 = (lat1, long1)
    cordinate2 = (lat2, long2)
    geo_dis = geodesic(cordinate1, cordinate2)  # calculation of greater circle distance

    if lev_dis<5 and geo_dis<=0.2:   #condition for similarity check
      df.loc[i, "is_similar"] = 1
      df.loc[j, "is_similar"] = 1

df.to_csv('final.csv')
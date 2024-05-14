import pandas as pd
import numpy as np

with open('url.txt', 'r') as file:
    url = file.read()

df = pd.read_csv(url)

# Minimizing size of numeric columns

df['CRASH DATETIME'] = df['CRASH DATE'] + ' ' + df['CRASH TIME']
df['CRASH DATETIME'] = pd.to_datetime(df['CRASH DATETIME'])
df = df.drop(['CRASH DATE', 'CRASH TIME', 'LOCATION'], axis=1) # location is too useless

new_order = ['CRASH DATETIME', 'BOROUGH', 'ZIP CODE', 'LATITUDE', 'LONGITUDE', 'ON STREET NAME',
       'CROSS STREET NAME', 'OFF STREET NAME', 'NUMBER OF PERSONS INJURED',
       'NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED',
       'NUMBER OF PEDESTRIANS KILLED', 'NUMBER OF CYCLIST INJURED',
       'NUMBER OF CYCLIST KILLED', 'NUMBER OF MOTORIST INJURED',
       'NUMBER OF MOTORIST KILLED', 'CONTRIBUTING FACTOR VEHICLE 1',
       'CONTRIBUTING FACTOR VEHICLE 2', 'CONTRIBUTING FACTOR VEHICLE 3',
       'CONTRIBUTING FACTOR VEHICLE 4', 'CONTRIBUTING FACTOR VEHICLE 5',
       'COLLISION_ID', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2',
       'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5']
df = df[new_order]

df['ZIP CODE'] = df['ZIP CODE'].replace('     ', np.nan)
df['ZIP CODE'] = df['ZIP CODE'].astype('float32')
df['ZIP CODE'] = df['ZIP CODE'].astype('Int32')
df['NUMBER OF PERSONS INJURED'] = df['NUMBER OF PERSONS INJURED'].astype('Int64')
df['NUMBER OF PERSONS INJURED'] = df['NUMBER OF PERSONS INJURED'].astype('Int8')
df['NUMBER OF PERSONS KILLED'] = df['NUMBER OF PERSONS KILLED'].astype('Int64')
df['NUMBER OF PERSONS KILLED'] = df['NUMBER OF PERSONS KILLED'].astype('Int8')
df['NUMBER OF PEDESTRIANS INJURED'] = df['NUMBER OF PEDESTRIANS INJURED'].astype('int8')
df['NUMBER OF PEDESTRIANS KILLED'] = df['NUMBER OF PEDESTRIANS KILLED'].astype('int8')
df['NUMBER OF CYCLIST INJURED'] = df['NUMBER OF CYCLIST INJURED'].astype('int8')
df['NUMBER OF CYCLIST KILLED'] = df['NUMBER OF CYCLIST KILLED'].astype('int8')
df['NUMBER OF MOTORIST INJURED'] = df['NUMBER OF MOTORIST INJURED'].astype('int8')
df['NUMBER OF MOTORIST KILLED'] = df['NUMBER OF MOTORIST KILLED'].astype('int8')
df['COLLISION_ID'] = df['COLLISION_ID'].astype('int32')

df.to_pickle('df.pkl')
print('data transform, proceed to loading')
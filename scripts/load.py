import pandas as pd
import json

df = pd.read_pickle('df.pkl')

# Creating Dimensions

## Vehicle dimension
vehicle_cols = ['VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2', 'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5']
all_values = pd.concat([df[col] for col in vehicle_cols])
unique_values_list = all_values.dropna().unique().tolist()

str_columns = df.select_dtypes(include = 'object').columns.to_list()

for col in str_columns:
  df[col] = df[col].str.lower()

vehicle_cols = ['VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2',
                'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4',
                'VEHICLE TYPE CODE 5'
]
all_vehicle_values = pd.concat([df[col] for col in vehicle_cols])
unique_vehicle_values = all_vehicle_values.dropna().unique().tolist()

dim_vehicle = pd.DataFrame({
    'VEHICLE_ID': range(1, len(unique_vehicle_values) + 1),
    'VEHICLE_TYPE': unique_vehicle_values
})

## Factor Dimension
factor_cols = ['CONTRIBUTING FACTOR VEHICLE 1', 'CONTRIBUTING FACTOR VEHICLE 2',
                'CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4',
                'CONTRIBUTING FACTOR VEHICLE 5'
]
all_factor_values = pd.concat([df[col] for col in factor_cols])
unique_factor_values = all_factor_values.dropna().unique().tolist()

dim_factor = pd.DataFrame({
    'FACTOR_ID': range(1, len(unique_factor_values) + 1),
    'CONTRIBUTING_FACTOR': unique_factor_values
})

## Date Dimension
import calendar

def week_of_month(dt):
    year = dt.year
    month = dt.month
    day = dt.day

    cal = calendar.monthcalendar(year, month)
    week_number = (day - 1) // 7 + 1
    return week_number


start_date = df['CRASH DATETIME'].min()
end_date = df['CRASH DATETIME'].max()

dim_date = pd.DataFrame({'date': pd.date_range(start_date, end_date, freq='H')})
# Extract attributes
dim_date['YEAR'] = dim_date['date'].dt.year
dim_date['QUARTER'] = dim_date['date'].dt.quarter
dim_date['MONTH'] = dim_date['date'].dt.month
dim_date['MONTH_NAME'] = dim_date['date'].dt.strftime('%B')
dim_date['DAY'] = dim_date['date'].dt.day
dim_date['DAY_NAME'] = dim_date['date'].dt.strftime('%A')
dim_date['HOUR'] = dim_date['date'].dt.hour
dim_date['DATE_ISO_FORMAT'] = dim_date['date'].apply(lambda x: x.isoformat())
dim_date['DATE_ID'] = dim_date['date'].dt.strftime('%Y%m%d%H')
dim_date['WEEK_OF_THE_MONTH'] = dim_date['date'].apply(week_of_month)
dim_date['WEEK_OF_THE_YEAR'] = dim_date['date'].dt.strftime('%U')

new_order = ['DATE_ID', 'DATE_ISO_FORMAT','YEAR','QUARTER','MONTH','DAY','HOUR','MONTH_NAME','DAY_NAME','WEEK_OF_THE_YEAR','WEEK_OF_THE_MONTH']
dim_date = dim_date[new_order]

## Location dimension
dim_location = df[['BOROUGH', 'ZIP CODE', 'LATITUDE', 'LONGITUDE', 'ON STREET NAME',
    'CROSS STREET NAME', 'OFF STREET NAME']].drop_duplicates()

dim_location['LOCATION_ID'] =  range(1, len(dim_location) + 1)

dim_location = dim_location[['LOCATION_ID', 'BOROUGH', 'ZIP CODE', 'LATITUDE', 'LONGITUDE', 'ON STREET NAME',
    'CROSS STREET NAME', 'OFF STREET NAME']]

dim_location = dim_location.rename(columns={
    'ZIP CODE': 'ZIPCODE',
    'ON STREET NAME': 'ON_STREET_NAME',
    'CROSS STREET NAME': 'CROSS_STREET_NAME',
    'OFF STREET NAME': 'OFF_STREET_NAME'
    })

## Fact table

df['DATE_ID'] = df['CRASH DATETIME'].dt.strftime('%Y%m%d%H')
vehicle_map = dim_vehicle.set_index('VEHICLE_TYPE')['VEHICLE_ID'].to_dict()

for col in vehicle_cols:
  df[col] = df[col].map(vehicle_map).astype('Int16')

factor_map = dim_factor.set_index('CONTRIBUTING_FACTOR')['FACTOR_ID'].to_dict()

for col in factor_cols:
  df[col] = df[col].map(factor_map).astype('Int8')

fact_table = df.copy()

fact_table = fact_table.rename(columns={
    'ZIP CODE': 'ZIPCODE',
    'ON STREET NAME': 'ON_STREET_NAME',
    'CROSS STREET NAME': 'CROSS_STREET_NAME',
    'OFF STREET NAME': 'OFF_STREET_NAME'
    })

fact_table = fact_table.merge(dim_location, on=['BOROUGH', 'ZIPCODE', 'LATITUDE', 'LONGITUDE',
                                      'ON_STREET_NAME', 'CROSS_STREET_NAME', 'OFF_STREET_NAME'],
                                  how='left')

fact_table['FACT_ID'] =  range(1, len(fact_table) + 1)

fact_table = fact_table[['FACT_ID', 'DATE_ID','LOCATION_ID', 'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED', 'NUMBER OF PEDESTRIANS INJURED',
                      'NUMBER OF PEDESTRIANS KILLED', 'NUMBER OF CYCLIST INJURED', 'NUMBER OF CYCLIST KILLED',
                      'NUMBER OF MOTORIST INJURED', 'NUMBER OF MOTORIST KILLED', 'CONTRIBUTING FACTOR VEHICLE 1',
                      'CONTRIBUTING FACTOR VEHICLE 2', 'CONTRIBUTING FACTOR VEHICLE 3', 'CONTRIBUTING FACTOR VEHICLE 4',
                      'CONTRIBUTING FACTOR VEHICLE 5', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2',
                      'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5']]

fact_table = fact_table.rename(columns={
    'NUMBER OF PERSONS INJURED':'NUMBER_PERSONS_INJURED', 'NUMBER OF PERSONS KILLED':'NUMBER_PERSONS_KILLED',
    'NUMBER OF PEDESTRIANS INJURED':'NUMBER_PEDESTRIANS_INJURED', 'NUMBER OF PEDESTRIANS KILLED':'NUMBER_PEDESTRIANS_KILLED',
    'NUMBER OF CYCLIST INJURED':'NUMBER_CYCLISTS_INJURED', 'NUMBER OF CYCLIST KILLED':'NUMBER_CYCLISTS_KILLED',
    'NUMBER OF MOTORIST INJURED':'NUMBER_MOTORISTS_INJURED', 'NUMBER OF MOTORIST KILLED':'NUMBER_MOTORISTS_KILLED',
    'CONTRIBUTING FACTOR VEHICLE 1':'FACTOR1_ID', 'CONTRIBUTING FACTOR VEHICLE 2':'FACTOR2_ID', 'CONTRIBUTING FACTOR VEHICLE 3':'FACTOR3_ID',
    'CONTRIBUTING FACTOR VEHICLE 4':'FACTOR4_ID', 'CONTRIBUTING FACTOR VEHICLE 5':'FACTOR5_ID',
    'VEHICLE TYPE CODE 1':'VEHICLE1_ID', 'VEHICLE TYPE CODE 2':'VEHICLE2_ID', 'VEHICLE TYPE CODE 3':'VEHICLE3_ID',
    'VEHICLE TYPE CODE 4':'VEHICLE4_ID', 'VEHICLE TYPE CODE 5': 'VEHICLE5_ID'
})

# Loading the data into snowflake



from sqlalchemy import create_engine
from snowflake.connector.pandas_tools import pd_writer


with open('snowflake.json') as f:
    snowflake_con = json.load(f)
    
# Create connection to Snowflake using your account and user
account_identifier = snowflake_con['account_identifier']
user = snowflake_con['user']
password = snowflake_con['password']
warehouse = snowflake_con['warehouse']
database = snowflake_con['database']
schema = snowflake_con['schema']

# Enhanced connection string including warehouse, database, and schema
conn_string = f"snowflake://{user}:{password}@{account_identifier}/{database}/{schema}?warehouse={warehouse}"

engine = create_engine(conn_string)
connection = engine.connect()

sql = "SELECT * FROM FACTS_COLLISIONS LIMIT 100"

try:
    connection.execute(sql)
finally:
    connection.close()
    engine.dispose()

dim_vehicle.to_sql('DIM_VEHICLE', con=engine, index=False, if_exists='append', method=pd_writer)

# Close the engine
engine.dispose()
print('dim vehicle uploaded')
dim_factor.to_sql('DIM_FACTOR', con=engine, index=False, if_exists='append', method=pd_writer)

# Close the engine
engine.dispose()
print('dim factor uploaded')

dim_date.to_sql('DIM_DATE', con=engine, index=False, if_exists='append', method=pd_writer)

# Close the engine
engine.dispose()
print('dim date uploaded')

dim_location.to_sql('DIM_LOCATION', con=engine, index=False, if_exists='append', method=pd_writer)

# Close the engine
engine.dispose()
print('dim location uploaded')

fact_table.to_sql('FACTS_COLLISIONS', con=engine, index=False, if_exists='append', method=pd_writer)

# Close the engine
engine.dispose()
print('fact table uploaded')


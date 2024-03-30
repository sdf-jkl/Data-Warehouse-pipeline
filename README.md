# Data-Warehouse-homework
## Intro

I decided to work on a NYC Data Collision Dataset because I want to get my drivers license soon and I thought it would be fun to explore different car crash statistics before I start driving.

The dataset is part of the NYC Opendata and it contains statistics on car crashes that happened in NYC. \
Link for the dataset is here: \
https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data

It is 2.08M rows and 29 columns. \
Link for the data dictionary: \
https://data.cityofnewyork.us/api/views/h9gi-nx95/files/bd7ab0b2-d48c-48c4-a0a5-590d31a3e120?download=true&filename=MVCollisionsDataDictionary_20190813_ERD.xlsx

## Part 1 - Data modelling

So to start I looked into the dataset dictionary to understand data and prepare for data warehouse modelling. \
I decided to start with facts and it was easy. Those were all quantifiable and aggrable columns. \
Else I separated into dimension tables of their own. \
You can see how I did it here:
![image](https://github.com/sdf-jkl/Data-Warehouse-homework/assets/33369833/d6e2e284-5be4-4531-8252-54b5062abe66)

Next step was to prepare schema. I used dbschema for this task.

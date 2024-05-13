CREATE SCHEMA NYC_CAR_CRASHES_SCHEMA;

CREATE  TABLE "NYC_CRASHES_DW_SNOWFLAKE".NYC_CAR_CRASHES_SCHEMA.DIM_DATE ( 
	DATE_ID              integer NOT NULL   ,
	DATE_ISO_FORMAT      datetime    ,
	YEAR                 integer    ,
	QUARTER              integer    ,
	MONTH                integer    ,
	DAY                  integer    ,
	HOUR                 integer    ,
	MONTH_NAME           varchar(100)    ,
	DAY_NAME             varchar(100)    ,
	WEEK_OF_THE_YEAR     integer    ,
	WEEK_OF_THE_MONTH    integer    ,
	CONSTRAINT PK_DIM_DATE PRIMARY KEY ( DATE_ID )
 );

CREATE  TABLE "NYC_CRASHES_DW_SNOWFLAKE".NYC_CAR_CRASHES_SCHEMA.DIM_FACTOR ( 
	FACTOR_ID            integer NOT NULL   ,
	CONTRIBUTING_FACTOR  varchar(255)    ,
	CONSTRAINT PK_DIM_FACTOR PRIMARY KEY ( FACTOR_ID )
 );

CREATE  TABLE "NYC_CRASHES_DW_SNOWFLAKE".NYC_CAR_CRASHES_SCHEMA.DIM_LOCATION ( 
	LOCATION_ID          integer NOT NULL   ,
	BOROUGH              varchar(15)    ,
	ZIPCODE              integer    ,
	LATITUDE             double    ,
	LONGITUDE            double    ,
	ON_STREET_NAME       varchar(100)    ,
	CROSS_STREET_NAME    varchar(100)    ,
	OFF_STREET_NAME      varchar(100)    ,
	CONSTRAINT PK_DIM_LOCATION PRIMARY KEY ( LOCATION_ID )
 );

CREATE  TABLE "NYC_CRASHES_DW_SNOWFLAKE".NYC_CAR_CRASHES_SCHEMA.DIM_VEHICLE ( 
	VEHICLE_ID           integer NOT NULL   ,
	VEHICLE_TYPE         varchar(255)    ,
	CONSTRAINT PK_DIM_VEHICLE PRIMARY KEY ( VEHICLE_ID )
 );

CREATE  TABLE "NYC_CRASHES_DW_SNOWFLAKE".NYC_CAR_CRASHES_SCHEMA.FACTS_COLLISIONS ( 
	FACT_ID              integer NOT NULL   ,
	NUMBER_PERSONS_INJURED integer    ,
	NUMBER_PERSONS_KILLED integer    ,
	NUMBER_PEDESTRIANS_INJURED integer    ,
	NUMBER_PEDESTRIANS_KILLED integer    ,
	NUMBER_CYCLISTS_INJURED integer    ,
	NUMBER_CYCLISTS_KILLED integer    ,
	NUMBER_MOTORISTS_INJURED integer    ,
	NUMBER_MOTORISTS_KILLED integer    ,
	DATE_ID              integer    ,
	LOCATION_ID          integer    ,
	FACTOR1_ID           integer    ,
	FACTOR2_ID           integer    ,
	FACTOR3_ID           integer    ,
	FACTOR4_ID           integer    ,
	FACTOR5_ID           integer    ,
	VEHICLE1_ID          integer    ,
	VEHICLE2_ID          integer    ,
	VEHICLE3_ID          integer    ,
	VEHICLE4_ID          integer    ,
	VEHICLE5_ID          integer    ,
	CONSTRAINT PK_FACTS_COLLISIONS PRIMARY KEY ( FACT_ID )
 );


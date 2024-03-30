CREATE SCHEMA nyc_car_crashes_schema;

CREATE TABLE nyc_car_crashes_schema.dim_date ( 
	date_id              integer  NOT NULL  ,
	date_original_format date    ,
	date_iso_format      date    ,
	"year"               integer    ,
	quarter              integer    ,
	"month"              integer    ,
	"day"                integer    ,
	"hour"               integer    ,
	month_name           varchar(100)    ,
	day_name             varchar(100)    ,
	week_of_the_year     integer    ,
	week_of_the_month    integer    ,
	CONSTRAINT pk_dim_date PRIMARY KEY ( date_id )
 );

CREATE TABLE nyc_car_crashes_schema.dim_factor ( 
	factor_id            integer  NOT NULL  ,
	contributing_factor  varchar(255)    ,
	CONSTRAINT pk_dim_factor PRIMARY KEY ( factor_id )
 );

CREATE TABLE nyc_car_crashes_schema.dim_location ( 
	location_id          integer  NOT NULL  ,
	borough              varchar(15)    ,
	zipcode              integer    ,
	latitude             double precision    ,
	longtitude           double precision    ,
	on_street_name       varchar(100)    ,
	cross_street_name    varchar(100)    ,
	off_street_name      varchar(100)    ,
	CONSTRAINT pk_dim_location PRIMARY KEY ( location_id )
 );

CREATE TABLE nyc_car_crashes_schema.dim_vehicle ( 
	vehicle_id           integer  NOT NULL  ,
	vehicle_type         varchar(255)    ,
	CONSTRAINT pk_dim_vehicle PRIMARY KEY ( vehicle_id )
 );

CREATE TABLE nyc_car_crashes_schema.facts_collisions ( 
	fact_id              bigint  NOT NULL  ,
	number_persons_injured integer    ,
	number_persons_killed integer    ,
	number_pedestrians_injured integer    ,
	number_pedestrians_killed integer    ,
	number_cyclists_injured integer    ,
	number_cyclists_killed integer    ,
	number_motorists_injured integer    ,
	number_motorists_killed integer    ,
	date_id              integer    ,
	location_id          integer    ,
	factor1_id           integer    ,
	factor2_id           integer    ,
	factor3_id           integer    ,
	factor4_id           integer    ,
	factor5_id           integer    ,
	vehicle1_id          integer    ,
	vehicle2_id          integer    ,
	vehicle3_id          integer    ,
	vehicle4_id          integer    ,
	vehicle5_id          integer    ,
	CONSTRAINT pk_facts_collisions PRIMARY KEY ( fact_id )
 );


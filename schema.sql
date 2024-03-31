-- public.home definition

-- Drop table

-- DROP TABLE home;

CREATE TABLE home (
	id serial4 NOT NULL,
	"date" timestamp NOT NULL,
	CONSTRAINT home_date_key UNIQUE (date),
	CONSTRAINT home_pkey PRIMARY KEY (id)
);


-- public.floor definition

-- Drop table

-- DROP TABLE floor;

CREATE TABLE floor (
	id serial4 NOT NULL,
	n int4 NOT NULL,
	home_id int4 NULL,
	CONSTRAINT floor_pkey PRIMARY KEY (id),
	CONSTRAINT floor_home_id_fkey FOREIGN KEY (home_id) REFERENCES home(id)
);


-- public.apart definition

-- Drop table

-- DROP TABLE apart;

CREATE TABLE apart (
	id serial4 NOT NULL,
	n int4 NOT NULL,
	floor_id int4 NULL,
	CONSTRAINT apart_pkey PRIMARY KEY (id),
	CONSTRAINT apart_floor_id_fkey FOREIGN KEY (floor_id) REFERENCES floor(id)
);


-- public.wind definition

-- Drop table

-- DROP TABLE wind;

CREATE TABLE wind (
	id serial4 NOT NULL,
	n int4 NOT NULL,
	apart_id int4 NULL,
	CONSTRAINT wind_pkey PRIMARY KEY (id),
	CONSTRAINT wind_apart_id_fkey FOREIGN KEY (apart_id) REFERENCES apart(id)
);
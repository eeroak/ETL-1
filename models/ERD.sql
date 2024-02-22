-- Script for creating the ERD model for the Electric Vehicle Population Data

BEGIN;


CREATE TABLE IF NOT EXISTS public."Electric_Vehicle_Population_Data"
(
    "VIN (1-10) " text COLLATE pg_catalog."default",
    "County               " text COLLATE pg_catalog."default",
    "City                     " text COLLATE pg_catalog."default",
    "State " text COLLATE pg_catalog."default",
    "Postal Code " text COLLATE pg_catalog."default",
    "Model Year " bigint,
    "Make                 " text COLLATE pg_catalog."default",
    "Model                    " text COLLATE pg_catalog."default",
    "Electric Vehicle Type                  " text COLLATE pg_catalog."default",
    "Clean Alternative Fuel Vehicle (CAFV) Eligibility            " text COLLATE pg_catalog."default",
    "Electric Range " bigint,
    "Base MSRP " bigint,
    "Legislative District " text COLLATE pg_catalog."default",
    "DOL Vehicle ID " bigint,
    "Vehicle Location                  " text COLLATE pg_catalog."default",
    "Electric Utility                                               " text COLLATE pg_catalog."default",
    "2020 Census Tract" text COLLATE pg_catalog."default"
);
END;
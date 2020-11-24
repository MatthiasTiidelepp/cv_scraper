This scraper requires a previously created database

Below are the commands I used in MySQL Workbench to create the requisite database

**
CREATE DATABASE db_listing;

USE db_listing;

CREATE TABLE listing (
    added VARCHAR(50),
    position VARCHAR(50),
    company VARCHAR(50),
    link VARCHAR(250),
    PRIMARY KEY (added, position)
);
**
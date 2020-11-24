### This scraper requires MySQL Python connector, BeautifulSoup and a previously created database


- **This video shows how to set up MySQL with Python**
[Python MySQL Tutorial - Setup & Basic Queries (w/ MySQL Connector)](https://www.youtube.com/watch?v=3vsC05rxZ8c)

- **To install BeautifulSoup and requests type into console**
```
pip install beautifulsoup4
pip install requests
```

- **Below are the commands I used in MySQL Workbench to create the requisite database**
```
CREATE DATABASE db_listing;

USE db_listing;

CREATE TABLE listing (
	added VARCHAR(50),
	position VARCHAR(50),
	company VARCHAR(50),
	link VARCHAR(250),
	PRIMARY KEY (added, position)
);
```
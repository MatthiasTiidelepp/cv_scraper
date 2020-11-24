import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime, timedelta

result = requests.get("https://cv.ee/search?limit=20&offset=0&categories%5B0%5D=INFORMATION_TECHNOLOGY&towns%5B0%5D=314&isHourlySalary=false")
src = result.content
soup = BeautifulSoup(src, 'html.parser')


db = mysql.connector.connect(
	host="localhost",
	user="matthias",
	passwd="matthias",
	database="db_listings"
	)

mycursor = db.cursor()

# Command for inserting scraped data into listing table. Ignores 'duplicate entry' errors
Q1 = "INSERT IGNORE INTO listing (added, position, company, link) VALUES (%s,%s,%s,%s)"


for class_tag in soup.find_all("div", class_="jsx-1471379408 vacancy-item__content"):
	link = "https://cv.ee" + class_tag.find('a').attrs["href"]
	position = class_tag.find("span", class_="jsx-1471379408 vacancy-item__title").text
	company = class_tag.find("div", class_="jsx-1471379408 vacancy-item__info-main").text.split('—')[0][:-1]
	added_temp = class_tag.find("span", class_="jsx-1471379408 secondary-text").text
	
	# If added_temp contains "tund", listing was added today. If it contains "üks" and not "tund",
	# listing was added 1 day ago. If it does not contain either of those, listing was added more than
	# 1 days ago.
	if("tund" in added_temp):
		added = datetime.today().strftime("%d-%m-%Y")
	elif(added_temp.split(" ")[-3] == "üks"):
		added = datetime.today() - timedelta(days=1)
		added = added.strftime("%d-%m-%Y")
	else:
		added = datetime.today() - timedelta(days=int(added_temp.split(" ")[-3]))
		added = added.strftime("%d-%m-%Y")

	# Add scraped data to SQL database
	mycursor.execute(Q1, (added, position, company, link))

db.commit()
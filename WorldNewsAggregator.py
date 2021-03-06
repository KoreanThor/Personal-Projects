#!/usr/bin/python3

#Python World News Scraper

import requests
import html5lib
from bs4 import BeautifulSoup
import sys
import urllib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import csv

now = datetime.now()
stdoutOrigin = sys.stdout
response2 = requests.get("https://www.bbc.com/news/world")
response3 = requests.get("https://www.npr.org/sections/world")
response4 = requests.get("https://www.apnews.com/hub/ap-top-news")
response5 = requests.get("https://www.washingtonpost.com/world/?hp_top_nav_world")
response7 = requests.get("https://abcnews.go.com/International")
soup2 = BeautifulSoup(response2.text, "html.parser")
soup3 = BeautifulSoup(response3.text, "html.parser")
soup4 = BeautifulSoup(response4.text, "html.parser")
soup5 = BeautifulSoup(response5.text, "html.parser")
soup7 = BeautifulSoup(response7.text, "html.parser")
bbc_stories1 = soup2.find_all("div", {"class": "gs-c-promo"})
npr_stories = soup3.find_all("div", {"class": "item-info-wrap"})
apnews_stories = soup4.find_all("div", {"class": "FeedCard"})
wpnews_stories = soup5.find_all("div", {"class": "col-lg-8"})
abc_stories1 = soup7.find_all("li", {"class": "LatestHeadlines__item"})
abc_stories2 = soup7.find_all("div", {"class": "ContentList__Item"})
article_ctr = 0

sys.stdout = open("World_News.txt", "w+") #Creates a new text file with the contents of the news articles. 

#Output to World_News.txt
print("\nBBC News:")
for story in bbc_stories1:
	headline = story.find("h3")
	article_ctr += 1
	print("{}." .format(article_ctr) + headline.text)
	link = story.find("a")
	print("www.bbc.com" + link["href"])
	summary = story.find("p")
	if summary:
		print(summary.text)

print("\nNPR News:")
for story in npr_stories:
	headline = story.find("h2")
	article_ctr += 1
	print("{}." .format(article_ctr) + headline.text)
	link = story.find("a")
	print(link["href"])
	summary = story.find("p", {"class": "teaser"})
	if summary:
		print(summary.text)

print("\nAP News:")
for story in apnews_stories:
	headline = story.find("h3")
	article_ctr += 1
	print("{}." .format(article_ctr) + headline.text)
	link = story.find("a")
	print("www.apnews.com" + link["href"])
	summary = story.find("p")
	if summary: 
		print(summary.text)

print("\nWashington Post News:")
for story in wpnews_stories:
	headline = story.find("a")
	article_ctr += 1
	print("{}." .format(article_ctr) + headline.text)
	link = story.find("a")
	print(link["href"])
	summary = story.find("div", {"class": "blurb"})
	if summary:
		print(summary.text)

print("\nABC News:")
for story in abc_stories1:
	headline = story.find("h4")
	article_ctr += 1
	print("{}." .format(article_ctr) + headline.text)
	link = story.find("a")
	print(link["href"])
	summary = story.find("p")
	if summary:
		print(summary.text)

for story in abc_stories2:
	headline = story.find("h2")
	article_ctr += 1
	print("{}." .format(article_ctr) + headline.text)
	link = story.find("a")
	print(link["href"])
	summary = story.find("p")
	if summary:
		print(summary.text)


 # SEND ALL NEWS THROUGH EMAIL
fromaddr = "type sender email address here" # HIDE IF USING REPLIT OR OTHER PUBLIC SITES
toaddr = "type receiving email address here" # HIDE IF USING REPLIT OR OTHER PUBLIC SITES
msg = MIMEMultipart()
msg["From"] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Top World News From: " + now.strftime("%m/%d/%Y %I:%M:%S %p")
body = "The text file attached includes top world news from BBC, NPR, AP News, Washington Post and ABC News."
msg.attach(MIMEText(body,"plain"))
filename = "World_News.txt" #File name can be changed
attachment = open(r"/file/path/to/World_News.txt", "rb") #Be sure the file name from above matches the file name in the file path
p = MIMEBase("application", "octet-stream")
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header("Content-Disposition", "attachment; filename= %s" % filename)
msg.attach(p)
sender_email_id = "type your sender email address here" # Add your sending email. Be sure to hide this if you are uploading this publicly.
sender_email_id_password = "type your sender email address password here" # Add your sending email's password. Be sure to hide this if you are uploading this publicly.
s = smtplib.SMTP("smtp.gmail.com", 587) # Need to turn on "less secure apps" for gmail, can be replaced with any other email service.(NEED TO FIND A WAY TO CONNECT SECURELY IF POSSIBLE)
s.starttls()
s.login(fromaddr, sender_email_id_password)
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()

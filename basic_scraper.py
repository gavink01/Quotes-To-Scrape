import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(website.text, 'html.parser')
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})
tags = soup.findAll("a", attrs={"class":"tag"})
top_tags = soup.findAll("span", attrs={"class":"tag-item"})

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    
print("-----------------------------------------")
for author in authors:
    print(author.text)
print("-----------------------------------------")
for tag in tags:
    print(tag.text)
print("-----------------------------------------")
print("Top 10 Tags:")
for tag in top_tags:
    print(tag.text)
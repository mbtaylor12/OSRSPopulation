from lxml import html
import requests
import re
import datetime
import sqlite3
from sqlite3 import Error

page = requests.get('http://oldschool.runescape.com')
tree = html.fromstring(page.content)

sentence = tree.xpath('//*[@id="os-home"]/div/div/main/p/text()')

players = str(re.search(r'\d+,\d+', str(sentence)).group())

players = players.replace(',', '')

date = datetime.datetime.now().strftime('%Y-%m-%d')
time = datetime.datetime.now().strftime('%H:%M')

conn = sqlite3.connect('population.db')
c = conn.cursor()

query = "INSERT INTO Population VALUES('" + date + "','" + time + "','" + players + "')" 

c.execute(query)
conn.commit()
conn.close()

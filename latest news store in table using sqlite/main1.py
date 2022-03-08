import sqlite3
conn=sqlite3.connect('employe.db')
c=conn.cursor()
c.execute("""CREATE TABLE employes(
    first text
        )""")
import re
import time
import requests
from bs4 import BeautifulSoup
URL ="https://news.google.com/search?q=latest%20updates&hl=en-IN&gl=IN&ceid=IN%3Aen"
r = requests.get(URL)
   
soup = BeautifulSoup(r.text, 'lxml')
while(True):

	for table in soup.find_all('h3'):
		as1=table.text.strip()
		as1=re.sub(r"[^a-zA-Z0-9,: ]", "",as1)
	
		c.execute("INSERT INTO employes VALUES ('{}')".format(as1))
	c.execute("SELECT * FROM employes")
	data = c.fetchall()
	for row in data:
		print(row)
	time.sleep(900)
conn.commit()
conn.close()

import requests
from bs4 import BeautifulSoup
import csv
   
URL ="https://news.google.com/search?q=content&hl=en-IN&gl=IN&ceid=IN%3Aen"
r = requests.get(URL)
   
soup = BeautifulSoup(r.text, 'lxml')
a="/n   "
quotes=[]  # a list to store quotes
file1 = open("myfile.txt","a")
for table in soup.find_all('h3'):
	s=table.text.strip()
	print() 
	file1.writelines(s)
	file1.writelines(a)
file1.close()
  
# Append-adds at last

file1 = open("myfile.txt","r")
print("Output of Readlines after appending") 
print(file1.readlines())
print()
file1.close()
  

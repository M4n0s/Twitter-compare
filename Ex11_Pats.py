from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import urllib2

class MyHtml(HTMLParser):
	def handle_data(self, data):
		if k==0:
			y.append(data)
		else:
			x.append(data)

first_name=raw_input("Give an excisting Twitter name>")
second_name=raw_input("Give another one>")
link1="https://twitter.com/"+first_name
link2="https://twitter.com/"+second_name
url1=urllib2.urlopen(link1)
url2=urllib2.urlopen(link2)

soup1=BeautifulSoup(url1.read())
value1=soup1.findAll("span", {"class": "ProfileNav-value"})

soup2=BeautifulSoup(url2.read())
value2=soup2.findAll("span", {"class": "ProfileNav-value"})

x=[]
y=[]
k=0
for i in range(4):
	MyHtml.feed(str(value1[i]))
	
k=1
for i in range(4):
	MyHtml.feed(str(value2[i]))

score1=0
score2=0
for i in range(4):
	if x[i]>y[i]:
		score1+=1
	elif x[i]<y[i]:
		score2+=1
		
print "first_name", score1,"-",score2 ,"second_name"
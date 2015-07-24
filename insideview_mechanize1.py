import mechanize 
import time
import csv
from BeautifulSoup import BeautifulSoup
import MySQLdb as mysql
import random

user = 'root'
password = 'root'
database_name = 'insideview'
port = '127.0.0.1'

def insert(name,title,company,tel,email,location,url,linkedin,companyId,jobFunction,jobLevel):    
    con = mysql.connect(port,user,password,database_name)
    cur = con.cursor()
    cur.execute('INSERT INTO insideviewdb(name,title,company,tel,email,location,url,linkedin,companyId,jobFunction,jobLevel) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(name,title,company,tel,email,location,url,linkedin,companyId,jobFunction,jobLevel))
    con.commit()
    con.close()
    return

def getLinks():
	con = mysql.connect(port,user,password,database_name)
	cur = con.cursor()
	cur.execute('select * from input_links')
	allrow = cur.fetchall()
	return allrow

def extracted(employmentId,companyId,jobFunction,jobLevel):
	con = mysql.connect(port,user,password,database_name)
	cur = con.cursor()
	cur.execute('INSERT INTO extracted_links(employmentId,companyId,jobFunction,jobLevel) VALUES(%s,%s,%s,%s)',(employmentId,companyId,jobFunction,jobLevel))
	con.commit()
	con.close()
	return



	

br = mechanize.Browser()

br.open('https://my.insideview.com/iv/welcome.do;jsessionid=4AE00087303B87291CCE292BA975F16F') 
time.sleep(5)
br.select_form( name="loginForm" ) 
# these two come from the code you posted
# where you would normally put in your username and password
br[ "userId" ] = "deler.john@linuxmail.org"
br[ "password" ] = "Deler@john1"
res = br.submit() 

print "Success!\n"

result = getLinks()
length =  len(result)

for i in range(1,length/2):#(length/2+1,length):
	randomNumber = random.randrange(3,6)
	print 'waiting........'+str(randomNumber)
	time.sleep(randomNumber)
	try:
		employmentId = str(result[i][0])
		companyId 	= str(result[i][1])
		jobFunction = str(result[i][2])
		jobLevel 	= str(result[i][3])

		url = 'https://my.insideview.com/iv/executiveinfo.do?methodToCall=overview&id='+employmentId

		url_id = url.split('=')[2]
		obj = br.open(url) 
		html = obj.read() 

		soup = BeautifulSoup(html.encode('utf-8'))
	except Exception,e:
		extracted(employmentId,companyId,jobFunction,jobLevel)
		continue

	

	try:
		name = soup.find('h1',{'class':'primary_header_1 emp-name'}).text.replace('\n','').strip()
	except Exception,e:
		name = 'N/A'
	try:
		title = soup.find('label',{'class':'sub-title-12'}).text.replace('\n','').strip()
	except Exception,e:
		title = 'N/A'
	try:
		company = soup.find('div',{'class':'company-name'}).text.replace('\n','').strip()
	except Exception,e:
		company = 'N/A'
	try:
		contact = soup.find('div',{'class':'contact-details'})
		try:
			email = contact.find('a',{'class':'bluefont'}).text.replace('\n','').strip()
		except Exception,e:
			email = 'N/A'
		try:
			tel = contact.find('span',{'class':'text-content'}).text.replace('\n','').strip()
		except Exception,e:
			tel = 'N/A'
	except Exception,e:
		email = 'N/A'
		tel = 'N/A'
	try:
		linkedin = soup.find('a',{'class':'linkedinView'})['href']
	except Exception,e:
		linkedin = 'N/A'
	try:
		location = soup.find('div',{'class':'company-loc'}).text.replace('\n','').strip()
	except Exception,e:
		location = 'N/A'

	print url_id
	# print name,title,company,email,tel,location,linkedin
	insert(name,title,company,tel,email,location,employmentId,linkedin,companyId,jobFunction,jobLevel)
	extracted(employmentId,companyId,jobFunction,jobLevel)

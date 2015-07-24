import mechanize 
import time
import csv
from BeautifulSoup import BeautifulSoup
import MySQLdb as mysql
import random   

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
for i in csv.reader(open('company_urls_to_extract.csv','rb')):
    companyName =  str(i[1])+'~'+str(i[0].split('=')[-1])
    obj = br.open(i[0]) 
    html = obj.read()
    print i[1]
    f = open('./Dump/' +str(companyName) + '.json', 'wb')
    f.write(html)
    f.close
    time.sleep(2)
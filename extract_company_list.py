"""This code developed by manoj Prajapati"""
import selenium
import csv
import BeautifulSoup as BeautifulSoup
from selenium import webdriver
import MySQLdb as mysql 
import time

driver = webdriver.Chrome()

driver.get('https://my.insideview.com/iv/logout.do')

userId = "deler.john@linuxmail.org"
pwd = "Deler@john1"

c = csv.writer(open('company_list.csv','w'))
username = driver.find_element_by_xpath('//*[@id="userId"]')
username.send_keys(userId)


password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(pwd)

signin = driver.find_element_by_xpath('//*[@id="pwd-login"]/div[1]/div[2]/input')
signin.click()
time.sleep(3)

driver.get('https://my.insideview.com/iv/loadListBuildPage.iv#/loadListBuildPage.iv?vs=CF')
time.sleep(5)

inputText = raw_input('Please check the inputs')

counter = 1
while 1:
	counter +=1
	print counter
	for val in range(20):
		try:
			name_obj  = driver.find_element_by_xpath('//*[@id="companyGrid"]/div/div[3]/div/div['+str(val+1)+']/div[1]/div')
			name = str(name_obj.text).encode('utf-8')
		except Exception ,e:
			name = ''
		try:
			href = name_obj.find_element_by_css_selector('a').get_attribute('href')
		except Exception,e:
			href = ''
		print name+'|'+href
		c.writerow([name,href])

	
	try:
		driver.find_element_by_link_text(str(counter)).click()
	except Exception,e:
		driver.find_element_by_partial_link_text('Next').click()
		time.sleep(3)
		continue
	time.sleep(3)
print "end of the program"
	


import simplejson as json
import csv
import MySQLdb as mysql
import os

user = 'root'
password = 'root'
database_name = 'insideview'
port = '127.0.0.1'

def insert(count,name,execFirstName,execLastName,execEmail,title,employmentId,companyId,executiveId,employmentType,jobFunctionDisplayName,ckName,jobLevel,jobLevelDisplayName,jobFunction):    
       con = mysql.connect(port,user,password,database_name)
       cur = con.cursor()
       cur.execute('INSERT INTO Company_links(count,name,execFirstName,execLastName,execEmail,title,employmentId,companyId,executiveId,employmentType,jobFunctionDisplayName,ckName,jobLevel,jobLevelDisplayName,jobFunction) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(count,name,execFirstName,execLastName,execEmail,title,employmentId,companyId,executiveId,employmentType,jobFunctionDisplayName,ckName,jobLevel,jobLevelDisplayName,jobFunction))
       con.commit()
       con.close()
       return

dr = "Dump\\"

dirs=os.listdir(dr)
for fil in dirs:
       filful=dr+fil
       print filful
       _file = open(filful)
       json_data =  _file.read()


       jsonFile = json.loads(json_data)
       totalCount =  jsonFile['totalCount']
       if int(totalCount) == 0:
              continue

       counter = 0
       for i in range(int(totalCount)):
              counter += 1 
              try:
                     count               =   str(jsonFile['executiveInfos'][i]['count']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     count = 'N/A'
              try:
                     employmentId =      str(jsonFile['executiveInfos'][i]['employmentId']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     employmentId = 'N/A'
              try:
                     executiveId         =   str(jsonFile['executiveInfos'][i]['executiveId']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     executiveId = 'N/A'
              try:
                     name                =   str(jsonFile['executiveInfos'][i]['name']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     name = 'N/A'
              try:
                     execFirstName       =   str(jsonFile['executiveInfos'][i]['execFirstName']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     execFirstName = 'N/A'
              try:
                     execLastName        =   str(jsonFile['executiveInfos'][i]['execLastName']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     execLastName = 'N/A'
              try:
                     companyId           =   str(jsonFile['executiveInfos'][i]['companyId']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     companyId = 'N/A'
              try:
                     employmentType      =   str(jsonFile['executiveInfos'][i]['employmentType']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     employmentType = 'N/A'
              try:
                     title               =   str(jsonFile['executiveInfos'][i]['title']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     title = 'N/A'
              try:
                     jobFunctionDisplayName = str('|'.join(jsonFile['executiveInfos'][i]['jobFunctionDisplayName'])).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     jobFunctionDisplayName = 'N/A'
              try:
                     execEmail       =   str(jsonFile['executiveInfos'][i]['execEmail']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     execEmail = 'N/A'
              try:
                     ckName          =   str(jsonFile['executiveInfos'][i]['ckName']).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     ckName = 'N/A'
              try:
                     jobLevel            =   str('|'.join(jsonFile['executiveInfos'][i]['jobLevel'])).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     jobLevel = 'N/A'
              try:
                     jobLevelDisplayName =   str('|'.join(jsonFile['executiveInfos'][i]['jobLevelDisplayName'])).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     jobLevelDisplayName = 'N/A'
              try:
                     jobFunction         =   str('|'.join(jsonFile['executiveInfos'][i]['jobFunction'])).encode('utf-8','ignore').encode('ascii','replace')
              except Exception,e:
                     jobFunction = 'N/A'
              print executiveId,counter
              try:
                     insert(count,name,execFirstName,execLastName,execEmail,title,employmentId,companyId,executiveId,employmentType,jobFunctionDisplayName,ckName,jobLevel,jobLevelDisplayName,jobFunction)
                     # pint "Hello"
              except Exception,e:
                     continue

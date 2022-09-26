import os
import requests
import sys

def retrive_html():
 for year in range(2013,2019):
     for month in range(1,13):
         #giving html url form where we to retrive the data
         if (month<10):
             url='https://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month,year)
         else:
             url='https://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month,year)
             
         texts=requests.get(url)
         #encoding the url with utf-8
         text_utf=texts.text.encode('utf=8')
      
        #specifying the folder where to save the html
         if not os.path.exists('data/html_data/{}'.format(year)):
             os.makedirs('data/html_data/{}'.format(year))
         with open('data/html_data/{}/{}.html'.format(year,month),'wb') as output:
             output.write(text_utf)
     sys.stdout.flush()
     
#to run
if __name__=='__main__':
    retrive_html()
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars/'
browser = webdriver.Chrome('/Users/nirvikkasula/Documents/Coding/Projects/Project 127 and 128/env/chromedriver')
browser.get(start_url)
time.sleep(15)
def scrape():
    headers = ["Name","Distance","Mass","Radius"]
    stars_data = []
    for i in range(0,97):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for ult in soup.find_all('ul',attrs = {'class','star'}):
            litags = ult.find_all('li')
            tempList = []
            for index,litag in enumerate(litags):
                if (index == 0):
                    tempList.append(litag.find_all('a')[0].contents[0])
                else:
                    try:
                        tempList.append(litag.contents[0])
                    except:
                        tempList.append('')
            
            stars_data.append(tempList)
        
    with open('scrapper1.csv','w') as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(stars_data)
scrape()

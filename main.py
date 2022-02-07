# Author Rashid Khan
# Created at 2/6/2022

import undetected_chromedriver as webdriver
from bs4 import BeautifulSoup
import pandas as pd

def main():

    # extract data from https://www.gartner.com/en/conferences/calendar
    driver1 = webdriver.Chrome(options=webdriver.ChromeOptions())   
    driver1.get('https://www.gartner.com/en/conferences/calendar')

    locations = []
    dates = []
    names = []

    content = driver1.page_source
    soup = BeautifulSoup(content, features="html.parser")
    for element in soup.findAll('div', attrs={'class': 'conference-data'}):
        location = element.find('p', attrs={'class': 'conference-location'})
        date = element.find('p', attrs={'class': 'conference-date'})
        name = element.find('p', attrs={'class': 'conference-title'})
        locations.append(location.text)
        dates.append(date.text)
        names.append(name.text)

    df = pd.DataFrame({'Location': locations, 'Date': dates, 'Name': names})
    df.to_csv('gartner-events.csv', index=False, encoding='utf-8')    
    driver1.close()

    # extract data from https://www.techmeme.com/events
    driver2 = webdriver.Chrome(options=webdriver.ChromeOptions())
    driver2.get('https://www.techmeme.com/events')

    locations = []
    dates = []
    names = []
    
    content = driver2.page_source
    soup = BeautifulSoup(content, features="html.parser")
    for element in soup.findAll('div', attrs={'class': 'rhov'}):
        location = element.findAll('div')[2]
        date = element.findAll('div')[0]
        name = element.findAll('div')[1]
        locations.append(location.text)
        dates.append(date.text)
        names.append(name.text)

    df = pd.DataFrame({'Location': locations, 'Date': dates, 'Name': names})
    df.to_csv('techmeme-events.csv', index=False, encoding='utf-8')    
    driver2.close()

    print("Done!")

if __name__ == "__main__":
    main()
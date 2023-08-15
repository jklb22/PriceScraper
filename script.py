from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from datetime import datetime

#Browser control - built on firefox
browser = webdriver.Firefox()
browser.get('https://www.amazon.com/Introduction-Quantitative-Macroeconomics-Using-State/dp/0128122196')
html = browser.page_source

soup = BeautifulSoup(html, features="html.parser")  # calling soup's html parser

price = soup.find("span", {"class": "a-offscreen"}).text  # soup sniffs out the price in the HTML

Pricing = {'Cost': [price], 'Timestamp': [datetime.now()]}  # establishing that soup's result is cost and the YYMMDD


# TODO figure out why datetime is formatting so weirdly in the csv
def repeat():
    # input your desired website here in browser.get
    browser.get('https://www.amazon.com/Introduction-Quantitative-Macroeconomics-Using-State/dp/0128122196')
    #gives the page time to load
    time.sleep(7)
    new_price = soup.find("span", {"class": "a-offscreen"}).text
    print(new_price)

    Pricing['Cost'].append(new_price)
    Pricing['Timestamp'].append(datetime.now())

    df = pd.DataFrame(Pricing)
    df.to_csv('Price_logger.csv', index=False)


while True:
    repeat()

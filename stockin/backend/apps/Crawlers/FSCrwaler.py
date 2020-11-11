import os,sys
import django
import requests
from bs4 import BeautifulSoup
import datetime
from multiprocessing import Pool, Process
from selenium import webdriver
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(BASE_DIR)
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockin.settings')
django.setup()

from apps.news.models import News
from apps.stocks.models import Stock, FinancialStat


def FSCrawler():
    driver = webdriver.PhantomJS(os.path.join(BASE_DIR, 'apps/stocks/phantomjs-2.1.1-linux/bin/phantomjs'))
   # driver = webdriver.PhantomJS(os.path.join(BASE_DIR, 'apps/stocks/phantomjs-2.1.1-macosx/bin/phantomjs')) #맥용!
    driver.implicitly_wait(2)
    
    stocks = Stock.objects.all()
    for stock in stocks:
        
        driver.get('https://stockplus.com/m/stocks/KOREA-A{}/analysis'.format(stock.code))
        time.sleep(1)
        raw = driver.page_source
        soup = BeautifulSoup(raw, 'html.parser')
        table = soup.select_one('.type02 tbody')

        for quarter, sales, operatingProfit, netIncome, operatingMargin, netProfitMargin, PER, PBR, ROE in zip(table.select('tr')[0].select('th'), table.select('tr')[1].select('td'), table.select('tr')[2].select('td'), table.select('tr')[3].select('td'), table.select('tr')[4].select('td'), table.select('tr')[5].select('td'), table.select('tr')[6].select('td'), table.select('tr')[7].select('td'), table.select('tr')[8].select('td')):
            if 'E' in quarter.text:
                break
            
            try:
                FinancialStat.objects.get(stock=stock, quarter=quarter.text.split('월')[0]+'월')
            except:
                FinancialStat(
                    stock=stock,
                    quarter=quarter.text.split('월')[0]+'월',
                    sales=sales.text.replace(',', ''),
                    operatingProfit=operatingProfit.text.replace(',', ''),
                    netIncome=netIncome.text.replace(',', ''),
                    operatingMargin=operatingMargin.text,
                    netProfitMargin=netProfitMargin.text,
                    PER=PER.text,
                    PBR=PBR.text,
                    ROE=ROE.text,
                ).save()
            

    driver.quit()     
            

if __name__ == '__main__':
    FSCrawler()
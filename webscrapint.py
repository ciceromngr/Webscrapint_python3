import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import json

url = 'https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1'
top10Ranking = {}

driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath("//button[@id='onetrust-accept-btn-handler']").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='TEAM_ABBREVIATION']").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='AGE']").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='MIN']").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()
time.sleep(3)

element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name = 'table')


df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM','AGE', 'MIN' ,'PTS']]
df.columns = ['posicion', 'jogador', 'time', 'age', 'min', 'pontos']


top10Ranking['points'] = df.to_dict('records')

driver.quit()

js = json.dumps(top10Ranking)
fp = open('ranking.json', 'w')
fp.write(js)
fp.close()

import  time
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

PROXY_SERVER ='185.20.26.41:43051'
PROXY_SERVER1 ='username:password@185.20.26.41:43051' # для авторизации в прокси

option = Options()
option.add_argument(f'--proxy-server={PROXY_SERVER}')
driver = webdriver.Chrome(options=option)

driver.get('https://2ip.ru') #178.46.109.144
time.sleep(5)



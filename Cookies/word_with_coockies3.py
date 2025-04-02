import time
import pickle
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait # будет отвечать за явные ожидания
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())#Прокидываем установку драйвера
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)



driver.get('https://www.freeconferencecall.com/ru/pl/login')
driver.delete_all_cookies()# удаляются куки чтоб применились которые мы записали
cookies = pickle.load(open(os.getcwd() + '\\cookies\\cookies.pkl', 'rb'))

for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(2)

driver.refresh() #чтобы куки применились

time.sleep(5)
#это может пригодиться чтоб не логиниться постоянно
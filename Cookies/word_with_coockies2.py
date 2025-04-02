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


LOGIN_FIELD = ('xpath', "//input[@aria-label='Введите адрес электронной почты']")
PASSWORD_FIELD = ('xpath', "//input[@id='password']")
SUBMIT_FIELD = ('xpath', "//button[@id='loginformsubmit']")
driver.get('https://www.freeconferencecall.com/ru/pl/login')
driver.find_element(*LOGIN_FIELD).send_keys('autocheck@ya.ru')
driver.find_element(*PASSWORD_FIELD).send_keys('123')
driver.find_element(*SUBMIT_FIELD).click()

pickle.dump(driver.get_cookies(), open(os.getcwd() + '\\cookies\\cookies.pkl', 'wb'))
# собираем куки логина и сохраняет в файл
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get('https://www.freeconferencecall.com/global/pl')

driver.find_element('xpath', "//a[@id='login-mobile']").click()
time.sleep(3)
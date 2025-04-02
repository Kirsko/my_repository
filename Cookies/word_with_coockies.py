import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait # будет отвечать за явные ожидания
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())#Прокидываем установку драйвера
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get('https://www.freeconferencecall.com/ru/pl/login')

# driver.add_cookie(
#     {
#         "name" : "Example",
#         "value" : "228"
#     }
# )
# print(driver.get_cookie("Example"))
before = driver.get_cookie('split')
print(before)

driver.delete_cookie('split')# delete_all_cookie
driver.add_cookie({
    'name' : 'split',
    'value' : 'ewrw'
})


after = driver.get_cookie('split')
print(after)
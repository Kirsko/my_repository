import time
#просто комментарий для удаленки
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#Класс Service отвечает за установку двайвера, за его открытие и закрытия. В Селениум4 инициализация двайвера происходит через объект Service
#service объект класса Service
#ЧЕКАЙ В НЕЙРОСЕТИ ОБЪЯСНЕНИЯ!!!1
# Создаем объект Service с автоматической установкой chromedriver
service = Service(executable_path=ChromeDriverManager().install())#Прокидываем установку дравера
# Инициализируем веб-драйвер Chrome с использованием Service
driver = webdriver.Chrome(service=service)#указываем ему тот объект, который будет управляться драйвер(браузер), передаем наш хром, инициализация драйвера

driver.get('https://yandex.com')
driver.execute_script("alert('Hello, Selenium!');")
time.sleep(4)
driver.switch_to.alert.accept()

time.sleep(10) # не использовать в автоматизации!!1
driver.back()
time.sleep(3) # не использовать в автоматизации!!1
driver.forward()
time.sleep(4)
driver.refresh()
time.sleep(3)


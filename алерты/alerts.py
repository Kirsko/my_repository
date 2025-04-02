import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait # будет отвечать за явные ожидания
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())#Прокидываем установку драйвера
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

driver.get('https://demoqa.com/alerts')

BUTTON_1 =('xpath', "//button[@id='alertButton']")
wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
alert.accept() # принятие алерта
time.sleep(3)
BUTTON_3 =('xpath', "//button[@id='confirmButton']")
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
print(alert.text) # считываем текст
alert.dismiss()# отклонение алерта
time.sleep(3)
BUTTON_4 =('xpath', "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
time.sleep(3)
alert.send_keys('Hello Chel') # вводим данные в поле
alert.accept()# нажимаем окей
time.sleep(3)
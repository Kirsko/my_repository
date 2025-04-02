import time

from yandex_class import YandexSearchTest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ozon import ozon_test
import unittest

object_yandex = YandexSearchTest()
object_ozon = ozon_test()
class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.options = webdriver.ChromeOptions()

    def test_google_search(self):
        driver = self.driver
        self.options.add_argument('--user-agent=Automation')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        driver.get("https://google.com")

        try:
            accept_button = WebDriverWait(driver, 10).until()(
                EC.element_to_be_clickable('id', 'APj2Fqb')
            )
            accept_button.click()
        except:
            print("Не такого")

        search_box = driver.find_element('xpath',"//textarea[@id='APjFqb']")
        search_box.send_keys('Гамбургер')
        search_box.send_keys(Keys.ENTER)
        time.sleep(10)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located('id','search')
            )
            print('Успешно загружено')

        except:
            print('Успешно загружено')

        self.assertIn('Гамбургер', driver.title)
        print(f'Титл {driver.title}')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    object_yandex()
    object_ozon()
    unittest.main()
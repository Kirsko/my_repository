import time
from xml.dom.xmlbuilder import Options

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class YandexSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.options = webdriver.ChromeOptions()

    def test_google_search(self):
        driver = self.driver
        self.options.add_argument('--user-agent=Automation')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        driver.get("https://ya.ru/")
        time.sleep(25)
        try:
            accept_button = WebDriverWait(driver, 10).until()(
                EC.element_to_be_clickable('id', 'APj2Fqb')
            )
            accept_button.click()
            print('И такое есть')
        except:
            print("Не такого")
        try:
            alert = WebDriverWait(driver, 10).until(
                EC.alert_is_present()
            )
            alert.dismiss()
            print('Кликнули что отказаться от Яндекс Браузера')
        except:
            print('Такого тоже нет')
        search_box = driver.find_element('xpath',"//input[@name='text']")
        search_box.send_keys('Гамбургер')
        search_box.send_keys(Keys.ENTER)
        time.sleep(20)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located('id','search')
            )
            print('Успешно загружено')

        except:
            print('Успешно загружено')

        try:
            accept_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable('xpath', "//body[@class='b-page__body i-ua Typo Typo_text_m Typo_line_m b-page b-page_tld_ru b-page_ajax_yes b-page_initial-scroll_yes Theme Theme_color_yandex-default Theme_root_serp-desktop i-font_loaded i-ua_platform_other i-ua_js_inited utilityfocus']")
            )
            accept_button.click()
            print('Не сделали основные Яндекс Браузер')
        except:
            print('И такого нет')
        self.assertIn('Гамбургер', driver.title)
        print(f'Титл {driver.title}')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
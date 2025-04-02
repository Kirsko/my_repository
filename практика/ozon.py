import time
import pickle
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait # будет отвечать за явные ожидания
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
import tracemalloc
tracemalloc.start()

class ozon_test(unittest.TestCase):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')# определяет как человек
    chrome_options.add_argument('--user-agent=Automation')
    chrome_options.add_argument('--headless')
    service = Service(executable_path=ChromeDriverManager().install())#Прокидываем установку драйвера
    driver = webdriver.Chrome(service=service,options=chrome_options)

    def test_ozon_search(self):
        wait = WebDriverWait(self.driver, 20)
        self.driver.get('https://www.ozon.ru/')
        self.driver.maximize_window()

        SEARCH = ['xpath', "//input[@placeholder='Искать на Ozon']"]
        SEARCH_LIST = ['xpath', "//div[@class='e1']"]
        ANORAK = ['xpath',"(//div[@class='j6n_25'])[1]"]
        BUY = ['xpath', "(//button[@class='pk0_29 p4k_29 b2122-a0 b2122-b2 b2122-a4'])[1]"]
        KORZINA = ['xpath', "//div[@class='m0_5 b7124-a b7124-a5 tsBodyControl500Medium']"]
        BUY_BITCH =['xpath', "//button[@class='b2122-a0 b2122-b2 b2122-a4']"]
        tovar = 'Анорак'

        search_input = wait.until(EC.element_to_be_clickable(SEARCH))
        search_input.click()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

        print('Кликнул на поиск')

        wait.until(EC.element_to_be_clickable(SEARCH_LIST))
        search_input.send_keys(tovar)
        print('Ввел '+ tovar)
        search_input.send_keys(Keys.ENTER)
        print('Нажал Enter')

        wait.until(EC.element_to_be_clickable(ANORAK)).click()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        print('Кликнул на первый товар')
        print('Переключился на другую вкладку, которая открылась, сделал ее активным')
        print('Заголовок страницы ' + self.driver.title )

        wait.until(EC.element_to_be_clickable(BUY)).click()
        print('Нажал Добавить в корзину')

        wait.until(EC.element_to_be_clickable(KORZINA)).click()
        print('Нажал на корзину')
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        print('Переключился на следующую вкладку(Корзина)')
        print('Заголовок страницы ' + self.driver.title )
        wait.until(EC.element_to_be_clickable(BUY_BITCH)).click()
        print('Оформляем товар')

    def cookies(self):

        pickle.dump(self.driver.get_cookies(), open(os.getcwd() + '\\cookies\\cookirs.pkl', 'wb'))
        print('Копирование куки')
        self.driver.delete_all_cookies()
        print('Удаление куки')

        cookies = pickle.load(open(os.getcwd() + '\\cookies\\cookirs.pkl', 'rb'))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        print('Добавление скопированной куки')
        self.driver.refresh()
        print('Обновление страницы')

        print('Заголовок страницы ' + self.driver.title )
        print('Готово!')

    def tecemaloc(self):
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
        print('[10 утечек памяти]')
        for stat in top_stats:
            print(stat)

    def Down(self):
        self.driver.quit()

if __name__ =='__main__':
    unittest.main()
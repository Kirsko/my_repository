from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера (для Chrome)
driver = webdriver.Chrome()

try:
    # Открываем Google
    driver.get("https://www.google.com")

    # Ожидаем, пока поле поиска станет доступным
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Вводим текст в поле поиска
    search_box.send_keys("Selenium Python")

    # Имитируем нажатие клавиши Enter
    search_box.send_keys(Keys.RETURN)

    # Ожидаем, пока заголовок страницы изменится
    WebDriverWait(driver, 10).until(
        EC.title_contains("Selenium Python")
    )

    # Выводим заголовок страницы
    print("Заголовок страницы:", driver.title)

    # Находим первый результат поиска
    first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
    )

    # Выводим текст первого результата
    print("Первый результат:", first_result.text)

    # Кликаем по первому результату
    first_result.click()

    # Ожидаем загрузки новой страницы
    WebDriverWait(driver, 10).until(
        EC.title_contains("Selenium")
    )

    # Выводим заголовок новой страницы
    print("Заголовок новой страницы:", driver.title)

finally:
    # Закрываем браузер
    driver.quit()

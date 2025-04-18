import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

FIRST_NAME = ['xpath', "//input[@id='firstName']"]
LAST_NAME = ['xpath', "//input[@id='lastName']"]
EMAIL = ['xpath', "//input[@id='userEmail']"]
LABEL_GENDER = ['xpath', "//label[@for='gender-radio-1']"]
MOBILE = ['xpath', "//input[@id='userNumber']"]
DATA = ['xpath', "//input[@id='dateOfBirthInput']"]
SUBJECT = ['xpath', "//div[class='subjects-auto-complete__control subjects-auto-complete__control-is-focused subjects-auto-complete__control--menu-is-open css-yk16xz-control']"]
SPORT_CHECK_LIST = ['xpath', "//*[@id='hobbiesWrapper']/div[2]/div[1]/label"]
READING_CHECK_LIST = ['xpath', "//*[@id='hobbiesWrapper']/div[2]/div[2]/label"]
MUSIC_CHECK_LIST = ['xpath', "//*[@id='hobbiesWrapper']/div[2]/div[3]/label"]
FILE_UPLOAD = ['xpath', '//input[@type="file"]']
FILE_PICTURE = r'C:\Users\madee\AquaProjects\Selenium\практика\file\file.jpeg'
CURRENT_ADDRESS = ['xpath', '//*[@id="currentAddress"]']
STATE= ['xpath', '//*[@id="state"]/div/div[1]/div[1]']
STATE_LIST= ['xpath', '//*[@id="react-select-3-option-0"]']
CITY= ['xpath', "//*[@id='city']/div/div[1]/div[1]"]
CITY_LIST= ['xpath', '//*[@id="react-select-4-option-0"]']
BUTTON_CLICK = ['xpath', "//button[text()='Submit']"]

def initialize_driver():
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    wait = WebDriverWait(driver, 5)
    return driver,action,wait

def open_form_QA(driver):
    driver.get('https://demoqa.com/automation-practice-form')

def fill_text_field(wait, locator, text):
    wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

def click_element(wait, locator):
    wait.until(EC.visibility_of_element_located(locator)).click()

def upload_file(wait, locator, file_path):
    wait.until(EC.visibility_of_element_located(locator)).send_keys(file_path)

def scroll_page(driver, pixel):
    driver.execute_script(f"window.scrollBy(0, {pixel});")

def fill_pesonal_info(wait):
    fill_text_field(wait, FIRST_NAME, 'Кирилл')
    fill_text_field(wait, LAST_NAME, 'Кириллов')
    fill_text_field(wait, EMAIL, 'exploer@mail.com')
    fill_text_field(wait, MOBILE, '7999999999')
    fill_text_field(wait, CURRENT_ADDRESS, FILE_PICTURE)

def select_hobbi(wait):
    click_element(wait,SPORT_CHECK_LIST)
    click_element(wait,READING_CHECK_LIST)
    click_element(wait,MUSIC_CHECK_LIST)

def select_state_and_city(wait):
    click_element(wait, STATE)
    click_element(wait, STATE_LIST)
    click_element(wait, CITY)
    click_element(wait, CITY_LIST)

def click_button(wait):
    click_element(wait, BUTTON_CLICK)

def gender_click(wait):
    click_element(wait, LABEL_GENDER)

def main():
    driver, action, wait = initialize_driver()
    open_form_QA(driver)
    fill_pesonal_info(wait)
    gender_click(wait)
    select_hobbi(wait)
    scroll_page(driver, 500)
    select_state_and_city(wait)
    click_button(wait)
    time.sleep(5)

if __name__ == "__main__":
    main()


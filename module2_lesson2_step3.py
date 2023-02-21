from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)
    num1_elem = browser.find_element(By.ID, 'num1').text
    num2_elem = browser.find_element(By.ID, 'num2').text
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    search_num = str(int(num1_elem) + int(num2_elem))
    select.select_by_value(search_num)
    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(6)
    browser.quit()

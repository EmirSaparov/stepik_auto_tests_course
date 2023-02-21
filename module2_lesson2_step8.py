from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)

    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Emir')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Saparov')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('emir@emir.emir')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_input = browser.find_element(By.NAME, 'file')
    file_input.send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()
finally:
    time.sleep(10)
    browser.quit()

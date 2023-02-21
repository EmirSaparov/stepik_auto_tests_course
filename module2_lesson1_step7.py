from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import math
import time

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)
    treasure_img = browser.find_element(By.ID, 'treasure')
    x = treasure_img.get_attribute('valuex')
    y = calc(x)
    input_element = browser.find_element(By.ID, 'answer')
    input_element.send_keys(y)
finally:
    time.sleep(10)
    browser.quit()

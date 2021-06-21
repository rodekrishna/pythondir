from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.w3schools.com/')

time.sleep(5)

button = browser.find_element_by_link_text('LEARN HTML')
button.click()

time.sleep(3)

browser.close()


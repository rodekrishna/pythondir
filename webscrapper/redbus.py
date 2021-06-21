from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.w3schools.com/html/html_examples.asp')

time.sleep(5)
#button = browser.find_element_by_id('_2AkmmA _2Npkh4 _2kuvG8 _7UHT_c')
#button = browser.find_elements_by_class_name('_2AkmmA _2Npkh4 _2kuvG8 _7UHT_c')
button = browser.find_element_by_link_text('Examples explained')
button.click()



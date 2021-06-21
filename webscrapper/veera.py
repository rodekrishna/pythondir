from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

visitor = ["kunal","vaibhav","gopal","ramesh","mahesh","deepak","dipti","leena"]
counter = [1,2,3]

var = 1
while var == 1:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://mycutebaby.in/contest/participant/?n=5efccf8754206')
    time.sleep(20)
    edittext = browser.find_element_by_id('v')
    edittext.send_keys(random.choice(visitor))
    time.sleep(5)
    button = browser.find_element_by_id('vote_btn')
    button.click()
    time.sleep(20)
    browser.close()
    time.sleep(1800+random.choice(counter))



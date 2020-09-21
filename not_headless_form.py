from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import chromedriver_binary
import numpy as np
import time

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")

#####　ここにformのloginURLを書く、規約で怒られたくないので今は書かない
web_path = """ url """

def click_next():
    buttons = driver.find_elements_by_tag_name("button")

    for button in buttons:
        if button.text == "次へ":
            button.click()

driver = webdriver.Chrome(options=options)

driver.get(web_path)
time.sleep(2)

element = driver.find_element_by_name("identifier")

##### ここにloginに使用するgmail及びアカウント名を入れる上記同様今は書かない
element.send_keys(""" loginID(gmail) """)
time.sleep(1)
            
click_next()
time.sleep(1)

element = driver.find_element_by_name("password")
#####　ここにpasswordを入れる、上記同様書かない
element.send_keys(""" password """)

click_next()
time.sleep(3)

element = driver.find_element_by_class_name("quantumWizMenuPaperselectOptionList")
element.click()
time.sleep(2)

elements = driver.find_elements_by_tag_name("span")
for num in elements:
    if num.text=="36":
        num.click()
        
element = driver.find_elements_by_class_name("quantumWizMenuPaperselectOptionList")
element[1].click()
time.sleep(2)

heat_list = [0,1,2,3,4,5,6,7,8,9]
heat_num = np.random.choice(heat_list)

elements = driver.find_elements_by_tag_name("span")
for num in elements:
    if num.text==str(heat_num):
        num.click()
time.sleep(2)

element = driver.find_element_by_id("i16")
element.click()
time.sleep(1)

elements = driver.find_elements_by_tag_name("span")
for num in elements:
    if num.text=="次へ":
        num.click()
        break
    
elements = driver.find_elements_by_tag_name("span")
for num in elements:
    if num.text=="送信":
        num.click()
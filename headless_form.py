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
options.add_argument("--headless")

#####　ここにformのloginURLを書く、規約で怒られたくないので今は書かない
web_path = """ url """

driver = webdriver.Chrome(options=options)

driver.get(web_path)
time.sleep(2)

element = driver.find_element_by_tag_name("input")
##### ここにloginに使用するgmail及びアカウント名を入れる上記同様今は書かない
text = """ loginID(gmail) """
driver.execute_script('document.getElementsByTagName("input")[0].value="%s";' % text)
time.sleep(1)

def click_next():
    buttons = driver.find_elements_by_tag_name("button")

    for button in buttons:
        if button.text == "次へ":
            button.click()
            
click_next()
time.sleep(1)

#####　ここにpasswordを入れる、上記同様書かない
password = """ password """
driver.execute_script('document.getElementsByTagName("input")[3].value="%s";' % password)

click_next()
time.sleep(3)

driver.execute_script('document.getElementsByTagName("span")[2].click();')
time.sleep(2)

elements = driver.find_elements_by_tag_name("span")
for num in elements:
    if num.text=="36":
        num.click()
        
elements = driver.find_elements_by_tag_name("span")
count  =0
for num in elements:
    if num.text=="選択":
        count += 1
        if count == 1:
            continue
        if count == 2:
            num.click()
        
##### 小数点以下をランダムで決定
heat_list = [0,1,2,3,4,5,6,7,8,9]
heat_num = np.random.choice(heat_list)

elements = driver.find_elements_by_tag_name("span")
for num in elements:
    if num.text==str(heat_num):
        num.click()
        
driver.execute_script('document.getElementsByTagName("label")[1].click();')
time.sleep(1)

elements = driver.find_elements_by_tag_name("span")
for num in elements:
    if num.text=="次へ":
        num.click()
        
elements = driver.find_elements_by_tag_name("span")
for num in elements:
    if num.text=="送信":
        num.click()
        
"""   以下はawsの設定をおこなわなかったためできなかったが、入力が完了したらgmailをおこなうコード   """

"""
import smtplib, ssl
from email.mime.text import MIMEText

# 以下にGmailの設定を書き込む
gmail_account = #####上記同様、書かない
gmail_password = #####上記同様、書かない
# メールの送信先
mail_to = #####上記同様、書かない

subject = "formへの投稿完了"
body = "formへの投稿完了"
msg = MIMEText(body, "html")
msg["Subject"] = subject
msg["To"] = mail_to
msg["From"] = gmail_account

server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
    context=ssl.create_default_context())
server.login(gmail_account, gmail_password)
server.send_message(msg) # メールの送信
"""
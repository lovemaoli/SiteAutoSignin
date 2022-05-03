from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import json
import requests

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")
wd = webdriver.Chrome(chrome_options=chrome_options)


configs = json.loads(os.getenv("CONFIG"))
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd.maximize_window()
wd.implicitly_wait(5)
wd.get('https://www.moe17.com/3496/')

login = wd.find_element(By.XPATH,'//*[@class="login-button"]/div[1]/button[1]')
login.click()
name = wd.find_element(By.XPATH,'//input[@tabindex="2"]')
name.send_keys(configs["1"])
pwd = wd.find_element(By.XPATH,'//input[@tabindex="4"][1]')
pwd.send_keys(configs["2"])
flogin = wd.find_element(By.XPATH,'//div[@class="login-bottom"][1]')
flogin.click()
time.sleep(2)

menu = wd.find_element(By.XPATH,'//*[@class="bar-item bar-mission"]')
menu.click()
try:
    sign = wd.find_element(By.XPATH,'//*[@class="bar-user-info-row bar-mission-action"]')
    sign.click()
    time.sleep(1)
except:
    print("moe17已签到")

try:
    wd.get('https://rjhome.me/30638.html')
    time.sleep(0.5)
except:
    try:
        wd.get('https://rjhome.me/30638.html')
        time.sleep(0.5)
    except:
        try:
            wd.get('https://rjhome.me/30638.html')
            time.sleep(0.5)
        except:
            try:
                wd.get('https://rjhome.me/30638.html')
                time.sleep(0.5)
            except:
                print("failed...")
login = wd.find_element(By.XPATH,'//*[@class="login-button"]/div[1]/button[1]')
login.click()
name = wd.find_element(By.XPATH,'//input[@tabindex="2"]')
name.send_keys(configs["3"])
pwd = wd.find_element(By.XPATH,'//input[@tabindex="4"][1]')
pwd.send_keys(configs["4"])
flogin = wd.find_element(By.XPATH,'//div[@class="login-bottom"][1]')
flogin.click()
time.sleep(2)

menu = wd.find_element(By.XPATH,'//*[@class="bar-item bar-mission"]')
menu.click()
try:
    sign = wd.find_element(By.XPATH,'//*[@class="bar-user-info-row bar-mission-action"]')
    sign.click()
    time.sleep(1)
except:
    print("rjhome已签到")

wd.get('https://www.wanbianios.com/')
time.sleep(0.5)

login = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div/div[4]/div[1]/i')
login.click()
name = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[3]/input')
name.send_keys(configs["5"])
pwd = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[4]/input')
pwd.send_keys(configs["6"])
flogin = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/button')
flogin.click()
time.sleep(2)

menu = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div/div[4]/div[3]')
menu.click()
try:
    sign = wd.find_element(By.XPATH,'//*[@id="cao_widget_userinfo-2"]/div/div[1]/div[3]/button')
    sign.click()
    time.sleep(1)
except:
    print("ios已签到")

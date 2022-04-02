from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import json

chrome_options = Options()
# 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--disable-gpu')
# 隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('--hide-scrollbars')

configs = json.loads(os.getenv("CONFIG"))
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(options=chrome_options)
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

requests.post('http://120.77.39.85:8080/mail/daily_report', data=json.dumps(
            {"title": "账号22929292292929打卡成功", "body": "Test ^_^", "dest": "maoliloveyou@foxmail.com"}))

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
# moe
print("moe1")
wd.maximize_window()
wd.implicitly_wait(5)
# huaxiashuyu 1
print("huaxiashuyu")
wd.get('https://www.huaxiashuyu.com/')
time.sleep(5)
try:
    close_ad = wd.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/button")
    close_ad.click()
except:
    print("关闭失败 尝试第二次")
    try:
        wd.refresh()
        time.sleep(4)
        close_ad = wd.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/button")
        close_ad.click()
    except:
        try:
            print("第三次尝试")
            wd.get('https://www.huaxiashuyu.com/')
            time.sleep(5)
            close_ad = wd.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/button")
            close_ad.click()
        except:
            print("第三次仍失败 放弃关闭弹窗")
time.sleep(1)
try:
    login = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div[4]/div[1]')
    login.click()
except:
    print("huaxia login出现问题 仍继续运行")
name = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[1]/input')
name.send_keys(configs["17"])
pwd = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[2]/input')
pwd.send_keys(configs["18"])
flogin = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/button')
flogin.click()
time.sleep(2)

menu = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div[4]/div[3]')
menu.click()
try:
    sign = wd.find_element(By.XPATH,'//*[@id="cao_widget_userinfo-5"]/div/div[1]/div[3]/button/i')
    sign.click()
    time.sleep(1)
except:
    print("ios已签到1")
# huaxiashuyu 2
wd.get("https://www.huaxiashuyu.com/user-2/")
time.sleep(3)
try:
    exit1 = wd.find_element(By.XPATH,'//*[@id="user-profile"]/div/div[1]/div[2]/ul/li[8]/a')
    exit1.click()
    time.sleep(1)
except:
    try:
        wd.refresh()
        time.sleep(5)
        print("账号2退出1次")
        exit1 = wd.find_element(By.XPATH,'//*[@id="user-profile"]/div/div[1]/div[2]/ul/li[8]/a')
        exit1.click()
        time.sleep(1)
    except:
        try:
            wd.get("https://www.wanbianios.com/user")
            time.sleep(5)
            print("账号2退出2次")
            exit1 = wd.find_element(By.XPATH,'//*[@id="user-profile"]/div/div[1]/div[2]/ul/li[8]/a')
            exit1.click()
            time.sleep(1)
        except:
            print("账号2退出3次仍失败")
print("huaxiashuyu2")
wd.get('https://www.huaxiashuyu.com/')
time.sleep(1)
try:
    login = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div[4]/div[1]')
    login.click()
except:
    print("huaxia login2出现问题 仍继续运行")
name = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[1]/input')
name.send_keys(configs["19"])
pwd = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[2]/input')
pwd.send_keys(configs["20"])
flogin = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/button')
flogin.click()
time.sleep(2)

menu = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div[4]/div[3]')
menu.click()
try:
    sign = wd.find_element(By.XPATH,'//*[@id="cao_widget_userinfo-5"]/div/div[1]/div[3]/button/i')
    sign.click()
    time.sleep(1)
except:
    print("ios已签到2")

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

# 光板小镇 账号1 试运行
wd.get("https://www.clfans.club/")
time.sleep(4)
try:
    logintab = wd.find_element(By.XPATH,"/html/body/main/div[2]/div[1]/div/div[2]/div/a")
    logintab.click()
except:
    print("manu_find failed,refresh...")
    wd.refresh()
    time.sleep(10)
    logintab = wd.find_element(By.XPATH,"/html/body/main/div[2]/div[1]/div/div[2]/div/div[2]/div/p[2]/a[1]/i")
    logintab.click()
name = wd.find_element(By.XPATH,'//*[@id="sign-in"]/form/div[1]/input')
name.send_keys(configs["15"])
pwd = wd.find_element(By.XPATH,'//*[@id="sign-in"]/form/div[2]/input')
pwd.send_keys(configs["16"])
loginbottom = wd.find_element(By.XPATH,'//*[@id="sign-in"]/form/div[4]/button')
loginbottom.click()
time.sleep(5)
wd.refresh()
sign = wd.find_element(By.XPATH,'/html/body/main/div[2]/div[1]/div/div[2]/div/a/i')
sign.click()
time.sleep(3)
print("krkr已签到")

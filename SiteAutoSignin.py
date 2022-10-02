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
wd.maximize_window()
wd.implicitly_wait(20)
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
part1 = 0;part2 = 1;part3 = 0;part4 = 0;part5 = 1
def work():
    global part1,part2,part3,part4,part5
    if part1 == 0:
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
        time.sleep(3)
        try:
            login = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div[4]/div[1]')
            login.click()
        except:
            wd.get('https://www.huaxiashuyu.com/')
            time.sleep(5)
            login = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div[4]/div[1]')
            login.click()
        name = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[1]/input')
        name.send_keys(configs["17"])
        pwd = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[2]/input')
        pwd.send_keys(configs["18"])
        flogin = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/button')
        flogin.click()
        time.sleep(3)

        menu = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div[4]/div[3]')
        menu.click()
        time.sleep(2)
        try:
            wd.execute_script("var data=document.querySelector('body > ins:nth-child(3)').remove()")
            time.sleep(5)
            sign = wd.find_element(By.XPATH,'//*[@id="cao_widget_userinfo-5"]/div/div[1]/div[3]/button/i')
            sign.click()
        except:
            print("try to close ad for twice click")
            # close_ad = wd.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/button")
            # close_ad.click()
            time.sleep(1)
            sign = wd.find_element(By.XPATH,'//*[@id="cao_widget_userinfo-5"]/div/div[1]/div[3]/button/i')
            sign.click()
        time.sleep(1)
        
        print("ios已签到4")
        part1 = 1
    
    if part2 == 0:
        # moe
        print("moe1")

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
        part2 = 1
    
    if part3 == 0:
        # rjhome 1
        print("rj1")
        try:
            wd.get('https://rjhome.me/30638.html')
            time.sleep(1)
        except:
            try:
                wd.get('https://rjhome.me/30638.html')
                time.sleep(1)
            except:
                try:
                    wd.get('https://rjhome.me/30638.html')
                    time.sleep(1)
                except:
                    try:
                        wd.get('https://rjhome.me/30638.html')
                        time.sleep(1)
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
        time.sleep(1)
        try:
            sign = wd.find_element(By.XPATH,'//*[@class="bar-user-info-row bar-mission-action"]')
            sign.click()
            time.sleep(1)
        except:
            print("rjhome已签到")

        # rjhome 2
        print("rj2")
        wd.refresh()
        time.sleep(1)
        exitrj = wd.find_element(By.XPATH,'//*[@id="page"]/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/picture/img')
        exitrj.click()
        time.sleep(1)
        exitlog = wd.find_element(By.XPATH,'//*[@id="page"]/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[2]/div/div[1]/div[2]/a/i')
        exitlog.click()
        time.sleep(1)
        login = wd.find_element(By.XPATH,'//*[@class="login-button"]/div[1]/button[1]')
        login.click()
        name = wd.find_element(By.XPATH,'//input[@tabindex="2"]')
        name.send_keys(configs["13"])
        pwd = wd.find_element(By.XPATH,'//input[@tabindex="4"][1]')
        pwd.send_keys(configs["14"])
        flogin = wd.find_element(By.XPATH,'//div[@class="login-bottom"][1]')
        flogin.click()
        time.sleep(2)

        menu = wd.find_element(By.XPATH,'//*[@class="bar-item bar-mission"]')
        menu.click()
        time.sleep(1)
        try:
            sign = wd.find_element(By.XPATH,'//*[@class="bar-user-info-row bar-mission-action"]')
            sign.click()
            time.sleep(1)
        except:
            print("rjhome已签到2")
        part3 = 1

    if part4 == 0:
        # ios
        wd.get('https://www.wanbianios.com/')
        time.sleep(1)
        try:
            close_ad = wd.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/button")
            close_ad.click()
        except:
            print("关闭失败 尝试第二次")
            try:
                close_ad = wd.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/button")
                close_ad.click()
            except:
                print("第二次仍失败 放弃关闭弹窗")
        time.sleep(1)
        try:
            login = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div/div[4]/div[1]')
            login.click()
        except:
            print("ios login出现问题 仍继续运行")
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
            print("ios已签到1")
        # 开始第二个账号
        wd.get("https://www.wanbianios.com/user")
        time.sleep(3)
        try:
            exit1 = wd.find_element(By.XPATH,'//*[@id="user-profile"]/div/div[1]/div[2]/ul/li[8]/a')
            exit1.click()
            time.sleep(1)
        except:
            try:
                wd.refresh()
                time.sleep(3)
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
        wd.get("https://www.wanbianios.com/")
        try:
            login = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div/div[4]/div[1]')
            login.click()
        except:
            print("ios login出现问题 仍继续运行")
        name = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[3]/input')
        name.send_keys(configs["7"])
        pwd = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[4]/input')
        pwd.send_keys(configs["8"])
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
            print("ios已签到3")
        # 开始第三个账号
        wd.get("https://www.wanbianios.com/user")
        time.sleep(3)
        try:
            exit1 = wd.find_element(By.XPATH,'//*[@id="user-profile"]/div/div[1]/div[2]/ul/li[8]/a')
            exit1.click()
            time.sleep(1)
        except:
            try:
                wd.get("https://www.wanbianios.com/user")
                time.sleep(3)
                print("账号3退出1次")
                exit1 = wd.find_element(By.XPATH,'//*[@id="user-profile"]/div/div[1]/div[2]/ul/li[8]/a')
                exit1.click()
                time.sleep(1)
            except:
                try:
                    wd.refresh()
                    time.sleep(5)
                    print("账号3退出2次")
                    exit1 = wd.find_element(By.XPATH,'//*[@id="user-profile"]/div/div[1]/div[2]/ul/li[8]/a')
                    exit1.click()
                    time.sleep(1)
                except:
                    print("账号3退出3次仍失败")
        wd.get("https://www.wanbianios.com/")
        try:
            login = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div/div[4]/div[1]')
            login.click()
        except:
            print("ios login出现问题 仍继续运行")
        name = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[3]/input')
        name.send_keys(configs["9"])
        pwd = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[4]/input')
        pwd.send_keys(configs["10"])
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
            print("ios已签到3")
        # 开始第四个账号
        wd.get("https://www.wanbianios.com/user")
        time.sleep(3)
        try:
            exit1 = wd.find_element(By.XPATH,'//*[@id="user-profile"]/div/div[1]/div[2]/ul/li[8]/a')
            exit1.click()
            time.sleep(1)
        except:
            try:
                wd.refresh()
                time.sleep(5)
                print("账号4退出1次")
                exit1 = wd.find_element(By.XPATH,'//*[@id="user-profile"]/div/div[1]/div[2]/ul/li[8]/a')
                exit1.click()
                time.sleep(1)
            except:
                try:
                    wd.get("https://www.wanbianios.com/user")
                    time.sleep(5)
                    print("账号4退出2次")
                    exit1 = wd.find_element(By.XPATH,'//*[@id="user-profile"]/div/div[1]/div[2]/ul/li[8]/a')
                    exit1.click()
                    time.sleep(1)
                except:
                    print("账号4退出3次仍失败")
        wd.get("https://www.wanbianios.com/")
        try:
            login = wd.find_element(By.XPATH,'/html/body/div[1]/header/div/div/div[4]/div[1]')
            login.click()
        except:
            print("ios login出现问题 仍继续运行")
        name = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[3]/input')
        name.send_keys(configs["11"])
        pwd = wd.find_element(By.XPATH,'//*[@id="login"]/div/form/div[4]/input')
        pwd.send_keys(configs["12"])
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
            print("ios已签到4")
        part4 = 1
    if part5 == 0:
        # baiwan
        wd.get("https://www.baiwangame.com/")
        login = wd.find_element(By.XPATH,'//*[@id="app"]/header/div/div/div[3]/a')
        login.click()
        time.sleep(5)
        try:
            loginname = wd.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/form/div[3]/div[1]/div/input')
            loginname.send_keys(configs["25"])
            loginpass = wd.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/form/div[3]/div[2]/div/input')
            loginpass.send_keys(configs["26"])
            confirm = wd.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/form/div[3]/div[3]/button')
            confirm.click()
        except:
            loginname = wd.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/form/div[3]/div[1]/div/input')
            loginname.send_keys(configs["25"])
            loginpass = wd.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/form/div[3]/div[2]/div/input')
            loginpass.send_keys(configs["26"])
            confirm = wd.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/form/div[3]/div[3]/button')
            confirm.click()
        time.sleep(5)
        wd.get("https://www.baiwangame.com/user")
        time.sleep(3)
        try:
            sign = wd.find_element(By.XPATH,'//*[@id="main"]/div[2]/div/div[1]/div/div[1]/div/button')
            sign.click()
        except:
            print("baiwan1 signed.")
        wd.delete_all_cookies()
        #baiwan2
        wd.get("https://www.baiwangame.com/")
        login = wd.find_element(By.XPATH,'//*[@id="app"]/header/div/div/div[3]/a')
        login.click()
        time.sleep(5)
        try:
            loginname = wd.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/form/div[3]/div[1]/div/input')
            loginname.send_keys(configs["27"])
            loginpass = wd.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/form/div[3]/div[2]/div/input')
            loginpass.send_keys(configs["28"])
            confirm = wd.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/form/div[3]/div[3]/button')
            confirm.click()
        except:
            loginname = wd.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/form/div[3]/div[1]/div/input')
            loginname.send_keys(configs["27"])
            loginpass = wd.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/form/div[3]/div[2]/div/input')
            loginpass.send_keys(configs["28"])
            confirm = wd.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/form/div[3]/div[3]/button')
            confirm.click()
        time.sleep(5)
        wd.get("https://www.baiwangame.com/user")
        time.sleep(3)
        try:
            sign = wd.find_element(By.XPATH,'//*[@id="main"]/div[2]/div/div[1]/div/div[1]/div/button')
            sign.click()
        except:
            print("baiwan1 signed.")
        wd.delete_all_cookies()
        #baiwan3
        wd.get("https://www.baiwangame.com/")
        login = wd.find_element(By.XPATH,'//*[@id="app"]/header/div/div/div[3]/a')
        login.click()
        time.sleep(5)
        try:
            loginname = wd.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/form/div[3]/div[1]/div/input')
            loginname.send_keys(configs["29"])
            loginpass = wd.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/form/div[3]/div[2]/div/input')
            loginpass.send_keys(configs["30"])
            confirm = wd.find_element(By.XPATH,'/html/body/div[8]/div/div[2]/form/div[3]/div[3]/button')
            confirm.click()
        except:
            loginname = wd.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/form/div[3]/div[1]/div/input')
            loginname.send_keys(configs["29"])
            loginpass = wd.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/form/div[3]/div[2]/div/input')
            loginpass.send_keys(configs["30"])
            confirm = wd.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/form/div[3]/div[3]/button')
            confirm.click()
        time.sleep(5)
        wd.get("https://www.baiwangame.com/user")
        time.sleep(3)
        try:
            sign = wd.find_element(By.XPATH,'//*[@id="main"]/div[2]/div/div[1]/div/div[1]/div/button')
            sign.click()
        except:
            print("baiwan1 signed.")


p = 30  # 设置失败重试次数
while(1):
    if(p == 0):
        exit()
    else:
        try:
            wd.delete_all_cookies()
            work()
            p = 0
        except:
            print("---------------------失败一次，尝试重新打卡！")
            time.sleep(40)
            p = p - 1
            if(p == 0):
                print("重试五十次仍失败，请检查代码！")
                sign = wd.find_element(By.XPATH,'/html/body/main/div[2]/div[1]/div/div[2]/div/a/i')
                sign.click()

# _*_ coding utf-8 _*_
# __author: Jason
# Date: 2018/12/17
#coding=utf-8
from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.woniuyanglao'
desired_caps['appActivity'] = 'com.woniuyanglao.ui.activity.SelectLoginActivity)'
desired_caps['noReset']= 'True'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print("启动中……")
driver.find_element_by_id("tv_wx_phone").click()
time.sleep(3)
print("启动成功")

# #计算9595+6
# driver.find_element_by_id("digit9").click()
# driver.find_element_by_id("digit5").click()
# driver.find_element_by_id("digit9").click()
# driver.find_element_by_id("del").click()
# driver.find_element_by_id("digit9").click()
# driver.find_element_by_id("digit5").click()
# driver.find_element_by_id("plus").click()
# driver.find_element_by_id("digit6").click()
# driver.find_element_by_id("equal").click()

driver.quit()
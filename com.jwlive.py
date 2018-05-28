# utf-8
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os, sys
sys.path.append(os.getcwd())
from base.专业 import gongkaike
from base.消息 import xiaoxi
from base.base_driver import init_driver


driver = init_driver()


# zhuanye = driver.find_element_by_xpath("//*[contains(@text,'专业')]").click()
# 点击专业模块
driver_wait = WebDriverWait(driver, 19, 1)
zhuanye = driver_wait.until(lambda hahaha: hahaha.find_element_by_id("com.wy.jwlive:id/l_courseClass"))
zhuanye.click()

# zhaunye = driver.find_element_by_id("com.wy.jwlive:id/l_courseClass").click()
# 开放大学
# time.sleep(1)
driver_wait.until(lambda haha:haha.find_element_by_xpath("//*[contains(@text,'开放大学')]")).click()
# driver.find_element_by_xpath("//*[contains(@text,'开放大学')]").click()
# time.sleep(1)
driver_wait.until(lambda haha:haha.find_element_by_xpath("//*[contains(@text,'成人高考')]")).click()
# driver.find_element_by_xpath("//*[contains(@text,'成人高考')]").click()
# time.sleep(1)
driver_wait.until(lambda haha:haha.find_element_by_xpath("//*[contains(@text,'远程教育')]")).click()
# driver.find_element_by_xpath("//*[contains(@text,'远程教育')]").click()
# time.sleep(1)
# 退出
driver.keyevent(4)
# 专业
time.sleep(1)
# 跳转到公开课
# gongkaike.gong(gongkaike,driver)
# driver_wait.until(lambda gongkaike: gongkaike.gong(gongkaike,driver))
gongkaike.gong(gongkaike,driver)
# back_button = driver_wait.until(lambda hahaha: hahaha.find_element_by_id("com.wy.jwlive:id/et_pass"))
# back_button.send_keys("456789")

# # 退出
time.sleep(1)
driver.keyevent(4)
time.sleep(1)
# 自考小条目滚动 开放大学
driver_wait.until(lambda haha:haha.find_element_by_xpath("//*[contains(@text,'开放大学')]")).click()
# driver.find_element_by_xpath("//*[contains(@text,'开放大学')]").click()
# time.sleep(1)
# 成人高考
driver_wait.until(lambda haha:haha.find_element_by_xpath("//*[contains(@text,'成人高考')]")).click()
# driver.find_element_by_xpath("//*[contains(@text,'成人高考')]").click()
# time.sleep(1)
# 远程教育
driver_wait.until(lambda haha:haha.find_element_by_xpath("//*[contains(@text,'远程教育')]")).click()
# driver.find_element_by_xpath("//*[contains(@text,'远程教育')]").click()


time.sleep(1)
# driver.find_element_by_xpath("//*[contains(@text,'消息')]").click()
# 跳转到消息
xiaoxi.xi(xiaoxi,driver)


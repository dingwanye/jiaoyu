# utf-8
import sys,os

from selenium.webdriver.support.wait import WebDriverWait

sys.path.append(os.getcwd())
import time

from appium import webdriver
from base.base_driver import init_driver
class xiaoxi():
    def xi(self,driver):
        time.sleep(2)
        self.driver = driver
        # time.sleep(2)
        driver_wait = WebDriverWait(self.driver, 19, 1)
        zhuanye = driver_wait.until(lambda hahaha: hahaha.find_element_by_xpath("//*[contains(@text,'消息')]")).click()
        # zhuanye.click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'消息')]").click()
        # time.sleep(1)
        self.driver.find_element_by_xpath("//*[contains(@text,'系统消息')]").click
        time.sleep(1)
        driver.keyevent(4)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[contains(@text,'廖奕炯')]").click()
        time.sleep(2)
        # 点击老师个人信息
        self.driver.find_element_by_id("com.wy.jwlive:id/right_image").click()
        time.sleep(2)
        # 二维码保存在相册里面
        self.driver.find_element_by_id("com.wy.jwlive:id/iv_teacherQr").click()

        time.sleep(2)
        driver.keyevent(4)
        time.sleep(1)
        driver.keyevent(4)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[contains(@text,'运营中心大家族')]").click()
        time.sleep(2)
        # 群信息

        self.driver.find_element_by_id("com.wy.jwlive:id/right_image").click()
        # time.sleep(10)

        driver_wait = WebDriverWait(self.driver, 15, 1)
        back_button = driver_wait.until(lambda  haha:haha.find_element_by_xpath("//*[contains(@text,'公告')]"))
        back_button.click()
        self.driver.find_element_by_xpath("//*[contains(@text,'公告')]").click()
        time.sleep(1)
        driver.keyevent(4)
        time.sleep(1)
        driver.keyevent(4)
        time.sleep(1)
        driver.keyevent(4)

# time.sleep(2)
# xiaoxi.xi(xiaoxi,init_driver())
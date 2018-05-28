# utf-8
# 公开课
import os, sys
sys.path.append(os.getcwd())
from appium import webdriver
class gongkaike():
    def gong(self,driver):
        self.driver = driver

        self.driver.find_element_by_id("com.wy.jwlive:id/l_openCourse").click()


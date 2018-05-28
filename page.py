import base64
import time
from appium import webdriver

# server 启动参数

desired_caps = {}
#什么平台
desired_caps['platformName'] = 'Android'
# 手机的版本号
desired_caps['platformVersion'] = '5.1'
# 这个在Android里面可以随便写
desired_caps['deviceName'] = '192.168.56.101:5555'
# App包名
desired_caps['appPackage'] = 'com.wy.jwlive'
# App启动页面名字
desired_caps['appActivity'] = '.login.LoginActivity'

# 声明driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


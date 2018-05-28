import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def init_driver():
    # # server 启动参数
    # desired_caps = {}
    # # 设备信息
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '5.1'
    # desired_caps['deviceName'] = '192.168.56.101:5555'
    # # app的信息
    # desired_caps['appPackage'] = 'com.wy.jwlive'
    # desired_caps['appActivity'] = '.MainActivity'
    # # 解决输入中文
    # desired_caps['unicodeKeyboard'] = True
    # desired_caps['resetKeyboard'] = True
    #
    # # 寻找toast
    # desired_caps['automationName'] = 'Uiautomator2'
    #
    # # 不要重置应用
    # desired_caps['noReset'] = True
    #
    # # 声明我们的driver对象
    # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    # desired_caps['platformVersion'] = '5.1'

    desired_caps['deviceName'] = '192.168.56.101:5555'
    # desired_caps['appPackage'] = 'com.wy.jwlive'
    desired_caps['appPackage'] = 'com.wy.jwlive'
    # desired_caps['appActivity'] = '.MainActivity'
    desired_caps['appActivity'] = '.MainActivity'
    # 输入框输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # desired_caps['automationName'] = 'Uiautomator2'
    # desired_caps['noReset'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 切换到账号密码登录
    setting_title = driver.find_element_by_xpath("//*[contains(@text,'密码登录')]").click()
    # 输入账号
    phone = driver.find_element_by_xpath("//*[contains(@text,'请输入你的手机号')]").send_keys("18604544301")

    # 输入密码  隐士等待
    driver_wait = WebDriverWait(driver, 19, 1)
    back_button = driver_wait.until(lambda hahaha: hahaha.find_element_by_id("com.wy.jwlive:id/et_pass"))
    back_button.send_keys("456789")

    # password = driver.find_element_by_id("com.wy.jwlive:id/et_pass").send_keys("456789")
    time.sleep(1)
    # 登录
    login = driver.find_element_by_id("com.wy.jwlive:id/iv_passLogin").click()
    return driver
from selenium import webdriver
import time

for i in range(10):
    driver = webdriver.Firefox()
    url = "http://www.7daysedu.com/"
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='nav']/li[2]/a").click()
    time.sleep(3)
    driver.quit()


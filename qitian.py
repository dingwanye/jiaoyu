
from selenium import webdriver
import time
driver = webdriver.Firefox()

url = "http://www.7daysedu.com/"
driver.get(url)
driver.maximize_window()


# 定位到商城
el_house = driver.find_element_by_xpath(".//*[@id='nav']/li[2]/a")
el_house.click()
time.sleep(3)
# 查看保存窗口句柄的列表的长度
print(len(driver.window_handles))
# 切换到第二个窗口
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
# 切换回第一个窗口
# driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[2]/ul/li[2]/a").click()
time.sleep(1)
# 大专
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[3]/ul/li[2]/a").click()
# 行政管理
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[2]/a").click()
# 汉语言文学
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[3]/a").click()
# 广告学
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[4]/a").click()
# 教育学
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[5]/a").click()
# 试听课
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[6]/a").click()
time.sleep(1)
# 本科
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[3]/ul/li[3]/a").click()
time.sleep(1)
# 行政管理
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[2]/a").click()
# 汉语言文学
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[3]/a").click()
# 学期教育
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[4]/a").click()
# 公共事业管理
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[5]/a").click()
# 人力资源管理
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[6]/a").click()
# 试听课
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[7]/a").click()



# 开放大学
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[2]/ul/li[3]/a").click()
time.sleep(1)
# 大专
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[3]/ul/li[1]/a").click()
# 深圳
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[3]/ul/li[2]/a").click()
# 东莞
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[3]/a").click()
# 成都
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[4]/a").click()
# 重庆
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[5]/a").click()
# 新疆
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[6]/a").click()

# 本科
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[3]/ul/li[3]/a").click()
# 深圳
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[2]/a").click()
# 东莞
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[3]/a").click()
# 成都
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[4]/a").click()
# 重庆
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[5]/a").click()
# 新疆
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[6]/a").click()





driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[2]/ul/li[4]/a").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[3]/ul/li[2]/a").click()

driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[2]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[3]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[4]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[5]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[6]/a").click()

driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[3]/ul/li[3]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[3]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[4]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[5]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[6]/a").click()




driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[2]/ul/li[5]/a").click()
time.sleep(1)

driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[3]/ul/li[2]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[2]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[3]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[4]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[5]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[6]/a").click()

driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[3]/ul/li[3]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[2]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[3]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[4]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[5]/a").click()
driver.find_element_by_xpath(".//*[@id='content-container']/div[1]/div[4]/ul/li[6]/a").click()
print(driver.current_url)

# driver.quit()
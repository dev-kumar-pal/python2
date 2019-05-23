from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/home/terralogic/PycharmProjects/SeleniumProjects/chromedriver')

driver.set_page_load_timeout("10")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("python projects online")
#driver.find_element_by_class("gNO89b").send_keys(Keys.ENTER)
driver.find_element_by_name("btnK").click()#send_keys(Keys.ENTER)
#time.sleep(4)
driver.close()

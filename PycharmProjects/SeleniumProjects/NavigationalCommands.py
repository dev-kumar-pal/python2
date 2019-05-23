from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='/home/terralogic/PycharmProjects/SeleniumProjects/chromedriver')
driver.get('http://www.google.com')
print(driver.title)
driver.get('http://www.python.org')
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

driver.close()

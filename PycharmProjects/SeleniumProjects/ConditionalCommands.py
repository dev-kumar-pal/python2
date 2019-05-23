from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='/home/terralogic/PycharmProjects/SeleniumProjects/chromedriver')

driver.get('http://www.facebook.com')

username = driver.find_element_by_name('email')
print(username.is_displayed())
print(username.is_enabled())

password = driver.find_element_by_name('pass')
print(password.is_displayed())
print(password.is_enabled())

gender = driver.find_element_by_css_selector("label[class=_58mt]")
#gender = driver.find_element_by_id('u_0_9')
print (gender.is_selected())

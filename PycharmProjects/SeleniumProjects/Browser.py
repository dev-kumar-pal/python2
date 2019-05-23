from selenium.webdriver.common.keys import Keys
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/terralogic/PycharmProjects/SeleniumProjects/chromedriver')

driver.get('http://www.google.com')
print(driver.title)
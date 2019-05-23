from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='/home/terralogic/PycharmProjects/SeleniumProjects/chromedriver')
driver.get('http://demo.automationtesting.in/Windows.html')

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button")

time.sleep(2)

#driver.close()
driver.quit()


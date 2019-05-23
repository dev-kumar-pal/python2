from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/terralogic/PycharmProjects/SeleniumProjects/chromedriver')

driver.get('http://www.facebook.com')

driver.implicitly_wait(10)

assert  "Facebook"  in driver.title

driver.find_element_by_name('email').send_keys('example@gmail.com')
driver.find_element_by_name('pass').send_keys('example123')

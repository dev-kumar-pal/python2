import unittest
from selenium import webdriver
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome(executable_path='/home/terralogic/PycharmProjects/SeleniumProjects/chromedriver')
		cls.driver.implicitly_wait(10)

	def test_search_python(self):
		self.driver.get("http://www.google.com")
		self.driver.find_element_by_name("q").send_keys("Python Projects online")
		self.driver.find_element_by_name('btnK').submit()

	def test_search_selenium(self):
		self.driver = self.driver
		self.driver.get("http://www.google.com")
		self.driver.find_element_by_name("q").send_keys("selenium python tutorial")
		self.driver.find_element_by_name('btnK').submit()

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		cls.driver.quit()

if __name__ =='__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/terralogic/PycharmProjects'))


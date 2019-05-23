from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(executable_path='/home/terralogic/PycharmProjects/SeleniumProjects/chromedriver')

driver.get("http://www.expedia.com")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,"tab-flight-tab-hp").click()
time.sleep(2)
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")
#time.sleep(2);

driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("05/23/2019")
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("05/25/2019")
#time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

wait = WebDriverWait(driver,10)
#driver.find_element(By.XPATH,"//*[@id='stopFilter_stops-0'")
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))
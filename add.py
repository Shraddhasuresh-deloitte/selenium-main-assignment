import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\\Users\\shrasuresh\\Downloads\\chromedriver\\chromedriver.exe")
driver.get("https://shraddhas-trials7401.orangehrmlive.com/client/#/dashboard")
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("ry@bL4S3KN")
button = driver.find_element(By.CLASS_NAME, "button-holder")
button.click()

button = driver.find_element(By.ID, "menu_pim_viewPimModule")
button.click()
driver.get("https://shraddhas-trials7401.orangehrmlive.com/client/#/pim/employees")

driver.get("https://shraddhas-trials7401.orangehrmlive.com/client/#/pim/addEmployee")

driver.implicitly_wait(60)
driver.find_element(By.ID, "first-name-box").send_keys("Varsha")
driver.implicitly_wait(5)
driver.find_element(By.ID, "middle-name-box").send_keys("T")
driver.implicitly_wait(5)
driver.find_element(By.ID, "last-name-box").send_keys("R")
driver.implicitly_wait(5)
sel = Select(driver.find_element(By.ID, "location"))
sel.select_by_visible_text('India Office')
driver.implicitly_wait(5)
# driver.get("https://shraddhas-trials7401.orangehrmlive.com/client/#/pim/wizard/personal_details")
# driver.implicitly_wait(60)
# driver.find_element(By.ID, "emp_birthday").send_keys("26-01-2001")
# driver.implicitly_wait(5)
#


from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\\Users\\shrasuresh\\Downloads\\chromedriver\\chromedriver.exe")
driver.get("https://shraddhas-trials7401.orangehrmlive.com/client/#/dashboard")
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("ry@bL4S3KN")
button = driver.find_element(By.CLASS_NAME, "button-holder")
button.click()
button = driver.find_element(By.ID, "menu_pim_viewPimModule")
button.click()

driver.get("https://shraddhas-trials7401.orangehrmlive.com/client/#/pim/employees")

from datetime import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\\Users\\shrasuresh\\Downloads\\chromedriver\\chromedriver.exe")
driver.get("https://shraddhas-trials7401.orangehrmlive.com/client/#/dashboard")
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("ry@bL4S3KN")
button = driver.find_element(By.CLASS_NAME, "button-holder")
button.click()


# driver = webdriver.Chrome("C:\\Users\\shrasuresh\\Downloads\\chromedriver\\chromedriver.exe")
def alert_pop():
    driver.get("https://shraddhas-trials7401.orangehrmlive.com/client/#/dashboard")


# sel = Select(driver.find_element(By.CLASS_NAME, "dropdown-button waves-effect active"))
# sel.select_by_visible_text('About')
button = driver.find_element(By.ID, "account-name")
button.click()
button = driver.find_element(By.ID, "aboutDisplayLink")
button.click()
time.sleep(5)
alert = Alert(driver)
alert.accept()
driver.close()
alert_pop()

import click as click
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\shrasuresh\\Downloads\\chromedriver\\chromedriver.exe")
driver.get("https://shraddhas-trials7401.orangehrmlive.com/client/#/dashboard")
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("ry@bL4S3KN")
button = driver.find_element(By.CLASS_NAME, "button-holder")
button.click()


# driver = webdriver.Chrome("C:\\Users\\shrasuresh\\Downloads\\chromedriver\\chromedriver.exe")
def title():
    driver.get("https://shraddhas-trials7401.orangehrmlive.com/client/#/dashboard")
    driver.find_element(By.CLASS_NAME, "page-title")


get_title = driver.title
print(get_title)
title()

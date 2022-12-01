from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#########################################
#STANDARD USER
#given
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.saucedemo.com/")
#assert "Python" in driver.title
#when

elem = driver.find_element(By.ID, "user-name")
elem.clear()
elem.send_keys("standard_user")

elem = driver.find_element(By.ID, "password")
elem.clear()
elem.send_keys("secret_sauce")

boton = driver.find_element(By.ID, "login-button")
boton.click();
time.sleep(3)

resultado = driver.find_element(By.XPATH, "//*[@class='header_secondary_container']/span")
assert resultado.text == 'PRODUCTS'
time.sleep(3)

driver.close()

#########################################
#LOCKED OUT USER
#given
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.saucedemo.com/")
#assert "Python" in driver.title
#when

elem = driver.find_element(By.ID, "user-name")
elem.clear()
elem.send_keys("locked_out_user")

elem = driver.find_element(By.ID, "password")
elem.clear()
elem.send_keys("secret_sauce")

boton = driver.find_element(By.ID, "login-button")
boton.click();

time.sleep(5)

resultado = driver.find_element(By.XPATH, "//*[@id='login_credentials']/h4")
assert resultado.text == 'Accepted usernames are:'
time.sleep(3)

driver.close()

########################################
#STANDARD USER       ABRIR MENU
#given
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.saucedemo.com/")
#assert "Python" in driver.title
#when

elem = driver.find_element(By.ID, "user-name")
elem.clear()
elem.send_keys("standard_user")

elem = driver.find_element(By.ID, "password")
elem.clear()
elem.send_keys("secret_sauce")

boton = driver.find_element(By.ID, "login-button")
boton.click();
time.sleep(3)

boton = driver.find_element(By.ID, "react-burger-menu-btn")
boton.click()


resultado = driver.find_element(By.XPATH, "//*[@class='header_secondary_container']/span")
assert resultado.text == 'PRODUCTS'
time.sleep(3)

driver.close()
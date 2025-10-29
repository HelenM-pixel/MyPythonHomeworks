from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()


driver.get("http://the-internet.herokuapp.com/login")


input_usr = driver.find_element(By.CSS_SELECTOR, "input#username")
input_usr.send_keys("tomsmith")
sleep(5)


input_pass = driver.find_element(By.CSS_SELECTOR, "input#password")
input_pass.send_keys("SuperSecretPassword!")
sleep(5)


driver.find_element(By.CLASS_NAME,
                    "fa-sign-in").click()


sleep(10)
driver.quit()

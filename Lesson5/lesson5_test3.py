from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")


input_panel = driver.find_element(By.CSS_SELECTOR, "input")
input_panel.send_keys("Sky")
sleep(3)

input_panel.clear()


input_panel.send_keys("Pro")

sleep(5)
driver.quit()

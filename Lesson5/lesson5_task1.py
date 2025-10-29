from time import sleep
from selenium import webdriver
import selenium.webdriver.chrome.service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=selenium.webdriver.chrome.service.
    Service(ChromeDriverManager().install()))


driver.get("http://uitestingplayground.com/classattr")


driver.find_element(By.CLASS_NAME,
                    "btn-primary").click()


sleep(10)
driver.quit()

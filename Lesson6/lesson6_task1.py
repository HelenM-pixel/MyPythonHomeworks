from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(40)


driver.find_element(By.ID, "ajaxButton").click()


txt = driver.find_element(By.CSS_SELECTOR, ".bg-success").text


print(txt)


driver.quit()

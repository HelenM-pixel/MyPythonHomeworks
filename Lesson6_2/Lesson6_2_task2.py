from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")


# нашли и очистили поле ввода, послали новое значение
element = driver.find_element(By.ID, "newButtonName")
element.clear()
element.send_keys("SkyPro")


# нашли и нажали кнопку, в ней стало новое значение
driver.find_element(By.ID, "updatingButton").click()


button_txt = (driver.find_element(By.ID, "updatingButton")).text


print(f"{button_txt}")


driver.quit()

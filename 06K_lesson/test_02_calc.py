from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


# нашли и очистили поле ввода, послали новое значение
element = driver.find_element(By.ID, "delay")
element.clear()
element.send_keys("45")


# нажимаем кнопки калькулятора
button_7 = (driver.find_element(
    By.CSS_SELECTOR, "span.btn-outline-primary:nth-child(1)"))
button_7.click()


button_plus = (driver.find_element(
    By.CSS_SELECTOR, "span.operator:nth-child(4)"))
button_plus.click()


button_8 = (driver.find_element(
    By.CSS_SELECTOR, "span.btn:nth-child(2)"))
button_8.click()


button_equal = (driver.find_element(
    By.CSS_SELECTOR, "span.btn:nth-child(15)"))
button_equal.click()

# ждун
button_txt = WebDriverWait(driver, 48).until(
    EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, ".screen"), "15")
)


txt = driver.find_element(
    By.CSS_SELECTOR, ".screen").text
print(f"{txt}")


# проверка assert - условие, либо True, либо False
result = f"{txt}"
assert result == "15"


driver.quit()

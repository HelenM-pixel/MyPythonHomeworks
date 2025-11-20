from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    # нашли и очистили поле ввода, послали новое значение
    driver.find_element(By.ID, "delay").clear()
    driver.find_element(By.ID, "delay").send_keys("45")
    # нажимаем кнопки калькулятора
    driver.find_element(
        By.CSS_SELECTOR, "span.btn-outline-primary:nth-child(1)").click()
    driver.find_element(
         By.CSS_SELECTOR, "span.operator:nth-child(4)").click()
    driver.find_element(
        By.CSS_SELECTOR, "span.btn:nth-child(2)").click()
    driver.find_element(
        By.CSS_SELECTOR, "span.btn:nth-child(15)").click()
    # ждун
    WebDriverWait(driver, 48).until(
        EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, ".screen"), "15"))
    txt = driver.find_element(By.CSS_SELECTOR, ".screen").text
    print(f"{txt}")
    # проверка assert
    result = f"{txt}"
    assert result == "15"
    driver.quit()

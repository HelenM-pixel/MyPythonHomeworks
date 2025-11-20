from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


def test_01():
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    # нашли поле ввода, послали новое значение
    driver.find_element(By.CSS_SELECTOR, ".form-control").clear()
    driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']").click()
    # проверка assert - что поле zip красное
    colour_field_zip = driver.find_element(
        By.ID, "zip-code").get_attribute("class")
    red_zip = f"{colour_field_zip}"
    assert red_zip == "alert py-2 alert-danger"
    # проверка assert - что остальные зелёные
    fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    for field_colour in fields:
        get_field = driver.find_element(By.ID, field_colour).get_attribute("class")
        green_field = f"{get_field}"
        assert green_field == "alert py-2 alert-success"
    driver.quit()

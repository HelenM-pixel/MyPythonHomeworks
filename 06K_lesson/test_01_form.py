from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Edge(
    service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


# нашли и очистили поле ввода, послали новое значение
first_name = driver.find_element(
    By.CSS_SELECTOR, ".form-control")
first_name.clear()
first_name.send_keys("Иван")


last_name = driver.find_element(
    By.XPATH, "/html/body/main/div/form/div[1]/div[2]/label/input")
last_name.clear()
last_name.send_keys("Петров")


address = driver.find_element(
    By.XPATH, "/html/body/main/div/form/div[2]/div[1]/label/input")
address.clear()
address.send_keys("Ленина, 55-3")


email = driver.find_element(
    By.XPATH, "/html/body/main/div/form/div[3]/div[1]/label/input")
email.clear()
email.send_keys("test@skypro.com")


phone_number = driver.find_element(
    By.XPATH, "/html/body/main/div/form/div[3]/div[2]/label/input")
phone_number.clear()
phone_number.send_keys("+7985899998787")


zip_code = driver.find_element(
    By.XPATH, "/html/body/main/div/form/div[2]/div[2]/label/input")
zip_code.clear()
zip_code.send_keys("")


city = driver.find_element(
    By.XPATH, "/html/body/main/div/form/div[2]/div[3]/label/input")
city.clear()
city.send_keys("Москва")


country = driver.find_element(
    By.XPATH, "/html/body/main/div/form/div[2]/div[4]/label/input")
country.clear()
country.send_keys("Россия")


job_position = driver.find_element(
    By.XPATH, "/html/body/main/div/form/div[4]/div[1]/label/input")
job_position.clear()
job_position.send_keys("QA")


company = driver.find_element(
    By.XPATH, "/html/body/main/div/form/div[4]/div[2]/label/input")
company.clear()
company.send_keys("SkyPro")


submit_button = (driver.find_element(
    By.XPATH, "/html/body/main/div/form/div[5]/div/button"))
submit_button.click()


# проверка assert - что поле zip красное
colour_field_zip = driver.find_element(
    By.ID, "zip-code").get_attribute("class")
print(f"{colour_field_zip}")
red_zip = f"{colour_field_zip}"
assert red_zip == "alert py-2 alert-danger"


# проверки, что остальные поля зелёные
colour_field_first_name = driver.find_element(
    By.ID, "first-name").get_attribute("class")
print(f"{colour_field_first_name}")
green_first_name = f"{colour_field_first_name}"
assert green_first_name == "alert py-2 alert-success"


colour_field_last_name = driver.find_element(
    By.ID, "last-name").get_attribute("class")
print(f"{colour_field_last_name}")
green_last_name = f"{colour_field_last_name}"
assert green_last_name == "alert py-2 alert-success"


colour_field_address = driver.find_element(
    By.ID, "address").get_attribute("class")
print(f"{colour_field_address}")
green_address = f"{colour_field_address}"
assert green_address == "alert py-2 alert-success"


colour_field_city = driver.find_element(
    By.ID, "city").get_attribute("class")
print(f"{colour_field_city}")
green_city = f"{colour_field_city}"
assert green_city == "alert py-2 alert-success"


colour_field_country = driver.find_element(
    By.ID, "country").get_attribute("class")
print(f"{colour_field_country}")
green_country = f"{colour_field_country}"
assert green_country == "alert py-2 alert-success"


colour_field_city = driver.find_element(
    By.ID, "city").get_attribute("class")
print(f"{colour_field_city}")
green_city = f"{colour_field_city}"
assert green_city == "alert py-2 alert-success"


colour_field_e_mail = driver.find_element(
    By.ID, "e-mail").get_attribute("class")
print(f"{colour_field_e_mail}")
green_e_mail = f"{colour_field_e_mail}"
assert green_e_mail == "alert py-2 alert-success"


colour_field_phone = driver.find_element(
    By.ID, "phone").get_attribute("class")
print(f"{colour_field_phone}")
green_phone = f"{colour_field_phone}"
assert green_phone == "alert py-2 alert-success"


colour_field_job_position = driver.find_element(
    By.ID, "job-position").get_attribute("class")
print(f"{colour_field_job_position}")
green_job_position = f"{colour_field_job_position}"
assert green_job_position == "alert py-2 alert-success"

colour_field_company = driver.find_element(
    By.ID, "company").get_attribute("class")
print(f"{colour_field_company}")
green_company = f"{colour_field_company}"
assert green_company == "alert py-2 alert-success"


driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# firefox
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

# авторизация
input_user = driver.find_element(By.ID, "user-name")
input_user.send_keys("standard_user")


input_pass = driver.find_element(By.ID, "password")
input_pass.send_keys("secret_sauce")


# нажимаем кнопки
button_login = (driver.find_element(
    By.CSS_SELECTOR, "#login-button"))
button_login.click()

sleep(1)

add_backpack = (driver.find_element(
    By.ID, "add-to-cart-sauce-labs-backpack"))
add_backpack.click()


add_t_shirt = (driver.find_element(
    By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
add_t_shirt.click()


add_onesie = (driver.find_element(
    By.ID, "add-to-cart-sauce-labs-onesie"))
add_onesie.click()


go_to_chart = (driver.find_element(
    By.CSS_SELECTOR, ".shopping_cart_container a.shopping_cart_link"))
go_to_chart.click()


checkout = (driver.find_element(By.ID, "checkout"))
checkout.click()


input_first_name = driver.find_element(By.ID, "first-name")
input_first_name.send_keys("Helen")


input_last_name = driver.find_element(By.ID, "last-name")
input_last_name.send_keys("Mis")


postal = driver.find_element(By.ID, "postal-code")
postal.send_keys("634021")


continue_button = (driver.find_element(
    By.CSS_SELECTOR, ".cart_button.btn_action"))
continue_button.click()


total = driver.find_element(
    By.CSS_SELECTOR, ".summary_total_label").text
print(f"{total}")

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By


# Вот так вроде надо переоформить в виде одной функции, а не кучи их
def test_test_03():
    # firefox
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    # авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # нажимаем кнопки
    driver.find_element(
        By.CSS_SELECTOR, "#login-button").click()
    driver.implicitly_wait(5)
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(
        By.CSS_SELECTOR, ".shopping_cart_container a.shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Helen")
    driver.find_element(By.ID, "last-name").send_keys("Mis")
    driver.find_element(By.ID, "postal-code").send_keys("634021")
    driver.find_element(
        By.CSS_SELECTOR, ".cart_button.btn_action").click()
    total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    print(f"{total}")
    driver.quit()
     # проверка assert
    total_sum = f"{total}"
    assert total_sum.strip() == "Total: $58.29"

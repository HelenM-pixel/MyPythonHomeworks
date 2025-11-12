from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


driver.refresh()  # обновление, Герман посоветовал


# ждём пока появятся все элементы с тэгом img,
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "img")))


# проверяем что были все элементы с тэгом img
images = driver.find_elements(By.TAG_NAME, "img")
print(len(images))  # это работает


# печатаем атрибут src для третьего элемента
# (list не нужен! даст буквы по одной вместо адреса)
third_image_src = images[2].get_attribute("src")
print(f"{third_image_src}")


driver.quit()

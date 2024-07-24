from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_elements():
    # Инициализация драйвера с опциями для headless режима
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--start-maximized')

    driver = webdriver.Chrome(options=options)

    # Переход на страницу
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов
    username = driver.find_element(By.CSS_SELECTOR, "#user-name")
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    submit_button = driver.find_element(By.CSS_SELECTOR, "#login-button")

    # Проверка наличия элементов
    if username and password and submit_button:
        print("Элементы найдены")

    # Закрытие драйвера
    driver.close()
    driver.quit()

if __name__ == "__main__":
    test_elements()
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import driver
import time

class Prok:
    def __init__(self, url):  # url адрес
        self.url = driver.get(url=url)

    def authorization(self, login, password):  # Авторизация

        login_input = driver.find_element(By.CLASS_NAME, "js-user-login")
        login_input.send_keys(login)

        # Поиск поля для пароля и ввод пароля
        password_input = driver.find_element(By.CLASS_NAME, "js-user-password")
        password_input.send_keys(password)

        # Отправка формы (можно использовать кнопку или клавишу Enter)
        return password_input.send_keys(Keys.RETURN)

    def execute_script(self):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        for i in range(5):  # Прокрутка 10 раз
            driver.execute_script("window.scrollBy(0, 500);")  # Прокрутка на 500 пикселей вниз
            time.sleep(1)

        tabulator_row = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.tabulator-row[role='row']"))
        )
        return tabulator_row.click()

    def receptionists_memo(self):
        try:
            # Ожидание, пока элемент станет кликабельным
            tab = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.js-menu-item[title='Памятки приемосдатчика']"))
            )

            tab.click()  # Клик по вкладке
        except Exception as e:
            print(f"Ошибка при переходе на вкладку: {e}")

    def save_html(self, html):
        html = html.page_source
        with open("index.html", "w", encoding="utf-8") as file:
            return file.write(html)

    def quit(self):
        return driver.quit()
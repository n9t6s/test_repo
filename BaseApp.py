from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://mail.ru"

    def find_element(self, locator, timeout = 5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Не найден локатор {locator}"
        )

    def get_main_page(self):
        return self.driver.get(self.base_url)
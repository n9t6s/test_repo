from MailRuPages import (
    LoginFormLocators,
    MailPageLocators,
    SendNewEmailLocators,
)
from Common import Creds, Text
from BaseApp import BasePage


class MailRuApp(BasePage):
    def _input_text(self, text: str, locator):
        self.find_element(locator).send_keys(text)

    def _input_login(self, login = Creds.login, locator=LoginFormLocators.input_email_field):
        self._input_text(login, locator)

    def _input_password(self, password = Creds.password, locator = LoginFormLocators.input_password_field):
        self.find_element(LoginFormLocators.password_input_btn).click()
        self._input_text(password, locator)

    def _click_login(self):
        self.find_element(LoginFormLocators.login_btn).click()

    def login(self):
        self._input_login()
        self._input_password()
        self._click_login()

    def _new_message(self):
        try:
            self.find_element(MailPageLocators.new_message_btn).click()
        except:
            self.find_element(MailPageLocators.new_message_small_btn).click()

    def _input_destination(self, destination = Text.destination):
        self.find_element(SendNewEmailLocators.input_destination_email_field).click()
        self._input_text(destination, SendNewEmailLocators.input_destination_email_field)

    def _input_theme(self, theme = Text.theme):
        self._input_text(theme, SendNewEmailLocators.input_theme_field)

    def _input_message(self, message = Text.message):
        self.find_element(SendNewEmailLocators.input_email_text_field).click()
        self._input_text(message, SendNewEmailLocators.input_email_text_field)

    def _send_message_click(self):
        self.find_element(SendNewEmailLocators.send_email_btn).click()

    def send_message(self):
        self._new_message()
        self._input_destination()
        self._input_theme()
        self._input_message()
        self._send_message_click()

    def assert_success(self):
            element = self.find_element(SendNewEmailLocators.success).text
            if element == "Письмо отправлено":
                return True
            else:
                print(f"Неверное значение {element}")
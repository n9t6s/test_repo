from selenium.webdriver.common.by import By


class LoginFormLocators:
    input_email_field = (By.XPATH, "//input[@data-testid='login-input']")
    password_input_btn = (By.XPATH, "//*[@data-testid='enter-password']")
    input_password_field = (By.XPATH, "//*[@data-testid='password-input']")
    login_btn = (By.XPATH, "//*[@data-testid='login-to-mail']")


class MailPageLocators:
    new_message_btn = (By.CLASS_NAME, "compose-button__txt")
    new_message_small_btn = (By.CLASS_NAME, "sidebar__compose-btn-box")


class SendNewEmailLocators:
    input_destination_email_field = (By.CLASS_NAME, "container--zU301")
    input_theme_field = (By.XPATH, "//*[@name='Subject']")
    input_email_text_field = (
        By.XPATH,
        "/html/body/div[15]/div[2]/div/div[1]/div[2]/"
        "div[3]/div[5]/div/div/div[2]/div[1]/div[1]"
    )
    send_email_btn = (By.XPATH, "//*[@data-title-shortcut='Ctrl+Enter']")
    success = (
        By.XPATH,
        "/html/body/div[9]/div/div/div[2]/div[2]/div/div/div[2]"
    )

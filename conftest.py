import  pytest
from selenium import webdriver
from App import MailRuApp


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--no-headless")
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def web_app(browser):
    app = MailRuApp(browser)
    yield app
    del app

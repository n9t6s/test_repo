import os


class Creds:
    login = os.getenv("TEST_LOGIN")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

class Text:
    destination = os.getenv("TEST_DEST")
    theme = os.getenv("TEST_THEME")
    message = os.getenv("TEST_MESSAGE")

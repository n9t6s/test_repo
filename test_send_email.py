class TestSendMessage:
    def test_send_message(self, web_app):
        web_app.get_main_page()
        web_app.login()
        web_app.send_message()
        assert web_app.assert_success()

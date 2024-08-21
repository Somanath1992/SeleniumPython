import pytest


class TestLogin:
    def test_login_by_email(self, setup):
        print("This is login by email..")
        assert True

    def test_login_by_facebook(self, setup):
        print("This is login by facebook")
        assert True

    def test_login_by_twitter(self, setup):
        print("This is login by twitter")
        assert True

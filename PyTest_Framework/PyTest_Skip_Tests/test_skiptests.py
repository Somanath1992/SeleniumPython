import pytest


class TestLogin:
    def test_login_by_email(self):
        print("This is login by email..")
        assert True

    def test_login_by_facebook(self):
        print("This is login by facebook")
        assert True

    def test_login_by_twitter(self):
        print("This is login by twitter")
        assert True

    @pytest.mark.skip   # marker to skip test cases
    def test_signup_by_email(self):
        print("This is signup by email..")
        assert True

    @pytest.mark.skip
    def test_signup_by_facebook(self):
        print("This is signup by facebook")
        assert True

    @pytest.mark.skip
    def test_signup_by_twitter(self):
        print("This is signup by twitter")
        assert True

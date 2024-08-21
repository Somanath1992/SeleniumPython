import pytest

''' pytest fixture()- If we want to execute some setup or pre-requisite method before starting any test method
we can use pytest fixture'''
'''Also if we wanted to write some statements after executing test methods then we need to use yield keyword
and write statements which will executed after tests, this help for teardown methods'''


class TestClass:

    @pytest.fixture()  # decorator
    def setup(self):
        print("Launching browser")
        yield
        print("Close Browser")

    def test_login(self, setup):
        print("This is login test")

    def test_search(self, setup):
        print("This is search test")

    def test_advanced_search(self):  # setup method will not execute before this method
        print("This is advanced search test")

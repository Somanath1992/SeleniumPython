import pytest


class TestLogin:
    @pytest.mark.first
    def test_method1(self):
        print("Running Method 1..")

    @pytest.mark.fourth
    def test_method2(self):
        print("Running Method 2..")

    @pytest.mark.second
    def test_method3(self):
        print("Running Method 3..")

    @pytest.mark.fifth
    def test_method4(self):
        print("Running Method 4..")

    @pytest.mark.third
    def test_method5(self):
        print("Running Method 5..")

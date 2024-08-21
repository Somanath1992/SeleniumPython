"""Apart from self defined markers we have @pytest.mark.run(order=num) default keyword which will control
order of execution"""
import pytest


class TestLogin:
    @pytest.mark.run(order=3)
    def test_method1(self):
        print("Running Method 1..")

    @pytest.mark.run(order=2)
    def test_method2(self):
        print("Running Method 2..")

    @pytest.mark.run(order=1)
    def test_method3(self):
        print("Running Method 3..")

    @pytest.mark.run(order=5)
    def test_method4(self):
        print("Running Method 4..")

    @pytest.mark.run(order=4)
    def test_method5(self):
        print("Running Method 5..")

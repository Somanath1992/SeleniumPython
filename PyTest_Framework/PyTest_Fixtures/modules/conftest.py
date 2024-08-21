"""When we have multiple test modules and requirement is use of same setup method in every test module
then we can write our setup fixture method in separate file. The file name should be 'conftest.py' which is
suggested by pytest and no other name should be given.This 'conftest.py' should be present in the same directory
where all test methods are present"""
import pytest


@pytest.fixture()
def setup():
    print("Launching browser")
    yield
    print("Close Browser")

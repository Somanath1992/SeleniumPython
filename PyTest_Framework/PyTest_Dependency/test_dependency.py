# We can specify markers in .ini file , also install pytest-dependency plugin
import pytest


class TestClass:
    @pytest.mark.dependency()
    def test_open_app(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_open_app'])
    def test_login(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_search(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login', 'TestClass::test_search'])
    def test_advance_search(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_logout(self):
        assert True

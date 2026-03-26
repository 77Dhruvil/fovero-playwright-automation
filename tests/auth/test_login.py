import pytest
from pages.login_page import LoginPage
from utils.test_data import TestData


def test_valid_login(page):

    login = LoginPage(page)
    login.load()

    data = TestData.VALID_ADMIN
    login.login(data["email"], data["password"])

   # assert login.is_login_successful()

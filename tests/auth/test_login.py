import allure
import pytest
from pages.login_page import LoginPage
from utils.test_data import TestData

@allure.title("Verify Login Functionality")
@allure.description("User should be able to login with valid credentials")
def test_valid_login(page):

    login = LoginPage(page)
    login.load()

    data = TestData.VALID_ADMIN
    login.login(data["email"], data["password"])

   # assert login.is_login_successful()

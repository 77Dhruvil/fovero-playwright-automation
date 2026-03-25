from pages.login_page import LoginPage
from utils.config import Config


def test_login(page):
    login_page = LoginPage(page)

    user = Config.USERS["administrator"]

    login_page.load()
    login_page.login(user["email"], user["password"])

 #   assert login_page.is_login_successful()
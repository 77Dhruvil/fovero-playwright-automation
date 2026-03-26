import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import Config

@pytest.fixture
def admin_dashboard(page):

    login_page = LoginPage(page)
    login_page.load()

    user = Config.USERS["administrator"]
    login_page.login(user["email"], user["password"])

    return DashboardPage(page)
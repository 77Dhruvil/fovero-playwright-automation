import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import Config


@pytest.fixture
def admin_dashboard_login(page):   # ✅ NO self, NO class

    print("🔥 admin_dashboard fixture running")

    login = LoginPage(page)
    login.load()

    user = Config.USERS["administrator"]
    login.login(user["email"], user["password"])


    return DashboardPage(page)
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import Config
from playwright.sync_api import sync_playwright



@pytest.fixture
def admin_dashboard_login(page):   # ✅ NO self, NO class
    page.goto("https://fovero-uat.concettoprojects.com",
    wait_until = "domcontentloaded",
    timeout = 60000
    )

    print("🔥 admin_dashboard fixture running")

    login = LoginPage(page)
    login.load()

    user = Config.USERS["administrator"]
    login.login(user["email"], user["password"])


    return DashboardPage(page)


import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()   # ✅ fresh context per test
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
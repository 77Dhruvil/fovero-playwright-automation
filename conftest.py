import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import Config


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        context = browser.new_context(
            ignore_https_errors=True
        )

        page = context.new_page()

        # Global timeouts
        page.set_default_timeout(60000)
        page.set_default_navigation_timeout(60000)

        yield page

        context.close()
        browser.close()


@pytest.fixture
def admin_dashboard_login(page):

    print("🔥 admin_dashboard fixture running")

    login = LoginPage(page)

    # Uses your updated login_page.load()
    login.load()

    user = Config.USERS["administrator"]

    login.login(
        user["email"],
        user["password"]
    )

    # safer than wait_for_load_state("load")
    page.wait_for_load_state(
        "domcontentloaded"
    )

    # optional small stabilization wait
    page.wait_for_timeout(2000)

    return DashboardPage(page)
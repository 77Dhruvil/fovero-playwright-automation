from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utils.config import Config

class LoginPage(BasePage):

    def load(self):
        self.page.goto(
            Config.get_login_url(),
            wait_until="domcontentloaded",
            timeout=60000
        )  # ✅ Login URL opens

    def login(self, email, password):
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()
from locators.dashboard_locators import DashboardLocators
from locators.setting_locators import SettingsLocators

class SettingsPage:

    def __init__(self, page):
        self.page = page

    def go_to_settings(self):
        self.page.locator("img[src*='setting']").click()

        general_settings = self.page.locator(
            "div.settings-nav-item",
            has_text="General settings"
        )

        general_settings.wait_for(state="visible", timeout=5000)
        general_settings.click()

        # ✅ wait for page load
        self.page.wait_for_timeout(1000)

    def set_week_off(self, day="sunday"):
        if day == "sunday":
            checkbox = self.page.locator(SettingsLocators.SUNDAY_CHECKBOX)
        else:
            checkbox = self.page.locator(SettingsLocators.SATURDAY_CHECKBOX)

        if not checkbox.is_checked():
            checkbox.click()

        self.page.click(SettingsLocators.SAVE_BUTTON)
        self.page.wait_for_timeout(1000)
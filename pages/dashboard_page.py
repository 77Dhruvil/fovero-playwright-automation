from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # 🔥 Scope (VERY IMPORTANT)
        self.birthday_section = page.locator(DashboardLocators.BIRTHDAY_SECTION)

    # 🔹 Click Today's tab
    def get_Todaybirthday_tab(self):
        self.page.locator(DashboardLocators.TODAYS_BIRTHDAY).click()

    # 🔥 FIXED: Proper boolean check
    def is_no_data_found(self):
        return self.birthday_section.locator(
            DashboardLocators.NO_DATA_FOUND
        ).first.is_visible()

    # 🔥 Get employee count
    def get_employee_count(self):
        return self.birthday_section.locator(
            DashboardLocators.EMPLOYEE_CARDS
        ).count()

    # 🔥 Next button click (safe)
    def click_next_button(self):
        next_btn = self.birthday_section.locator(DashboardLocators.NEXT_BUTTON)

        if next_btn.is_visible():
            next_btn.click()
            return True
        return False

    # 🔥 Previous button click (safe)
    def click_previous_button(self):
        prev_btn = self.birthday_section.locator(DashboardLocators.PREVIOUS_BUTTON)

        if prev_btn.is_visible():
            prev_btn.click()
            return True
        return False
from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.birthday_section = page.locator(DashboardLocators.BIRTHDAY_SECTION)

    # 🔥 Generic tab click (REUSABLE)
    def click_birthday_tab(self, tab_type="today"):

        if tab_type == "today":
            self.page.locator(DashboardLocators.TODAYS_BIRTHDAY).click()

        elif tab_type == "upcoming":
            self.page.locator(DashboardLocators.UPCOMING_BIRTHDAY).click()

        else:
            raise ValueError("Invalid tab type")

    # 🔥 No Data check
    def is_no_data_found(self):
        return self.birthday_section.locator(
            DashboardLocators.NO_DATA_FOUND
        ).first.is_visible()

    # 🔥 Employee count
    def get_employee_count(self):
        return self.birthday_section.locator(
            DashboardLocators.EMPLOYEE_CARDS
        ).count()

    # 🔥 Next button
    def click_next_button(self):
        next_btn = self.birthday_section.locator(DashboardLocators.NEXT_BUTTON)

        if next_btn.is_visible():
            next_btn.click()
            return True
        return False

    # 🔥 Previous button
    def click_previous_button(self):
        prev_btn = self.birthday_section.locator(DashboardLocators.PREVIOUS_BUTTON)

        if prev_btn.is_visible():
            prev_btn.click()
            return True
        return False
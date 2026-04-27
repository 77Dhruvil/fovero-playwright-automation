from pages.base_page import BasePage
from locators.birthday_locators import BirthdayLocators


class BirthdayPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.birthday_section = self.page.locator(
            BirthdayLocators.BIRTHDAY_SECTION
        )

    # =====================================================
    # TAB NAVIGATION
    # =====================================================

    def click_today_birthday_tab(self):
        self.page.locator(
            BirthdayLocators.TODAYS_BIRTHDAY
        ).click()
        self.page.wait_for_timeout(500)


    def click_upcoming_birthday_tab(self):
        self.page.locator(
            BirthdayLocators.UPCOMING_BIRTHDAY
        ).click()
        self.page.wait_for_timeout(500)


    def click_birthday_tab(self, tab_type="today"):

        if tab_type.lower() == "today":
            self.click_today_birthday_tab()

        elif tab_type.lower() == "upcoming":
            self.click_upcoming_birthday_tab()

        else:
            raise ValueError(
                "Invalid tab type. Use 'today' or 'upcoming'"
            )


    # =====================================================
    # DATA VALIDATION
    # =====================================================

    def is_no_data_found(self):
        try:
            return self.birthday_section.locator(
                BirthdayLocators.NO_DATA_FOUND
            ).first.is_visible()
        except Exception:
            return False


    def get_employee_count(self):
        return self.birthday_section.locator(
            BirthdayLocators.EMPLOYEE_CARDS
        ).count()


    # =====================================================
    # BUTTON VISIBILITY
    # =====================================================

    def is_next_button_visible(self):

        try:
            btn = self.birthday_section.locator(
                BirthdayLocators.NEXT_BUTTON
            )

            if btn.count() == 0:
                return False

            is_visible = btn.first.is_visible()
            is_disabled = btn.first.evaluate(
                "el => el.classList.contains('slick-disabled')"
            )

            return is_visible and not is_disabled

        except Exception as e:
            print("Next button error:", e)
            return False


    def is_previous_button_visible(self):

        try:
            btn = self.birthday_section.locator(
                BirthdayLocators.PREVIOUS_BUTTON
            )

            if btn.count() == 0:
                return False

            is_visible = btn.first.is_visible()
            is_disabled = btn.first.evaluate(
                "el => el.classList.contains('slick-disabled')"
            )

            return is_visible and not is_disabled

        except Exception as e:
            print("Previous button error:", e)
            return False


    # =====================================================
    # BUTTON ACTIONS
    # =====================================================

    def click_next_button(self):

        try:
            btn = self.birthday_section.locator(
                BirthdayLocators.NEXT_BUTTON
            )

            if btn.count() == 0:
                return False

            if btn.first.evaluate(
                "el => el.classList.contains('slick-disabled')"
            ):
                return False

            btn.first.click()
            self.page.wait_for_timeout(700)

            return True

        except Exception as e:
            print("Next click failed:", e)
            return False


    def click_previous_button(self):

        try:
            btn = self.birthday_section.locator(
                BirthdayLocators.PREVIOUS_BUTTON
            )

            if btn.count() == 0:
                return False

            if btn.first.evaluate(
                "el => el.classList.contains('slick-disabled')"
            ):
                return False

            btn.first.click()
            self.page.wait_for_timeout(700)

            return True

        except Exception as e:
            print("Previous click failed:", e)
            return False


    # =====================================================
    # HELPER
    # =====================================================

    def get_pagination_status(self):

        status = {
            "next_visible": self.is_next_button_visible(),
            "prev_visible": self.is_previous_button_visible(),
            "employee_count": self.get_employee_count(),
            "has_data": not self.is_no_data_found()
        }

        print(status)
        return status
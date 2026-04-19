from pages.base_page import BasePage
from locators.birthday_locators import BirthdayLocators


class BirthdayPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.birthday_section = page.locator(BirthdayLocators.BIRTHDAY_SECTION)

    # =====================================================
    # TAB NAVIGATION
    # =====================================================

    def get_Todaybirthday_tab(self):
        """Click Today's Birthday tab"""
        self.page.locator(BirthdayLocators.TODAYS_BIRTHDAY).click()

    def click_birthday_tab(self, tab_type="today"):
        """
        Switch between birthday tabs
        
        Args:
            tab_type: "today" or "upcoming"
            
        Usage:
            birthday.click_birthday_tab("today")
            birthday.click_birthday_tab("upcoming")
        """
        if tab_type == "today":
            self.page.locator(BirthdayLocators.TODAYS_BIRTHDAY).click()
        elif tab_type == "upcoming":
            self.page.locator(BirthdayLocators.UPCOMING_BIRTHDAY).click()
        else:
            raise ValueError("Invalid tab type. Use 'today' or 'upcoming'")

    # =====================================================
    # DATA VALIDATION
    # =====================================================

    def is_no_data_found(self):

        return self.birthday_section.locator(
            BirthdayLocators.NO_DATA_FOUND
        ).first.is_visible()

    def get_employee_count(self):

        return self.birthday_section.locator(
            BirthdayLocators.EMPLOYEE_CARDS
        ).count()

    # =====================================================
    # BUTTON VISIBILITY CHECKS
    # =====================================================

    def is_next_button_visible(self):

        try:
            btn = self.birthday_section.locator(BirthdayLocators.NEXT_BUTTON)
            count = btn.count()
            
            if count > 0:
                is_visible = btn.first.is_visible()
                # Check for Slick carousel's disabled class
                is_enabled = not btn.first.evaluate("el => el.classList.contains('slick-disabled')")
                status = "[✓]" if (is_visible and is_enabled) else "[✗]"
                print(f"{status} Next Button - Exists: Yes, Visible: {is_visible}, Enabled: {is_enabled}")
                return is_visible and is_enabled
            else:
                print("[ℹ] Next Button - Not present in DOM")
                return False
        except Exception as e:
            print(f"[⚠] Error checking next button: {str(e)[:60]}")
            return False

    def is_prev_button_visible(self):

        try:
            btn = self.birthday_section.locator(BirthdayLocators.PREVIOUS_BUTTON)
            count = btn.count()
            
            if count > 0:
                is_visible = btn.first.is_visible()
                # Check for Slick carousel's disabled class
                is_enabled = not btn.first.evaluate("el => el.classList.contains('slick-disabled')")
                status = "[✓]" if (is_visible and is_enabled) else "[✗]"
                print(f"{status} Previous Button - Exists: Yes, Visible: {is_visible}, Enabled: {is_enabled}")
                return is_visible and is_enabled
            else:
                print("[ℹ] Previous Button - Not present in DOM")
                return False
        except Exception as e:
            print(f"[⚠] Error checking previous button: {str(e)[:60]}")
            return False

    # =====================================================
    # BUTTON CLICK OPERATIONS
    # =====================================================

    def click_next_button(self):

        try:
            next_btn = self.birthday_section.locator(BirthdayLocators.NEXT_BUTTON)
            
            # Step 1: Check if button exists in DOM
            if next_btn.count() == 0:
                print("[ℹ] Next Button - Not found in DOM (no pagination needed)")
                return {"status": "not_found", "clicked": False, "message": "Button not present"}
            
            # Step 2: Check visibility
            if not next_btn.first.is_visible():
                print("[⚠] Next Button - Found but not visible")
                return {"status": "not_visible", "clicked": False, "message": "Button not visible"}
            
            # Step 3: Check if disabled (Slick carousel uses 'slick-disabled' class)
            is_disabled = next_btn.first.evaluate("el => el.classList.contains('slick-disabled')")
            if is_disabled:
                print("[⚠] Next Button - Visible but DISABLED (reached end)")
                return {"status": "disabled", "clicked": False, "message": "Button is disabled"}
            
            # Step 4: Wait for button to be stable
            next_btn.first.wait_for(state="visible", timeout=5000)
            self.page.wait_for_timeout(200)  # Small delay for animations
            
            # Step 5: Perform click
            next_btn.first.click()
            print("[✓] Next Button - Clicked successfully")
            
            # Step 6: Wait for content to change
            self.page.wait_for_timeout(500)
            
            return {"status": "success", "clicked": True, "message": "Button clicked"}
            
        except Exception as e:
            error_msg = str(e)[:80]
            print(f"[✗] Next Button - Click failed: {error_msg}")
            return {"status": "error", "clicked": False, "message": error_msg}

    def click_previous_button(self):

        try:
            prev_btn = self.birthday_section.locator(BirthdayLocators.PREVIOUS_BUTTON)
            
            # Step 1: Check if button exists in DOM
            if prev_btn.count() == 0:
                print("[ℹ] Previous Button - Not found in DOM (no pagination needed)")
                return {"status": "not_found", "clicked": False, "message": "Button not present"}
            
            # Step 2: Check visibility
            if not prev_btn.first.is_visible():
                print("[⚠] Previous Button - Found but not visible")
                return {"status": "not_visible", "clicked": False, "message": "Button not visible"}
            
            # Step 3: Check if disabled (Slick carousel uses 'slick-disabled' class)
            is_disabled = prev_btn.first.evaluate("el => el.classList.contains('slick-disabled')")
            if is_disabled:
                print("[⚠] Previous Button - Visible but DISABLED (at first page)")
                return {"status": "disabled", "clicked": False, "message": "Button is disabled"}
            
            # Step 4: Wait for button to be stable
            prev_btn.first.wait_for(state="visible", timeout=5000)
            self.page.wait_for_timeout(200)  # Small delay for animations
            
            # Step 5: Perform click
            prev_btn.first.click()
            print("[✓] Previous Button - Clicked successfully")
            
            # Step 6: Wait for content to change
            self.page.wait_for_timeout(500)
            
            return {"status": "success", "clicked": True, "message": "Button clicked"}
            
        except Exception as e:
            error_msg = str(e)[:80]
            print(f"[✗] Previous Button - Click failed: {error_msg}")
            return {"status": "error", "clicked": False, "message": error_msg}

    # =====================================================
    # HELPER METHODS
    # =====================================================

    def get_pagination_status(self):

        result = {
            "next_visible": self.is_next_button_visible(),
            "prev_visible": self.is_prev_button_visible(),
            "employee_count": self.get_employee_count(),
            "has_data": not self.is_no_data_found()
        }
        print(f"[PAGINATION STATUS] {result}")
        return result

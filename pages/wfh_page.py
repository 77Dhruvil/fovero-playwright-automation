from pages.base_page import BasePage
from locators.wfh_locators import WFHLocators


class WFHPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.wfh_section = self.page.locator(WFHLocators.WFH_SECTION)

    # =====================================================
    # WFH SECTION
    # =====================================================

    def wait_for_wfh_section(self):
        self.page.wait_for_selector(WFHLocators.WFH_SECTION, timeout=10000)

        # Wait for either cards OR no data
        try:
            self.page.wait_for_selector(
                WFHLocators.WFH_CARDS,
                timeout=4000
            )
        except:
            self.page.wait_for_selector(
                WFHLocators.WFH_NO_DATA,
                timeout=4000
            )

    def get_wfh_cards(self):
        return self.page.locator(WFHLocators.WFH_CARDS)

    def get_wfh_cards_count(self):
        """Get count of visible WFH cards"""
        cards = self.get_wfh_cards()
        valid = 0

        for i in range(cards.count()):
            card = cards.nth(i)

            if not card.is_visible():
                continue

            text = card.inner_text().strip()

            if text:
                valid += 1

        return valid

    def is_wfh_no_data_visible(self):
        """Check if no data message is visible"""
        locator = self.page.locator(WFHLocators.WFH_NO_DATA)
        return locator.count() > 0 and locator.first.is_visible()

    def get_wfh_card_data(self, index):
        """Get data from WFH card"""
        card = self.get_wfh_cards().nth(index)

        return {
            "name": card.locator(WFHLocators.WFH_EMPLOYEE_NAME).inner_text().strip(),
            "type": card.locator(WFHLocators.WFH_TYPE).inner_text().strip(),
            "status": card.locator(WFHLocators.WFH_STATUS).inner_text().strip()
            if card.locator(WFHLocators.WFH_STATUS).count() > 0 else ""
        }

    def click_wfh_card(self, index=0):
        """Click on WFH card to open details"""
        card = self.get_wfh_cards().nth(index)
        if card.is_visible():
            card.click()
            self.page.wait_for_load_state("load")
            return True
        return False

    def click_wfh_detail_back_button(self):
        """Click back button on detail page"""
        btn = self.page.locator(WFHLocators.WFH_DETAIL_BACK_BUTTON)
        if btn.count() > 0 and btn.first.is_visible():
            btn.first.click()
            self.page.wait_for_load_state("load")
            return True
        return False

    def go_back_to_dashboard(self):
        """Navigate back to dashboard"""
        try:
            if self.click_wfh_detail_back_button():
                print("[✓] Used back button")
                return True
        except:
            pass
        
        try:
            self.page.go_back()
            self.page.wait_for_load_state("load")
            print("[✓] Used browser back")
            return True
        except:
            return False

    # =========================
    # WFH TAB ACTIONS
    # =========================

    def click_wfh_today_tab(self):
        """Click Today tab"""
        tab = self.page.locator(WFHLocators.WFH_TODAY_TAB)
        tab.wait_for(state="visible")
        tab.click()
        self.page.wait_for_timeout(500)
        self.wait_for_wfh_section()

    def click_wfh_upcoming_tab(self):
        """Click Upcoming tab"""
        try:
            tab = self.page.locator(WFHLocators.WFH_UPCOMING_TAB)
            # Wait for section first to ensure we're in the right place
            self.page.wait_for_selector(WFHLocators.WFH_SECTION, timeout=5000)
            self.page.wait_for_timeout(300)
            tab.wait_for(state="visible", timeout=5000)
            tab.click()
            self.page.wait_for_timeout(500)
            self.wait_for_wfh_section()
        except Exception as e:
            print(f"[⚠] Upcoming tab click - retrying: {str(e)[:40]}")
            # Retry once
            tab = self.page.locator(WFHLocators.WFH_UPCOMING_TAB)
            tab.click()
            self.page.wait_for_timeout(500)
            self.wait_for_wfh_section()

    def is_wfh_today_active(self):
        """Check if Today tab is active"""
        tab = self.page.locator(WFHLocators.WFH_TODAY_TAB)
        return tab.count() > 0 and "active" in tab.get_attribute("class")

    def is_wfh_upcoming_active(self):
        """Check if Upcoming tab is active"""
        tab = self.page.locator(WFHLocators.WFH_UPCOMING_TAB)
        return tab.count() > 0 and "active" in tab.get_attribute("class")

    # =========================
    # HELPER METHODS
    # =========================

    def get_wfh_status(self):
        """Get complete WFH section status"""
        return {
            "cards_count": self.get_wfh_cards_count(),
            "has_no_data": self.is_wfh_no_data_visible(),
            "today_active": self.is_wfh_today_active(),
            "upcoming_active": self.is_wfh_upcoming_active()
        }

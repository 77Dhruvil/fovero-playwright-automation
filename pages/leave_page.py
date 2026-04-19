from pages.base_page import BasePage
from locators.leave_locators import LeaveLocators


class LeavePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.leave_section = self.page.locator(LeaveLocators.LEAVES_SECTION)

    # =====================================================
    # COMMON WAIT (IMPORTANT)
    # =====================================================
    def wait_for_leaves_section(self):
        self.page.wait_for_selector(LeaveLocators.LEAVES_SECTION, timeout=10000)

        # Wait for either cards OR no data
        try:
            self.page.wait_for_selector(
                LeaveLocators.LEAVE_CARDS,
                timeout=4000
            )
        except:
            self.page.wait_for_selector(
                LeaveLocators.LEAVES_NO_DATA_IMG,
                timeout=4000
            )

    # =====================================================
    # TODAY TAB
    # =====================================================
    def click_today_leaves(self):
        self.page.locator(LeaveLocators.TODAYS_LEAVE).click()
        self.wait_for_leaves_section()

    def get_today_leaves_count(self):
        text = self.page.locator(LeaveLocators.TODAYS_LEAVE).inner_text()
        return int(''.join(filter(str.isdigit, text))) if any(c.isdigit() for c in text) else 0

    def is_today_tab_active(self):
        return "active" in self.page.locator(LeaveLocators.TODAYS_LEAVE).get_attribute("class")

    # =====================================================
    # UPCOMING TAB
    # =====================================================
    def click_upcoming_leaves(self):
        tab = self.page.locator(LeaveLocators.UPCOMING_LEAVE_TAB)
        tab.wait_for(state="visible")
        tab.click()
        self.wait_for_leaves_section()

    def get_upcoming_leaves_count(self):
        text = self.page.locator(LeaveLocators.UPCOMING_LEAVE_TAB).inner_text()
        return int(''.join(filter(str.isdigit, text))) if any(c.isdigit() for c in text) else 0

    def is_upcoming_tab_active(self):
        return "active" in self.page.locator(LeaveLocators.UPCOMING_LEAVE_TAB).get_attribute("class")

    # =====================================================
    # NO DATA CHECK (SAFE)
    # =====================================================
    def is_leaves_no_data_visible(self):
        locator = self.page.locator(LeaveLocators.LEAVES_NO_DATA_IMG)

        try:
            return locator.first.is_visible(timeout=2000)
        except:
            return False

    # =====================================================
    # GET VALID CARDS (FINAL FIX)
    # =====================================================
    def get_leave_cards_count(self):
        cards = self.page.locator(LeaveLocators.LEAVE_CARDS)

        visible_cards = 0

        for i in range(cards.count()):
            card = cards.nth(i)

            try:
                if card.is_visible():
                    visible_cards += 1
            except:
                continue

        return visible_cards

    def get_leave_cards(self):
        return self.page.locator(LeaveLocators.LEAVE_CARDS)

    # =====================================================
    # CARD DATA
    # =====================================================
    def get_leave_card_data(self, index):

        card = self.get_leave_cards().nth(index)

        return {
            "name": card.locator(LeaveLocators.EMPLOYEE_NAME).inner_text().strip(),
            "is_adhoc": card.locator(LeaveLocators.ADHOC_TAG).count() > 0,
            "leave_type": card.locator(LeaveLocators.LEAVE_TYPE).inner_text().strip(),
            "status": card.locator(LeaveLocators.LEAVE_STATUS).inner_text().strip()
            if card.locator(LeaveLocators.LEAVE_STATUS).count() > 0 else "",
            "date_range": card.locator(LeaveLocators.DATE_RANGE).inner_text().strip()
            if card.locator(LeaveLocators.DATE_RANGE).count() > 0 else ""
        }

    # =====================================================
    # ACTIONS
    # =====================================================
    def click_leave_card(self, index=0):
        self.get_leave_cards().nth(index).click()

    def click_back_button(self):
        btn = self.page.locator(LeaveLocators.LEAVE_DETAIL_BACK_BUTTON)
        if btn.count() > 0:
            btn.first.click()

    def click_dashboard_menu(self):
        self.page.get_by_role("link", name="Dashboard").first.click()

from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    # =====================================================
    # COMMON WAIT (IMPORTANT)
    # =====================================================
    def wait_for_leaves_section(self):
        self.page.wait_for_selector(DashboardLocators.LEAVES_SECTION, timeout=10000)

        # Wait for either cards OR no data
        try:
            self.page.wait_for_selector(
                DashboardLocators.LEAVE_CARDS,
                timeout=4000
            )
        except:
            self.page.wait_for_selector(
                DashboardLocators.LEAVES_NO_DATA_IMG,
                timeout=4000
            )

    # =====================================================
    # TODAY TAB
    # =====================================================
    def click_today_leaves(self):
        self.page.locator(DashboardLocators.TODAYS_LEAVE).click()
        self.wait_for_leaves_section()

    def get_today_leaves_count(self):
        text = self.page.locator(DashboardLocators.TODAYS_LEAVE).inner_text()
        return int(''.join(filter(str.isdigit, text))) if any(c.isdigit() for c in text) else 0

    def is_today_tab_active(self):
        return "active" in self.page.locator(DashboardLocators.TODAYS_LEAVE).get_attribute("class")

    # =====================================================
    # UPCOMING TAB
    # =====================================================
    def click_upcoming_leaves(self):
        tab = self.page.locator(DashboardLocators.UPCOMING_LEAVE_TAB)
        tab.wait_for(state="visible")
        tab.click()
        self.wait_for_leaves_section()

    def get_upcoming_leaves_count(self):
        text = self.page.locator(DashboardLocators.UPCOMING_LEAVE_TAB).inner_text()
        return int(''.join(filter(str.isdigit, text))) if any(c.isdigit() for c in text) else 0

    def is_upcoming_tab_active(self):
        return "active" in self.page.locator(DashboardLocators.UPCOMING_LEAVE_TAB).get_attribute("class")

    # =====================================================
    # NO DATA CHECK (SAFE)
    # =====================================================
    def is_leaves_no_data_visible(self):
        locator = self.page.locator(DashboardLocators.LEAVES_NO_DATA_IMG)

        try:
            return locator.first.is_visible(timeout=2000)
        except:
            return False

    # =====================================================
    # GET VALID CARDS (FINAL FIX)
    # =====================================================
    def get_leave_cards_count(self):
        cards = self.page.locator(DashboardLocators.LEAVE_CARDS)

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
        return self.page.locator(DashboardLocators.LEAVE_CARDS)

    # =====================================================
    # CARD DATA
    # =====================================================
    def get_leave_card_data(self, index):

        card = self.get_leave_cards().nth(index)

        return {
            "name": card.locator(DashboardLocators.EMPLOYEE_NAME).inner_text().strip(),
            "is_adhoc": card.locator(DashboardLocators.ADHOC_TAG).count() > 0,
            "leave_type": card.locator(DashboardLocators.LEAVE_TYPE).inner_text().strip(),
            "status": card.locator(DashboardLocators.LEAVE_STATUS).inner_text().strip()
            if card.locator(DashboardLocators.LEAVE_STATUS).count() > 0 else "",
            "date_range": card.locator(DashboardLocators.DATE_RANGE).inner_text().strip()
            if card.locator(DashboardLocators.DATE_RANGE).count() > 0 else ""
        }

    # =====================================================
    # ACTIONS
    # =====================================================
    def click_leave_card(self, index=0):
        self.get_leave_cards().nth(index).click()

    def click_back_button(self):
        btn = self.page.locator(DashboardLocators.LEAVE_DETAIL_BACK_BUTTON)
        if btn.count() > 0:
            btn.first.click()

    def click_dashboard_menu(self):
        self.page.get_by_role("link", name="Dashboard").first.click()


# # ==========================================
# # GENERIC SECTION HANDLER (REUSABLE)
# # ==========================================
#     def click_tab(self, locator):
#         self.page.locator(locator).click()
#
#
#     def get_count_from_tab(self, locator):
#         text = self.page.locator(locator).inner_text()
#         return int(''.join(filter(str.isdigit, text))) if any(c.isdigit() for c in text) else 0
#
#
#     def wait_for_section(self, section_locator, cards_locator, no_data_locator):
#         self.page.wait_for_selector(section_locator, timeout=10000)
#
#         try:
#             self.page.wait_for_selector(cards_locator, timeout=4000)
#         except:
#             self.page.wait_for_selector(no_data_locator, timeout=4000)
#
#
#     def is_no_data_visible_generic(self, no_data_locator):
#         try:
#             return self.page.locator(no_data_locator).first.is_visible(timeout=2000)
#         except:
#             return False
#
#
#     def get_cards_count_generic(self, cards_locator):
#         cards = self.page.locator(cards_locator)
#
#         visible = 0
#         for i in range(cards.count()):
#             try:
#                 if cards.nth(i).is_visible():
#                     visible += 1
#             except:
#                 continue
#
#         return visible
#
#     def validate_section(self, tab_locator, section_locator, cards_locator, no_data_locator):
#
#         # Click tab
#         self.click_tab(tab_locator)
#
#         # Wait
#         self.wait_for_section(section_locator, cards_locator, no_data_locator)
#
#         # Get data
#         count = self.get_count_from_tab(tab_locator)
#         no_data = self.is_no_data_visible_generic(no_data_locator)
#         cards = self.get_cards_count_generic(cards_locator)
#
#         print("Count:", count)
#         print("Cards:", cards)
#         print("No Data:", no_data)
#
#         # FINAL LOGIC
#         if cards > 0:
#             return "data"
#
#         elif no_data:
#             return "no_data"
#
#         else:
#             raise Exception("UI not stable")

    # =====================================================
    # WFH SECTION
    # =====================================================

    def wait_for_wfh_section(self):
        self.page.wait_for_selector(DashboardLocators.WFH_SECTION, timeout=10000)

    def get_wfh_cards(self):
        return self.page.locator(DashboardLocators.WFH_CARDS)

    def get_wfh_cards_count(self):
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
        locator = self.page.locator(DashboardLocators.WFH_NO_DATA)
        return locator.count() > 0 and locator.first.is_visible()

    def get_wfh_card_data(self, index):
        card = self.get_wfh_cards().nth(index)

        return {
            "name": card.locator(DashboardLocators.WFH_EMPLOYEE_NAME).inner_text().strip(),
            "type": card.locator(DashboardLocators.WFH_TYPE).inner_text().strip(),
            "status": card.locator(DashboardLocators.WFH_STATUS).inner_text().strip()
            if card.locator(DashboardLocators.WFH_STATUS).count() > 0 else ""
        }

    def click_wfh_card(self, index=0):
        self.get_wfh_cards().nth(index).click()

    def click_wfh_detail_back_button(self):
        btn = self.page.locator(DashboardLocators.WFH_DETAIL_BACK_BUTTON)
        if btn.count() > 0:
            btn.first.click()

    # =========================
    # WFH TAB ACTIONS
    # =========================

    def click_wfh_today_tab(self):
        tab = self.page.locator(DashboardLocators.WFH_TODAY_TAB)
        tab.wait_for(state="visible")
        tab.click()
        self.wait_for_wfh_section()

    def click_wfh_upcoming_tab(self):
        tab = self.page.locator(DashboardLocators.WFH_UPCOMING_TAB)
        tab.wait_for(state="visible")
        tab.click()
        self.wait_for_wfh_section()

    def is_wfh_today_active(self):
        return "active" in self.page.locator(DashboardLocators.WFH_TODAY_TAB).get_attribute("class")

    def is_wfh_upcoming_active(self):
        return "active" in self.page.locator(DashboardLocators.WFH_UPCOMING_TAB).get_attribute("class")
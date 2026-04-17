from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.birthday_section = page.locator(DashboardLocators.BIRTHDAY_SECTION)

    # =====================================================
    # BASIC HELPERS (UNCHANGED)
    # =====================================================

    def get_Todaybirthday_tab(self):
        self.page.locator(DashboardLocators.TODAYS_BIRTHDAY).click()

    def click_birthday_tab(self, tab_type="today"):
        if tab_type == "today":
            self.page.locator(DashboardLocators.TODAYS_BIRTHDAY).click()
        elif tab_type == "upcoming":
            self.page.locator(DashboardLocators.UPCOMING_BIRTHDAY).click()
        else:
            raise ValueError("Invalid tab type")

    def is_no_data_found(self):
        return self.birthday_section.locator(
            DashboardLocators.NO_DATA_FOUND
        ).first.is_visible()

    def get_employee_count(self):
        return self.birthday_section.locator(
            DashboardLocators.EMPLOYEE_CARDS
        ).count()

    def click_next_button(self):
        next_btn = self.birthday_section.locator(DashboardLocators.NEXT_BUTTON)
        if next_btn.is_visible():
            next_btn.click()
        return True

    def click_previous_button(self):
        prev_btn = self.birthday_section.locator(DashboardLocators.PREVIOUS_BUTTON)
        if prev_btn.is_visible():
            prev_btn.click()
        return True

    def is_next_button_visible(self):
        btn = self.page.locator(DashboardLocators.NEXT_BUTTON)
        return btn.count() > 0 and btn.first.is_visible()

    def is_prev_button_visible(self):
        btn = self.page.locator(DashboardLocators.PREVIOUS_BUTTON)
        return btn.count() > 0 and btn.first.is_visible()

    # =====================================================
    # LEAVES SECTION (UNCHANGED LOGIC)
    # =====================================================

    def wait_for_leaves_section(self):
        self.page.wait_for_selector(DashboardLocators.LEAVES_SECTION, timeout=10000)

        self.page.wait_for_function(
            """() => {
                const cards = document.querySelectorAll('div[role="row"]');
                const bodyText = document.body.innerText;

                return cards.length > 1 ||
                       bodyText.includes('No Data') ||
                       bodyText.includes('No Records');
            }""",
            timeout=15000
        )

    def click_today_leaves(self):
        self.page.locator(DashboardLocators.TODAYS_LEAVE).click()
        self.wait_for_leaves_section()

    def get_today_leaves_count(self):
        text = self.page.locator(DashboardLocators.TODAYS_LEAVE).inner_text()
        return int(''.join(filter(str.isdigit, text))) if any(c.isdigit() for c in text) else 0

    def is_today_tab_active(self):
        return "active" in (self.page.locator(DashboardLocators.TODAYS_LEAVE).get_attribute("class") or "")

    def click_upcoming_leaves(self):
        tab = self.page.locator(DashboardLocators.UPCOMING_LEAVE_TAB)
        tab.wait_for(state="visible", timeout=10000)
        tab.click()
        self.wait_for_leaves_section()

    def get_upcoming_leaves_count(self):
        text = self.page.locator(DashboardLocators.UPCOMING_LEAVE_TAB).inner_text()
        return int(''.join(filter(str.isdigit, text))) if any(c.isdigit() for c in text) else 0

    def is_upcoming_tab_active(self):
        return "active" in (self.page.locator(DashboardLocators.UPCOMING_LEAVE_TAB).get_attribute("class") or "")

    def is_leaves_no_data_visible(self):
        locators = [
            DashboardLocators.LEAVES_NO_DATA_IMG,
            "text=No Data",
            "text=No Records"
        ]

        for loc in locators:
            try:
                el = self.page.locator(loc)
                if el.count() > 0 and el.first.is_visible():
                    return True
            except:
                continue

        return False

    def get_leave_cards(self):
        return self.page.locator(DashboardLocators.LEAVE_CARDS)

    def get_leave_cards_count(self):
        return self.get_leave_cards().count()

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

    def click_leave_card(self, index=0):
        self.get_leave_cards().nth(index).click()

    def click_back_button(self):
        btn = self.page.locator(DashboardLocators.LEAVE_DETAIL_BACK_BUTTON)
        if btn.count() > 0:
            btn.first.click()

    # =====================================================
    # WFH - FIXED STABLE VERSION (MAIN FIX)
    # =====================================================

    def wait_for_wfh_section(self):

        # wait for either cards or no-data (NO LOCATOR DEPENDENCY)
        self.page.wait_for_function(
            """() => {
                const cards = document.querySelectorAll('div[role="button"]');

                const text = document.body.innerText.toLowerCase();

                return cards.length > 0 || text.includes('no data') || text.includes('no records');
            }""",
            timeout=15000
        )

    def get_wfh_cards(self):
        return self.page.locator("//div[@role='button']")

    def get_wfh_cards_count(self):
        return self.get_wfh_cards().count()

    def is_wfh_no_data_visible(self):
        locators = [
            DashboardLocators.WFH_NO_DATA,
            "text=No Data",
            "text=No Records",
            "text=No WFH",
            "img[alt*='no data']"
        ]

        for loc in locators:
            try:
                el = self.page.locator(loc)
                if el.count() > 0 and el.first.is_visible():
                    return True
            except:
                pass

        return False

    def get_wfh_card_data(self, index):
        cards = self.get_wfh_cards()
        card = cards.nth(index)

        return {
            "name": card.locator(DashboardLocators.WFH_EMPLOYEE_NAME).inner_text().strip(),
            "type": card.locator(DashboardLocators.WFH_TYPE).inner_text().strip(),
            "status": card.locator(DashboardLocators.WFH_STATUS).inner_text().strip()
            if card.locator(DashboardLocators.WFH_STATUS).count() > 0 else ""
        }

    def click_wfh_card(self, index=0):
        self.get_wfh_cards().nth(index).click()

    # =====================================================
    # TAB CLICK (FIXED — NO get_by_role PROBLEM)
    # =====================================================

    def click_wfh_today_tab(self):
        tab = self.page.locator(DashboardLocators.WFH_TODAY_TAB)
        tab.wait_for(state="visible", timeout=10000)
        tab.click()
        self.wait_for_wfh_section()

    def click_wfh_upcoming_tab(self):
        tab = self.page.locator("xpath=//button[contains(.,'Upcoming') and contains(@id,'WFH')]")
        tab.click()
        self.page.wait_for_timeout(2000)
        self.wait_for_wfh_section()

    # =====================================================
    # ACTIVE TAB CHECK (FIXED SAFE)
    # =====================================================

    def is_wfh_today_active(self):
        el = self.page.locator(DashboardLocators.WFH_TODAY_TAB)
        cls = el.get_attribute("class")
        return cls and "active" in cls

    def is_wfh_upcoming_active(self):
        el = self.page.locator(DashboardLocators.WFH_UPCOMING_TAB)
        cls = el.get_attribute("class")
        return cls and "active" in cls

    # =====================================================
    # DASHBOARD MENU (FIXED SAFE)
    # =====================================================

    def click_dashboard_menu(self):
        menu = self.page.get_by_role("link", name="Dashboard")

        # ❌ DON'T hard fail if not immediately visible
        try:
            menu.wait_for(state="visible", timeout=15000)
            menu.click()
        except:
            # fallback (UI re-render safe)
            self.page.wait_for_timeout(1000)
            menu = self.page.get_by_role("link", name="Dashboard")
            menu.click()

        self.page.wait_for_load_state("domcontentloaded")
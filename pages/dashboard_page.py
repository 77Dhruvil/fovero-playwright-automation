from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.birthday_section = page.locator(DashboardLocators.BIRTHDAY_SECTION)

        # 🔹 Click Today's tabc
    def get_Todaybirthday_tab(self):
                self.page.locator(DashboardLocators.TODAYS_BIRTHDAY).click()

        # 🔥 Generic tab click (REUSABLE)
    def click_birthday_tab(self, tab_type="today"):

            # 🔥 FIXED: Proper boolean check
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

        # 🔥 Get employee count
        # 🔥 Employee count
    def get_employee_count(self):
            return self.birthday_section.locator(
                DashboardLocators.EMPLOYEE_CARDS
            ).count()

        # 🔥 Next button click (safe)
        # 🔥 Next button
    def click_next_button(self):
            next_btn = self.birthday_section.locator(DashboardLocators.NEXT_BUTTON)

            if next_btn.is_visible():
                next_btn.click()
            return True
            return False

        # 🔥 Previous button click (safe)
        # 🔥 Previous button
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

    def close_modal_if_open(self):
        modal = self.page.locator("div[role='dialog']")

        if modal.count() > 0 and modal.is_visible():

            # 🔹 Try clicking close button
            close_btn = self.page.locator("button[aria-label='Close'], .btn-close")

            if close_btn.count() > 0 and close_btn.is_visible():
                close_btn.click()

            else:
                # 🔹 Fallback: click top-right area (sometimes no proper button)
                self.page.mouse.click(1900, 100)  # adjust if needed

            # 🔹 Wait for modal to disappear (safe wait)
            self.page.wait_for_selector("div[role='dialog']", state="hidden", timeout=10000)

# -------- TAB CLICK --------

    def click_tab(self, tab_name):
        self.close_modal_if_open()

        if tab_name == "in":
            tab = self.page.locator("#present")
        elif tab_name == "out":
            tab = self.page.locator("#absent")
        elif tab_name == "yet":
            tab = self.page.locator("#yetToCheckin")

        # ✅ Get expected count BEFORE click
        expected_count = int(''.join(filter(str.isdigit, tab.inner_text())) or 0)

        tab.click()

        # ✅ Wait until table matches tab count
        self.wait_for_attendance_data(expected_count)


        # -------- GET EMPLOYEES --------

    def get_employee_names(self):
        if self.is_no_data_found():
            return []

        table = self.page.locator("div[role='table']")

        rows = table.locator("div[role='row']").filter(
            has_not=self.page.locator("[role='columnheader']")
        )

        names = []
        for i in range(rows.count()):
            name = rows.nth(i).locator("div[data-column-id='2']").inner_text().strip()

            if name and name.lower() != "name":  # ✅ avoid header issue
                names.append(name)

        return names

    def is_attendance_no_data(self):
        return self.page.locator("text=No data").count() > 0

    def wait_for_attendance_data(self, expected_count):
        self.page.wait_for_function(
            """(expected) => {
                const rows = document.querySelectorAll('div[role="row"]');

                // remove header row
                const dataRows = rows.length > 0 ? rows.length - 1 : 0;

                return dataRows === expected || expected === 0;
            }""",
            arg=expected_count,
            timeout=10000
        )

    def get_employee_names(self):
        rows = self.page.locator("div[role='row']").filter(
            has_not=self.page.locator("[role='columnheader']")
        )

        names = []
        count = rows.count()

        print(f"🔍 Total rows found: {count}")

        for i in range(count):
            try:
                name = rows.nth(i).locator("div[data-column-id='2']").inner_text().strip()

                if name and name.lower() != "name":
                    names.append(name)

            except Exception as e:
                print(f"⚠️ Error reading row {i}: {e}")

        return names

    def get_attendance_data(self):
        rows = self.page.locator("div[role='row']").filter(
            has_not=self.page.locator("[role='columnheader']")
        )

        names = []

        for i in range(rows.count()):
            try:
                name = rows.nth(i).locator("div[data-column-id='2']").inner_text().strip()

                if name and name.lower() != "name":
                    names.append(name)
            except:
                continue

        return len(names), names

    def get_tab_count(self, tab_name):
        if tab_name == "yet":
            locator = self.page.locator("#yetToCheckin")
        elif tab_name == "in":
            locator = self.page.locator("#present")
        elif tab_name == "out":
            locator = self.page.locator("#absent")

        text = locator.inner_text()

        # Extract number from text (e.g., "Yet (5)")
        count = int(''.join(filter(str.isdigit, text))) if any(c.isdigit() for c in text) else 0

        return count

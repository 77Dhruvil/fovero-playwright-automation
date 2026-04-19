from pages.base_page import BasePage
from locators.live_attendance_locators import LiveAttendanceLocators


class LiveAttendancePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

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
        if self.is_attendance_no_data():
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

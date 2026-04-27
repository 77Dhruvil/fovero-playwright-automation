from pages.base_page import BasePage


class LiveAttendancePage(BasePage):

    def __init__(self, page):
        super().__init__(page)


    # -----------------------------------
    # Close modal if opened
    # -----------------------------------

    def close_modal_if_open(self):

        modal = self.page.locator("div[role='dialog']")

        if modal.count() > 0:

            try:
                if modal.first.is_visible():

                    close_btn = self.page.locator(
                        "button[aria-label='Close'], .btn-close"
                    )

                    if close_btn.count() > 0:
                        close_btn.first.click()

                    else:
                        self.page.mouse.click(1900,100)

                    self.page.wait_for_selector(
                        "div[role='dialog']",
                        state="hidden",
                        timeout=5000
                    )

            except:
                pass


    # -----------------------------------
    # Tab click
    # -----------------------------------

    def click_tab(self, tab_name):

        self.close_modal_if_open()

        if tab_name == "yet":
            tab = self.page.locator("#yetToCheckin")

        elif tab_name == "in":
            tab = self.page.locator("#present")

        elif tab_name == "out":
            tab = self.page.locator("#absent")

        else:
            raise Exception("Invalid tab name")

        expected_count = int(
            ''.join(
                filter(str.isdigit, tab.inner_text())
            ) or 0
        )

        tab.click()

        self.wait_for_attendance_data(
            expected_count
        )


    # -----------------------------------
    # Wait for rows load
    # -----------------------------------

    def wait_for_attendance_data(
        self,
        expected_count
    ):

        self.page.wait_for_function(
        """
        (expected) => {
            const rows =
            document.querySelectorAll(
             'div[role="row"]'
            );

            const dataRows =
            rows.length > 0 ?
            rows.length - 1 : 0;

            return (
             dataRows === expected ||
             expected === 0
            );
        }
        """,
        arg=expected_count,
        timeout=10000
        )


    # -----------------------------------
    # No data check
    # -----------------------------------

    def is_attendance_no_data(self):

        return (
            self.page.locator(
                "text=No data"
            ).count() > 0
        )


    # -----------------------------------
    # Employee names
    # -----------------------------------

    def get_employee_names(self):

        if self.is_attendance_no_data():
            return []

        rows = self.page.locator(
            "div[role='row']"
        ).filter(
            has_not=self.page.locator(
                "[role='columnheader']"
            )
        )

        names=[]

        for i in range(rows.count()):

            try:
                name = rows.nth(i).locator(
                    "div[data-column-id='2']"
                ).inner_text().strip()

                if (
                   name and
                   name.lower() != "name"
                ):
                    names.append(name)

            except:
                continue

        return names


    # -----------------------------------
    # Count + names
    # -----------------------------------

    def get_attendance_data(self):

        names = self.get_employee_names()

        return len(names), names


    # -----------------------------------
    # Tab count
    # -----------------------------------

    def get_tab_count(
        self,
        tab_name
    ):

        if tab_name=="yet":
            locator=self.page.locator(
                "#yetToCheckin"
            )

        elif tab_name=="in":
            locator=self.page.locator(
                "#present"
            )

        else:
            locator=self.page.locator(
                "#absent"
            )

        text=locator.inner_text()

        return int(
            ''.join(
                filter(str.isdigit,text)
            ) or 0
        )
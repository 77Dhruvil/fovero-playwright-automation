# =====================================================
# FINAL UPDATED employee_listing_page.py
# =====================================================

from pages.base_page import BasePage
from locators.employee_locators import EmployeeLocators


class EmployeeListingPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    # =====================================================
    # WAIT PAGE LOAD
    # =====================================================
    def wait_for_employee_section(self):

        try:

            self.page.wait_for_load_state("networkidle")

            self.page.locator(
                EmployeeLocators.SEARCH_INPUT
            ).wait_for(
                state="visible",
                timeout=15000
            )

            print("[✓] Employee page loaded")

            return True

        except Exception as e:

            print(f"[✗] Employee page load failed: {e}")

            return False

    # =====================================================
    # SEARCH EMPLOYEE
    # =====================================================
    def search_employee(self, employee_name):

        try:

            search_box = self.page.locator(
                EmployeeLocators.SEARCH_INPUT
            ).first

            search_box.wait_for(
                state="visible",
                timeout=10000
            )

            search_box.click(force=True)

            search_box.fill("")

            self.page.wait_for_timeout(500)

            search_box.type(
                employee_name,
                delay=120
            )

            self.page.wait_for_timeout(3000)

            print(f"[✓] Search successful: {employee_name}")

            return True

        except Exception as e:

            print(f"[✗] Search failed: {e}")

            return False

    # =====================================================
    # CLEAR SEARCH
    # =====================================================
    def clear_search(self):

        try:

            search_box = self.page.locator(
                EmployeeLocators.SEARCH_INPUT
            ).first

            search_box.click(force=True)

            self.page.keyboard.press("Control+A")

            self.page.keyboard.press("Backspace")

            self.page.wait_for_timeout(3000)

            print("[✓] Search cleared")

            return True

        except Exception as e:

            print(f"[✗] Clear search failed: {e}")

            return False

    # =====================================================
    # SELECT DEPARTMENT
    # =====================================================
    def select_department(self, department_name):

        try:

            dropdown = self.page.locator(
                "input[id*='react-select-2-input']"
            )

            dropdown.wait_for(
                state="visible",
                timeout=10000
            )

            dropdown.click(force=True)

            self.page.wait_for_timeout(1000)

            dropdown.fill(department_name)

            self.page.wait_for_timeout(1500)

            option = self.page.locator(
                f"div[role='option']:has-text('{department_name}')"
            ).first

            option.wait_for(
                state="visible",
                timeout=5000
            )

            option.click(force=True)

            self.page.wait_for_timeout(3000)

            print(f"[✓] Department selected: {department_name}")

            return True

        except Exception as e:

            print(f"[✗] Department selection failed: {e}")

            return False

    # =====================================================
    # CLEAR DEPARTMENT FILTER
    # =====================================================
    def clear_department_filter(self):

        try:

            clear_icon = self.page.locator(
                "div.css-5pujaa"
            ).first

            clear_icon.wait_for(
                state="visible",
                timeout=5000
            )

            clear_icon.click(force=True)

            self.page.wait_for_timeout(3000)

            print("[✓] Department filter cleared")

            return True

        except Exception as e:

            print(f"[✗] Department clear failed: {e}")

            return False

    # =====================================================
    # SELECT STATUS
    # =====================================================
    def select_status(self, status_name):

        try:

            status_dropdown = self.page.locator(
                "input[id*='react-select-3-input']"
            )

            status_dropdown.wait_for(
                state="visible",
                timeout=10000
            )

            status_dropdown.click(force=True)

            self.page.wait_for_timeout(1000)

            status_dropdown.fill(status_name)

            self.page.wait_for_timeout(1500)

            option = self.page.locator(
                f"div[role='option']:has-text('{status_name}')"
            ).first

            option.wait_for(
                state="visible",
                timeout=5000
            )

            option.click(force=True)

            self.page.wait_for_timeout(3000)

            print(f"[✓] Status selected: {status_name}")

            return True

        except Exception as e:

            print(f"[✗] Status selection failed: {e}")

            return False

    # =====================================================
    # CLEAR STATUS FILTER
    # =====================================================
    def clear_status_filter(self):

        try:

            clear_icon = self.page.locator(
                "div.css-5pujaa"
            ).last

            clear_icon.wait_for(
                state="visible",
                timeout=5000
            )

            clear_icon.click(force=True)

            self.page.wait_for_timeout(3000)

            print("[✓] Status filter cleared")

            return True

        except Exception as e:

            print(f"[✗] Status clear failed: {e}")

            return False

    # =====================================================
    # ACTIVE / INACTIVE TOGGLE
    # =====================================================

    def toggle_active_employee(self):

        try:

            toggle = self.page.locator(
                EmployeeLocators.ACTIVE_EMPLOYEE_TOGGLE
            )

            toggle.wait_for(
                state="visible",
                timeout=10000
            )

            # =================================================
            # CURRENT STATUS
            # =================================================

            before = toggle.is_checked()

            print(f"[✓] Initial Toggle State: {before}")

            toggle.scroll_into_view_if_needed()

            self.page.wait_for_timeout(1000)

            # =================================================
            # FIRST CLICK
            # =================================================

            toggle.click(force=True)

            self.page.wait_for_timeout(3000)

            first_after = toggle.is_checked()

            print(f"[✓] After First Click: {first_after}")

            # =================================================
            # SECOND CLICK
            # =================================================

            toggle.click(force=True)

            self.page.wait_for_timeout(3000)

            second_after = toggle.is_checked()

            print(f"[✓] After Second Click: {second_after}")

            # =================================================
            # VALIDATION
            # =================================================

            if before == second_after:

                print("[✓] Toggle ON/OFF functionality working properly")

                return True

            else:

                print("[✗] Toggle state not restored properly")

                return False

        except Exception as e:

            print(f"[✗] Toggle failed: {e}")

            return False

    # =====================================================
    # GET EMPLOYEE ROW COUNT
    # =====================================================

    def get_employee_rows_count(self):

        try:

            self.page.wait_for_timeout(3000)

            # =================================================
            # TRY MULTIPLE ROW LOCATORS
            # =================================================

            possible_rows = [
                "tbody tr",
                "tr[role='row']",
                "div[role='row']",
                "table tbody tr",
            ]

            final_count = 0

            for locator_text in possible_rows:

                rows = self.page.locator(locator_text)

                count = rows.count()

                visible_rows = 0

                for i in range(count):

                    row = rows.nth(i)

                    try:

                        text = row.inner_text().strip()

                        if row.is_visible() and text != "":
                            visible_rows += 1

                    except:
                        pass

                if visible_rows > final_count:
                    final_count = visible_rows

            # Remove table header row if counted
            if final_count > 0:
                final_count -= 1

            print(f"[✓] Visible employee rows: {final_count}")

            return final_count

        except Exception as e:

            print(f"[✗] Row count failed: {e}")

            return 0


    # =====================================================
    # TABLE DATA
    # =====================================================
    def get_employee_table_data(self, row_index=0):

        try:

            row = self.page.locator(
                "tbody tr"
            ).nth(row_index)

            cells = row.locator("td")

            total_cells = cells.count()

            data = {
                "emp_id": cells.nth(1).inner_text().strip() if total_cells > 1 else "",
                "name": cells.nth(2).inner_text().strip() if total_cells > 2 else "",
                "department": cells.nth(4).inner_text().strip() if total_cells > 4 else "",
                "join_date": cells.nth(6).inner_text().strip() if total_cells > 6 else "",
                "status": cells.nth(8).inner_text().strip() if total_cells > 8 else "",
            }

            print("[✓] Employee data fetched")

            return data

        except Exception as e:

            print(f"[✗] Table data fetch failed: {e}")

            return {}

    def click_export_button(self):

        try:

            button = self.page.locator(
                EmployeeLocators.EXPORT_BUTTON
            ).first

            button.wait_for(
                state="visible",
                timeout=10000
            )

            button.click(force=True)

            self.page.wait_for_timeout(3000)

            print("[✓] Export button clicked")

            return True

        except Exception as e:

            print(f"[✗] Export button failed: {e}")

            return False

    # =====================================================
    # ADD EMPLOYEE
    # =====================================================
    def click_add_employee_button(self):

        try:

            button = self.page.locator(
                EmployeeLocators.ADD_EMPLOYEE_BUTTON
            ).first

            button.wait_for(
                state="visible",
                timeout=10000
            )

            button.click(force=True)

            self.page.wait_for_timeout(3000)

            print("[✓] Add Employee button clicked")

            return True

        except Exception as e:

            print(f"[✗] Add Employee click failed: {e}")

            return False

    # =====================================================
    # CHECK ADD MODAL
    # =====================================================
    def is_add_modal_open(self):

        try:

            modal = self.page.locator(
                EmployeeLocators.ADD_MODAL
            )

            return modal.is_visible()

        except:

            return False
import datetime
import re

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
            locator = self.page.locator("text=There are no records to display")

            return locator.is_visible(timeout=3000)


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
                self.page.locator("#present").click()
            elif tab_name == "out":
                self.page.locator("#absent").click()
            elif tab_name == "yet":
                self.page.locator("#yetToCheckin").click()

            # ✅ WAIT for loader OR table change (dynamic wait)
            self.wait_for_table_update()

        def wait_for_table_update(self):
                # Wait for table to be visible
            self.page.locator("div[role='table']").wait_for(state="visible")

            self.page.wait_for_timeout(500)

            # -------- GET EMPLOYEES --------

        def get_employee_names(self):
            # Wait for rows to be stable
            table = self.page.locator("div[role='table']")

            rows = table.locator("div[role='row']").filter(
                has_not=self.page.locator("[role='columnheader']")
            )

            # ✅ Wait until rows count stabilizes
            self.page.wait_for_timeout(500)

            count = rows.count()

            # If only 0 or 1 row → likely no data
            if count <= 1:
                return []

            names = []
            for i in range(count):
                name = rows.nth(i).locator("div[data-column-id='2']").inner_text().strip()

                if name and name.lower() != "name":
                    names.append(name)

            return names
        # =========================
        # 🔹 WAIT DASHBOARD
        # =========================
        def open_dashboard(self):
            self.page.wait_for_selector("h6:has-text('Monthly Work Timing Insights')")

        # =========================
        # 🔹 TIME CONVERTER
        # =========================
        def convert_to_minutes(self, time_str):
            try:
                dt = datetime.strptime(time_str.strip(), "%I:%M %p")
                return dt.hour * 60 + dt.minute
            except:
                return None

        # =========================
        # 🔹 EXTRACT DATA
        # =========================
        def parse_time_data(self, text):

            result = {
                "raw": text,
                "value": None,
                "condition": None
            }

            # Normalize text
            text_lower = text.lower()

            # Extract condition (IMPROVED)
            if "early" in text_lower:
                result["condition"] = "Early"
            elif "late" in text_lower:
                result["condition"] = "Late"
            elif "extra" in text_lower or "more" in text_lower:
                result["condition"] = "Extra"
            elif "short" in text_lower or "less" in text_lower:
                result["condition"] = "Short"
            elif "on time" in text_lower:
                result["condition"] = "On Time"
            elif "-" in text_lower:
                result["condition"] = None
            else:
                # 👇 catch unknown condition
                print("⚠️ Unknown condition found:", text)
                result["condition"] = "Unknown"

            # Extract time
            match = re.search(r'(\d+.*?(AM|PM|Hr|Min))', text)
            if match:
                result["value"] = match.group(1)

            return result
        # =========================
        # 🔹 GET DASHBOARD DATA
        # =========================
        def get_dashboard_data(self):

            cards = self.page.locator("div:has-text('Avg')")
            count = cards.count()

            data = []

            for i in range(count):
                text = cards.nth(i).inner_text()

                if "Avg" not in text:
                    continue

                parsed = self.extract_time_and_condition(text)
                data.append(parsed)

            return data

        # =========================
        # 🔹 VALIDATE WITH SETTINGS
        # =========================
        def validate_with_settings(self, office_start, office_end, break_start, break_end):

            dashboard_data = self.get_dashboard_data()

            office_start_min = self.convert_to_minutes(office_start)
            office_end_min = self.convert_to_minutes(office_end)

            print("\n🔍 Office Time:", office_start, "-", office_end)

            for item in dashboard_data:

                print("\nChecking:", item["raw"])

                # Skip no data
                if "-" in item["raw"]:
                    print("⚠️ No Data → Skipped")
                    continue

                # START TIME VALIDATION
                if "Start" in item["raw"] and item["minutes"]:

                    if item["minutes"] < office_start_min:
                        assert item["condition"] == "Early"
                    elif item["minutes"] > office_start_min:
                        assert item["condition"] == "Late"
                    else:
                        assert item["condition"] in ["On Time", None]

                # END TIME VALIDATION
                if "End" in item["raw"] and item["minutes"]:

                    if item["minutes"] > office_end_min:
                        assert item["condition"] == "Late"
                    elif item["minutes"] < office_end_min:
                        assert item["condition"] == "Early"

                if "Break" in item["raw"]:

                    if item["condition"]:

                        # allow all valid + unknown
                        assert item["condition"] in ["Extra", "Short", "On Time", "Unknown"], \
                            f"❌ Invalid Break Condition: {item['condition']}"

                    else:
                        print("ℹ️ Break has no condition → acceptable")


                if "Working" in item["raw"]:

                    if item["condition"]:
                        assert item["condition"] in ["Extra", "Short", "On Time"]
                    else:
                        print("ℹ️ Working time has no condition → acceptable")

        def extract_time_and_condition(self, text):
            import re

            lines = text.split("\n")

            time_value = None
            condition = None

            for line in lines:
                line = line.strip()

                # Match time like 08:30 or 08:30 AM
                if re.match(r"\d{1,2}:\d{2}", line):
                    time_value = line

                elif line.lower() in ["early", "late", "on time"]:
                    condition = line

            # ✅ Convert to minutes if time exists
            minutes = None
            if time_value:
                try:
                    minutes = self.convert_to_minutes(time_value)
                except Exception as e:
                    print("⚠️ Time conversion failed:", time_value)

            return {
                "raw": text,
                "time": time_value,
                "condition": condition,
                "minutes": minutes  # ✅ ADD THIS
            }

        def get_monthly_card(self):
            return self.page.locator(DashboardLocators.CARDS)
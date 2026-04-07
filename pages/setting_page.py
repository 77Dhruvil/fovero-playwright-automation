from locators.settings_locators import SettingsLocators


class SettingsPage:

    def __init__(self, page):
        self.page = page

    # =========================
    # 🔹 NAVIGATION
    # =========================
    def go_to_settings(self):
        self.page.locator("img[src*='setting']").click()

        general_settings = self.page.locator(
            "div.settings-nav-item",
            has_text="General settings"
        )

        general_settings.wait_for(state="visible", timeout=5000)
        general_settings.click()

        self.page.wait_for_timeout(1000)

    def open_settings(self):

        # click settings icon
        self.page.locator("img[src*='setting']").click()

        # click General Settings
        general = self.page.locator("div.settings-nav-item", has_text="General settings")
        general.wait_for(state="visible")
        general.click()

        # wait for field to load
        self.page.wait_for_selector("#office_timing_start_time")
    # =========================
    # 🔹 WEEK OFF
    # =========================
    def set_week_off(self, day="sunday"):

        if day.lower() == "sunday":
            checkbox = self.page.locator(SettingsLocators.SUNDAY_CHECKBOX)
        else:
            checkbox = self.page.locator(SettingsLocators.SATURDAY_CHECKBOX)

        if not checkbox.is_checked():
            checkbox.click()

        self.page.locator(SettingsLocators.SAVE_BUTTON).click()
        self.page.wait_for_timeout(1000)

    # =========================
    # 🔹 OFFICE TIMING
    # =========================
    def set_office_time(self, start, end):
        self.page.locator(SettingsLocators.OFFICE_START_TIME).fill(start)
        self.page.locator(SettingsLocators.OFFICE_END_TIME).fill(end)

    # =========================
    # 🔹 BREAK TIMING
    # =========================
    def set_break_time(self, start, end):
        self.page.locator(SettingsLocators.BREAK1_START_TIME).fill(start)
        self.page.locator(SettingsLocators.BREAK1_END_TIME).fill(end)

    # =========================
    # 🔹 SAVE
    # =========================
    def save(self):
        self.page.locator(SettingsLocators.SAVE_BUTTON).click()

    # =========================
    # 🔹 COMBINED METHOD (BEST)
    # =========================
    def update_work_timing(self, office_start, office_end, break_start, break_end):
        self.set_office_time(office_start, office_end)
        self.set_break_time(break_start, break_end)
        self.save()

    def get_office_time(self):

        field = self.page.locator(SettingsLocators.OFFICE_START_TIME)

        # ✅ scroll into view
        field.scroll_into_view_if_needed()

        start = field.input_value()

        end_field = self.page.locator(SettingsLocators.OFFICE_END_TIME)
        end_field.scroll_into_view_if_needed()

        end = end_field.input_value()

        return start, end

    def get_break_time(self):

        start_field = self.page.locator(SettingsLocators.BREAK1_START_TIME)
        start_field.scroll_into_view_if_needed()

        start = start_field.input_value()

        end_field = self.page.locator(SettingsLocators.BREAK1_END_TIME)
        end_field.scroll_into_view_if_needed()

        end = end_field.input_value()

        return start, end
from locators.Attendance_and_Productivity_Insights import Attendance_and_Productivity_Insights


class AttendanceAndProductivityInsights:

    def __init__(self, page):
        self.page = page
        self.loc = Attendance_and_Productivity_Insights

    # =========================
    # SECTION
    # =========================
    def section_header(self):
        return self.page.locator(self.loc.SECTION_HEADER)

    # =========================
    # TABS
    # =========================
    def click_arrivals(self):
        self.page.locator(self.loc.ARRIVALS_TAB_SCOPED).click()

    def click_departures(self):
        self.page.locator(self.loc.DEPARTURES_TAB_SCOPED).click()

    def click_breaks(self):
        self.page.locator(self.loc.BREAKS_TAB_SCOPED).click()

    def click_productivity(self):
        self.page.locator(self.loc.PRODUCTIVITY_TAB_SCOPED).click()

    # =========================
    # BLOCKS
    # =========================
    def get_block(self, text: str):
        return self.page.locator(f"//p[normalize-space()='{text}']/parent::div")

    # =========================
    # NO DATA
    # =========================
    def is_no_data_visible(self):
        return self.page.locator("//img[contains(@class,'noDataImg')]").first.is_visible()
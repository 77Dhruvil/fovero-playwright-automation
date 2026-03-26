from locators.dashboard_locators import DashboardLocators


class DashboardPage:

    def __init__(self, page):
        self.page = page

    # -------------------------------
    # GRAPH ACTIONS
    # -------------------------------
    def open_graph_filter(self):
        btn = self.page.get_by_role("button", name="Last 12 Months More")
        btn.wait_for(state="visible")
        btn.click()


    def select_this_fiscal(self):
        self.page.locator(DashboardLocators.GRAPH_OPTION_THIS_FISCAL).click()

    def select_previous_fiscal(self):
        self.page.locator(DashboardLocators.GRAPH_OPTION_PREVIOUS).click()

    def click_graph_bar(self):
        self.page.locator(DashboardLocators.GRAPH_BAR).first.click()

    def close_graph_popup(self):
        self.page.locator(DashboardLocators.GRAPH_CLOSE_BTN).click()

    def is_graph_visible(self):
        return self.page.locator(DashboardLocators.GRAPH_TITLE).is_visible()

    # -------------------------------
    # BIRTHDAY
    # -------------------------------
    def open_upcoming_birthday(self):
        self.page.locator(DashboardLocators.UPCOMING_BIRTHDAY).click()

    # -------------------------------
    # LIVE ATTENDANCE
    # -------------------------------
    def open_live_attendance(self):
        self.page.locator(DashboardLocators.LIVE_ATTENDANCE).click()

    # -------------------------------
    # LEAVE / WFH
    # -------------------------------
    def open_upcoming_leaves(self):
        self.page.locator(DashboardLocators.UPCOMING_LEAVES).click()

    def open_upcoming_wfh(self):
        self.page.locator(DashboardLocators.UPCOMING_WFH).click()

    # -------------------------------
    # PRODUCTIVITY
    # -------------------------------
    def open_departures(self):
        self.page.locator(DashboardLocators.DEPARTURES_TAB).click()

    def open_breaks(self):
        self.page.locator(DashboardLocators.BREAKS_TAB).click()

    def open_productivity(self):
        #self.page.locator(DashboardLocators.PRODUCTIVITY_TAB).click()
        self.page.locator("strong:has-text('Productivity')").click()

    # -------------------------------
    # ANNOUNCEMENT
    # -------------------------------
    def click_add_announcement(self):
        self.page.locator(DashboardLocators.ADD_ANNOUNCEMENT_BTN).click()

    # -------------------------------
    # APPLY LEAVE
    # -------------------------------
    def click_apply_leave(self):
        self.page.locator(DashboardLocators.APPLY_LEAVE).click()

    # -------------------------------
    # NAVIGATION
    # -------------------------------
    def go_to_dashboard(self):
        self.page.locator(DashboardLocators.DASHBOARD_LINK).click()

    def wait_for_dashboard_load(self):
        self.page.wait_for_load_state("networkidle")
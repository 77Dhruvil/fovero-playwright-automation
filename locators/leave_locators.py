class LeaveLocators:

    ##### Leave Section ######################

    # Tabs
    TODAYS_LEAVE = "//button[starts-with(@id, \"Today's\") and contains(@id, 'Leaves')]"
    UPCOMING_LEAVE_TAB = "button[id*='Upcoming-Leaves']"

    # Section base
    LEAVES_SECTION = "//h6[text()='Leaves']/ancestor::div[contains(@class,'card')]"

    # No Data
    LEAVES_NO_DATA_IMG = "//h6[text()='Leaves']/ancestor::div//img[contains(@src,'no-data-found')]"

    # 🔥 FIXED (Removed strict filtering)
    LEAVE_CARDS = "//h6[text()='Leaves']/ancestor::div[contains(@class,'card')]//div[@role='button']"

    # Inside card
    EMPLOYEE_NAME = "xpath=.//strong[contains(@class,'fs-13')]"
    ADHOC_TAG = "xpath=.//span[contains(text(),'Ad hoc')]"
    LEAVE_TYPE = "xpath=.//span[contains(@class,'fs-13')]"
    LEAVE_STATUS = "xpath=.//div[contains(text(),'Approved') or contains(text(),'Not Approved')]"
    DATE_RANGE = "xpath=.//div[contains(@class,'fs-12')]"

    # Navigation
    LEAVE_DETAIL_BACK_BUTTON = "a.back-arrow-btn[href='/leave/']"

    # 🔥 FIXED strict mode issue
    DASHBOARD_MENU = "role=link[name='Dashboard']"

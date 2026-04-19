class WFHLocators:

    ##### WFH SECTION ######################

    # Section base
    WFH_SECTION = "//h6[text()='WFH']/ancestor::div[contains(@class,'card')]"

    # Cards
    WFH_CARDS = "//h6[text()='WFH']/ancestor::div[contains(@class,'card')]//div[@role='button']"

    WFH_TODAY_TAB = "//button[contains(@id,'WFH') and contains(text(),'Today')]"
    WFH_UPCOMING_TAB = "//button[contains(@id,'WFH') and contains(text(),'Upcoming')]"

    # Inside card - More flexible selectors
    WFH_EMPLOYEE_NAME = "xpath=.//strong[contains(@class,'fs-')]"
    WFH_TYPE = "xpath=.//span[contains(@class,'fs-')]"
    WFH_STATUS = "xpath=.//div[contains(text(),'Approved') or contains(text(),'Not Approved')]"

    # No Data
    WFH_NO_DATA = "//h6[text()='WFH']/ancestor::div//img[contains(@src,'no-data-found')]"

    # Back Button - More flexible selector
    WFH_DETAIL_BACK_BUTTON = "a.back-arrow-btn, button.back-button, [aria-label='Back']"
    
    # Dashboard menu
    WFH_DASHBOARD_MENU = "a[href*='/dashboard'], button:has-text('Dashboard')"

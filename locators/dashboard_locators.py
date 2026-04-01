import page


class DashboardLocators:

    ##### Birthday Section ######################

    TODAYS_BIRTHDAY = '[id="Today\'s-Birthday"]'
    UPCOMING_BIRTHDAY = '[id="Upcoming-Birthday"]'

    BIRTHDAY_SECTION = "div.birthdayCard"
    NO_DATA_FOUND = "img.noDataImg"
    EMPLOYEE_CARDS = ".slick-track > div:not(.slick-cloned)"

    NEXT_BUTTON = ".slick-next"
    PREVIOUS_BUTTON = ".slick-prev"

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

    ##### WFH SECTION ######################

    # Section base
    WFH_SECTION = "//h6[text()='WFH']/ancestor::div[contains(@class,'card')]"

    # Cards
    WFH_CARDS = "//h6[text()='WFH']/ancestor::div[contains(@class,'card')]//div[@role='button']"

    WFH_TODAY_TAB = "//button[contains(@id,'WFH') and contains(text(),'Today')]"
    WFH_UPCOMING_TAB = "//button[contains(@id,'WFH') and contains(text(),'Upcoming')]"

    # Inside card
    WFH_EMPLOYEE_NAME = "xpath=.//strong[contains(@class,'fs-13')]"
    WFH_TYPE = "xpath=.//span[contains(@class,'fs-13')]"
    WFH_STATUS = "xpath=.//div[contains(text(),'Approved') or contains(text(),'Not Approved')]"

    # No Data
    WFH_NO_DATA = "//h6[text()='WFH']/ancestor::div//img[contains(@src,'no-data-found')]"

    #Back Button
    WFH_DETAIL_BACK_BUTTON = "a.back-arrow-btn[href='/wfh/']"


####################################################################################
######## Live attendance ################################

    LIVE_ATTENDANCE_SECTION = "//h6[text()='LIVE Attendance']"
    IN_TAB = "#present"
    OUT_TAB = "#absent"
    YET_TO_CHECKIN_TAB = "#yetToCheckin"
    # ✅ ONLY STRING (Correct)
    EMPLOYEE_LIST = "div[role='row'] div[data-column-id='2']"

    ALL_ROWS = "div[role='row']"
    TABLE = "div[role='table']"
    NO_DATA = "text='There are no records to display'"


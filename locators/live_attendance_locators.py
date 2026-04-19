class LiveAttendanceLocators:

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

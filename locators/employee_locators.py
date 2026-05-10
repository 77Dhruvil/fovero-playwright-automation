"""
EMPLOYEE LOCATORS
=====================================================
FINAL UPDATED LOCATORS FILE
Based on actual Fovero Employee UI
"""

class EmployeeLocators:

    # =====================================================
    # MAIN EMPLOYEE PAGE
    # =====================================================
    EMPLOYEE_SECTION = "div[class*='employee'], div[class*='Employee'], table"
    EMPLOYEE_TABLE = "table"
    EMPLOYEE_ROWS = "tbody tr"

    # =====================================================
    # PAGE HEADER
    # =====================================================
    PAGE_TITLE = "text=Employee"
    TOTAL_EMPLOYEE_COUNT = "text=Total:"

    # =====================================================
    # SEARCH
    # =====================================================
    SEARCH_INPUT = "input#search"
    CLEAR_ICON = "div.css-5pujaa svg"

    # =====================================================
    # DEPARTMENT FILTER
    # =====================================================
    DEPARTMENT_DROPDOWN = "input[id*='react-select-2-input']"


    DEPARTMENT_OPTIONS = (
        "li, div[role='option']"
    )

    DEPARTMENT_CLEAR_ICON = "(//div[contains(@class,'css-5pujaa')])[1]"

    # =====================================================
    # STATUS FILTER
    # =====================================================
    STATUS_DROPDOWN = "input[id*='react-select-3-input']"

    STATUS_OPTION = "div[role='option']"

    STATUS_CLEAR_ICON = "(//div[contains(@class,'css-5pujaa')])[2]"

    # =====================================================
    # ACTIVE EMPLOYEE TOGGLE
    # =====================================================

    ACTIVE_EMPLOYEE_TOGGLE = "input#custom-switch"

    # =====================================================
    # BUTTONS
    # =====================================================
    ADD_EMPLOYEE_BUTTON = "button:has-text('Add Employee')"

    EXPORT_BUTTON = "button:has-text('Export')"

    # =====================================================
    # ADD EMPLOYEE MODAL
    # =====================================================
    ADD_MODAL = "div[role='dialog']"

    MODAL_TITLE = "text=Add Employee"

    MODAL_CLOSE_BUTTON = (
        "button[aria-label='Close'], "
        "button:has-text('×')"
    )

    MODAL_SAVE_BUTTON = (
        "button:has-text('Save')"
    )

    MODAL_CANCEL_BUTTON = (
        "button:has-text('Cancel')"
    )

    # =====================================================
    # TABLE HEADERS
    # =====================================================
    HEADER_EMP_ID = "th:has-text('Emp ID')"
    HEADER_NAME = "th:has-text('Name')"
    HEADER_DEPARTMENT = "th:has-text('Department')"
    HEADER_JOIN_DATE = "th:has-text('Join Date')"
    HEADER_EMAIL = "th:has-text('Email')"
    HEADER_LOGIN = "th:has-text('Login')"

    # =====================================================
    # TABLE COLUMN DATA
    # =====================================================
    EMPLOYEE_ROWS = "tbody tr"

    TABLE_EMP_ID = "td:nth-child(2)"
    TABLE_NAME = "td:nth-child(3)"
    TABLE_DEPARTMENT = "td:nth-child(5)"
    TABLE_JOIN_DATE = "td:nth-child(7)"
    TABLE_EMAIL = "td:nth-child(8)"
    TABLE_LOGIN_STATUS = "td:nth-child(9)"

    # =====================================================
    # LOGIN STATUS
    # =====================================================
    LOGIN_ENABLED = "text=Enabled"
    LOGIN_INVITED = "text=Invited"

    # =====================================================
    # PAGINATION
    # =====================================================
    PAGINATION_INFO = "text=/\\d+-\\d+ of \\d+/"

    PAGINATION_NEXT = (
        "button[aria-label='Go to next page'], "
        "button svg[data-testid='KeyboardArrowRightIcon']"
    )

    PAGINATION_PREVIOUS = (
        "button[aria-label='Go to previous page'], "
        "button svg[data-testid='KeyboardArrowLeftIcon']"
    )

    ROWS_PER_PAGE = (
        "div[role='button']:has-text('50')"
    )

    # =====================================================
    # FILTER OPTIONS
    # =====================================================
    FILTER_ACTIVE = "text=Active"
    FILTER_INACTIVE = "text=Inactive"
    FILTER_ENABLED = "text=Enabled"
    FILTER_INVITED = "text=Invited"

    # =====================================================
    # DEPARTMENT OPTIONS
    # =====================================================
    QA_TEAM_OPTION = "text=QA Team"
    MOBILE_TEAM_OPTION = "text=Mobile Team"
    UIUX_TEAM_OPTION = "text=UI / UX Team"
    MANAGEMENT_OPTION = "text=Management"

    # =====================================================
    # EMPTY / NO DATA
    # =====================================================
    NO_DATA_MESSAGE = (
        "text='No data', "
        "text='No employees found'"
    )

    # =====================================================
    # LOADER
    # =====================================================
    PAGE_LOADER = (
        "div[class*='loader'], "
        "div[class*='spinner'], "
        "svg[class*='spinner']"
    )

    # =====================================================
    # SUCCESS / ERROR MESSAGE
    # =====================================================
    SUCCESS_MESSAGE = (
        "div[class*='success'], "
        "div[role='alert']"
    )

    ERROR_MESSAGE = (
        "div[class*='error'], "
        "div[class*='danger']"
    )

    # =====================================================
    # ADD EMPLOYEE FORM
    # =====================================================

    EMPLOYEE_ID_INPUT = (
        "input[name='employeeId'], "
        "input[placeholder*='Employee ID']"
    )

    EMAIL_INPUT = (
        "input[type='email'], "
        "input[name='email']"
    )

    FIRST_NAME_INPUT = (
        "input[name='firstName'], "
        "input[placeholder*='First Name']"
    )

    LAST_NAME_INPUT = (
        "input[name='lastName'], "
        "input[placeholder*='Last Name']"
    )

    # =====================================================
    # DROPDOWNS
    # =====================================================

    GENDER_DROPDOWN = (
        "input[id*='gender']"
    )

    DEPARTMENT_FORM_DROPDOWN = (
        "input[id*='department']"
    )

    EMPLOYMENT_TYPE_DROPDOWN = (
        "input[id*='employment']"
    )

    ROLE_DROPDOWN = (
        "input[id*='role']"
    )

    REPORTING_TO_DROPDOWN = (
        "input[id*='reporting']"
    )

    # =====================================================
    # CHECKBOXES
    # =====================================================

    INVITE_CHECKBOX = (
        "input[type='checkbox']"
    )

    JOINING_WINDOW_CHECKBOX = (
        "input[type='checkbox']"
    )

    # =====================================================
    # BUTTONS
    # =====================================================

    SAVE_BUTTON = (
        "//button[contains(., 'Save')]"
    )

    CANCEL_BUTTON = (
        "//button[contains(., 'Cancel')]"
    )

    # =====================================================
    # SUCCESS / ERROR
    # =====================================================

    SUCCESS_MESSAGE = (
        ".toast-message, .alert-success"
    )

    VALIDATION_ERROR = (
        ".invalid-feedback, .error-message"
    )
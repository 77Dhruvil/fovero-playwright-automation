class AnnouncementLocators:
    """Locators for Announcement Module"""
    
    # Section - More specific to avoid strict mode violation
    ANNOUNCEMENT_SECTION = "div.card:has-text('Announcement'):has-text('Test')"
    ANNOUNCEMENT_CARD = "div:has(:text('Announcement')):has(button[aria-label*='Add'], button:has-text('+'))"
    
    # Fallback: Use xpath for more control
    ANNOUNCEMENT_SECTION_XPATH = "//div[contains(@class,'card')]//h6[text()='Announcement']/ancestor::div[contains(@class,'card')]"
    ANNOUNCEMENT_SECTION_ALT = "div[class*='card']:has-text('Announcement'):has-text('DP')"
    
    # Announcement List
    ANNOUNCEMENT_LIST = "div[class*='announcement']"
    ANNOUNCEMENT_ITEM = "div[role='button']:has-text('Automation Test Announcement')"
    ANNOUNCEMENT_ITEMS = "//div[@role='button' and contains(text(), 'Announcement')]"
    
    # Buttons
    ADD_ANNOUNCEMENT_BTN = "button:has-text('Add Announcement'), button:has-text('+'), button[aria-label*='Add'], button[title*='Add']"
    SAVE_BTN = "button:has-text('Save')"
    CANCEL_BTN = "button:has-text('Cancel'), button:has-text('Close')"
    CLOSE_MODAL_BTN = "button[aria-label='Close'], .btn-close, [role='button']:has-text('×')"
    
    # Form Fields
    TITLE_FIELD = "input[placeholder*='Title'], input[name='title'], input[type='text'][placeholder*='title']"
    DESCRIPTION_FIELD = "textarea[placeholder*='Description'], textarea[name='description']"
    SCHEDULE_DATE_FIELD = "input[type='date'], input[placeholder*='Schedule'], input[name='scheduleDate']"
    CATEGORY_DROPDOWN = "select[name='category'], div[role='combobox']:has-text('Category'), button:has-text('Category')"
    EMPLOYEE_DROPDOWN = "select[name='employee'], div[role='combobox']:has-text('Select employee'), button:has-text('Select employee')"
    
    # Dropdown Options
    DROPDOWN_OPTION = "//div[@role='option'], //li[@role='option']"
    CATEGORY_OPTION = "//div[@role='option' or @class*='option']:has-text"
    
    # Category Modal
    CATEGORY_MODAL = "div[role='dialog']:has-text('Category')"
    CATEGORY_INPUT = "input[placeholder='Enter category name']"
    CATEGORY_LIST = "//div[@class*='category']:has-text"
    CATEGORY_ITEM_EDIT = "button[aria-label*='Edit'], svg[class*='edit']"
    CATEGORY_ITEM_DELETE = "button[aria-label*='Delete'], svg[class*='delete'], button[class*='delete']"
    
    # Validation/Status
    ERROR_MESSAGE = "div[class*='error'], span[class*='error'], p[class*='error']"
    SUCCESS_MESSAGE = "div[class*='success'], span[class*='success']"
    NO_DATA = "text='No Data', text='No announcements'"
    
    # Modal
    MODAL = "div[role='dialog']"
    MODAL_TITLE = "h1, h2, h3, .modal-title"
    MODAL_CLOSE = "button[aria-label='Close'], button[class*='close']"

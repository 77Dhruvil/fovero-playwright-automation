class WorkTimingInsightsLocators:
    # Updated section locator to be strict and unique
    SECTION = "div.card:has(:text('Monthly Work Timing Insights')):has(:text('View All'))"
    TITLE = "text=Monthly Work Timing Insights"
    VIEW_ALL = "text=View All"
    
    # More flexible month label - looks for any text with month pattern
    MONTH_LABEL = "//div[contains(@class,'card')]//span[contains(text(),'2026') or contains(text(),'2025') or contains(text(),'2027')]"
    
    # Updated to be more flexible with structure
    STARTING_DAY = "//div[contains(text(),'Starting Day Early')]"
    ENDING_DAY = "//div[contains(text(),'Ending Day Late')]"
    REQUIRED_EXTRA_BREAK = "//div[contains(text(),'Required Extra Break')]"
    EXTRA_HOURS = "//div[contains(text(),'Extra Hours')]"
    
    AVG_START_TIME = "//div[contains(text(),'Avg Start Time')]"
    AVG_END_TIME = "//div[contains(text(),'Avg End Time')]"
    AVG_BREAK_TIME = "//div[contains(text(),'Avg Break Time')]"
    AVG_WORKING_TIME = "//div[contains(text(),'Avg Working Time')]"

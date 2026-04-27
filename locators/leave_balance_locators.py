class LeaveBalanceLocators:
    SECTION = "//h6[contains(.,'Leave Balance')]"
    TOTAL_LEAVES = "//span[contains(text(),'Total Leaves')]/following-sibling::span"
    APPLY_LEAVE_BUTTON = "//button[contains(.,'Apply Leave')]"
    CASUAL_LEAVE = ("//div[@class='card-body']//div[normalize-space()='Casual Leave']")
    COMP_OFF_LEAVE = "//div[contains(.,'Compensatory Off')]"
    CASUAL_LEAVE_TOTAL = "//div[contains(.,'Casual Leave')]//span[contains(@class,'leave-total')]"
    CASUAL_LEAVE_BOOKED = "//div[contains(.,'Casual Leave')]//span[contains(@class,'leave-booked')]"
    CASUAL_LEAVE_PENDING = "//div[contains(.,'Casual Leave')]//span[contains(@class,'leave-pending')]"
    COMP_OFF_TOTAL = "//div[contains(.,'Compensatory Off')]//span[contains(@class,'leave-total')]"
    COMP_OFF_BOOKED = "//div[contains(.,'Compensatory Off')]//span[contains(@class,'leave-booked')]"
    COMP_OFF_PENDING = "//div[contains(.,'Compensatory Off')]//span[contains(@class,'leave-pending')]"


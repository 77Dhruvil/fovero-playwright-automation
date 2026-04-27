import re
from locators.leave_balance_locators import LeaveBalanceLocators

class LeaveBalancePage:
    def __init__(self, page):
        self.page = page

    # Section visibility
    def is_section_visible(self):
        try:
            self.page.get_by_text("Leave Balance").wait_for(state="visible", timeout=10000)
            return True
        except:
            return False

    # Core function (condition-based per leave type)
    def get_leave_type_counts(self, leave_type: str):
        leave_type = leave_type.lower().strip()

        if leave_type == "casual leave":
            label = "Casual Leave"
        elif leave_type == "compensatory off":
            label = "Compensatory Off"
        else:
            raise ValueError(f"Unsupported leave type: {leave_type}")

        # Find the exact leave block (avoid multiple matches)
        leave_block = self.page.locator("div.card-body").filter(
            has_text=label
        )

        # Ensure block is visible
        leave_block.first.wait_for(state="visible")

        # Extract the text
        text = leave_block.inner_text()
        # Debug: raise AssertionError(f"Text for {label}: {repr(text)}")

        # Try different regex patterns
        patterns = [
            r"Total:\s*(\d+\.?\d*).*Booked:\s*(\d+\.?\d*).*Pending:\s*(\d+\.?\d*)",  # Total: X Booked: Y Pending: Z
            r"(\d+\.?\d*)\s*-\s*(\d+\.?\d*)\s*=\s*(\d+\.?\d*)",  # X - Y = Z (total - booked = pending)
            r"(\d+\.?\d*)\s*=\s*(\d+\.?\d*)\s*-\s*(\d+\.?\d*)",  # X = Y - Z (pending = total - booked)
            r"(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*)",  # X Y Z (total booked pending)
        ]

        match = None
        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL)
            if match:
                break

        if not match:
            raise AssertionError(f"Could not parse leave counts for {label}. Text: {repr(text)}")

        # Determine which pattern matched and assign accordingly
        if 'Total:' in text:
            total = float(match.group(1))
            booked = float(match.group(2))
            pending = float(match.group(3))
        elif '=' in text and '-' in text:
            if match.re.pattern == patterns[1]:  # X - Y = Z
                total = float(match.group(1))
                booked = float(match.group(2))
                pending = float(match.group(3))
            else:  # X = Y - Z
                pending = float(match.group(1))
                total = float(match.group(2))
                booked = float(match.group(3))
        else:
            # Assume X Y Z is total booked pending
            total = float(match.group(1))
            booked = float(match.group(2))
            pending = float(match.group(3))

        return {
            "total": total,
            "booked": booked,
            "pending": pending
        }

    # Validation logic
    def verify_pending_leaves(self, leave_type: str):
        counts = self.get_leave_type_counts(leave_type)

        # Condition: total - booked == pending
        return round(counts["total"] - counts["booked"], 2) == round(counts["pending"], 2)
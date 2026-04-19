from pages.base_page import BasePage
from locators.work_timing_insights_locators import WorkTimingInsightsLocators
import re

class WorkTimingInsightsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.section = page.locator(WorkTimingInsightsLocators.SECTION)

    def wait_for_section(self, timeout=10000):
        # Wait for the section to be visible, robustly
        try:
            self.page.wait_for_selector(WorkTimingInsightsLocators.SECTION, timeout=timeout)
            return True
        except Exception as e:
            print(f"[ERROR] Work Timing Insights section not found: {e}")
            return False

    def is_section_visible(self):
        # Wait for section before checking visibility
        found = self.wait_for_section(timeout=10000)
        if not found:
            return False
        try:
            return self.section.is_visible()
        except Exception as e:
            print(f"[ERROR] Section visibility check failed: {e}")
            return False

    def get_section_text(self):
        """Get all text from section for parsing"""
        try:
            return self.section.inner_text()
        except Exception as e:
            print(f"[ERROR] Failed to get section text: {e}")
            return ""

    def get_all_section_text(self):
        """Get all text from the section for debugging"""
        return self.get_section_text()

    def get_title(self):
        try:
            return self.section.locator(WorkTimingInsightsLocators.TITLE).first.inner_text()
        except Exception as e:
            print(f"[ERROR] Title not found: {e}")
            return ""

    def click_view_all(self):
        try:
            self.section.locator(WorkTimingInsightsLocators.VIEW_ALL).click()
            print("[INFO] Clicked View All button")
        except Exception as e:
            print(f"[ERROR] Failed to click View All: {e}")

    def get_month_label(self):
        """Extract month label from section text"""
        try:
            text = self.get_section_text()
            # Look for pattern like "MARCH 2026"
            match = re.search(r'(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s+(\d{4})', text)
            if match:
                return match.group(0)
            return ""
        except Exception as e:
            print(f"[ERROR] Month label parsing failed: {e}")
            return ""

    def get_starting_day_text(self):
        """Extract starting day text from section"""
        try:
            text = self.get_section_text()
            # Look for "Starting Day Early by ..." pattern
            match = re.search(r'Starting Day Early by (.+?)(?:\n|Avg)', text)
            if match:
                return f"Starting Day Early by {match.group(1).strip()}"
            return ""
        except Exception as e:
            print(f"[ERROR] Starting Day parsing failed: {e}")
            return ""

    def get_ending_day_text(self):
        """Extract ending day text from section"""
        try:
            text = self.get_section_text()
            # Look for "Ending Day Late by ..." pattern
            match = re.search(r'Ending Day Late by (.+?)(?:\n|Required)', text)
            if match:
                return f"Ending Day Late by {match.group(1).strip()}"
            return ""
        except Exception as e:
            print(f"[ERROR] Ending Day parsing failed: {e}")
            return ""

    def get_required_extra_break_text(self):
        """Extract required extra break from section"""
        try:
            text = self.get_section_text()
            # Look for "Required Extra Break ..." pattern
            match = re.search(r'Required Extra Break\s+(.+?)(?:\n|Avg)', text)
            if match:
                return f"Required Extra Break {match.group(1).strip()}"
            return ""
        except Exception as e:
            print(f"[ERROR] Required Extra Break parsing failed: {e}")
            return ""

    def get_extra_hours_text(self):
        """Extract extra hours from section"""
        try:
            text = self.get_section_text()
            # Look for "Extra Hours ..." pattern
            match = re.search(r'Extra Hours\s+(.+?)(?:\n|Avg)', text)
            if match:
                return f"Extra Hours {match.group(1).strip()}"
            return ""
        except Exception as e:
            print(f"[ERROR] Extra Hours parsing failed: {e}")
            return ""

    def get_avg_start_time(self):
        """Extract average start time from section"""
        try:
            text = self.get_section_text()
            # Look for "Avg Start Time : ..." pattern
            match = re.search(r'Avg Start Time\s*:\s*(.+?)(?:\n)', text)
            if match:
                return match.group(1).strip()
            return ""
        except Exception as e:
            print(f"[ERROR] Avg Start Time parsing failed: {e}")
            return ""

    def get_avg_end_time(self):
        """Extract average end time from section"""
        try:
            text = self.get_section_text()
            # Look for "Avg End Time : ..." pattern
            match = re.search(r'Avg End Time\s*:\s*(.+?)(?:\n)', text)
            if match:
                return match.group(1).strip()
            return ""
        except Exception as e:
            print(f"[ERROR] Avg End Time parsing failed: {e}")
            return ""

    def get_avg_break_time(self):
        """Extract average break time from section"""
        try:
            text = self.get_section_text()
            # Look for "Avg Break Time : ..." pattern
            match = re.search(r'Avg Break Time\s*:\s*(.+?)(?:\n)', text)
            if match:
                return match.group(1).strip()
            return ""
        except Exception as e:
            print(f"[ERROR] Avg Break Time parsing failed: {e}")
            return ""

    def get_avg_working_time(self):
        """Extract average working time from section"""
        try:
            text = self.get_section_text()
            # Look for "Avg Working Time : ..." pattern
            match = re.search(r'Avg Working Time\s*:\s*(.+?)(?:\n|$)', text)
            if match:
                return match.group(1).strip()
            return ""
        except Exception as e:
            print(f"[ERROR] Avg Working Time parsing failed: {e}")
            return ""

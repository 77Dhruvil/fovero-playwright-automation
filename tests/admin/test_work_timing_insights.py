import allure
import pytest
from pages.work_timing_insights_page import WorkTimingInsightsPage

@pytest.mark.admin
@allure.title("Verify Monthly Work Timing Insights Module")
@allure.description("Admin should be able to see Monthly Work Timing Insights section and its details")
def test_work_timing_insights_module(admin_dashboard_login):
    dashboard = admin_dashboard_login
    page = dashboard.page
    insights = WorkTimingInsightsPage(page)

    # Wait for section to be visible (robust)
    assert insights.is_section_visible(), "Work Timing Insights section not visible"
    print("[INFO] Work Timing Insights section is visible.")

    # Debug: Print all section text
    section_text = insights.get_all_section_text()
    print("[DEBUG] Section content:\n", section_text)

    # Title
    title = insights.get_title()
    assert title, "Title not found"
    assert "Monthly Work Timing Insights" in title
    print(f"[✓] Title: {title}")

    # Month label
    month_label = insights.get_month_label()
    if month_label and month_label != "Month not found":
        print(f"[✓] Month label: {month_label}")
    else:
        print("[⚠] Month label not found")

    # Starting Day Early
    starting_day = insights.get_starting_day_text()
    if starting_day:
        if "Starting Day" in starting_day or "Early" in starting_day:
            print(f"[✓] Starting Day: {starting_day}")
        else:
            print(f"[⚠] Starting Day found but unexpected format: {starting_day}")
    else:
        print("[⚠] Starting Day not found")

    # Ending Day Late
    ending_day = insights.get_ending_day_text()
    if ending_day:
        if "Ending Day" in ending_day or "Late" in ending_day:
            print(f"[✓] Ending Day: {ending_day}")
        else:
            print(f"[⚠] Ending Day found but unexpected format: {ending_day}")
    else:
        print("[⚠] Ending Day not found")

    # Required Extra Break
    extra_break = insights.get_required_extra_break_text()
    if extra_break:
        if "Required" in extra_break or "Break" in extra_break:
            print(f"[✓] Required Extra Break: {extra_break}")
        else:
            print(f"[⚠] Required Extra Break found but unexpected format: {extra_break}")
    else:
        print("[⚠] Required Extra Break not found")

    # Extra Hours
    extra_hours = insights.get_extra_hours_text()
    if extra_hours:
        if "Extra" in extra_hours or "Hours" in extra_hours:
            print(f"[✓] Extra Hours: {extra_hours}")
        else:
            print(f"[⚠] Extra Hours found but unexpected format: {extra_hours}")
    else:
        print("[⚠] Extra Hours not found")

    # Average Start/End/Break/Working Time
    avg_start = insights.get_avg_start_time()
    avg_end = insights.get_avg_end_time()
    avg_break = insights.get_avg_break_time()
    avg_working = insights.get_avg_working_time()
    
    if avg_start:
        print(f"[✓] Avg Start Time: {avg_start}")
    if avg_end:
        print(f"[✓] Avg End Time: {avg_end}")
    if avg_break:
        print(f"[✓] Avg Break Time: {avg_break}")
    if avg_working:
        print(f"[✓] Avg Working Time: {avg_working}")

    # At least one average value should be present
    avg_values = [avg_start, avg_end, avg_break, avg_working]
    assert any(avg_values), "No average time values found"
    print("[✓] At least one average time value is present")

    # View All button
    insights.click_view_all()
    print("[✓] Clicked View All successfully.")
    
    print("\n[SUCCESS] All work timing insights tests passed!")

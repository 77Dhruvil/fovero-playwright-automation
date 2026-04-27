import pytest
from pages.leave_balance_page import LeaveBalancePage

# @pytest.mark.smoke
#@pytest.mark.usefixtures("login_fixture")
def test_leave_balance_functionality(admin_dashboard_login):
    leave_balance = LeaveBalancePage(admin_dashboard_login.page)
    # Check section is visible
    try:
        visible = leave_balance.is_section_visible()
        print(f"Leave Balance section visible: {visible}")
        assert visible, "Leave Balance section should be visible for all users."
    except AssertionError:
        admin_dashboard_login.page.reload()
        admin_dashboard_login.page.wait_for_timeout(1500)
        visible = leave_balance.is_section_visible()
        print(f"After reload, Leave Balance section visible: {visible}")
        assert visible, "Leave Balance section should be visible for all users."
    # Check for both leave types
    for leave_type in ["casual leave", "compensatory off"]:
        counts = leave_balance.get_leave_type_counts(leave_type)
        verification = leave_balance.verify_pending_leaves(leave_type)
        print(f"For {leave_type}: total={counts['total']}, booked={counts['booked']}, pending={counts['pending']}, verification (total - booked == pending): {verification}")
        assert counts["total"] >= 0, f"Total leaves for {leave_type} should be >= 0"
        assert counts["booked"] >= 0, f"Booked leaves for {leave_type} should be >= 0"
        assert counts["pending"] >= 0, f"Pending leaves for {leave_type} should be >= 0"

import pytest


@pytest.mark.admin
def test_admin_dashboard_complete_flow(admin_dashboard):

    dashboard = admin_dashboard

    # ✅ Graph validation
#    assert dashboard.is_graph_visible()

  #  dashboard.open_graph_filter()
    # dashboard.select_this_fiscal()
    #
    # dashboard.open_graph_filter()
    # dashboard.select_previous_fiscal()
    #
    # # Click graph bars
    # for _ in range(2):
    #     dashboard.click_graph_bar()
    #     dashboard.close_graph_popup()

    # ✅ Birthday
    dashboard.open_upcoming_birthday()

    # ✅ Live Attendance
    dashboard.open_live_attendance()

    # ✅ Leaves & WFH
    dashboard.open_upcoming_leaves()
    dashboard.open_upcoming_wfh()

    # ✅ Productivity Tabs
    dashboard.open_departures()
    dashboard.open_breaks()
    dashboard.open_productivity()

    # ✅ Announcement
    dashboard.click_add_announcement()

    # ✅ Apply Leave
    dashboard.click_apply_leave()

    # Back to dashboard
    dashboard.go_to_dashboard()
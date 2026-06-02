from playwright.sync_api import expect

from pages.Attendance_and_productivity_insights_page import AttendanceAndProductivityInsights


def test_attendance_and_productivity_dashboard(admin_dashboard_login):

    att = AttendanceAndProductivityInsights(admin_dashboard_login)

    # =========================
    # SECTION CHECK
    # =========================
    att.section_header().wait_for(state="visible")
    assert att.section_header().is_visible()

    # =========================
    # ARRIVALS
    # =========================
    att.click_arrivals()

    assert att.get_block("Top 5 Late Arrivals").is_visible()
    assert att.get_block("Top 5 Early Arrivals").is_visible()

    # =========================
    # DEPARTURES
    # =========================
    att.click_departures()

    expect(att.get_block("Top 5 Early Departures")).to_be_visible()
    expect(att.get_block("Top 5 Late Departures")).to_be_visible()

    # =========================
    # BREAKS
    # =========================
    att.click_breaks()

    expect(att.get_block("Top 5 Extended Break Hours")).to_be_visible()
    expect(att.get_block("Top 5 Minimal Break Hours")).to_be_visible()

    # =========================
    # PRODUCTIVITY
    # =========================
    att.click_productivity()

    expect(att.get_block("Top 5 Low Productivity Hours")).to_be_visible()
    expect(att.get_block("Top 5 High Productivity Hours")).to_be_visible()

    # =========================
    # NO DATA CHECK
    # =========================
    assert isinstance(att.is_no_data_visible(),bool)
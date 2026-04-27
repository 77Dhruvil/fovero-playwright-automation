from pages.setting_page import SettingsPage
from pages.live_attendance_page import LiveAttendancePage


def test_live_attendance_logic(admin_dashboard_login):

    dashboard = admin_dashboard_login
    settings = SettingsPage(dashboard.page)

    # Create page object directly
    live_attendance = LiveAttendancePage(
        dashboard.page
    )

    print("\n========== LIVE ATTENDANCE TEST START ==========")

    # YET
    live_attendance.click_tab("yet")
    yet_count, yet_names = live_attendance.get_attendance_data()

    print("Yet Count:", yet_count)
    print("Yet Names:", yet_names)


    # IN
    live_attendance.click_tab("in")
    in_count, in_names = live_attendance.get_attendance_data()

    print("IN Count:", in_count)
    print("IN Names:", in_names)


    # OUT
    live_attendance.click_tab("out")
    out_count, out_names = live_attendance.get_attendance_data()

    print("OUT Count:", out_count)
    print("OUT Names:", out_names)


    # Validation
    for name in in_names:
        assert name not in yet_names, (
            f"{name} exists in Yet and IN"
        )

    for name in out_names:
        assert name not in yet_names, (
            f"{name} exists in Yet and OUT"
        )

    print("Validation Passed")

    live_attendance.close_modal_if_open()

    settings.go_to_settings()

    print("========== TEST COMPLETED ==========")
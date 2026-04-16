from pages.setting_page import SettingsPage

def test_live_attendance_logic(admin_dashboard_login):
    dashboard = admin_dashboard_login
    settings = SettingsPage(dashboard.page)

    print("\n========== LIVE ATTENDANCE TEST START ==========")

    # ================= YET =================
    # YET
    dashboard.click_tab("yet")
    yet_count, yet_names = dashboard.get_attendance_data()

    print(f"👉 Yet Count: {yet_count}")
    print(f"👉 Yet Names: {yet_names}")

    # IN
    dashboard.click_tab("in")
    in_count, in_names = dashboard.get_attendance_data()

    print(f"👉 IN Count: {in_count}")
    print(f"👉 IN Names: {in_names}")

    # OUT
    dashboard.click_tab("out")
    out_count, out_names = dashboard.get_attendance_data()

    print(f"👉 OUT Count: {out_count}")
    print(f"👉 OUT Names: {out_names}")
    # ================= VALIDATION =================
    print("\n🔍 Validating IN/OUT not in YET...")

    for name in in_names:
        assert name not in yet_names, f"❌ {name} in Yet & IN"

    for name in out_names:
        assert name not in yet_names, f"❌ {name} in Yet & OUT"

    print("✅ Validation Passed")

    # ================= SETTINGS =================
    dashboard.close_modal_if_open()
    settings.go_to_settings()

    print("========== TEST COMPLETED ==========\n")
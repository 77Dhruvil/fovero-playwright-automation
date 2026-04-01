from pages.setting_page import SettingsPage


def test_live_attendance_logic(admin_dashboard_login):
    dashboard = admin_dashboard_login
    settings = SettingsPage(dashboard.page)

    print("\n========== LIVE ATTENDANCE TEST START ==========")

    # STEP 1 - YET
    dashboard.click_tab("yet")

    if dashboard.is_no_data_found():
        print("✅ No Yet-to-checkin data")
        yet_names = []
    else:
        yet_names = dashboard.get_employee_names()
        print(f"👉 Yet Count: {len(yet_names)}")
        print(f"👉 Yet Names: {yet_names}")

    # STEP 2 - IN
    dashboard.click_tab("in")

    if dashboard.is_no_data_found():
        print("✅ No IN data")
        in_names = []
    else:
        in_names = dashboard.get_employee_names()
        print(f"👉 IN Count: {len(in_names)}")
        print(f"👉 IN Names: {in_names}")

    # STEP 3 - OUT
    dashboard.click_tab("out")

    if dashboard.is_no_data_found():
        print("✅ No OUT data")
        out_names = []
    else:
        out_names = dashboard.get_employee_names()
        print(f"👉 OUT Count: {len(out_names)}")
        print(f"👉 OUT Names: {out_names}")

    # VALIDATION 1
    print("\n🔍 Validating IN/OUT not in YET...")

    for name in in_names:
        assert name not in yet_names, f"❌ {name} found in Yet & IN"

    for name in out_names:
        assert name not in yet_names, f"❌ {name} found in Yet & OUT"

    print("✅ Validation Passed")

    # STEP 4 - SETTINGS
    dashboard.close_modal_if_open()
    settings.go_to_settings()

    print("✅ Navigated to Settings Successfully")

    print("========== TEST COMPLETED ==========\n")
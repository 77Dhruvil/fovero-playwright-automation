import allure


@allure.title("Verify Birthday  Functionality")
@allure.description("Admin should be able to get all the Birthday Section data properly")
def test_birthday_section(admin_dashboard_login):
    dashboard = admin_dashboard_login

    # =========================
    # 🔥 TODAY TAB
    # =========================
    print("\n--- Testing TODAY Birthday ---")

    dashboard.click_birthday_tab("today")

    if dashboard.is_no_data_found():
        print("✅ Today: No Data Found")

    else:
        count = dashboard.get_employee_count()
        print(f"Today Count: {count}")

        if count <= 2:
            assert not dashboard.is_next_button_visible()
        else:
            assert dashboard.is_next_button_visible()


    # =========================
    # 🔥 UPCOMING TAB
    # =========================
    print("\n--- Testing UPCOMING Birthday ---")

    dashboard.click_birthday_tab("upcoming")

    if dashboard.is_no_data_found():
        print("✅ Upcoming: No Data Found")

    else:
        count = dashboard.get_employee_count()
        print(f"Upcoming Count: {count}")

        if count <= 2:
            assert not dashboard.click_next_button()
            assert not dashboard.click_previous_button()
        else:
            assert dashboard.click_next_button()
            assert dashboard.click_previous_button()


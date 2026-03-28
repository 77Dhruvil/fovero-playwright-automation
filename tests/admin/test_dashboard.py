def test_birthday_section(admin_dashboard_login):
    dashboard = admin_dashboard_login

    dashboard.get_Todaybirthday_tab()

    # Case 1: No Data
    if dashboard.is_no_data_found():
        print("✅ No Data Found")
        return

    # Get count
    count = dashboard.get_employee_count()
    print(f"Employee Count: {count}")

    # Case 2: Single
    if count == 1:
        print("✅ Single Birthday - No navigation")
        return

    # Case 3: Two users (IMPORTANT FIX)
    if count == 2:
        print("✅ Two Birthdays - Still no navigation")

        # Ensure buttons NOT visible
        assert not dashboard.click_next_button(), "❌ Next should not be visible"
        assert not dashboard.click_previous_button(), "❌ Prev should not be visible"
        return

    # Case 4: More than 2 users
    if count > 2:
        print("✅ Multiple Birthdays (>2)")

        assert dashboard.click_next_button(), "❌ Next button not visible"
        assert dashboard.click_previous_button(), "❌ Previous button not visible"
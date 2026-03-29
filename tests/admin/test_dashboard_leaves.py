import allure
import pytest


@pytest.mark.admin
@allure.title("Verify Leave Functionality")
@allure.description("Admin should be able to see all the leaves of other users")
def test_leaves_complete_validation(admin_dashboard_login):

    dashboard = admin_dashboard_login

    # =====================================================
    # 🔵 TODAY TAB
    # =====================================================
    dashboard.click_today_leaves()

    today_count = dashboard.get_today_leaves_count()
    print("Today Count:", today_count)

    assert dashboard.is_today_tab_active()

    no_data = dashboard.is_leaves_no_data_visible()
    cards_count = dashboard.get_leave_cards_count()

    print("Today No Data:", no_data)
    print("Today Cards:", cards_count)

    # 🔥 FINAL LOGIC
    if cards_count > 0:
        for i in range(cards_count):
            data = dashboard.get_leave_card_data(i)

            print(f"Today Card {i}:", data)

            assert data["name"]
            assert data["leave_type"]

            assert any(
                keyword in data["leave_type"]
                for keyword in ["Full Day", "Half", "Days"]
            )

    elif no_data:
        assert True

    else:
        pytest.fail("Today tab: UI not stable (no cards & no no-data)")

    # Navigation
    if cards_count > 0:
        current_url = dashboard.page.url

        dashboard.click_leave_card(0)
        dashboard.page.wait_for_load_state("load")

        assert current_url != dashboard.page.url

        dashboard.page.go_back()
        dashboard.page.wait_for_load_state("load")

    # =====================================================
    # 🟢 UPCOMING TAB
    # =====================================================
    dashboard.click_upcoming_leaves()

    upcoming_count = dashboard.get_upcoming_leaves_count()
    print("Upcoming Count:", upcoming_count)

    assert dashboard.is_upcoming_tab_active()

    no_data = dashboard.is_leaves_no_data_visible()
    cards_count = dashboard.get_leave_cards_count()

    print("Upcoming No Data:", no_data)
    print("Upcoming Cards:", cards_count)

    # 🔥 FINAL LOGIC (NO FAIL CASE)
    if cards_count > 0:
        for i in range(cards_count):
            data = dashboard.get_leave_card_data(i)

            print(f"Upcoming Card {i}:", data)

            assert data["name"]
            assert data["leave_type"]

    elif no_data:
        assert True

    else:
        pytest.fail("Upcoming tab: UI not stable (no cards & no no-data)")
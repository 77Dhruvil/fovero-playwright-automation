import pytest
import allure


@pytest.mark.admin
@allure.title("Verify WFH Functionality")
def test_wfh_complete_validation(admin_dashboard_login):

    dashboard = admin_dashboard_login

    # =====================================================
    # 🔵 TODAY TAB
    # =====================================================

    dashboard.click_wfh_today_tab()
    dashboard.wait_for_wfh_section()

    assert dashboard.is_wfh_today_active()

    today_cards = dashboard.get_wfh_cards_count()
    no_data = dashboard.is_wfh_no_data_visible()

    print("\nWFH Today Cards:", today_cards)
    print("WFH Today No Data:", no_data)

    if today_cards > 0:

        for i in range(today_cards):
            data = dashboard.get_wfh_card_data(i)
            print(f"Today Card {i}:", data)

            assert data["name"]
            assert data["type"]
            assert any(x in data["type"] for x in ["Full Day", "Half"])

        # navigation
        current_url = dashboard.page.url

        dashboard.click_wfh_card(0)
        dashboard.page.wait_for_load_state("load")

        assert dashboard.page.url != current_url

        if dashboard.page.locator("a.back-arrow-btn").count() > 0:
            dashboard.page.locator("a.back-arrow-btn").click()
        else:
            dashboard.page.go_back()

        dashboard.page.wait_for_load_state("load")

    elif no_data:
        assert True
    else:
        pytest.fail("WFH Today tab unstable (no cards & no no-data)")


    # =====================================================
    # 🟢 UPCOMING TAB
    # =====================================================
    dashboard.click_dashboard_menu()
    dashboard.click_wfh_upcoming_tab()
    dashboard.wait_for_wfh_section()

    assert dashboard.is_wfh_upcoming_active()

    upcoming_cards = dashboard.get_wfh_cards_count()
    no_data = dashboard.is_wfh_no_data_visible()

    print("\nWFH Upcoming Cards:", upcoming_cards)
    print("WFH Upcoming No Data:", no_data)

    if upcoming_cards > 0:

        for i in range(upcoming_cards):
            data = dashboard.get_wfh_card_data(i)

            print(f"Upcoming Card {i}:", data)

            assert data["name"]
            assert data["type"]
            assert any(x in data["type"] for x in ["Full Day", "Half"])

    elif no_data:
        assert True
    else:
        pytest.fail("WFH Upcoming unstable")
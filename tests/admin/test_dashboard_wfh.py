import pytest


@pytest.mark.admin
def test_wfh_complete_validation(admin_dashboard_login):

    dashboard = admin_dashboard_login

    # =====================================================
    # 🔵 TODAY TAB
    # =====================================================
    dashboard.click_wfh_today_tab()

    assert dashboard.is_wfh_today_active()

    today_cards = dashboard.get_wfh_cards_count()
    print("WFH Today Cards:", today_cards)

    if today_cards == 0:
        assert dashboard.is_wfh_no_data_visible()

    else:
        for i in range(today_cards):

            data = dashboard.get_wfh_card_data(i)
            print(f"WFH Today Card {i}:", data)

            assert data["name"] != ""
            assert data["type"] != ""

            assert any(
                keyword in data["type"]
                for keyword in ["Full Day", "Half"]
            )

        # Navigation check
        current_url = dashboard.page.url

        dashboard.click_wfh_card(0)
        dashboard.page.wait_for_load_state("load")

        assert current_url != dashboard.page.url

        # Back handling
        if dashboard.page.locator("a.back-arrow-btn").count() > 0:
            dashboard.click_wfh_detail_back_button()
            dashboard.page.wait_for_load_state("load")
        else:
            dashboard.page.go_back()
            dashboard.page.wait_for_load_state("load")

        dashboard.click_dashboard_menu()
        dashboard.wait_for_wfh_section()

    # =====================================================
    # 🟢 UPCOMING TAB
    # =====================================================
    dashboard.click_wfh_upcoming_tab()

    assert dashboard.is_wfh_upcoming_active()

    upcoming_cards = dashboard.get_wfh_cards_count()
    print("WFH Upcoming Cards:", upcoming_cards)

    if upcoming_cards == 0:
        assert dashboard.is_wfh_no_data_visible()

    else:
        for i in range(upcoming_cards):

            data = dashboard.get_wfh_card_data(i)
            print(f"WFH Upcoming Card {i}:", data)

            assert data["name"] != ""
            assert data["type"] != ""

            assert any(
                keyword in data["type"]
                for keyword in ["Full Day", "Half"]
            )
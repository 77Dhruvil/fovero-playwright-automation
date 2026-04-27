import pytest
import allure

from pages.wfh_page import WFHPage


@pytest.mark.admin
@allure.title("WFH Section Comprehensive Functionality Test")
@allure.description(
    "Validate Today and Upcoming WFH tabs, cards, no-data and navigation"
)
def test_wfh_functionality(
    admin_dashboard_login
):

    wfh = WFHPage(
        admin_dashboard_login.page
    )

    print("\n" + "=" * 80)
    print("WFH COMPREHENSIVE TEST START")
    print("=" * 80)

    # ====================================================
    # TODAY TAB
    # ====================================================

    print("\n[STEP] Open Today WFH tab")
    wfh.click_wfh_today_tab()
    wfh.wait_for_wfh_section()

    assert wfh.is_wfh_today_active(), \
        "Today WFH tab not active"

    today_cards = wfh.get_wfh_cards_count()
    no_data = wfh.is_wfh_no_data_visible()

    print(f"Today Cards: {today_cards}")
    print(f"No Data Visible: {no_data}")

    if today_cards > 0:

        for i in range(today_cards):

            data = wfh.get_wfh_card_data(i)

            print(f"Card {i}: {data}")

            assert data["name"], "Employee name missing"
            assert data["type"], "WFH type missing"

            assert any(
                x in data["type"]
                for x in ["Full Day", "Half"]
            )

        # -----------------------------
        # Card Navigation Validation
        # -----------------------------
        print("\n[STEP] Validate card click navigation")

        current_url = page.url

        if wfh.click_wfh_card(0):

            page.wait_for_timeout(1000)

            new_url = page.url

            assert current_url != new_url, \
                "Card click did not navigate"

            print("Navigation success")

            if wfh.go_back_to_dashboard():
                page.wait_for_timeout(1000)

    elif no_data:

        print("No WFH records for today")

    else:

        pytest.fail(
            "Today tab unstable (no cards and no no-data)"
        )

    # ====================================================
    # UPCOMING TAB
    # ====================================================

    print("\n[STEP] Open Upcoming WFH tab")

    wfh.click_wfh_upcoming_tab()
    wfh.wait_for_wfh_section()

    assert wfh.is_wfh_upcoming_active(), \
        "Upcoming WFH tab not active"

    upcoming_cards = wfh.get_wfh_cards_count()
    no_data = wfh.is_wfh_no_data_visible()

    print(f"Upcoming Cards: {upcoming_cards}")
    print(f"No Data Visible: {no_data}")

    if upcoming_cards > 0:

        for i in range(upcoming_cards):

            data = wfh.get_wfh_card_data(i)

            print(f"Upcoming Card {i}: {data}")

            assert data["name"], \
                "Employee name missing"

            assert data["type"], \
                "WFH type missing"

            assert any(
                x in data["type"]
                for x in ["Full Day", "Half"]
            )

    elif no_data:

        print("No upcoming WFH records")

    else:

        pytest.fail(
            "Upcoming tab unstable (no cards and no no-data)"
        )

    # ====================================================
    # STATUS VALIDATION
    # ====================================================

    print("\n[STEP] Final status validation")

    status = wfh.get_wfh_status()

    print(status)

    assert "cards_count" in status
    assert "has_no_data" in status

    print("\n" + "=" * 80)
    print("WFH TEST PASSED")
    print("=" * 80)
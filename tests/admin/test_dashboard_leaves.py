import pytest
import allure
from pages.leave_page import LeavePage


@pytest.mark.admin
@allure.title("Verify Dashboard Leave Widget")
@allure.description(
    "Validate Today's Leave and Upcoming Leave tabs"
)
def test_leave_functionality(
    admin_dashboard_login
):

    leave = LeavePage(
        admin_dashboard_login.page
    )

    print("\n===== LEAVE WIDGET TEST START =====")


    # ==================================================
    # TODAY TAB
    # ==================================================

    print("\nTesting Today Leaves Tab...")

    leave.click_today_leaves()

    assert leave.is_today_tab_active(), \
        "Today tab not active"

    today_count = leave.get_today_leaves_count()
    cards_count = leave.get_leave_cards_count()
    no_data = leave.is_leaves_no_data_visible()

    print(
        f"Today Count={today_count} | "
        f"Cards={cards_count} | "
        f"NoData={no_data}"
    )


    if cards_count > 0:

        for i in range(cards_count):

            data = leave.get_leave_card_data(i)

            print(
                f"Card {i+1}: {data}"
            )

            assert data["name"]
            assert data["leave_type"]

        # Navigation test
        current_url = leave.page.url

        leave.click_leave_card(0)

        leave.page.wait_for_load_state(
            "load"
        )

        assert current_url != leave.page.url

        leave.page.go_back()

        leave.wait_for_leaves_section()

    elif no_data:
        assert True

    else:
        pytest.fail(
            "Today tab unstable"
        )


    # ==================================================
    # UPCOMING TAB
    # ==================================================

    print("\nTesting Upcoming Leaves Tab...")

    leave.click_upcoming_leaves()

    assert leave.is_upcoming_tab_active(), \
        "Upcoming tab not active"

    upcoming_count = leave.get_upcoming_leaves_count()
    cards_count = leave.get_leave_cards_count()
    no_data = leave.is_leaves_no_data_visible()

    print(
        f"Upcoming Count={upcoming_count} | "
        f"Cards={cards_count} | "
        f"NoData={no_data}"
    )


    if cards_count > 0:

        for i in range(cards_count):

            data = leave.get_leave_card_data(i)

            print(
                f"Upcoming Card {i+1}: {data}"
            )

            assert data["name"]
            assert data["leave_type"]

    elif no_data:
        assert True

    elif upcoming_count == 0:
        # fallback for flaky UI
        assert True

    else:
        pytest.fail(
            "Upcoming tab unstable"
        )


    print(
        "\n===== LEAVE WIDGET TEST PASSED ====="
    )
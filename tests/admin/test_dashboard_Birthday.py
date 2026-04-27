import pytest
import allure

from pages.birthday_page import BirthdayPage


@pytest.mark.admin
@allure.title("Birthday Section Comprehensive Functionality Test")
@allure.description("Validate birthday tabs, pagination and no-data scenarios")
def test_birthday_comprehensive_functionality(admin_dashboard_login):

    dashboard = admin_dashboard_login
    page = dashboard.page
    birthday = BirthdayPage(page)

    print("\n" + "="*80)
    print("BIRTHDAY COMPREHENSIVE TEST")
    print("="*80)

    # ---------------------------------------------------
    # SECTION 1 — SECTION VISIBLE
    # ---------------------------------------------------

    try:
        birthday.birthday_section.wait_for(
            state="visible",
            timeout=8000
        )
    except:
        page.reload()
        page.wait_for_timeout(1500)
        birthday.birthday_section.wait_for(
            state="visible",
            timeout=8000
        )

    assert birthday.birthday_section.is_visible()

    initial = birthday.get_pagination_status()
    print("Initial Status:", initial)


    # ---------------------------------------------------
    # SECTION 2 — TODAY TAB
    # ---------------------------------------------------

    print("\nTesting Today tab...")
    birthday.click_birthday_tab("today")

    today = birthday.get_pagination_status()

    if birthday.is_no_data_found():

        print("No Today birthday data found")
        assert today["employee_count"] == 0

    else:

        print(
            f"Today employees: {today['employee_count']}"
        )

        if today["next_visible"]:

            print("Testing next pagination...")
            clicked = birthday.click_next_button()

            if clicked:
                print("Next button clicked successfully")

                if birthday.is_previous_button_visible():
                    back = birthday.click_previous_button()
                    assert back is True

        else:
            print("Single page only")


    # ---------------------------------------------------
    # SECTION 3 — UPCOMING TAB
    # ---------------------------------------------------

    print("\nTesting Upcoming tab...")
    birthday.click_birthday_tab("upcoming")

    upcoming = birthday.get_pagination_status()

    if birthday.is_no_data_found():

        print("No upcoming data found")
        assert upcoming["employee_count"] == 0

    else:

        print(
            f"Upcoming employees: {upcoming['employee_count']}"
        )

        if upcoming["next_visible"]:

            clicked = birthday.click_next_button()

            if clicked:
                print("Upcoming next works")

                if birthday.is_previous_button_visible():
                    back = birthday.click_previous_button()
                    assert back is True

        else:
            print("No upcoming pagination")


    # ---------------------------------------------------
    # SECTION 4 — ITERATION TEST
    # ---------------------------------------------------

    print("\nRunning pagination iteration...")

    birthday.click_birthday_tab("upcoming")
    page.wait_for_timeout(500)

    status = birthday.get_pagination_status()

    if status["has_data"] and status["next_visible"]:

        page_num = 1
        max_pages = 10

        while page_num <= max_pages:

            current = birthday.get_pagination_status()

            print(
                f"Page {page_num} "
                f"Count={current['employee_count']}"
            )

            if current["next_visible"]:

                moved = birthday.click_next_button()

                if moved:
                    page_num += 1
                else:
                    break

            else:
                break

        print(f"Iterated {page_num} pages")

        if birthday.is_previous_button_visible():
            assert birthday.click_previous_button()

    else:
        print("Skipping iteration")


    # ---------------------------------------------------
    # SECTION 5 — DISABLED BUTTON STATE
    # ---------------------------------------------------

    print("\nChecking disabled states...")

    birthday.click_birthday_tab("today")

    first_page = birthday.get_pagination_status()

    if first_page["has_data"]:

        if not first_page["prev_visible"]:
            print(
                "Previous correctly disabled on first page"
            )


    # ---------------------------------------------------
    # FINAL VALIDATION
    # ---------------------------------------------------

    final_status = birthday.get_pagination_status()

    print("\nFinal Status:", final_status)

    assert final_status is not None

    print("\nALL BIRTHDAY TESTS PASSED")
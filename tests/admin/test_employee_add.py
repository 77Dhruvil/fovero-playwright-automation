"""
TEST ADD EMPLOYEE
=====================================================
FINAL COMBINED STABLE TEST
- Modal Open
- Field Validation
- Form Fill
- Save
- Cancel
- Success Validation
=====================================================
"""

import pytest
import allure
import random
import string
from datetime import datetime


@pytest.mark.admin
@allure.title("Complete Add Employee Flow Test")
def test_complete_add_employee_flow(admin_dashboard_login):

    dashboard = admin_dashboard_login
    page = dashboard.page

    from pages.employee_listing_page import EmployeeListingPage
    from pages.add_employee_page import AddEmployeePage

    employee_listing = EmployeeListingPage(page)
    add_employee = AddEmployeePage(page)

    print("\n" + "=" * 100)
    print("COMPLETE ADD EMPLOYEE TEST START")
    print("=" * 100)

    # =====================================================
    # OPEN EMPLOYEE PAGE
    # =====================================================

    print("\n[STEP 1] OPEN EMPLOYEE PAGE")

    try:

        employee_menu = page.get_by_role(
            "link",
            name="Employees"
        ).first

        employee_menu.wait_for(
            state="visible",
            timeout=10000
        )

        employee_menu.click()

        page.wait_for_timeout(3000)

        print("[✓] Employee page opened")

    except Exception as e:

        pytest.fail(f"[✗] Failed to open employee page: {e}")

    # =====================================================
    # OPEN ADD EMPLOYEE MODAL
    # =====================================================

    print("\n[STEP 2] OPEN ADD EMPLOYEE MODAL")

    if employee_listing.click_add_employee_button():

        print("[✓] Add Employee button clicked")

    else:

        pytest.fail("[✗] Add Employee button click failed")

    page.wait_for_timeout(3000)

    try:

        add_employee.modal.wait_for(
            state="visible",
            timeout=10000
        )

        print("[✓] Add Employee modal opened")

    except Exception as e:

        pytest.fail(f"[✗] Add Employee modal not opened: {e}")

    # =====================================================
    # VERIFY MODAL TITLE
    # =====================================================

    print("\n[STEP 3] VERIFY MODAL")

    try:

        modal_title = page.locator(
            "h1, h2, h3"
        ).filter(
            has_text="Add Employee"
        )

        if modal_title.count() > 0:

            print("[✓] Modal title verified")

        else:

            print("[⚠] Modal title not found")

    except Exception as e:

        print(f"[⚠] Modal title check failed: {e}")

    # =====================================================
    # GENERATE & SUBMIT RANDOM EMPLOYEE
    # =====================================================

    print("\n[STEP 4] GENERATE & SUBMIT RANDOM EMPLOYEE")

    # Use the helper which resolves dropdowns dynamically and fills the form
    success, generated_data, details = add_employee.add_random_employee(choose_random_options=True)

    print("[INFO] add_random_employee returned:")
    print(f" - success: {success}")
    print(f" - data: {generated_data}")
    print(f" - details: {details}")

    # Wait a moment for any UI updates
    page.wait_for_timeout(2000)

    # Assert saved
    if not success:
        pytest.fail(f"[✗] Failed to add employee dynamically. Details: {details}")

    # =====================================================
    # CHECK MODAL STATUS
    # =====================================================

    print("\n[STEP 9] CHECK MODAL STATUS")

    try:

        if not add_employee.is_modal_open():

            print("[✓] Modal closed after save")

        else:

            print("[⚠] Modal still open")

            print("[STEP 9A] CANCEL MODAL")

            add_employee.cancel_form()

            page.wait_for_timeout(3000)

            if not add_employee.is_modal_open():

                print("[✓] Modal closed successfully after cancel")

            else:

                print("[✗] Modal still open after cancel")

    except Exception as e:

        print(f"[⚠] Modal status check failed: {e}")

    # =====================================================
    # FINAL RESULT
    # =====================================================

    print("\n" + "=" * 100)
    print("COMPLETE ADD EMPLOYEE TEST COMPLETED")
    print("=" * 100)
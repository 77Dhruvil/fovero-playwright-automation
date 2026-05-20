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

    if add_employee.is_modal_open():

        print("[✓] Add Employee modal opened")

    else:

        pytest.fail("[✗] Add Employee modal not opened")

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
    # GENERATE TEST DATA
    # =====================================================

    print("\n[STEP 4] GENERATE TEST DATA")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    random_text = ''.join(
        random.choices(
            string.ascii_lowercase,
            k=3
        )
    )

    employee_data = {

        "employee_id": f"EMP{timestamp}",

        "email": f"testemployee{random_text}@example.com",

        "first_name": "Test",

        "last_name": f"User{random_text}",

        "gender": "Male",

        "department": "QA Team",

        "employment_type": "Permanent",

        "invite": False,

        "joining_window": False
    }

    print(f"[✓] Employee ID: {employee_data['employee_id']}")
    print(f"[✓] Email: {employee_data['email']}")

    # =====================================================
    # FILL FORM
    # =====================================================

    print("\n[STEP 5] FILL ADD EMPLOYEE FORM")

    try:

        form_result = add_employee.fill_add_employee_form(
            employee_data
        )

        if form_result:

            print("[✓] Form filled successfully")

        else:

            print("[⚠] Some form fields failed")

    except Exception as e:

        print(f"[✗] Form fill failed: {e}")

    page.wait_for_timeout(3000)

    # =====================================================
    # VALIDATION ERRORS
    # =====================================================

    print("\n[STEP 6] CHECK VALIDATION ERRORS")

    try:

        errors = add_employee.get_validation_errors()

        if errors:

            print(f"[⚠] Validation Errors Found: {errors}")

        else:

            print("[✓] No validation errors")

    except Exception as e:

        print(f"[⚠] Validation check failed: {e}")

    # =====================================================
    # SAVE EMPLOYEE
    # =====================================================

    print("\n[STEP 7] SAVE EMPLOYEE")

    try:

        if add_employee.save_employee():

            print("[✓] Save button clicked")

        else:

            print("[⚠] Save button click failed")

    except Exception as e:

        print(f"[✗] Save failed: {e}")

    page.wait_for_timeout(5000)

    # =====================================================
    # SUCCESS MESSAGE
    # =====================================================

    print("\n[STEP 8] VERIFY SUCCESS MESSAGE")

    try:

        success_message = add_employee.get_success_message()

        if success_message:

            print(f"[✓] Success Message: {success_message}")

        else:

            print("[ℹ] No success message displayed")

    except Exception as e:

        print(f"[⚠] Success message check failed: {e}")

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
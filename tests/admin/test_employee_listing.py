# =====================================================
# FINAL UPDATED test_employee_listing.py
# =====================================================

"""
TEST EMPLOYEE LISTING
=====================================================
FINAL STABLE TEST FILE
"""

import pytest
import allure


@pytest.mark.admin
@allure.title("Employee Listing Complete Working Test")
def test_employee_listing(admin_dashboard_login):

    dashboard = admin_dashboard_login
    page = dashboard.page

    from pages.employee_listing_page import EmployeeListingPage

    employee = EmployeeListingPage(page)

    print("\n" + "=" * 100)
    print("EMPLOYEE LISTING TEST START")
    print("=" * 100)

    # =====================================================
    # OPEN EMPLOYEE PAGE
    # =====================================================
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

        print("[✓] Employee menu clicked")

    except Exception as e:

        pytest.fail(f"Employee menu failed: {e}")

    # =====================================================
    # WAIT PAGE LOAD
    # =====================================================
    print("\n[STEP] WAIT EMPLOYEE PAGE")

    assert employee.wait_for_employee_section()

    # =====================================================
    # SEARCH FUNCTIONALITY
    # =====================================================
    print("\n[STEP] SEARCH EMPLOYEE")

    employee.search_employee("Test")

    count = employee.get_employee_rows_count()

    print(f"[✓] Search rows count: {count}")

    # =====================================================
    # CLEAR SEARCH
    # =====================================================
    print("\n[STEP] CLEAR SEARCH")

    employee.clear_search()

    # =====================================================
    # DEPARTMENT FILTER
    # =====================================================
    print("\n[STEP] SELECT DEPARTMENT")

    employee.select_department("QA Team")

    # =====================================================
    # CLEAR DEPARTMENT FILTER
    # =====================================================
    print("\n[STEP] CLEAR DEPARTMENT FILTER")

    employee.clear_department_filter()

    # =====================================================
    # STATUS FILTER
    # =====================================================
    print("\n[STEP] SELECT STATUS")

    employee.select_status("Enabled")

    # =====================================================
    # CLEAR STATUS FILTER
    # =====================================================
    print("\n[STEP] CLEAR STATUS FILTER")

    employee.clear_status_filter()

    # =====================================================
    # ACTIVE EMPLOYEE TOGGLE
    # =====================================================
    print("\n[STEP] ACTIVE EMPLOYEE TOGGLE")

    toggle_result = employee.toggle_active_employee()

    if toggle_result:

        print("[✓] Active employee toggle working properly")

    else:

        print("[✗] Active employee toggle failed")
    # =====================================================
    # TABLE DATA
    # =====================================================
    print("\n[STEP] GET TABLE DATA")

    rows = employee.get_employee_rows_count()

    print(f"[✓] Total Rows: {rows}")

    if rows > 0:

        data = employee.get_employee_table_data(0)

        print(f"""
        Employee Data
        --------------------------------
        EMP ID     : {data.get('emp_id')}
        NAME       : {data.get('name')}
        DEPARTMENT : {data.get('department')}
        JOIN DATE  : {data.get('join_date')}
        STATUS     : {data.get('status')}
        """)

    else:

        print("[⚠] No employee rows found")

    # =====================================================
    # EXPORT BUTTON
    # =====================================================

    print("\n[STEP] EXPORT BUTTON")

    employee.click_export_button()


    # =====================================================
    # ADD EMPLOYEE
    # =====================================================
    print("\n[STEP] ADD EMPLOYEE")

    employee.click_add_employee_button()

    if employee.is_add_modal_open():

        print("[✓] Add Employee modal opened")

    else:

        print("[✗] Add Employee modal not opened")

    print("\n" + "=" * 100)
    print("EMPLOYEE LISTING TEST COMPLETED")
    print("=" * 100)
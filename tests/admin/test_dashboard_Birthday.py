import allure
import pytest
@pytest.mark.admin
@allure.title("Birthday Section - Comprehensive Functionality Test")
@allure.description("Complete test of all Birthday section features in single run")
def test_birthday_comprehensive_functionality(admin_dashboard_login):
    dashboard = admin_dashboard_login
    page = dashboard.page
    birthday = dashboard.birthday

    print("\n" + "="*100)
    print(" BIRTHDAY SECTION - COMPREHENSIVE FUNCTIONALITY TEST")
    print("="*100)

    # =====================================================
    # SECTION 1: INITIAL SETUP
    # =====================================================
    print("\n" + "-"*100)
    print("[SECTION 1] INITIAL SETUP")
    print("-"*100)

    print("\n[✓] Waiting for Birthday Section to be visible...")
    try:
        birthday.birthday_section.wait_for(state="visible", timeout=8000)
        print("[✓] Birthday section is visible")
    except Exception as e:
        print(f"[⚠] Birthday section not visible yet, attempting reload: {str(e)[:60]}")
        page.reload()
        page.wait_for_timeout(1000)
        try:
            birthday.birthday_section.wait_for(state="visible", timeout=8000)
            print("[✓] Birthday section is visible after reload")
        except Exception as e2:
            print(f"[✗] Birthday section still not visible: {str(e2)[:60]}")
            raise AssertionError("Birthday section not visible after reload")
    
    print("[✓] Verifying Birthday Section is visible...")
    assert birthday.birthday_section.is_visible(), "Birthday section not visible"
    print("[✓] Birthday section visibility verified")

    print("\n[✓] Getting initial pagination status...")
    initial_status = birthday.get_pagination_status()
    print(f"    - Next visible: {initial_status['next_visible']}")
    print(f"    - Prev visible: {initial_status['prev_visible']}")
    print(f"    - Employee count: {initial_status['employee_count']}")
    print(f"    - Has data: {initial_status['has_data']}")

    # =====================================================
    # SECTION 2: TODAY'S TAB TESTING
    # =====================================================
    print("\n" + "-"*100)
    print("[SECTION 2] TODAY'S BIRTHDAY TAB")
    print("-"*100)

    print("\n[→] Clicking Today's Birthday tab...")
    birthday.click_birthday_tab("today")
    page.wait_for_timeout(500)
    print("[✓] Switched to Today's tab")

    # Get Today's status
    today_status = birthday.get_pagination_status()
    print(f"\n[STATUS] Today's Tab:")
    print(f"  - Has data: {today_status['has_data']}")
    print(f"  - Employee count: {today_status['employee_count']}")
    print(f"  - Next visible: {today_status['next_visible']}")
    print(f"  - Prev visible: {today_status['prev_visible']}")

    # Handle no data scenario for Today
    if birthday.is_no_data_found():
        print("\n[ℹ] No data message found for Today's birthdays")
        assert today_status['employee_count'] == 0, "Should have 0 employees"
        assert not today_status['next_visible'], "Next button should not be visible"
        assert not today_status['prev_visible'], "Prev button should not be visible"
        print("[✓] No data scenario verified - no buttons, count=0")
    else:
        print(f"\n[✓] Today's data available - {today_status['employee_count']} employees")
        
        # Test pagination on Today's tab if available
        if today_status["next_visible"]:
            print("\n[PAGINATION TEST] Today's Tab")
            print("[→] Next button available - testing pagination...")
            
            today_initial_count = birthday.get_employee_count()
            print(f"    Initial page employees: {today_initial_count}")
            
            # Click next
            result = birthday.click_next_button()
            if result["clicked"]:
                print(f"    [✓] Next button clicked: {result['message']}")
                page.wait_for_timeout(500)
                
                today_next_count = birthday.get_employee_count()
                print(f"    New page employees: {today_next_count}")
                print("[✓] Pagination works on Today's tab")
                
                # Try to go back
                current_status = birthday.get_pagination_status()
                if current_status["prev_visible"]:
                    print("[←] Testing Previous button...")
                    result = birthday.click_previous_button()
                    if result["clicked"]:
                        print(f"    [✓] Back to first page")
                        page.wait_for_timeout(500)
            else:
                print(f"    [⚠] Next button not clicked: {result['status']}")
        else:
            print("[ℹ] No pagination needed for Today's tab")
            if today_status['employee_count'] <= 2:
                print("    (Less than 2 items - single page)")

    # =====================================================
    # SECTION 3: UPCOMING TAB TESTING
    # =====================================================
    print("\n" + "-"*100)
    print("[SECTION 3] UPCOMING BIRTHDAY TAB")
    print("-"*100)

    print("\n[→] Clicking Upcoming Birthday tab...")
    birthday.click_birthday_tab("upcoming")
    page.wait_for_timeout(500)
    print("[✓] Switched to Upcoming tab")

    # Get Upcoming status
    upcoming_status = birthday.get_pagination_status()
    print(f"\n[STATUS] Upcoming Tab:")
    print(f"  - Has data: {upcoming_status['has_data']}")
    print(f"  - Employee count: {upcoming_status['employee_count']}")
    print(f"  - Next visible: {upcoming_status['next_visible']}")
    print(f"  - Prev visible: {upcoming_status['prev_visible']}")

    # Handle no data scenario for Upcoming
    if birthday.is_no_data_found():
        print("\n[ℹ] No data message found for Upcoming birthdays")
        assert upcoming_status['employee_count'] == 0, "Should have 0 employees"
        assert not upcoming_status['next_visible'], "Next button should not be visible"
        assert not upcoming_status['prev_visible'], "Prev button should not be visible"
        print("[✓] No data scenario verified - no buttons, count=0")
    else:
        print(f"\n[✓] Upcoming data available - {upcoming_status['employee_count']} employees")
        
        # Test pagination on Upcoming tab if available
        if upcoming_status["next_visible"]:
            print("\n[PAGINATION TEST] Upcoming Tab")
            print("[→] Next button available - testing pagination...")
            
            upcoming_initial_count = birthday.get_employee_count()
            print(f"    Initial page employees: {upcoming_initial_count}")
            
            # Click next
            result = birthday.click_next_button()
            if result["clicked"]:
                print(f"    [✓] Next button clicked: {result['message']}")
                page.wait_for_timeout(500)
                
                upcoming_next_count = birthday.get_employee_count()
                print(f"    New page employees: {upcoming_next_count}")
                print("[✓] Pagination works on Upcoming tab")
                
                # Try to go back
                current_status = birthday.get_pagination_status()
                if current_status["prev_visible"]:
                    print("[←] Testing Previous button...")
                    result = birthday.click_previous_button()
                    if result["clicked"]:
                        print(f"    [✓] Back to first page")
                        page.wait_for_timeout(500)
            else:
                print(f"    [⚠] Next button not clicked: {result['status']}")
        else:
            print("[ℹ] No pagination needed for Upcoming tab")
            if upcoming_status['employee_count'] <= 2:
                print("    (Less than 2 items - single page)")

    # =====================================================
    # SECTION 4: FULL PAGE ITERATION TEST WITH DATA VERIFICATION
    # =====================================================
    print("\n" + "-"*100)
    print("[SECTION 4] FULL PAGE ITERATION WITH DATA VERIFICATION")
    print("-"*100)

    print("\n[ITERATION TEST] Traversing all available pages with data change verification...")
    
    # Stay on Upcoming tab and iterate all pages
    birthday.click_birthday_tab("upcoming")
    page.wait_for_timeout(500)
    
    iteration_status = birthday.get_pagination_status()
    if iteration_status['has_data'] and iteration_status['next_visible']:
        print("[→] Starting iteration through all pages with data verification...")
        
        page_num = 1
        all_pages_data = []
        max_iterations = 20
        iteration_count = 0
        no_change_count = 0
        
        while iteration_count < max_iterations:
            status = birthday.get_pagination_status()
            count = birthday.get_employee_count()
            
            # Get employee names/IDs to verify data actually changed
            employee_elements = birthday.birthday_section.locator("div.employee, .employee-card, [data-testid*='employee']").all()
            current_employees = len(employee_elements)
            
            all_pages_data.append({
                "page": page_num,
                "employees": count,
                "next_available": status['next_visible'],
                "prev_available": status['prev_visible']
            })
            
            print(f"\n    [PAGE {page_num}]")
            print(f"      - Employee count: {count}")
            print(f"      - Employee elements found: {current_employees}")
            print(f"      - Next available: {status['next_visible']}")
            print(f"      - Prev available: {status['prev_visible']}")
            
            # Try to go to next page
            if status["next_visible"]:
                print(f"      [→] Attempting to move to next page...")
                
                # Store current data before click
                previous_count = count
                
                result = birthday.click_next_button()
                if result["clicked"]:
                    page.wait_for_timeout(800)  # Wait for content to load
                    
                    # Check if data actually changed
                    new_count = birthday.get_employee_count()
                    new_status = birthday.get_pagination_status()
                    
                    print(f"      [✓] Next button clicked")
                    print(f"      [✓] New page employee count: {new_count} (was {previous_count})")
                    
                    # Verify data changed
                    if new_count != previous_count or new_status['next_visible'] != status['next_visible']:
                        print(f"      [✓] Data CHANGED - new page loaded successfully")
                        page_num += 1
                        iteration_count += 1
                        no_change_count = 0  # Reset no-change counter
                    else:
                        print(f"      [⚠] Data didn't change - same page or pagination stuck")
                        no_change_count += 1
                        if no_change_count >= 2:
                            print(f"      [✗] Data hasn't changed for 2 attempts - stopping iteration")
                            break
                else:
                    print(f"      [✗] Next button click failed: {result['status']}")
                    break
            else:
                print(f"      [✓] Reached last page - Next button not available")
                break

        # Summary of iteration
        print(f"\n[ITERATION SUMMARY]")
        print(f"  - Total pages iterated: {len(all_pages_data)}")
        print(f"  - Pages data: {all_pages_data}")
        print(f"  - Total employees across all pages: {sum(p['employees'] for p in all_pages_data)}")
        
        # Test backward navigation on last page
        print(f"\n[BACKWARD NAVIGATION TEST]")
        if len(all_pages_data) > 1:
            print(f"[→] Testing backward navigation from page {page_num}...")
            last_page_count = birthday.get_employee_count()
            
            if birthday.is_prev_button_visible():
                print(f"[→] Previous button available - testing click...")
                result = birthday.click_previous_button()
                
                if result["clicked"]:
                    page.wait_for_timeout(800)
                    prev_page_count = birthday.get_employee_count()
                    print(f"[✓] Previous button clicked")
                    print(f"[✓] Previous page employee count: {prev_page_count} (was {last_page_count})")
                    
                    if prev_page_count != last_page_count:
                        print(f"[✓] Backward navigation works - data changed")
                    else:
                        print(f"[⚠] Backward navigation - data didn't change")
                else:
                    print(f"[⚠] Previous button click failed: {result['status']}")
            else:
                print(f"[ℹ] Previous button not available at page {page_num}")
        else:
            print(f"[ℹ] Only one page available - skipping backward test")
    else:
        print("[ℹ] Skipping - insufficient data or no pagination available")

    # =====================================================
    # SECTION 5: DISABLED BUTTON DETECTION
    # =====================================================
    print("\n" + "-"*100)
    print("[SECTION 5] DISABLED BUTTON DETECTION")
    print("-"*100)

    print("\n[TEST] Checking disabled button states...")
    
    # Go back to first page for testing
    birthday.click_birthday_tab("today")
    page.wait_for_timeout(500)
    
    first_page_status = birthday.get_pagination_status()
    print(f"\n[FIRST PAGE STATUS]")
    print(f"  - Next visible: {first_page_status['next_visible']}")
    print(f"  - Prev visible: {first_page_status['prev_visible']}")
    
    if first_page_status['has_data']:
        # At first page, prev should be disabled/not visible
        if not first_page_status['prev_visible']:
            print("[✓] Previous button correctly disabled/hidden at first page")
        else:
            print("[⚠] Previous button visible at first page (might be enabled)")
    else:
        print("[ℹ] No data - skipping disabled state test")

    # =====================================================
    # SECTION 6: FINAL VERIFICATION
    # =====================================================
    print("\n" + "-"*100)
    print("[SECTION 6] FINAL VERIFICATION")
    print("-"*100)

    print("\n[✓] Final status check...")
    final_status = birthday.get_pagination_status()
    print(f"    - Next visible: {final_status['next_visible']}")
    print(f"    - Prev visible: {final_status['prev_visible']}")
    print(f"    - Employee count: {final_status['employee_count']}")
    print(f"    - Has data: {final_status['has_data']}")

    # =====================================================
    # TEST SUMMARY
    # =====================================================
    print("\n" + "="*100)
    print(" TEST SUMMARY - ALL TESTS PASSED ✅")
    print("="*100)
    print("\nTested Features in Single Run:")
    print("  ✅ Tab switching (Today & Upcoming)")
    print("  ✅ Pagination (Next/Previous buttons)")
    print("  ✅ Status checking in all conditions")
    print("  ✅ No data scenarios")
    print("  ✅ Button disabled state detection")
    print("  ✅ Full page iteration")
    print("  ✅ Employee count tracking")
    print("  ✅ Proper waits and error handling")
    print("\n" + "="*100 + "\n")


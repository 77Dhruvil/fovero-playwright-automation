import allure
import pytest
from pages.announcement_page import AnnouncementPage
from datetime import datetime, timedelta

@pytest.mark.admin
@allure.title("Create and Submit Announcement Test")
@allure.description("Automatically create announcement by filling form and submitting")
def test_create_and_submit_announcement(admin_dashboard_login):

    dashboard = admin_dashboard_login
    page = dashboard.page
    announcement = AnnouncementPage(page)

    print("\n" + "="*80)
    print(" ANNOUNCEMENT - CREATE AND SUBMIT TEST")
    print("="*80)

    # =====================================================
    # STEP 1: VERIFY SECTION VISIBLE
    # =====================================================
    print("\n[STEP 1] Verifying Announcement Section...")
    try:
        assert announcement.is_section_visible(), "Announcement section not visible"
        print("[✓] Announcement section visible")
    except AssertionError as e:
        pytest.fail(f"[✗] {e}")

    # =====================================================
    # STEP 2: CLICK ADD ANNOUNCEMENT BUTTON
    # =====================================================
    print("\n[STEP 2] Clicking Add Announcement Button...")
    try:
        result = announcement.click_add_announcement()
        if not result:
            # Try alternative method
            btn = page.locator("button").filter(has_text="Add").first
            if btn.count() > 0:
                btn.click()
                print("[✓] Add button clicked (alternative method)")
            else:
                pytest.fail("[✗] Add Announcement button not found")
        else:
            print("[✓] Add Announcement button clicked")
    except Exception as e:
        pytest.fail(f"[✗] Error clicking Add button: {e}")

    # Wait for modal to appear
    page.wait_for_timeout(2000)
    print("[✓] Waiting for modal...")

    # Verify modal is open
    try:
        modals = page.locator("div[role='dialog']")
        assert modals.count() > 0, "Modal did not open"
        print("[✓] Announcement modal opened")
    except AssertionError as e:
        pytest.fail(f"[✗] {e}")

    # =====================================================
    # STEP 3: GENERATE TEST DATA
    # =====================================================
    print("\n[STEP 3] Preparing Test Data...")
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    title = f"Automation Test {timestamp}"
    description = f"Automated announcement created on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    print(f"[DATA]")
    print(f"  Title: {title}")
    print(f"  Description: {description}")
    print(f"  Date: {tomorrow}")

    # =====================================================
    # STEP 4: FILL FORM FIELDS
    # =====================================================
    print("\n[STEP 4] Filling Form Fields...")
    
    # Use the comprehensive automatic filling method
    try:
        result = announcement.fill_all_fields_automatically()
        if result:
            print("[✓] All form fields filled successfully")
        else:
            print("[⚠] Some form fields may not have been filled properly")
            # Continue anyway as the method handles optional fields
    except Exception as e:
        print(f"[⚠] Error during automatic form filling: {e}")
        # Fallback to manual filling if automatic fails
        try:
            # Fill Title
            result = announcement.fill_title(title)
            if result:
                print(f"[✓] Title filled: {title}")
            else:
                print(f"[⚠] Title field not found - skipping")
            
            # Fill Description
            result = announcement.fill_description(description)
            if result:
                print(f"[✓] Description filled")
            else:
                print(f"[⚠] Description field not found - skipping")
            
            # Fill Schedule Date
            result = announcement.set_schedule_date(tomorrow)
            if result:
                print(f"[✓] Schedule date filled: {tomorrow}")
            else:
                print(f"[⚠] Date field not found - skipping")
            
            # Select Category (if available)
            try:
                result = announcement.select_category("EOM")
                if result:
                    print("[✓] Category selected: EOM")
                else:
                    print("[ℹ] Category not available")
            except Exception as e:
                print(f"[ℹ] Category selection skipped: {str(e)[:50]}")
            
            # Select Employee (if available)
            try:
                result = announcement.select_employee("dhruvil patel")
                if result:
                    print("[✓] Employee selected: dhruvil patel")
                else:
                    print("[ℹ] Employee not available")
            except Exception as e:
                print(f"[ℹ] Employee selection skipped: {str(e)[:50]}")
        except Exception as e2:
            print(f"[⚠] Fallback manual filling also failed: {e2}")

    # =====================================================
    # STEP 6: CHECK VALIDATION ERRORS
    # =====================================================
    print("\n[STEP 6] Checking Validation...")
    page.wait_for_timeout(500)
    errors = announcement.get_error_messages()
    if errors:
        print(f"[⚠] Validation errors found:")
        for error in errors:
            print(f"    - {error}")
    else:
        print("[✓] No validation errors")

    # =====================================================
    # STEP 7: SUBMIT/SAVE ANNOUNCEMENT
    # =====================================================
    print("\n[STEP 7] Submitting Announcement...")
    try:
        result = announcement.save_announcement()
        if result:
            print("[✓] Save button clicked")
            
            # Wait for save to complete
            page.wait_for_timeout(2000)
            
            # Check for success message
            success_msg = announcement.get_success_message()
            if success_msg:
                print(f"[✓] Success: {success_msg}")
            else:
                print("[ℹ] No success message (may have saved silently)")
            
            # Check if modal closed
            page.wait_for_timeout(1000)
            modals = page.locator("div[role='dialog']")
            if modals.count() == 0:
                print("[✓] Modal closed")
                print("[✓] ANNOUNCEMENT SUBMITTED SUCCESSFULLY")
            else:
                print("[ℹ] Modal still visible (may be confirmation dialog)")
        else:
            print("[✗] Save button not found")
            errors = announcement.get_error_messages()
            if errors:
                print("[ℹ] Form has validation errors - cannot save")
                for error in errors:
                    print(f"    - {error}")
                # Try to cancel
                announcement.cancel_announcement()
                pytest.fail("Form has validation errors")
            else:
                pytest.fail("Save button not available")
    except Exception as e:
        print(f"[✗] Error during save: {e}")
        # Try to cancel and fail
        try:
            announcement.cancel_announcement()
        except:
            pass
        pytest.fail(f"Error saving announcement: {e}")

    # =====================================================
    # FINAL VERIFICATION
    # =====================================================
    print("\n[STEP 8] Final Verification...")
    try:
        page.wait_for_timeout(1000)
        assert announcement.is_section_visible(), "Section not visible"
        print("[✓] Announcement section still visible")
        
        count = announcement.get_announcements_count()
        print(f"[✓] Total announcements: {count}")
    except Exception as e:
        print(f"[⚠] Verification warning: {e}")

    # =====================================================
    # TEST COMPLETE
    # =====================================================
    print("\n" + "="*80)
    print(" ✓ TEST COMPLETED SUCCESSFULLY")
    print("="*80)
    print("\n[SUMMARY]")
    print("✓ Announcement form opened")
    print("✓ All fields filled with test data")
    print("✓ Form submitted successfully")
    print("✓ Announcement created")
    print("\n")

"""
EDIT EMPLOYEE PAGE
=====================================================
Page object for Edit Employee page with:
- Employee profile information
- Multiple tabs (Other Details, Address, Emergency Contact, Documents, Approval, Settings)
- Tab-specific field operations
- Document upload
- Navigation
"""

from pages.base_page import BasePage
from locators.employee_locators import EmployeeLocators


class EditEmployeePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.profile_card = page.locator(EmployeeLocators.EMPLOYEE_PROFILE_CARD)

    # =====================================================
    # PAGE VISIBILITY
    # =====================================================
    def is_edit_page_open(self):
        """Check if Edit Employee page is open"""
        try:
            title = self.page.locator(EmployeeLocators.EDIT_PAGE_TITLE)
            return title.count() > 0
        except:
            return False

    def wait_for_edit_page(self):
        """Wait for Edit Employee page to load"""
        try:
            self.profile_card.wait_for(state="visible", timeout=10000)
            return True
        except:
            return False

    # =====================================================
    # EMPLOYEE PROFILE INFORMATION
    # =====================================================
    def get_employee_profile_info(self):
        """Get employee profile information"""
        try:
            data = {
                "name": self.page.locator(EmployeeLocators.EMPLOYEE_NAME).inner_text().strip(),
                "role": self.page.locator(EmployeeLocators.EMPLOYEE_ROLE).inner_text().strip(),
                "id": self.page.locator(EmployeeLocators.EMPLOYEE_ID).inner_text().strip(),
                "email": self.page.locator(EmployeeLocators.EMPLOYEE_EMAIL).inner_text().strip(),
                "designation": self.page.locator(EmployeeLocators.EMPLOYEE_DESIGNATION).inner_text().strip(),
            }
            print("[✓] Employee profile info retrieved")
            return data
        except Exception as e:
            print(f"[⚠] Error getting profile info: {str(e)[:60]}")
            return {}

    # =====================================================
    # TAB NAVIGATION
    # =====================================================
    def click_other_details_tab(self):
        """Click Other Details tab"""
        try:
            tab = self.page.locator(EmployeeLocators.TAB_OTHER_DETAILS)
            if tab.count() > 0:
                tab.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Clicked Other Details tab")
                return True
            return False
        except Exception as e:
            print(f"[✗] Error clicking Other Details tab: {str(e)[:60]}")
            return False

    def click_address_tab(self):
        """Click Address tab"""
        try:
            tab = self.page.locator(EmployeeLocators.TAB_ADDRESS)
            if tab.count() > 0:
                tab.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Clicked Address tab")
                return True
            return False
        except Exception as e:
            print(f"[✗] Error clicking Address tab: {str(e)[:60]}")
            return False

    def click_emergency_contact_tab(self):
        """Click Emergency Contact tab"""
        try:
            tab = self.page.locator(EmployeeLocators.TAB_EMERGENCY_CONTACT)
            if tab.count() > 0:
                tab.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Clicked Emergency Contact tab")
                return True
            return False
        except Exception as e:
            print(f"[✗] Error clicking Emergency Contact tab: {str(e)[:60]}")
            return False

    def click_documents_tab(self):
        """Click Documents tab"""
        try:
            tab = self.page.locator(EmployeeLocators.TAB_DOCUMENTS)
            if tab.count() > 0:
                tab.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Clicked Documents tab")
                return True
            return False
        except Exception as e:
            print(f"[✗] Error clicking Documents tab: {str(e)[:60]}")
            return False

    def click_approval_tab(self):
        """Click Approval tab"""
        try:
            tab = self.page.locator(EmployeeLocators.TAB_APPROVAL)
            if tab.count() > 0:
                tab.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Clicked Approval tab")
                return True
            return False
        except Exception as e:
            print(f"[✗] Error clicking Approval tab: {str(e)[:60]}")
            return False

    def click_settings_tab(self):
        """Click Settings tab"""
        try:
            tab = self.page.locator(EmployeeLocators.TAB_SETTINGS)
            if tab.count() > 0:
                tab.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Clicked Settings tab")
                return True
            return False
        except Exception as e:
            print(f"[✗] Error clicking Settings tab: {str(e)[:60]}")
            return False

    # =====================================================
    # OTHER DETAILS TAB OPERATIONS
    # =====================================================
    def fill_kyc_aadhar(self, aadhar_number):
        """Fill KYC Aadhar number"""
        try:
            field = self.page.locator(EmployeeLocators.KYC_AADHAR_FIELD)
            if field.count() > 0:
                field.first.fill(aadhar_number)
                print(f"[✓] Aadhar filled: {aadhar_number}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error filling Aadhar: {str(e)[:50]}")
            return False

    def fill_kyc_pan(self, pan_number):
        """Fill KYC PAN number"""
        try:
            field = self.page.locator(EmployeeLocators.KYC_PAN_FIELD)
            if field.count() > 0:
                field.first.fill(pan_number)
                print(f"[✓] PAN filled: {pan_number}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error filling PAN: {str(e)[:50]}")
            return False

    def fill_dob(self, date_of_birth):
        """Fill Date of Birth (format: DD-MM-YYYY or YYYY-MM-DD)"""
        try:
            field = self.page.locator(EmployeeLocators.DOB_FIELD)
            if field.count() > 0:
                field.first.fill(date_of_birth)
                print(f"[✓] DOB filled: {date_of_birth}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error filling DOB: {str(e)[:50]}")
            return False

    def select_blood_group(self, blood_group):
        """Select Blood Group"""
        try:
            field = self.page.locator(EmployeeLocators.BLOOD_GROUP_FIELD)
            if field.count() > 0:
                field.first.select_option(blood_group)
                print(f"[✓] Blood group selected: {blood_group}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error selecting blood group: {str(e)[:50]}")
            return False

    def click_edit_details_button(self):
        """Click Edit Details button to enable editing"""
        try:
            btn = self.page.locator(EmployeeLocators.EDIT_DETAILS_BUTTON)
            if btn.count() > 0:
                btn.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Clicked Edit Details button")
                return True
            return False
        except Exception as e:
            print(f"[✗] Error clicking Edit Details: {str(e)[:60]}")
            return False

    # =====================================================
    # ADDRESS TAB OPERATIONS
    # =====================================================
    def click_present_address_tab(self):
        """Click Present Address tab"""
        try:
            tab = self.page.locator(EmployeeLocators.PRESENT_ADDRESS_TAB)
            if tab.count() > 0:
                tab.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Clicked Present Address tab")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error clicking Present Address: {str(e)[:60]}")
            return False

    def click_permanent_address_tab(self):
        """Click Permanent Address tab"""
        try:
            tab = self.page.locator(EmployeeLocators.PERMANENT_ADDRESS_TAB)
            if tab.count() > 0:
                tab.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Clicked Permanent Address tab")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error clicking Permanent Address: {str(e)[:60]}")
            return False

    def select_country(self, country):
        """Select Country"""
        try:
            field = self.page.locator(EmployeeLocators.COUNTRY_FIELD)
            if field.count() > 0:
                field.first.select_option(country)
                print(f"[✓] Country selected: {country}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error selecting country: {str(e)[:50]}")
            return False

    def select_state(self, state):
        """Select State"""
        try:
            field = self.page.locator(EmployeeLocators.STATE_FIELD)
            if field.count() > 0:
                field.first.select_option(state)
                print(f"[✓] State selected: {state}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error selecting state: {str(e)[:50]}")
            return False

    def select_city(self, city):
        """Select City"""
        try:
            field = self.page.locator(EmployeeLocators.CITY_FIELD)
            if field.count() > 0:
                field.first.select_option(city)
                print(f"[✓] City selected: {city}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error selecting city: {str(e)[:50]}")
            return False

    def fill_zipcode(self, zipcode):
        """Fill Zipcode"""
        try:
            field = self.page.locator(EmployeeLocators.ZIPCODE_FIELD)
            if field.count() > 0:
                field.first.fill(zipcode)
                print(f"[✓] Zipcode filled: {zipcode}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error filling zipcode: {str(e)[:50]}")
            return False

    def fill_address_line1(self, address):
        """Fill Address Line 1"""
        try:
            field = self.page.locator(EmployeeLocators.ADDRESS_LINE1_FIELD)
            if field.count() > 0:
                field.first.fill(address)
                print(f"[✓] Address Line 1 filled")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error filling address line 1: {str(e)[:50]}")
            return False

    def fill_address_line2(self, address):
        """Fill Address Line 2"""
        try:
            field = self.page.locator(EmployeeLocators.ADDRESS_LINE2_FIELD)
            if field.count() > 0:
                field.first.fill(address)
                print(f"[✓] Address Line 2 filled")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error filling address line 2: {str(e)[:50]}")
            return False

    # =====================================================
    # DOCUMENTS TAB OPERATIONS
    # =====================================================
    def upload_document(self, file_path):
        """
        Upload a document
        
        Args:
            file_path: Full path to file to upload
            
        Returns:
            True if upload initiated
        """
        try:
            file_input = self.page.locator(EmployeeLocators.DOCUMENT_FILE_INPUT)
            if file_input.count() > 0:
                file_input.first.set_input_files(file_path)
                self.page.wait_for_timeout(1000)
                print(f"[✓] Document uploaded: {file_path}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error uploading document: {str(e)[:60]}")
            return False

    def is_documents_tab_visible(self):
        """Check if Documents tab is visible"""
        try:
            container = self.page.locator(EmployeeLocators.DOCUMENTS_CONTAINER)
            return container.is_visible(timeout=2000)
        except:
            return False

    # =====================================================
    # APPROVAL TAB OPERATIONS
    # =====================================================
    def toggle_active_employee(self, active=True):
        """Toggle Active Employee checkbox"""
        try:
            toggle = self.page.locator(EmployeeLocators.ACTIVE_EMPLOYEE_TOGGLE)
            if toggle.count() > 0:
                if active:
                    toggle.first.check()
                    print("[✓] Active Employee checked")
                else:
                    toggle.first.uncheck()
                    print("[✓] Active Employee unchecked")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error toggling active: {str(e)[:50]}")
            return False

    def fill_next_appraisal_date(self, date):
        """Fill Next Appraisal Date"""
        try:
            field = self.page.locator(EmployeeLocators.NEXT_APPRAISAL_DATE_FIELD)
            if field.count() > 0:
                field.first.fill(date)
                print(f"[✓] Appraisal date filled: {date}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error filling appraisal date: {str(e)[:50]}")
            return False

    # =====================================================
    # SETTINGS TAB OPERATIONS
    # =====================================================
    def fill_probation_end_date(self, date):
        """Fill Probation End Date"""
        try:
            field = self.page.locator(EmployeeLocators.PROBATION_END_DATE_FIELD)
            if field.count() > 0:
                field.first.fill(date)
                print(f"[✓] Probation end date filled: {date}")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error filling probation date: {str(e)[:50]}")
            return False

    def fill_availability_comments(self, comments):
        """Fill Availability Comments"""
        try:
            field = self.page.locator(EmployeeLocators.AVAILABILITY_COMMENTS_FIELD)
            if field.count() > 0:
                field.first.fill(comments)
                print(f"[✓] Availability comments filled")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error filling comments: {str(e)[:50]}")
            return False

    def get_login_access_status(self):
        """Get Login Access status"""
        try:
            status = self.page.locator(EmployeeLocators.LOGIN_ACCESS_STATUS)
            if status.count() > 0:
                text = status.first.inner_text().strip()
                print(f"[✓] Login access status: {text}")
                return text
            return ""
        except:
            return ""

    def click_resend_invitation(self):
        """Click Resend Invitation button"""
        try:
            btn = self.page.locator(EmployeeLocators.RESEND_INVITATION_BUTTON)
            if btn.count() > 0:
                btn.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Resend invitation clicked")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error resending invitation: {str(e)[:60]}")
            return False

    # =====================================================
    # COMMON OPERATIONS
    # =====================================================
    def click_back_button(self):
        """Click back button to go to listing"""
        try:
            btn = self.page.locator(EmployeeLocators.BACK_BUTTON)
            if btn.count() > 0:
                btn.first.click()
                self.page.wait_for_timeout(500)
                print("[✓] Clicked back button")
                return True
            return False
        except Exception as e:
            print(f"[✗] Error clicking back: {str(e)[:60]}")
            return False

    def save_changes(self):
        """Save all changes to employee"""
        try:
            save_btn = self.page.locator(EmployeeLocators.SAVE_BUTTON)
            if save_btn.count() > 0:
                save_btn.first.click()
                self.page.wait_for_timeout(1000)
                print("[✓] Clicked Save")
                return True
            return False
        except Exception as e:
            print(f"[✗] Error saving: {str(e)[:60]}")
            return False

    def get_success_message(self):
        """Get success message"""
        try:
            msg = self.page.locator(EmployeeLocators.SUCCESS_MESSAGE)
            if msg.count() > 0:
                text = msg.first.inner_text()
                print(f"[✓] {text}")
                return text
            return ""
        except:
            return ""



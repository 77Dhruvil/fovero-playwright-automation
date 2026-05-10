"""
ADD EMPLOYEE PAGE
=====================================================
Page object for Add Employee modal/form with:
- All form fields
- Modal operations
- Field fill methods
- Validation and submission
"""

from pages.base_page import BasePage
from locators.employee_locators import EmployeeLocators


class AddEmployeePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.modal = page.locator(EmployeeLocators.ADD_MODAL)

    # =====================================================
    # MODAL VISIBILITY
    # =====================================================
    def is_modal_open(self):
        """Check if Add Employee modal is open"""
        try:
            return self.modal.is_visible(timeout=5000)
        except:
            return False

    def wait_for_modal(self):
        """Wait for modal to open"""
        try:
            self.modal.wait_for(state="visible", timeout=10000)
            return True
        except:
            return False

    # =====================================================
    # FORM FIELD OPERATIONS
    # =====================================================
    def fill_employee_id(self, emp_id):
        """Fill Employee ID field"""
        try:
            field = self.page.locator(EmployeeLocators.EMPLOYEE_ID_FIELD)
            field.fill(emp_id)
            print(f"[✓] Employee ID filled: {emp_id}")
            return True
        except Exception as e:
            print(f"[⚠] Employee ID field not found: {str(e)[:50]}")
            return False

    def fill_email(self, email):
        """Fill Email field"""
        try:
            field = self.page.locator(EmployeeLocators.EMAIL_FIELD)
            field.fill(email)
            print(f"[✓] Email filled: {email}")
            return True
        except Exception as e:
            print(f"[⚠] Email field not found: {str(e)[:50]}")
            return False

    def fill_first_name(self, first_name):
        """Fill First Name field"""
        try:
            field = self.page.locator(EmployeeLocators.FIRST_NAME_FIELD)
            field.fill(first_name)
            print(f"[✓] First name filled: {first_name}")
            return True
        except Exception as e:
            print(f"[⚠] First name field not found: {str(e)[:50]}")
            return False

    def fill_last_name(self, last_name):
        """Fill Last Name field"""
        try:
            field = self.page.locator(EmployeeLocators.LAST_NAME_FIELD)
            field.fill(last_name)
            print(f"[✓] Last name filled: {last_name}")
            return True
        except Exception as e:
            print(f"[⚠] Last name field not found: {str(e)[:50]}")
            return False

    def select_gender(self, gender):
        """
        Select Gender
        
        Args:
            gender: 'Male', 'Female', 'Other'
        """
        try:
            field = self.page.locator(EmployeeLocators.GENDER_FIELD)
            if field.count() > 0:
                field.first.select_option(gender)
                print(f"[✓] Gender selected: {gender}")
                return True
            else:
                print(f"[⚠] Gender field not found")
                return False
        except Exception as e:
            print(f"[⚠] Error selecting gender: {str(e)[:50]}")
            return False

    def select_department(self, department):
        """
        Select Department
        
        Args:
            department: Department name
        """
        try:
            field = self.page.locator(EmployeeLocators.DEPARTMENT_FIELD)
            if field.count() > 0:
                field.first.select_option(department)
                print(f"[✓] Department selected: {department}")
                return True
            else:
                print(f"[⚠] Department field not found")
                return False
        except Exception as e:
            print(f"[⚠] Error selecting department: {str(e)[:50]}")
            return False

    def select_reporting_to(self, manager):
        """
        Select Reporting To (Manager)
        
        Args:
            manager: Manager name
        """
        try:
            field = self.page.locator(EmployeeLocators.REPORTING_TO_FIELD)
            if field.count() > 0:
                field.first.select_option(manager)
                print(f"[✓] Reporting To selected: {manager}")
                return True
            else:
                print(f"[⚠] Reporting To field not found")
                return False
        except Exception as e:
            print(f"[⚠] Error selecting reporting: {str(e)[:50]}")
            return False

    def select_employment_type(self, emp_type):
        """
        Select Employment Type
        
        Args:
            emp_type: 'Permanent', 'Contract', etc.
        """
        try:
            field = self.page.locator(EmployeeLocators.EMPLOYMENT_TYPE_FIELD)
            if field.count() > 0:
                field.first.select_option(emp_type)
                print(f"[✓] Employment Type selected: {emp_type}")
                return True
            else:
                print(f"[⚠] Employment Type field not found")
                return False
        except Exception as e:
            print(f"[⚠] Error selecting employment type: {str(e)[:50]}")
            return False

    def select_role(self, role):
        """
        Select Role
        
        Args:
            role: Role name
        """
        try:
            field = self.page.locator(EmployeeLocators.ROLE_FIELD)
            if field.count() > 0:
                field.first.select_option(role)
                print(f"[✓] Role selected: {role}")
                return True
            else:
                print(f"[⚠] Role field not found")
                return False
        except Exception as e:
            print(f"[⚠] Error selecting role: {str(e)[:50]}")
            return False

    # =====================================================
    # CHECKBOXES
    # =====================================================
    def check_invite_employee(self, check=True):
        """Check/uncheck Invite Employee checkbox"""
        try:
            checkbox = self.page.locator(EmployeeLocators.INVITE_CHECKBOX)
            if checkbox.count() > 0:
                if check:
                    checkbox.first.check()
                    print("[✓] Invite Employee checked")
                else:
                    checkbox.first.uncheck()
                    print("[✓] Invite Employee unchecked")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error with invite checkbox: {str(e)[:50]}")
            return False

    def check_joining_window(self, check=True):
        """Check/uncheck Enable joining window checkbox"""
        try:
            checkbox = self.page.locator(EmployeeLocators.JOINING_WINDOW_CHECKBOX)
            if checkbox.count() > 0:
                if check:
                    checkbox.first.check()
                    print("[✓] Joining window checked")
                else:
                    checkbox.first.uncheck()
                    print("[✓] Joining window unchecked")
                return True
            return False
        except Exception as e:
            print(f"[⚠] Error with joining checkbox: {str(e)[:50]}")
            return False

    # =====================================================
    # FORM SUBMISSION
    # =====================================================
    def save_employee(self):
        """
        Save employee
        
        Returns:
            True if save button was clicked
        """
        try:
            save_btn = self.page.locator(EmployeeLocators.MODAL_SAVE_BUTTON)
            if save_btn.count() > 0:
                save_btn.first.click()
                print("[✓] Save button clicked")
                self.page.wait_for_timeout(1000)
                return True
            else:
                print("[✗] Save button not found")
                return False
        except Exception as e:
            print(f"[✗] Error saving employee: {str(e)[:60]}")
            return False

    def cancel_form(self):
        """
        Cancel Add Employee form
        
        Returns:
            True if cancel was successful
        """
        try:
            cancel_btn = self.page.locator(EmployeeLocators.MODAL_CANCEL_BUTTON)
            if cancel_btn.count() > 0:
                cancel_btn.first.click()
                print("[✓] Cancel button clicked")
                self.page.wait_for_timeout(500)
                return True
            else:
                print("[✗] Cancel button not found")
                return False
        except Exception as e:
            print(f"[✗] Error canceling: {str(e)[:60]}")
            return False

    # =====================================================
    # VALIDATION
    # =====================================================
    def get_validation_errors(self):
        """
        Get all validation error messages
        
        Returns:
            List of error messages
        """
        try:
            errors = self.page.locator(EmployeeLocators.VALIDATION_ERROR)
            error_list = []
            
            for i in range(errors.count()):
                error_text = errors.nth(i).inner_text()
                if error_text.strip():
                    error_list.append(error_text.strip())
            
            if error_list:
                print(f"[⚠] Validation errors found: {error_list}")
            return error_list
        except:
            return []

    def get_success_message(self):
        """
        Get success message if available
        
        Returns:
            Success message text or empty string
        """
        try:
            message = self.page.locator(EmployeeLocators.SUCCESS_MESSAGE)
            if message.count() > 0:
                text = message.first.inner_text()
                print(f"[✓] Success message: {text}")
                return text
            return ""
        except:
            return ""

    # =====================================================
    # FILL COMPLETE FORM
    # =====================================================
    def fill_add_employee_form(self, employee_data):
        """
        Fill complete Add Employee form with all data
        
        Args:
            employee_data: Dict with employee details
        
        Returns:
            True if all fields filled successfully
        """
        print("\n[FILLING ADD EMPLOYEE FORM]")
        print("-" * 60)
        
        all_filled = True
        
        # Fill required fields
        if "employee_id" in employee_data:
            all_filled = self.fill_employee_id(employee_data["employee_id"]) and all_filled
        
        if "email" in employee_data:
            all_filled = self.fill_email(employee_data["email"]) and all_filled
        
        if "first_name" in employee_data:
            all_filled = self.fill_first_name(employee_data["first_name"]) and all_filled
        
        if "last_name" in employee_data:
            all_filled = self.fill_last_name(employee_data["last_name"]) and all_filled
        
        # Fill optional fields
        if "gender" in employee_data and employee_data["gender"]:
            self.select_gender(employee_data["gender"])
        
        if "department" in employee_data and employee_data["department"]:
            self.select_department(employee_data["department"])
        
        if "reporting_to" in employee_data and employee_data["reporting_to"]:
            self.select_reporting_to(employee_data["reporting_to"])
        
        if "employment_type" in employee_data and employee_data["employment_type"]:
            self.select_employment_type(employee_data["employment_type"])
        
        if "role" in employee_data and employee_data["role"]:
            self.select_role(employee_data["role"])
        
        # Handle checkboxes
        if "invite" in employee_data:
            self.check_invite_employee(employee_data["invite"])
        
        if "joining_window" in employee_data:
            self.check_joining_window(employee_data["joining_window"])
        
        print("-" * 60)
        print(f"[{'✓' if all_filled else '⚠'}] Form filling completed")
        
        return all_filled



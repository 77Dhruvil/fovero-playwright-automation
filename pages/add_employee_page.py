"""
ADD EMPLOYEE PAGE - FINAL CLEAN VERSION
=====================================================
"""

from pages.base_page import BasePage
from utils.test_data import TestData
import random
import uuid


class AddEmployeePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.modal = page.locator("div[role='dialog']")

    def is_modal_open(self):
        try:
            return self.modal.is_visible(timeout=5000)
        except:
            return False

    def wait_for_modal(self):
        try:
            self.modal.wait_for(state="visible", timeout=10000)
            return True
        except:
            return False

    # INPUTS - using exact IDs from HTML
    def fill_employee_id(self, emp_id):
        try:
            field = self.modal.locator('input#employee_id')
            field.wait_for(state="visible", timeout=5000)
            # Clear with Ctrl+A then Delete, then fill (instead of triple_click which doesn't exist)
            field.click()
            self.page.keyboard.press('Control+A')
            field.fill(str(emp_id), timeout=5000)
            print(f"[✓] Employee ID: {emp_id}")
            return True
        except Exception as e:
            print(f"[⚠] Employee ID: {str(e)[:100]}")
            return False

    def fill_email(self, email):
        try:
            field = self.modal.locator('input#email')
            field.wait_for(state="visible", timeout=5000)
            field.fill(email, timeout=5000)
            print(f"[✓] Email: {email}")
            return True
        except Exception as e:
            print(f"[⚠] Email: {str(e)[:100]}")
            return False

    def fill_first_name(self, first_name):
        try:
            field = self.modal.locator('input#first_name')
            field.wait_for(state="visible", timeout=5000)
            field.fill(first_name, timeout=5000)
            print(f"[✓] First Name: {first_name}")
            return True
        except Exception as e:
            print(f"[⚠] First Name: {str(e)[:100]}")
            return False

    def fill_last_name(self, last_name):
        try:
            field = self.modal.locator('input#last_name')
            field.wait_for(state="visible", timeout=5000)
            field.fill(last_name, timeout=5000)
            print(f"[✓] Last Name: {last_name}")
            return True
        except Exception as e:
            print(f"[⚠] Last Name: {str(e)[:100]}")
            return False

    # REACT-SELECT DROPDOWNS
    def select_gender(self, gender):
        return self._select_react_dropdown('gender', gender, 'Gender')

    def select_department(self, department):
        return self._select_react_dropdown('department', department, 'Department')

    def select_reporting_to(self, manager):
        return self._select_react_dropdown('reporting_manager', manager, 'Reporting To')

    def select_employment_type(self, emp_type):
        return self._select_react_dropdown('employeement_type', emp_type, 'Employment Type')

    def select_designation(self, designation):
        return self._select_react_dropdown('designation', designation, 'Designation')

    def select_role(self, role):
        return self._select_react_dropdown('role', role, 'Role')

    # CHECKBOXES
    def check_invite_employee(self, check=True):
        try:
            checkbox = self.modal.locator('input#invite_employee[type="checkbox"]')
            checkbox.wait_for(state="visible", timeout=5000)
            if check:
                checkbox.check(timeout=5000)
                print("[✓] Invite Employee: checked")
            else:
                checkbox.uncheck(timeout=5000)
                print("[✓] Invite Employee: unchecked")
            return True
        except Exception as e:
            print(f"[⚠] Invite: {str(e)[:100]}")
            return False

    def check_joining_window(self, check=True):
        try:
            checkbox = self.modal.locator('input#enable_joining_process_window[type="checkbox"]')
            checkbox.wait_for(state="visible", timeout=5000)
            if check:
                checkbox.check(timeout=5000)
                print("[✓] Joining Window: checked")
            else:
                checkbox.uncheck(timeout=5000)
                print("[✓] Joining Window: unchecked")
            return True
        except Exception as e:
            print(f"[⚠] Joining: {str(e)[:100]}")
            return False

    # SUBMIT
    def save_employee(self):
        try:
            save_btn = self.modal.locator('button[type="submit"]')
            save_btn.wait_for(state="visible", timeout=5000)
            save_btn.click()
            print("[✓] Add button clicked")
            self.page.wait_for_timeout(2000)
            return True
        except Exception as e:
            print(f"[✗] Save: {str(e)[:100]}")
            return False

    def cancel_form(self):
        try:
            cancel_btn = self.page.locator("button.btn-close")
            cancel_btn.first.click()
            print("[✓] Cancelled")
            self.page.wait_for_timeout(500)
            return True
        except Exception as e:
            print(f"[✗] Cancel: {str(e)[:100]}")
            return False

    # VALIDATION
    def get_validation_errors(self):
        try:
            errors = self.page.locator('.error')
            error_list = []
            for i in range(errors.count()):
                error_text = errors.nth(i).inner_text()
                if error_text and error_text.strip():
                    error_list.append(error_text.strip())
            if error_list:
                print(f"[⚠] Errors: {error_list}")
            return error_list
        except:
            return []

    def get_success_message(self):
        try:
            message = self.page.locator(".toast-message, .alert-success")
            if message.count() > 0:
                text = message.first.inner_text()
                print(f"[✓] {text}")
                return text
            return ""
        except:
            return ""

    # FILL FORM
    def fill_add_employee_form(self, employee_data):
        print("\n[FILLING FORM]")
        print("-" * 60)
        all_filled = True

        # Critical fields that must be filled
        if "employee_id" in employee_data and employee_data["employee_id"]:
            if not self.fill_employee_id(employee_data["employee_id"]):
                all_filled = False
        if "email" in employee_data and employee_data["email"]:
            if not self.fill_email(employee_data["email"]):
                all_filled = False
        if "first_name" in employee_data and employee_data["first_name"]:
            if not self.fill_first_name(employee_data["first_name"]):
                all_filled = False
        if "last_name" in employee_data and employee_data["last_name"]:
            if not self.fill_last_name(employee_data["last_name"]):
                all_filled = False

        # Optional fields
        if "gender" in employee_data and employee_data["gender"]:
            self.select_gender(employee_data["gender"])
        if "department" in employee_data and employee_data["department"]:
            self.select_department(employee_data["department"])
        if "designation" in employee_data and employee_data["designation"]:
            self.select_designation(employee_data["designation"])
        if "reporting_to" in employee_data and employee_data["reporting_to"]:
            self.select_reporting_to(employee_data["reporting_to"])
        if "employment_type" in employee_data and employee_data["employment_type"]:
            self.select_employment_type(employee_data["employment_type"])
        if "role" in employee_data and employee_data["role"]:
            self.select_role(employee_data["role"])

        # Checkboxes
        if "invite" in employee_data:
            self.check_invite_employee(employee_data["invite"])
        if "joining_window" in employee_data:
            self.check_joining_window(employee_data["joining_window"])

        print("-" * 60)
        print(f"[{'✓' if all_filled else '⚠'}] Form: {'COMPLETE' if all_filled else 'INCOMPLETE'}")
        return all_filled

    # REACT-SELECT HANDLER
    def _select_react_dropdown(self, dropdown_id, value, friendly_name):
        try:
            container = self.modal.locator(f"div#{dropdown_id}")
            input_control = container.locator("input[role='combobox']")
            input_control.wait_for(state="visible", timeout=5000)
            
            # Click to open dropdown
            input_control.click()
            self.page.wait_for_timeout(300)
            
            # Type the value
            input_control.fill(str(value), timeout=5000)
            self.page.wait_for_timeout(500)
            
            # Wait for options to appear
            self.page.wait_for_timeout(300)
            self.page.keyboard.press('Enter')
            self.page.wait_for_timeout(200)
            
            print(f"[✓] {friendly_name}: {value}")
            return True
        except Exception as e:
            print(f"[⚠] {friendly_name}: {str(e)[:80]}")
            return False

    # DATA GENERATION
    def generate_random_employee_data(self):
        first_names = ["Alex", "Sam", "Jordan", "Taylor", "Casey", "Riley", "Morgan", "Jamie", "Chris", "Parker"]
        last_names = ["Smith", "Johnson", "Lee", "Brown", "Garcia", "Martinez", "Davis", "Wilson", "Anderson"]
        first = random.choice(first_names)
        last = random.choice(last_names)
        uid = uuid.uuid4().hex[:8]
        emp_id = str(random.randint(100000, 999999))
        email = f"{first.lower()}.{last.lower()}+{uid}@example.com"
        return {
            "employee_id": emp_id,
            "email": email,
            "first_name": first,
            "last_name": last,
            "gender": random.choice(TestData.EMPLOYEE_GENDERS),
            "department": random.choice(TestData.EMPLOYEE_DEPARTMENTS),
            "designation": random.choice(TestData.EMPLOYEE_DESIGNATIONS),
            "reporting_to": None,
            "employment_type": random.choice(TestData.EMPLOYEE_EMPLOYMENT_TYPES),
            "role": random.choice(TestData.EMPLOYEE_ROLES),
            "invite": True,
            "joining_window": False,
        }

    # MAIN FLOW
    def add_random_employee(self, choose_random_options=False):
        print("\n" + "=" * 70)
        print("[ ADD RANDOM EMPLOYEE ]")
        print("=" * 70)
        data = self.generate_random_employee_data()
        print("\n[GENERATED]")
        for k, v in data.items():
            if v is not None:
                print(f"  {k}: {v}")
        filled = self.fill_add_employee_form(data)
        details = {"filled": filled}
        if not filled:
            print("\n[✗] Form incomplete")
            return (False, data, details)
        saved = self.save_employee()
        details["saved"] = saved
        details["success_message"] = self.get_success_message()
        details["validation_errors"] = self.get_validation_errors()
        print(f"\n[{'✓' if saved else '✗'}] Result: {saved}")
        print("=" * 70)
        return (saved, data, details)


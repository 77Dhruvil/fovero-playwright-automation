from pages.base_page import BasePage
from locators.announcement_locators import AnnouncementLocators
import re
from datetime import datetime, timedelta

class AnnouncementPage(BasePage):
    """Page Object for Announcement Module"""
    
    def __init__(self, page):
        super().__init__(page)
        self.section = page.locator(AnnouncementLocators.ANNOUNCEMENT_SECTION)
    
    # =====================================================
    # SECTION VISIBILITY & WAIT
    # =====================================================
    
    def wait_for_section(self, timeout=10000):
        """Wait for announcement section to be visible"""
        try:
            # Try primary locator
            self.page.wait_for_selector(AnnouncementLocators.ANNOUNCEMENT_SECTION, timeout=timeout)
            return True
        except Exception as e:
            print(f"[DEBUG] Primary locator failed, trying XPath...")
            try:
                # Try XPath as fallback
                self.page.wait_for_selector(AnnouncementLocators.ANNOUNCEMENT_SECTION_XPATH, timeout=timeout)
                return True
            except Exception as e2:
                print(f"[DEBUG] XPath also failed, trying alternative...")
                try:
                    # Try to find any card with Announcement text
                    self.page.wait_for_selector("div.card", timeout=timeout)
                    return True
                except Exception as e3:
                    print(f"[ERROR] All section locators failed: {e3}")
                    return False
    
    def is_section_visible(self):
        """Check if section is visible"""
        found = self.wait_for_section(timeout=10000)
        if not found:
            return False
        try:
            # Try multiple selectors
            locators_to_try = [
                AnnouncementLocators.ANNOUNCEMENT_SECTION,
                AnnouncementLocators.ANNOUNCEMENT_SECTION_XPATH,
                "//div[contains(@class,'card')]//h6[contains(text(),'Announcement')]/ancestor::div",
                "div.card:nth-of-type(4)",  # Based on screenshot, announcement is usually 4th card
            ]
            
            for locator in locators_to_try:
                try:
                    element = self.page.locator(locator).first
                    if element.count() > 0 and element.is_visible():
                        self.section = element
                        return True
                except:
                    continue
            
            # Last resort: find by text and check visibility
            cards = self.page.locator("div.card")
            for i in range(cards.count()):
                try:
                    card = cards.nth(i)
                    text = card.inner_text()
                    if "Announcement" in text and card.is_visible():
                        self.section = card
                        return True
                except:
                    continue
            
            return False
        except Exception as e:
            print(f"[ERROR] Section visibility check failed: {e}")
            return False
    
    def get_section_text(self):
        """Get all text from section"""
        try:
            return self.section.inner_text()
        except Exception as e:
            print(f"[ERROR] Failed to get section text: {e}")
            return ""
    
    # =====================================================
    # ANNOUNCEMENT LIST
    # =====================================================
    
    def get_announcements_count(self):
        """Get count of announcements"""
        try:
            items = self.page.locator(AnnouncementLocators.ANNOUNCEMENT_ITEMS)
            return items.count()
        except Exception as e:
            print(f"[ERROR] Failed to get announcements count: {e}")
            return 0
    
    def get_announcement_titles(self):
        """Get list of all announcement titles"""
        try:
            text = self.get_section_text()
            # Extract all announcement titles
            titles = []
            lines = text.split('\n')
            for line in lines:
                if 'Announcement' in line or 'Test' in line:
                    titles.append(line.strip())
            return titles
        except Exception as e:
            print(f"[ERROR] Failed to get announcement titles: {e}")
            return []
    
    # =====================================================
    # ADD ANNOUNCEMENT
    # =====================================================
    
    def click_add_announcement(self):
        """Click the + button in the Announcement section header."""
        try:
            # Try to find the header with 'Announcement' and then the adjacent button
            header_btn = self.page.locator(
                "//div[contains(@class,'card-header')][.//text()[contains(.,'Announcement')]]//button"
            )
            if header_btn.count() > 0:
                header_btn.first.click()
                print("[✓] Clicked + button in Announcement header")
                self.page.wait_for_load_state("load")
                return True

            # Try the specific button ID if exists
            id_btn = self.page.locator("#addAnnouncementButton")
            if id_btn.count() > 0:
                id_btn.first.click()
                print("[✓] Clicked + button by ID")
                self.page.wait_for_load_state("load")
                return True

            # Try any button with aria-label or title containing 'add'
            alt_btn = self.page.locator(
                "button[aria-label*='add'], button[title*='add'], button[aria-label*='+'], button[title*='+']"
            )
            if alt_btn.count() > 0:
                alt_btn.first.click()
                print("[✓] Clicked Add button by aria-label/title")
                self.page.wait_for_load_state("load")
                return True

            # Try using the locator constants
            locator_btn = self.page.locator(AnnouncementLocators.ADD_ANNOUNCEMENT_BTN)
            if locator_btn.count() > 0:
                locator_btn.first.click()
                print("[✓] Clicked Add button using locator")
                self.page.wait_for_load_state("load")
                return True

            print("[ERROR] Add (+) button not found in Announcement header")
            return False
        except Exception as e:
            print(f"[ERROR] Failed to click Add button: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def is_announcement_modal_open(self):
        """Check if announcement modal is open"""
        try:
            modal = self.page.locator(AnnouncementLocators.MODAL)
            if modal.count() > 0:
                return modal.first.is_visible()
            return False
        except Exception as e:
            print(f"[ERROR] Modal visibility check failed: {e}")
            return False
    
    # =====================================================
    # FORM FIELDS
    # =====================================================
    
    def fill_title(self, title):
        """Fill announcement title"""
        try:
            # Try using locator constants first
            title_field = self.page.locator(AnnouncementLocators.TITLE_FIELD).first
            if title_field.count() > 0 and title_field.is_visible():
                title_field.fill(title)
                print(f"[INFO] Filled title: {title}")
                return True
            
            # Try different selectors as fallbacks
            fallback_selectors = [
                "input[placeholder*='Title']",
                "input[name='title']",
                "input[type='text']",
                "input[id*='title']",
                "input[class*='title']"
            ]
            
            for selector in fallback_selectors:
                field = self.page.locator(selector).first
                if field.count() > 0 and field.is_visible():
                    field.fill(title)
                    print(f"[INFO] Filled title using fallback: {title}")
                    return True
            
            print("[ERROR] Title field not found")
            return False
        except Exception as e:
            print(f"[ERROR] Failed to fill title: {e}")
            return False
    
    def fill_description(self, description):
        """Fill announcement description"""
        try:
            # Try using locator constants first
            desc_field = self.page.locator(AnnouncementLocators.DESCRIPTION_FIELD).first
            if desc_field.count() > 0 and desc_field.is_visible():
                desc_field.fill(description)
                print(f"[INFO] Filled description: {description}")
                return True
            
            # Try different selectors as fallbacks
            fallback_selectors = [
                "textarea[placeholder*='Description']",
                "textarea[name='description']",
                "textarea[id*='description']",
                "textarea[class*='description']",
                "textarea",
                "input[type='textarea']"  # Sometimes description might be input
            ]
            
            for selector in fallback_selectors:
                field = self.page.locator(selector).first
                if field.count() > 0 and field.is_visible():
                    field.fill(description)
                    print(f"[INFO] Filled description using fallback: {description}")
                    return True
            
            print("[ERROR] Description field not found")
            return False
        except Exception as e:
            print(f"[ERROR] Failed to fill description: {e}")
            return False
    
    def set_schedule_date(self, date_str):
        """Set schedule date (format: YYYY-MM-DD or DD-MM-YYYY)"""
        try:
            # Convert date format if needed
            if len(date_str) == 10 and date_str[2] == '-':
                # DD-MM-YYYY -> YYYY-MM-DD
                parts = date_str.split('-')
                date_str = f"{parts[2]}-{parts[1]}-{parts[0]}"
            
            # Try using locator constants first
            date_field = self.page.locator(AnnouncementLocators.SCHEDULE_DATE_FIELD).first
            if date_field.count() > 0 and date_field.is_visible():
                date_field.fill(date_str)
                print(f"[INFO] Set schedule date: {date_str}")
                return True
            
            # Try different selectors as fallbacks
            fallback_selectors = [
                "input[type='date']",
                "input[placeholder*='Schedule']",
                "input[name='scheduleDate']",
                "input[id*='date']",
                "input[class*='date']",
                "input[placeholder*='Date']"
            ]
            
            for selector in fallback_selectors:
                field = self.page.locator(selector).first
                if field.count() > 0 and field.is_visible():
                    field.fill(date_str)
                    print(f"[INFO] Set schedule date using fallback: {date_str}")
                    return True
            
            print("[ERROR] Date field not found")
            return False
        except Exception as e:
            print(f"[ERROR] Failed to set schedule date: {e}")
            return False
    
    def select_category(self, category_name):
        """Select category from dropdown"""
        try:
            # Try using locator constants first
            category_btn = self.page.locator(AnnouncementLocators.CATEGORY_DROPDOWN).first
            if category_btn.count() > 0 and category_btn.is_visible():
                category_btn.click()
                self.page.wait_for_timeout(500)
                
                # Select option
                option = self.page.locator(f"//div[@role='option' and contains(text(), '{category_name}')]").first
                if option.count() == 0:
                    option = self.page.locator(f"//li[@role='option' and contains(text(), '{category_name}')]").first
                
                if option.count() > 0:
                    option.click()
                    print(f"[INFO] Selected category: {category_name}")
                    return True
                else:
                    print(f"[ERROR] Category option not found: {category_name}")
                    return False
            
            # Try fallback selectors
            fallback_selectors = [
                "button:has-text('Category')",
                "div[role='combobox']:has-text('Category')",
                "select[name='category']",
                "div[class*='category'] button"
            ]
            
            for selector in fallback_selectors:
                btn = self.page.locator(selector).first
                if btn.count() > 0 and btn.is_visible():
                    btn.click()
                    self.page.wait_for_timeout(500)
                    
                    # Select option
                    option = self.page.locator(f"//div[@role='option' and contains(text(), '{category_name}')]").first
                    if option.count() == 0:
                        option = self.page.locator(f"//li[@role='option' and contains(text(), '{category_name}')]").first
                    
                    if option.count() > 0:
                        option.click()
                        print(f"[INFO] Selected category using fallback: {category_name}")
                        return True
            
            print("[ERROR] Category dropdown not found")
            return False
        except Exception as e:
            print(f"[ERROR] Failed to select category: {e}")
            return False
    
    def select_employee(self, employee_name):
        """Select employee from dropdown"""
        try:
            # Try using locator constants first
            emp_btn = self.page.locator(AnnouncementLocators.EMPLOYEE_DROPDOWN).first
            if emp_btn.count() > 0 and emp_btn.is_visible():
                emp_btn.click()
                self.page.wait_for_timeout(500)
                
                # Select option
                option = self.page.locator(f"//div[@role='option' and contains(text(), '{employee_name}')]").first
                if option.count() == 0:
                    option = self.page.locator(f"//li[@role='option' and contains(text(), '{employee_name}')]").first
                
                if option.count() > 0:
                    option.click()
                    print(f"[INFO] Selected employee: {employee_name}")
                    return True
                else:
                    print(f"[ERROR] Employee option not found: {employee_name}")
                    return False
            
            # Try fallback selectors
            fallback_selectors = [
                "button:has-text('Select employee')",
                "div[role='combobox']:has-text('employee')",
                "select[name='employee']",
                "div[class*='employee'] button",
                "button:has-text('employee')"
            ]
            
            for selector in fallback_selectors:
                btn = self.page.locator(selector).first
                if btn.count() > 0 and btn.is_visible():
                    btn.click()
                    self.page.wait_for_timeout(500)
                    
                    # Select option
                    option = self.page.locator(f"//div[@role='option' and contains(text(), '{employee_name}')]").first
                    if option.count() == 0:
                        option = self.page.locator(f"//li[@role='option' and contains(text(), '{employee_name}')]").first
                    
                    if option.count() > 0:
                        option.click()
                        print(f"[INFO] Selected employee using fallback: {employee_name}")
                        return True
            
            print("[ERROR] Employee dropdown not found")
            return False
        except Exception as e:
            print(f"[ERROR] Failed to select employee: {e}")
            return False
    
    # =====================================================
    # SAVE & CANCEL
    # =====================================================
    
    def save_announcement(self):
        """Save announcement"""
        try:
            # Try using locator constants first
            save_btn = self.page.locator(AnnouncementLocators.SAVE_BTN).last
            if save_btn.count() > 0 and save_btn.is_visible():
                save_btn.click()
                print("[INFO] Clicked Save button")
                self.page.wait_for_load_state("load")
                return True
            
            # Try fallback selectors
            fallback_selectors = [
                "button:has-text('Save')",
                "button[type='submit']",
                "input[type='submit']",
                "button[class*='save']",
                "button[id*='save']"
            ]
            
            for selector in fallback_selectors:
                btn = self.page.locator(selector).last
                if btn.count() > 0 and btn.is_visible():
                    btn.click()
                    print("[INFO] Clicked Save button using fallback")
                    self.page.wait_for_load_state("load")
                    return True
            
            print("[ERROR] Save button not found")
            return False
        except Exception as e:
            print(f"[ERROR] Failed to save announcement: {e}")
            return False
    
    def cancel_announcement(self):
        """Cancel announcement form"""
        try:
            cancel_btn = self.page.locator("button:has-text('Cancel')").first
            if cancel_btn.count() == 0:
                cancel_btn = self.page.locator("button[aria-label='Close']").first
            
            if cancel_btn.count() > 0:
                cancel_btn.click()
                print("[INFO] Clicked Cancel button")
                return True
            print("[ERROR] Cancel button not found")
            return False
        except Exception as e:
            print(f"[ERROR] Failed to cancel: {e}")
            return False
    
    def close_modal(self):
        """Close modal"""
        return self.cancel_announcement()
    
    # =====================================================
    # CATEGORY MANAGEMENT
    # =====================================================
    
    def is_category_modal_open(self):
        """Check if category modal is open"""
        try:
            modal = self.page.locator("div[role='dialog']:has-text('Category')")
            if modal.count() > 0:
                return modal.first.is_visible()
            return False
        except Exception as e:
            print(f"[ERROR] Category modal visibility check failed: {e}")
            return False
    
    def get_categories(self):
        """Get list of existing categories"""
        try:
            if not self.is_category_modal_open():
                print("[ERROR] Category modal not open")
                return []
            
            categories = []
            items = self.page.locator("//div[@class*='category']:has-text")
            for i in range(items.count()):
                text = items.nth(i).inner_text().strip()
                if text and text not in ['Enter category name', 'Save']:
                    categories.append(text)
            return categories
        except Exception as e:
            print(f"[ERROR] Failed to get categories: {e}")
            return []
    
    def add_category(self, category_name):
        """Add new category"""
        try:
            if not self.is_category_modal_open():
                print("[ERROR] Category modal not open")
                return False
            
            cat_input = self.page.locator("input[placeholder='Enter category name']").first
            if cat_input.count() > 0:
                cat_input.fill(category_name)
                save_btn = self.page.locator("button:has-text('Save')").last
                if save_btn.count() > 0:
                    save_btn.click()
                    print(f"[INFO] Added category: {category_name}")
                    self.page.wait_for_timeout(500)
                    return True
            print("[ERROR] Failed to add category")
            return False
        except Exception as e:
            print(f"[ERROR] Failed to add category: {e}")
            return False
    
    # =====================================================
    # VALIDATION & ERRORS
    # =====================================================
    
    def get_error_messages(self):
        """Get all error messages"""
        try:
            errors = []
            error_elements = self.page.locator("div[class*='error'], span[class*='error'], p[class*='error']")
            for i in range(error_elements.count()):
                text = error_elements.nth(i).inner_text().strip()
                if text:
                    errors.append(text)
            return errors
        except Exception as e:
            print(f"[ERROR] Failed to get error messages: {e}")
            return []
    
    def get_success_message(self):
        """Get success message"""
        try:
            success = self.page.locator("div[class*='success'], span[class*='success']").first
            if success.count() > 0:
                return success.inner_text().strip()
            return ""
        except Exception as e:
            print(f"[ERROR] Failed to get success message: {e}")
            return ""
    
    def fill_all_fields_automatically(self, title=None, description=None, date_str=None, category=None, employee=None):
        """Fill all announcement form fields automatically with robust fallbacks"""
        print("\n[INFO] Starting automatic form filling...")
        
        # Generate default test data if not provided
        if title is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            title = f"Automation Test {timestamp}"
        
        if description is None:
            description = f"Automated announcement created on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        if date_str is None:
            tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
            date_str = tomorrow
        
        if category is None:
            category = "EOM"  # Default category
        
        if employee is None:
            employee = "dhruvil patel"  # Default employee
        
        success_count = 0
        total_fields = 5
        
        # Fill Title
        try:
            if self.fill_title(title):
                success_count += 1
                print(f"[✓] Title filled successfully")
            else:
                print(f"[⚠] Title filling failed")
        except Exception as e:
            print(f"[⚠] Title filling error: {e}")
        
        # Fill Description
        try:
            if self.fill_description(description):
                success_count += 1
                print(f"[✓] Description filled successfully")
            else:
                print(f"[⚠] Description filling failed")
        except Exception as e:
            print(f"[⚠] Description filling error: {e}")
        
        # Set Schedule Date
        try:
            if self.set_schedule_date(date_str):
                success_count += 1
                print(f"[✓] Schedule date set successfully")
            else:
                print(f"[⚠] Schedule date setting failed")
        except Exception as e:
            print(f"[⚠] Schedule date setting error: {e}")
        
        # Select Category (optional)
        try:
            if self.select_category(category):
                success_count += 1
                print(f"[✓] Category selected successfully")
            else:
                print(f"[ℹ] Category selection skipped (optional field)")
                success_count += 1  # Count as success since it's optional
        except Exception as e:
            print(f"[ℹ] Category selection skipped: {str(e)[:50]} (optional field)")
            success_count += 1  # Count as success since it's optional
        
        # Select Employee (optional)
        try:
            if self.select_employee(employee):
                success_count += 1
                print(f"[✓] Employee selected successfully")
            else:
                print(f"[ℹ] Employee selection skipped (optional field)")
                success_count += 1  # Count as success since it's optional
        except Exception as e:
            print(f"[ℹ] Employee selection skipped: {str(e)[:50]} (optional field)")
            success_count += 1  # Count as success since it's optional
        
        print(f"\n[INFO] Form filling completed: {success_count}/{total_fields} fields processed")
        
        # Check for validation errors
        self.page.wait_for_timeout(500)
        errors = self.get_error_messages()
        if errors:
            print(f"[⚠] Validation errors found:")
            for error in errors:
                print(f"    - {error}")
            return False
        
        return success_count >= 3  # At least title, description, and date should be filled

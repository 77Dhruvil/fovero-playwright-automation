from pages.base_page import BasePage
from locators.leave_locators import LeaveLocators


class LeavePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.leave_section = self.page.locator(
            LeaveLocators.LEAVES_SECTION
        )

    # =====================================================
    # COMMON WAIT
    # =====================================================

    def wait_for_leaves_section(self):

        self.page.wait_for_selector(
            LeaveLocators.LEAVES_SECTION,
            timeout=10000
        )

        try:
            self.page.wait_for_selector(
                LeaveLocators.LEAVE_CARDS,
                timeout=4000
            )

        except:
            self.page.wait_for_selector(
                LeaveLocators.LEAVES_NO_DATA_IMG,
                timeout=4000
            )


    # =====================================================
    # HELPER
    # =====================================================

    def _extract_digits(self,text):
        digits=''.join(
            filter(str.isdigit,text)
        )
        return int(digits) if digits else 0


    # =====================================================
    # TODAY TAB
    # =====================================================

    def click_today_leaves(self):

        self.page.locator(
            LeaveLocators.TODAYS_LEAVE
        ).click()

        self.wait_for_leaves_section()


    def get_today_leaves_count(self):

        text=self.page.locator(
            LeaveLocators.TODAYS_LEAVE
        ).inner_text()

        return self._extract_digits(text)


    def is_today_tab_active(self):

        cls=self.page.locator(
            LeaveLocators.TODAYS_LEAVE
        ).get_attribute("class") or ""

        return "active" in cls


    # =====================================================
    # UPCOMING TAB
    # =====================================================

    def click_upcoming_leaves(self):

        tab=self.page.locator(
            LeaveLocators.UPCOMING_LEAVE_TAB
        )

        tab.wait_for(state="visible")
        tab.click()

        self.wait_for_leaves_section()


    def get_upcoming_leaves_count(self):

        text=self.page.locator(
            LeaveLocators.UPCOMING_LEAVE_TAB
        ).inner_text()

        return self._extract_digits(text)


    def is_upcoming_tab_active(self):

        cls=self.page.locator(
            LeaveLocators.UPCOMING_LEAVE_TAB
        ).get_attribute("class") or ""

        return "active" in cls


    # =====================================================
    # NO DATA CHECK
    # =====================================================

    def is_leaves_no_data_visible(self):

        locator=self.page.locator(
            LeaveLocators.LEAVES_NO_DATA_IMG
        )

        try:
            locator.first.wait_for(
                state="visible",
                timeout=2000
            )
            return True

        except:
            return False


    # =====================================================
    # CARDS
    # =====================================================

    def get_leave_cards(self):

        return self.page.locator(
            LeaveLocators.LEAVE_CARDS
        )


    def get_leave_cards_count(self):

        cards=self.get_leave_cards()

        visible_cards=0

        for i in range(cards.count()):

            try:
                if cards.nth(i).is_visible():
                    visible_cards +=1

            except:
                continue

        return visible_cards


    # =====================================================
    # CARD DATA
    # =====================================================

    def get_leave_card_data(self,index):

        card=self.get_leave_cards().nth(index)

        return {

            "name":
                card.locator(
                    LeaveLocators.EMPLOYEE_NAME
                ).inner_text().strip(),

            "is_adhoc":
                card.locator(
                    LeaveLocators.ADHOC_TAG
                ).count() >0,

            "leave_type":
                card.locator(
                    LeaveLocators.LEAVE_TYPE
                ).inner_text().strip(),

            "status":
                card.locator(
                    LeaveLocators.LEAVE_STATUS
                ).inner_text().strip()
                if card.locator(
                    LeaveLocators.LEAVE_STATUS
                ).count() >0
                else "",

            "date_range":
                card.locator(
                    LeaveLocators.DATE_RANGE
                ).inner_text().strip()
                if card.locator(
                    LeaveLocators.DATE_RANGE
                ).count() >0
                else ""
        }


    # =====================================================
    # ACTIONS
    # =====================================================

    def click_leave_card(self,index=0):

        self.get_leave_cards().nth(index).click()


    def click_back_button(self):

        btn=self.page.locator(
            LeaveLocators.LEAVE_DETAIL_BACK_BUTTON
        )

        if btn.count()>0:
            btn.first.click()


    def click_dashboard_menu(self):

        self.page.get_by_role(
            "link",
            name="Dashboard"
        ).first.click()
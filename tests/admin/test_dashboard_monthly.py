from pages.setting_page import SettingsPage


def test_monthly_work_timing_insights(admin_dashboard_login):

    dashboard = admin_dashboard_login
    page = dashboard.page

    settings = SettingsPage(page)

    # ✅ MUST open settings page first
    settings.open_settings()

    # ✅ Then get values
    office_start, office_end = settings.get_office_time()
    break_start, break_end = settings.get_break_time()

    # ✅ Go back to dashboard
    page.goto("https://fovero-uat.concettoprojects.com/dashboard")

    dashboard.open_dashboard()
    dashboard.get_monthly_card()

    # ✅ Validate
    dashboard.validate_with_settings(
        office_start,
        office_end,
        break_start,
        break_end
    )
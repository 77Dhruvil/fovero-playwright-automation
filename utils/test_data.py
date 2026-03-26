class TestData:

    # -------------------------------
    # 🔐 LOGIN DATA
    # -------------------------------
    VALID_ADMIN = {
        "email": "dhruvil.patel+801@concettolabs.com",
        "password": "Test@1234"
    }

    # VALID_EMPLOYEE = {
    #     "email": "employee@fovero.com",
    #     "password": "Emp@123"
    # }
    #
    # INVALID_LOGIN = {
    #     "email": "wrong@fovero.com",
    #     "password": "wrong123"
    # }


    # -------------------------------
    # 📊 DASHBOARD EXPECTATIONS
    # -------------------------------
    DASHBOARD = {
        "sections": [
            "Last 12 Months",
            "Birthday",
            "Live Attendance",
            "Leaves",
            "WFH",
            "Announcement",
            "Attendance & Productivity Insights",
            "Monthly Work Timing Insights",
            "Leave Balance"
        ]
    }


    # -------------------------------
    # 🟢 ATTENDANCE DATA RULES
    # -------------------------------
    ATTENDANCE = {
        "min_value": 0
    }


    # -------------------------------
    # 🏖️ LEAVE DATA
    # -------------------------------
    LEAVE = {
        "types": ["Casual Leave", "Compensatory Off"]
    }


    # -------------------------------
    # 📢 ANNOUNCEMENT DATA
    # -------------------------------
    ANNOUNCEMENT = {
        "title": "Test Announcement",
        "description": "This is automated test announcement"
    }
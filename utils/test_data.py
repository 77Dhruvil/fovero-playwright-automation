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

    # -------------------------------
    # 👨‍💼 EMPLOYEE DATA
    # -------------------------------
    EMPLOYEE_GENDERS = [
        "Male",
        "Female",
        "Other"
    ]

    EMPLOYEE_DEPARTMENTS = [
        "Other",
        "Project Management",
        "PHP",
        "Mobile Team",
        "SEO Team",
        "QA Team"
    ]

    EMPLOYEE_DESIGNATIONS = [
        "Software Engineer",
        "Senior Software Engineer",
        "Business Analyst",
        "Technical Lead",
        "Project Manager",
        "Quality Analyst",
        "Junior Quality Analyst",
        "Administrator",
        "Web Analyst",
        "Tech Lead"
    ]

    EMPLOYEE_EMPLOYMENT_TYPES = [
        "Full-Time",
        "Part-Time",
        "Contract",
        "Intern"
    ]

    EMPLOYEE_ROLES = [
        "Admin",
        "Employee",
        "Manager",
        "HR",
        "Finance"
    ]

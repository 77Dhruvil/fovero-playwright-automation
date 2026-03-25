import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL")
    LOGIN_PATH = os.getenv("LOGIN_PATH")

    @classmethod
    def get_login_url(cls):
        return f"{cls.BASE_URL}{cls.LOGIN_PATH}"

    USERS = {
        "administrator": {
            "email": os.getenv("ADMINISTRATOR_EMAIL"),
            "password": os.getenv("ADMINISTRATOR_PASSWORD")
        },
        "employee": {
            "email": os.getenv("EMPLOYEE_EMAIL"),
            "password": os.getenv("EMPLOYEE_PASSWORD")
        },
        "pm": {
            "email": os.getenv("PM_EMAIL"),
            "password": os.getenv("PM_PASSWORD")
        },
        "hr": {
            "email": os.getenv("HR_EMAIL"),
            "password": os.getenv("HR_PASSWORD")
        },
        "sales": {
            "email": os.getenv("SALES_EMAIL"),
            "password": os.getenv("SALES_PASSWORD")
        },
    }
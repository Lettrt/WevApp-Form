import re
from datetime import datetime

def validate_email_address(email: str) -> bool:
    pattern = r'^\w+[\w.-]*@\w+[\w.-]*\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    pattern = r'^\+7\s?\d{3}\s?\d{3}\s?\d{2}\s?\d{2}$'
    return re.match(pattern, phone) is not None

def validate_date(date: str) -> bool:
    for date_format in ('%d.%m.%Y', '%Y-%m-%d'):
        try:
            datetime.strptime(date, date_format)
            return True
        except ValueError:
            continue
    return False

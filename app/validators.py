from email_validator import validate_email, EmailNotValidError
import phonenumbers
from datetime import datetime

def validate_email_address(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def validate_phone(phone: str) -> bool:
    try:
        phone_number = phonenumbers.parse(phone, 'RU')
        return phonenumbers.is_valid_number(phone_number)
    except phonenumbers.NumberParseException:
        return False

def validate_date(date: str) -> bool:
    for date_format in ('%d.%m.%Y', '%Y-%m-%d'):
        try:
            datetime.strptime(date, date_format)
            return True
        except ValueError:
            continue
    return False

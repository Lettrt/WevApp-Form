import pytest
from .validators import validate_email_address, validate_phone, validate_date
from .routers import find_template, validate_field
from .models import Form

def test_validate_email_address():
    assert validate_email_address("test@example.com") == True
    assert validate_email_address("invalid-email") == False

def test_validate_phone():
    assert validate_phone("+7 123 456 7890") == True
    assert validate_phone("12345") == False

def test_validate_date():
    assert validate_date("01.01.2020") == True
    assert validate_date("2020-01-01") == True
    assert validate_date("01/01/2020") == False

@pytest.fixture
def mock_forms():
    return [
        Form(name='Test Form 1', fields={'email': 'email', 'phone': 'phone'}),
        Form(name='Test Form 2', fields={'email': 'email', 'full_name': 'text'})
    ]

def test_find_template_with_valid_data(mock_forms):
    form_data = {'email': 'test@example.com', 'phone': '+71234567890'}
    matched_template = find_template(form_data, mock_forms)
    assert matched_template.name == 'Test Form 1'

def test_find_template_with_missing_field(mock_forms):
    form_data = {'email': 'test@example.com'}
    matched_template = find_template(form_data, mock_forms)
    assert matched_template is None

def test_find_template_with_extra_field(mock_forms):
    form_data = {'email': 'test@example.com', 'phone': '+71234567890', 'extra_field': 'extra'}
    matched_template = find_template(form_data, mock_forms)
    assert matched_template.name == 'Test Form 1'

def test_validate_field():
    assert validate_field('test@example.com', 'email') == True
    assert validate_field('+71234567890', 'phone') == True
    assert validate_field('01.01.2020', 'date') == True
    assert validate_field('some text', 'text') == True
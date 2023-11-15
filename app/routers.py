from fastapi import APIRouter, Request
from .models import Form
from .validators import validate_email_address, validate_date, validate_phone
from typing import Dict, List, Optional

router = APIRouter()

def find_template(form_data: Dict[str, str], templates: List[Form]) -> Optional[Form]:
    for template in templates:
        if all(key in form_data for key in template.fields.keys()):
            if all(validate_field(form_data[key], template.fields[key]) for key in template.fields.keys()):
                return template

    print("No templates found.")
    return None

def validate_field(value: str, field_type: str) -> bool:
    if field_type == 'email':
        return validate_email_address(value)
    elif field_type == 'phone':
        return validate_phone(value)
    elif field_type == 'date':
        return validate_date(value)
    else:
        return True

@router.post('/get_form')
async def get_form(request: Request):
    form_data = await request.form()
    templates = list(Form.objects())
    matched_template = find_template(form_data, templates)
    if matched_template:
        return {'template_name': matched_template.name}
    else:
        unknown_fields = {key: unknown_field_type(value) for key, value in form_data.items()}
        return unknown_fields
    
def unknown_field_type(value: str) -> str:
    if validate_email_address(value):
        return 'email'
    elif validate_phone(value):
        return 'phone'
    elif validate_date(value):
        return 'date'
    else:
        return 'text'

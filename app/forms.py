from .models import Form

def create_initial_templates():
    templates = [
        {
            'name': 'Contact Form',
            'fields': {
                'email': 'email',
                'phone': 'phone',
                'full_name': 'text',
            }
        },
        {
            'name': 'Feedback Form',
            'fields': {
                'user_email': 'email',
                'message': 'text',
            }
        },
        {
            'name': 'Full Form',
            'fields': {
                'first_name': 'text',
                'last_name': 'text',
                'age': 'text',
                'phone': 'phone',
                'email_address': 'email',
                'message': 'text',
            }
        },

    ]

    for template_data in templates:
        try:
            template = Form.objects.get(name=template_data['name'])
            print(f"Template {template.name} already exists.")
        except Form.DoesNotExist:
            template = Form(name=template_data['name'], fields=template_data['fields']).save()
            print(f"Created template: {template.name}")
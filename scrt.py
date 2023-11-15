import requests

url = "http://127.0.0.1:8000/get_form"

data = {
    "email": "example@email.com",
    "phone": "+7 123 456 7890",
    "full_name": "No name"
}
response = requests.post(url, data=data)
print("Response for 'Contact Form':", response.text)

data = {
    "email": "example@email.com",
    "phone": "+7 123 456 7890",
    "full_name": "No name",
    "extra_field": "bla bla bla"
}
response = requests.post(url, data=data)
print("Response with extra field:", response.text)

data = {
    "random_field": "random data"
}
response = requests.post(url, data=data)
print("Response for unknown fields:", response.text)

data = {
    "email": "not an email",
    "phone": "not a phone number",
    "full_name": "Igor Nikolaev"
}
response = requests.post(url, data=data)
print("Response for invalid data:", response.text)

from django.test import TestCase
from mapApp.forms import RegisterForm
import json


# Create your tests here.

class RegisterFormTestCase(TestCase):
    def test_register_form_errors(self):
        data = {'email': 'abc', 'password1': 'cde', 'password2': 'cde'}
        form = RegisterForm(data)
        errors_json = form.errors.as_json()
        errors = json.loads(errors_json)
        print(errors)

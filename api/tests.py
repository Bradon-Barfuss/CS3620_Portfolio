from django.test import TestCase
from .models import Project, Contact

class SimpleTestCase(TestCase):
    def test_contact_creation(self):
        contact = Contact.objects.create(contact_name="John Doe", contact_email="john@example.com", contact_message="Hello")
        self.assertEqual(contact.contact_name, "John Doe")

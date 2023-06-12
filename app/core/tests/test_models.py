from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='rajsourav.singh58@gmail.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password) # type: ignore


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successfull"""
        email = 'rajkingpin910@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user( # type: ignore
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'rajkingpin910@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')  # type: ignore
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123') # type: ignore

    def test_create_new_superuser(self):
        """Test creating a new SuperUser"""
        user = get_user_model().objects.create_superuser( # type: ignore
            'rajkingpin910@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create( # type: ignore
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
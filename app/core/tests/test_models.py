from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'testpassword1'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_normalized(self):
        test_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in test_emails:
            user = get_user_model().objects.create_user(email, 'Password1')
            self.assertEqual(user.email, expected)

    def test_email_requirement(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Password1')

    def test_super_user(self):
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'Super1'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

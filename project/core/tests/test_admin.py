from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin = get_user_model().objects.create_superuser("admin@example.com", "password")
        self.client.force_login(self.admin)

        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="password",
            name="test_user"
        )

    def test_users_list(self):
        url = reverse("admin:core_user_changelist")

        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)
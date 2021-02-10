from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase

from django_cookie_app.tests import factories


class ListViewsetsTestMixin:
    """
        ListViewsetsTestMixin
    """
    client = Client()

    def test_user_get(self):
        """
            test_user_get
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class OrderViewsetsTest(ListViewsetsTestMixin, APITestCase):
    """
        OrderViewsetsTest
    """
    url = reverse('rest:order-list')
    factory = factories.OrderFactory


class ChocoOrangeViewsetsTest(ListViewsetsTestMixin, APITestCase):
    """
        ChocoOrangeViewsetsTest
    """
    url = reverse('rest:choc-oran-list')
    factory = factories.ChocoOrangeFactory


class RaspberryWhiteChocolateViewsetsTest(ListViewsetsTestMixin, APITestCase):
    """
        RaspberryWhiteChocolateViewsetsTest"
    """
    url = reverse('rest:rasp-whit-choc-list')
    factory = factories.RaspberryWhiteChocolateFactory


class VanillaStrawberryChocolateViewsetsTest(ListViewsetsTestMixin, APITestCase):
    """
        VanillaStrawberryChocolateViewsetsTest
    """
    url = reverse('rest:vani-stra-choc-list')
    factory = factories.VanillaStrawberryChocolateFactory


class SyrupViewsetsTest(ListViewsetsTestMixin, APITestCase):
    """
        SyrupViewsetsTest
    """
    url = reverse('rest:mapple-syrup-list')
    factory = factories.SyrupFactory


class MintChocoViewsetsTest(ListViewsetsTestMixin, APITestCase):
    """
        MintChocoViewsetsTest
    """
    url = reverse('rest:mint-choc-list')
    factory = factories.MintChocoFactory

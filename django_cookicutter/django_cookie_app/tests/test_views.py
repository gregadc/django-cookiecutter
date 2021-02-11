from django.contrib.auth.models import User, AnonymousUser
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from django_cookie_app import models
from django_cookie_app.tests import factories


class ListViewTestMixin:
    """
        ListViewTestMixin class
    """
    def SetUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def test_user_get(self):
        """
            test_user_get
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_anonymous_view(self):
        response = self.client.get(self.url)
        response.user = AnonymousUser()
        self.view.setup(response)


class HomeViewTest(ListViewTestMixin, TestCase):
    """
        HomeViewTest class
    """
    url = reverse('home')


class ChocoOrangeListViewTest(ListViewTestMixin, TestCase):
    """
        ChocoOrangeListViewTest class
    """
    url = reverse('choco-orange-view')


class MintChocoListViewTest(ListViewTestMixin, TestCase):
    """
        MintChocoListViewTest class
    """
    url = reverse('mint-choco-view')


class SyrupListViewTest(ListViewTestMixin, TestCase):
    """
        SyrupListViewTest class
    """
    url = reverse('syrup-view')


class VanillaStrawberryChocolateListViewTest(ListViewTestMixin, TestCase):
    """
        VanillaStrawberryChocolateListViewTest class
    """
    url = reverse('vani-stra-choc-view')


class RaspberryWhiteChocolateListViewTest(ListViewTestMixin, TestCase):
    """
        RaspberryWhiteChocolateListViewTest class
    """
    url = reverse('rasp-whit-choc-view')


class OrderListViewTest(ListViewTestMixin, TestCase):
    """
        OrderListViewTest class
    """
    url = reverse('order-list-view')


class OrderDetailViewTest(TestCase):
    """
        OrderDetailView class
    """
    factory = factories.OrderFactory
    queryset = models.Order.objects.all()

    def setUp(self):
        """
            setUp method
        """
        self.instance = self.factory.create()
        self.url = self.instance.get_absolute_url()

    def test_user_get(self):
        """
            test_user_get test
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

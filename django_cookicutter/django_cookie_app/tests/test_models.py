from django.test import TestCase

from django_cookie_app import models
from django_cookie_app.tests import factories


class OrderQuerysetTest(TestCase):
    """
        OrderQueryset
    """
    queryset = models.Order.objects.all()

    def setUp(self):
        """
            setUp method
        """
        self.factory = factories.OrderFactory.create()

    def test_queryset(self):
        """
            test_queryset method
        """
        self.assertEqual(self.queryset.get(id=self.factory.id), self.factory)


class ChocoOrangeQuerysetTest(TestCase):
    """
        ChocoOrangeQueryset
    """
    queryset = models.ChocoOrange.objects.all()

    def setUp(self):
        """
            setUp method
        """
        self.factory = factories.ChocoOrangeFactory.create()

    def test_queryset(self):
        """
            test_queryset method
        """
        self.assertEqual(self.queryset.get(id=self.factory.id), self.factory)


class MintChocoQuerysetTest(TestCase):
    """
        MintChocoQueryset
    """
    queryset = models.MintChoco.objects.all()

    def setUp(self):
        """
            setUp method
        """
        self.factory = factories.MintChocoFactory.create()

    def test_queryset(self):
        """
            test_queryset method
        """
        self.assertEqual(self.queryset.get(id=self.factory.id), self.factory)


class SyrupQuerysetTest(TestCase):
    """
        SyrupQueryset
    """
    queryset = models.Syrup.objects.all()

    def setUp(self):
        """
            setUp method
        """
        self.factory = factories.SyrupFactory.create()

    def test_queryset(self):
        """
            test_queryset method
        """
        self.assertEqual(self.queryset.get(id=self.factory.id), self.factory)


class VanillaStrawberryChocolateQuerysetTest(TestCase):
    """
        VanillaStrawberryChocolateQueryset
    """
    queryset = models.VanillaStrawberryChocolate.objects.all()

    def setUp(self):
        """
            setUp method
        """
        self.factory = factories.VanillaStrawberryChocolateFactory.create()

    def test_queryset(self):
        """
            test_queryset method
        """
        self.assertEqual(self.queryset.get(id=self.factory.id), self.factory)


class VanillaStrawberryChocolateTest(TestCase):
    """
        RaspberryWhiteChocolateTest
    """
    queryset = models.VanillaStrawberryChocolate.objects.all()

    def setUp(self):
        self.factory = factories.VanillaStrawberryChocolateFactory.create()

    def test_model(self):
        self.assertTrue(isinstance(self.factory, models.VanillaStrawberryChocolate))


class RaspberryWhiteChocolateQuerysetTest(TestCase):
    """
        RaspberryWhiteChocolateQueryset
    """
    queryset = models.RaspberryWhiteChocolate.objects.all()

    def setUp(self):
        """
            setUp method
        """
        self.factory = factories.RaspberryWhiteChocolateFactory.create()

    def test_queryset(self):
        """
            test_queryset method
        """
        self.assertEqual(self.queryset.get(id=self.factory.id), self.factory)


class RaspberryWhiteChocolateTest(TestCase):
    """
        RaspberryWhiteChocolateTest
    """
    queryset = models.RaspberryWhiteChocolate.objects.all()

    def setUp(self):
        self.factory = factories.RaspberryWhiteChocolateFactory.create()

    def test_model(self):
        self.assertTrue(isinstance(self.factory, models.RaspberryWhiteChocolate))

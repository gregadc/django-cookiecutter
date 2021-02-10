from datetime import date

import factory
from factory import fuzzy
from django_cookie_app import models


class BasePerfumFactory(factory.django.DjangoModelFactory):
    """
        BasePerfumFactory class
    """
    date = fuzzy.FuzzyDate(date(2000, 1, 1))
    total_ball = fuzzy.FuzzyInteger(0, 42)
    number_time_fill = fuzzy.FuzzyInteger(0, 42)
    percentage = fuzzy.FuzzyFloat(0.5, 42.7)
    ball_bought = fuzzy.FuzzyInteger(0, 42)


class ChocoOrangeFactory(BasePerfumFactory):
    """
        ChocoOrangeFactory class
    """
    perfume = factory.Faker('name')

    class Meta:
        model = models.ChocoOrange


class MintChocoFactory(BasePerfumFactory):
    """
        MintChocoFactory class
    """
    perfume = factory.Faker('name')

    class Meta:
        model = models.MintChoco


class SyrupFactory(BasePerfumFactory):
    """
        SyrupFactory class
    """
    perfume = factory.Faker('name')

    class Meta:
        model = models.Syrup


class VanillaStrawberryChocolateFactory(BasePerfumFactory):
    """
        VanillaStrawberryChocolateFactory class
    """
    perfume = factory.Faker('name')

    class Meta:
        model = models.VanillaStrawberryChocolate


class RaspberryWhiteChocolateFactory(BasePerfumFactory):
    """
        RaspberryWhiteChocolateFactory class
    """
    perfume = factory.Faker('name')

    class Meta:
        model = models.RaspberryWhiteChocolate


class OrderFactory(factory.django.DjangoModelFactory):
    """
        OrderFactory class
    """
    price = fuzzy.FuzzyInteger(0, 42)
    count_ball = fuzzy.FuzzyInteger(0, 42)
    code = factory.Faker('name')
    date = fuzzy.FuzzyDate(date(2000, 1, 1))
    choco_oran = factory.SubFactory(ChocoOrangeFactory)
    mint_choco = factory.SubFactory(MintChocoFactory)
    syrup = factory.SubFactory(SyrupFactory)
    vanilla = factory.SubFactory(VanillaStrawberryChocolateFactory)
    raspberry = factory.SubFactory(RaspberryWhiteChocolateFactory)

    class Meta:
        model = models.Order

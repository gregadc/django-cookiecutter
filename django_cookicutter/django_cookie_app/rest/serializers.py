from rest_framework import serializers
from django_cookie_app import models


class OrderSerializer(serializers.ModelSerializer):
    """
        OrderSerializer
    """
    class Meta:
        model = models.Order
        fields = '__all__'


class ChocoOrangeSerializer(serializers.ModelSerializer):
    """
        ChocoOrangeSerializer
    """
    class Meta:
        model = models.ChocoOrange
        fields = '__all__'


class MintChocoSerializer(serializers.ModelSerializer):
    """
        MintChocoSerializer
    """
    class Meta:
        model = models.MintChoco
        fields = '__all__'


class SyrupSerializer(serializers.ModelSerializer):
    """
        SyrupSerializer
    """
    class Meta:
        model = models.Syrup
        fields = '__all__'


class VanillaStrawberryChocolateSerializer(serializers.ModelSerializer):
    """
        VanillaStrawberryChocolateSerializer"
    """
    class Meta:
        """
            Meta
        """
        model = models.VanillaStrawberryChocolate
        fields = '__all__'


class RaspberryWhiteChocolateSerializer(serializers.ModelSerializer):
    """
        RaspberryWhiteChocolateSerializer
    """
    class Meta:
        model = models.RaspberryWhiteChocolate
        fields = '__all__'

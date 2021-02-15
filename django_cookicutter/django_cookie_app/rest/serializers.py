from rest_framework import serializers
from django_cookie_app import models


class ChocoOrangeSerializer(serializers.HyperlinkedModelSerializer):
    """
        ChocoOrangeSerializer
    """
    url = serializers.HyperlinkedIdentityField(view_name="rest:choc-oran-detail")

    class Meta:
        model = models.ChocoOrange
        fields = '__all__'


class MintChocoSerializer(serializers.HyperlinkedModelSerializer):
    """
        MintChocoSerializer
    """
    url = serializers.HyperlinkedIdentityField(view_name="rest:mint-choc-detail")

    class Meta:
        model = models.MintChoco
        fields = '__all__'


class SyrupSerializer(serializers.HyperlinkedModelSerializer):
    """
        SyrupSerializer
    """
    url = serializers.HyperlinkedIdentityField(view_name="rest:mapple-syrup-detail")

    class Meta:
        model = models.Syrup
        fields = '__all__'


class VanillaStrawberryChocolateSerializer(serializers.HyperlinkedModelSerializer):
    """
        VanillaStrawberryChocolateSerializer"
    """
    url = serializers.HyperlinkedIdentityField(view_name="rest:vani-stra-choc-detail")
    class Meta:
        """
            Meta
        """
        model = models.VanillaStrawberryChocolate
        fields = '__all__'


class RaspberryWhiteChocolateSerializer(serializers.HyperlinkedModelSerializer):
    """
        RaspberryWhiteChocolateSerializer
    """
    url = serializers.HyperlinkedIdentityField(view_name="rest:rasp-whit-choc-detail")

    class Meta:
        model = models.RaspberryWhiteChocolate
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
        OrderSerializer
    """
    url = serializers.HyperlinkedIdentityField(view_name="rest:order-detail")
    choco_oran = ChocoOrangeSerializer()
    mint_choco = MintChocoSerializer()
    syrup = SyrupSerializer()
    vanilla = VanillaStrawberryChocolateSerializer()
    raspberry = RaspberryWhiteChocolateSerializer()

    class Meta:
        model = models.Order
        fields = '__all__'

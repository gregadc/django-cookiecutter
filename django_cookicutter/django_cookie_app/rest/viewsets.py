from django.http import JsonResponse

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django_cookie_app import models
from django_cookie_app.rest import serializers


class OrderViewSet(ModelViewSet):
    """
        OrderViewSet
    """
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        #permissions.IsAuthenticated,
    ]

    @action(detail=False, methods=['post'])
    def inspect(self, request):
        """
            inspect
        """
        if request.method == 'POST':
            order_id = models.Order.objects.inspect(dict(request.data))
            return JsonResponse(order_id)
        return Response({"message": "Hello, world!"})

    def create(self, validated_data):
        return models.Order.create(**validated_data)

    def update(self, validated_data):
        pass


class ChocoOrangeViewSet(ModelViewSet):
    """
        ChocoOrangeViewSet
    """
    serializer_class = serializers.ChocoOrangeSerializer
    queryset = models.ChocoOrange.objects.all()

    @action(detail=False, methods=['post'])
    def update_bucket(self, request):
        """
            update_bucket
        """
        if request.method == 'POST':
            order_id = models.ChocoOrange.objects.update_last()
            return JsonResponse(order_id)
        return Response({"message": "Hello, world!"})


class MintChocoViewSet(ModelViewSet):
    """
        MintChocoViewSet
    """
    serializer_class = serializers.MintChocoSerializer
    queryset = models.MintChoco.objects.all()

    @action(detail=False, methods=['post'])
    def update_bucket(self, request):
        """
            update_bucket
        """
        if request.method == 'POST':
            order_id = models.MintChoco.objects.update_last()
            return JsonResponse(order_id)
        return Response({"message": "Hello, world!"})


class SyrupViewSet(ModelViewSet):
    """
        SyrupViewSet
    """
    serializer_class = serializers.SyrupSerializer
    queryset = models.Syrup.objects.all()

    @action(detail=False, methods=['post'])
    def update_bucket(self, request):
        """
            update_bucket
        """
        if request.method == 'POST':
            order_id = models.Syrup.objects.update_last()
            return JsonResponse(order_id)
        return Response({"message": "Hello, world!"})


class VanillaStrawberryChocolateViewSet(ModelViewSet):
    """
        VanillaStrawberryChocolateViewSet
    """
    serializer_class = serializers.VanillaStrawberryChocolateSerializer
    queryset = models.VanillaStrawberryChocolate.objects.all()

    @action(detail=False, methods=['post'])
    def update_bucket(self, request):
        """
            update_bucket
        """
        if request.method == 'POST':
            order_id = models.VanillaStrawberryChocolate.objects.update_last()
            return JsonResponse(order_id)
        return Response({"message": "Hello, world!"})


class RaspberryWhiteChocolateViewSet(ModelViewSet):
    """
        RaspberryWhiteChocolateViewSet
    """
    serializer_class = serializers.RaspberryWhiteChocolateSerializer
    queryset = models.RaspberryWhiteChocolate.objects.all()

    @action(detail=False, methods=['post'])
    def update_bucket(self, request):
        """
            update_bucket"
        """
        if request.method == 'POST':
            order_id = models.RaspberryWhiteChocolate.objects.update_last()
            return JsonResponse(order_id)
        return Response({"message": "Hello, world!"})

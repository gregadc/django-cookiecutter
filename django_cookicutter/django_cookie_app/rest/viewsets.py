from django.http import JsonResponse

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django_cookie_app import models
from django_cookie_app.rest import serializers
from django_cookie_app import filtersets


class MyViewSetMixin:
    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes.append(
                permissions.IsAuthenticated
            )
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in self.permission_classes]


class OrderViewSet(MyViewSetMixin, ModelViewSet):
    """
        OrderViewSet
    """
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.select_related(
        'choco_oran',
        'mint_choco',
        'syrup',
        'vanilla',
        'raspberry').all()
    permission_classes = []
    filterset_class = filtersets.OrderFilter
    filter_backends = (DjangoFilterBackend,)

    @action(
        detail=False,
        methods=['post', 'get'],
        permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def inspect(self, request, pk=None):
        """
            inspect
        """
        if request.method == 'POST':
            order_id = models.Order.objects.inspect(dict(request.data))
            return JsonResponse(order_id)
        return Response({"user": request.user})


class ChocoOrangeViewSet(MyViewSetMixin, ModelViewSet):
    """
        ChocoOrangeViewSet
    """
    serializer_class = serializers.ChocoOrangeSerializer
    queryset = models.ChocoOrange.objects.all()

    @action(
        detail=False,
        methods=['post'],
        permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def update_bucket(self, request, pk=None):
        """
            update_bucket
        """
        if request.method == 'POST':
            order_id = models.ChocoOrange.objects.update_last()
            return JsonResponse(order_id)
        return Response({"user": request.user})


class MintChocoViewSet(MyViewSetMixin, ModelViewSet):
    """
        MintChocoViewSet
    """
    serializer_class = serializers.MintChocoSerializer
    queryset = models.MintChoco.objects.all()

    @action(
        detail=False,
        methods=['post'],
        permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def update_bucket(self, request, pk=None):
        """
            update_bucket
        """
        if request.method == 'POST':
            order_id = models.MintChoco.objects.update_last()
            return JsonResponse(order_id)
        return Response({"user": request.user})


class SyrupViewSet(MyViewSetMixin, ModelViewSet):
    """
        SyrupViewSet
    """
    serializer_class = serializers.SyrupSerializer
    queryset = models.Syrup.objects.all()

    @action(
        detail=False,
        methods=['post'],
        permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def update_bucket(self, request, pk=None):
        """
            update_bucket
        """
        if request.method == 'POST':
            order_id = models.Syrup.objects.update_last()
            return JsonResponse(order_id)
        return Response({"user": request.user})


class VanillaStrawberryChocolateViewSet(MyViewSetMixin, ModelViewSet):
    """
        VanillaStrawberryChocolateViewSet
    """
    serializer_class = serializers.VanillaStrawberryChocolateSerializer
    queryset = models.VanillaStrawberryChocolate.objects.all()

    @action(
        detail=False,
        methods=['post'],
        permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def update_bucket(self, request, pk=None):
        """
            update_bucket
        """
        if request.method == 'POST':
            order_id = models.VanillaStrawberryChocolate.objects.update_last()
            return JsonResponse(order_id)
        return Response({"user": request.user})


class RaspberryWhiteChocolateViewSet(MyViewSetMixin, ModelViewSet):
    """
        RaspberryWhiteChocolateViewSet
    """
    serializer_class = serializers.RaspberryWhiteChocolateSerializer
    queryset = models.RaspberryWhiteChocolate.objects.all()

    @action(
        detail=False,
        methods=['post'],
        permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def update_bucket(self, request, pk=None):
        """
            update_bucket"
        """
        if request.method == 'POST':
            order_id = models.RaspberryWhiteChocolate.objects.update_last()
            return JsonResponse(order_id)
        return Response({"user": request.user})

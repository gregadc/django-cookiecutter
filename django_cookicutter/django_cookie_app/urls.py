from django.urls import include, path, re_path
from django.contrib.auth.views import LogoutView
from rest_framework import routers

from django_cookie_app import views
from django_cookie_app.rest import viewsets


router = routers.DefaultRouter()
router.register(r'order', viewsets.OrderViewSet, basename="order")
router.register(r'choc-oran', viewsets.ChocoOrangeViewSet, basename="choc-oran")
router.register(r'mint-choc', viewsets.MintChocoViewSet, basename="mint-choc")
router.register(r'mapple-syrup', viewsets.SyrupViewSet, basename="mapple-syrup")
router.register(r'rasp-whit-choc', viewsets.RaspberryWhiteChocolateViewSet, basename="rasp-whit-choc")
router.register(r'Vani-stra-choc', viewsets.VanillaStrawberryChocolateViewSet, basename="vani-stra-choc")

urlpatterns = [
    # Main
    path(r'', views.HomeView.as_view(), name='home'),
    # User
    path(r'login/', views.LoginCookieView.as_view(), name="login"),
    path(r'logout/', LogoutView.as_view(), name="logout"),
    path(r'users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail-view'),
    path(r'users/update/<int:pk>/', views.UserUpdateView.as_view(), name='user-update-view'),
    path(r'users/add', views.UserCreateView.as_view(), name='user-create-view'),
    # Rest
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'rest/', include((router.urls, 'rest'), namespace='rest')),
    # Others
    path(r'orders/', views.OrderListView.as_view(), name='order-list-view'),
    path(r'orders/<int:pk>', views.OrderDetailView.as_view(), name='order-detail-view'),
    path(r'choco-orange/', views.ChocoOrangeListView.as_view(), name='choco-orange-view'),
    path(r'mint-choco/', views.MintChocoListView.as_view(), name='mint-choco-view'),
    path(r'syrup/', views.SyrupListView.as_view(), name='syrup-view'),
    path(r'vani-stra-choc/', views.VanillaStrawberryChocolateListView.as_view(), name='vani-stra-choc-view'),
    path(r'rasp-whit-choc/', views.RaspberryWhiteChocolateListView.as_view(), name='rasp-whit-choc-view'),
]

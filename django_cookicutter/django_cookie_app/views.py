from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy as reverse
from django.views.generic import CreateView
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormMixin

from django_cookie_app.forms import (
    LoginForm,
    UserUpdateForm,
    UserCreateForm,
    ChoicePerfumeForm
)
from django_cookie_app import models
from django_cookie_app import filtersets


class HomeView(LoginRequiredMixin, FormMixin, View):
    """
        HomeView
    """
    template_name = "django_cookie_app/index.html"
    form_class = ChoicePerfumeForm
    model = models.Order

    def get_success_url(self):
        return reverse('order-detail-view', args=[self.pk])

    def get(self, request, *args, **kwargs):
        """
            Get method
        """
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        form = self.get_form()
        if form.is_valid():
            return render(request, self.template_name, {'form': form})
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return super(HomeView).form_valid(form)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = models.CustomUser
    template_name = "django_cookie_app/user_detail.html"
    form_class = UserUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "model": self.model
        })
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = models.CustomUser
    template_name = "django_cookie_app/user_update.html"
    fields = ['username', 'email', 'avatar', 'search']


class UserCreateView(CreateView):
    model = models.CustomUser
    template_name = "django_cookie_app/user_create.html"
    form_class = UserCreateForm

    def get_success_url(self):
        messages.success(self.request, 'User created!')
        return reverse("login")


class LoginCookieView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    success_message = "%(username)s connected."

    def get_success_message(self, cleaned_data):
        username = cleaned_data['username'].capitalize()
        return self.success_message % dict(
            cleaned_data,
            username=username,
        )


class IceCreamListView(ListView):
    """
        IceCreamListView
    """
    template_name = "django_cookie_app/base_list.html"

    def get_context_data(self, **kwargs):
        """
            get_context_data method
        """
        context = super().get_context_data(**kwargs)
        last_percentage = ""
        if self.model.objects.all().exists():
            last_percentage = self.model.objects.last().percentage_data
        context.update({
            "verbose_name": self.model._meta.get_field("perfume").verbose_name,
            "default_name": self.model._meta.get_field("perfume").default,
            "model": self.model.objects.last(),
            "last_percentage": "{} %".format(last_percentage),
        })
        return context


class ChocoOrangeListView(IceCreamListView):
    """
        Choco_orangeListView
    """
    model = models.ChocoOrange


class MintChocoListView(IceCreamListView):
    """
        MintChocoListView
    """
    model = models.MintChoco


class SyrupListView(IceCreamListView):
    """
        SyrupListView
    """
    model = models.Syrup


class VanillaStrawberryChocolateListView(IceCreamListView):
    """
        VanillaStrawberryChocolateListView
    """
    model = models.VanillaStrawberryChocolate


class RaspberryWhiteChocolateListView(IceCreamListView):
    """
        RaspberryWhiteChocolateListView
    """
    model = models.RaspberryWhiteChocolate


class OrderListView(ListView):
    """
        OrderListView
    """
    queryset = models.Order.objects.order_by('-date')
    template_name = "django_cookie_app/order_list.html"
    filterset_class = filtersets.OrderFilter
    context_object_name = "order_list"
    paginate_by = 10


class OrderDetailView(DetailView):
    """
        OrderDetailView
    """
    model = models.Order
    template_name = "django_cookie_app/order_detail.html"

    def get_context_data(self, **kwargs):
        """
            get_context_data method
        """
        context = super().get_context_data(**kwargs)
        context.update({
            "model": self.model
        })
        return context

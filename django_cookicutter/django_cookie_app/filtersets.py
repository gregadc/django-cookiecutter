from django import forms
from django_filters import rest_framework as filters
from django.utils.translation import ugettext_lazy as _

from django_cookie_app import models


class DateWidget(forms.DateInput):
    """
        DateWidget
    """
    def __init__(self, *args, **kwargs):
        """
            __init__ method
        """
        super().__init__(*args, **kwargs)
        self.attrs['data-format'] = 'YYYY-MM-DD'


class DateTimeWidget(forms.DateTimeInput):
    """
        DateTimeWidget
    """
    def __init__(self, *args, **kwargs):
        """
            __init__ method
        """
        super().__init__(*args, **kwargs)
        self.attrs['data-format'] = 'YYYY-MM-DD HH:mm:ss'


class OrderFilter(filters.FilterSet):
    """
        OrderFilter
    """
    date = filters.DateFilter(
        field_name='date__date',
        widget=DateWidget(attrs={'placeholder': _("Date")})
    )
    date_gte = filters.DateFilter(
        field_name='date',
        widget=DateWidget(attrs={'placeholder': _("After")}),
        lookup_expr='gte')
    date_lte = filters.DateFilter(
        field_name='date',
        widget=DateWidget(attrs={'placeholder': _("Before")}),
        lookup_expr='lte')
    code = filters.CharFilter(field_name='code')

    class Meta:
        model = models.Order
        fields = [
            'date',
            'date_gte',
            'date_lte',
            'code',
        ]

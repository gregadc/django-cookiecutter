from django import forms
from django_filters import FilterSet, DateFilter, CharFilter
from django.utils.translation import ugettext_lazy as _

from django_cookie_app import models


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


class OrderFilter(FilterSet):
    """
        OrderFilter
    """
    date = DateFilter(
        name='date',
        widget=DateTimeWidget(attrs={'placeholder': _("Date")})
    )
    code = CharFilter(name='code')

    class Meta:
        model = models.Order
        fields = [
            'date',
            'code',
        ]


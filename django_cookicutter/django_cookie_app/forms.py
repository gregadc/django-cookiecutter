from django import forms
from django.db import transaction
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField
)
from django.utils.translation import ugettext_lazy as _

from django_cookie_app.models import CustomUser, GENDER_IDENTITY


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Required')
    last_name = forms.CharField(max_length=30, help_text='Required')
    email = forms.EmailField(
        max_length=254,
        help_text='Email address',
        error_messages={'required': 'Please enter valid email'}
    )

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    @transaction.atomic
    def save(self, commit=False):
        user = super().save(commit=False)
        user.save()
        return user


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control materail_input text-center',
                'placeholder': 'Username'
                }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control materail_input text-center',
                'placeholder': 'Password'
            }
        )
    )

    class Meta:
        model = CustomUser


class UserUpdateForm(forms.Form):
    avatar = forms.FileField()
    search = forms.CharField(label=_("Search"))
    username = forms.CharField(label=_("Username"))
    email = forms.EmailField(label=_("Email"))

    class Meta:
        model = CustomUser


class UserCreateForm(UserCreationForm):
    avatar = forms.FileField(required=False)
    password1 = forms.CharField(
        label=_("Password1"),
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control text-center',
                'placeholder': 'Password1'
            }
        )
    )
    password2 = forms.CharField(
        label=_("Password2"),
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control text-center',
                'placeholder': 'Password2'
            }
        )
    )
    sex = forms.ChoiceField(label=_("Sex"), choices=GENDER_IDENTITY)
    search = forms.ChoiceField(label=_("Search"), choices=GENDER_IDENTITY)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'sex', 'search']

    field_order = [
        'username',
        'email',
        'password1',
        'password2',
        'sex',
        'search',
        'avatar']


class ChoicePerfumeForm(forms.Form):
    choco = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control input-number',
                'min': '0', 'value': '0', 'pattern': '[0-9]+'}))
    mint = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control input-number',
                'min': '0', 'value': '0', 'pattern': '[0-9]+'}))
    syrup = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control input-number',
                'min': '0', 'value': '0', 'pattern': '[0-9]+'}))
    vanilla = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control input-number',
                'min': '0', 'value': '0', 'pattern': '[0-9]+'}))
    raspberry = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'class': 'form-control input-number',
                'min': '0', 'value': '0', 'pattern': '[0-9]+'}))

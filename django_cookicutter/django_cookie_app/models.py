from __future__ import unicode_literals
import uuid

from django.db import models
from django.contrib.auth import models as auth_models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator

from django_cookie_app import querysets


GENDER_IDENTITY = (
    ('Man', _('Man')),
    ('Woman', _('Woman'))
)


class CustomUser(auth_models.AbstractUser):
    """
        CustomUser class
    """
    avatar = models.ImageField(default='user.png')
    sex = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        choices=GENDER_IDENTITY
    )
    search = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        choices=GENDER_IDENTITY,
        verbose_name=_("Search gender"))
    objects = querysets.UserCookieManager()

    class Meta:
        app_label = 'django_cookie_app'

    def get_absolute_url(self):
        return reverse('user-detail-view', args=[self.id])
        #return reverse('user-detail-view', kwargs={'pk': int(self.id)})


class BasePerfume(models.Model):
    """
        BasePerfume class
    """
    date = models.DateTimeField(verbose_name=_("Date"))
    total_ball = models.IntegerField(default=40, validators=[MinValueValidator(40)])
    number_time_fill = models.IntegerField()
    percentage = models.FloatField()
    ball_bought = models.IntegerField()

    class Meta:
        abstract = True

    @property
    def percentage_data(self):
        """
            Return percentage
        """
        if isinstance(self.percentage, float) and not None:
            return str(int((100 * self.percentage) / 40))
        return 100


class ChocoOrange(BasePerfume):
    """
        ChocoOrange class
    """
    perfume = models.CharField(
        max_length=35,
        default="choc-oran",
        verbose_name=_("Chocolat Orange")
    )

    class Meta:
        app_label = "django_cookie_app"
        verbose_name = "{} ice cream.".format(_("Chocolat-Orange"))

    def __str__(self):
        return "{} ice cream.".format(self.perfume)

    objects = querysets.ChocoOrangeQueryset.as_manager()


class MintChoco(BasePerfume):
    """
        MintChoco class
    """
    perfume = models.CharField(
        max_length=35,
        default="mint-choc",
        verbose_name=_("Mint Choco")
    )

    class Meta:
        app_label = "django_cookie_app"
        verbose_name = "{} ice cream.".format(_("Mint-Choco"))

    def __str__(self):
        return "{} ice cream.".format(self.perfume)

    objects = querysets.MintQueryset.as_manager()


class Syrup(BasePerfume):
    """
        Syrup class
    """
    perfume = models.CharField(
        max_length=35,
        default="mapple-syrup",
        verbose_name=_("Maple syrup")
    )

    class Meta:
        app_label = "django_cookie_app"
        verbose_name = "{} ice cream.".format(_("Maple-syrup"))

    def __str__(self):
        return "{} ice cream.".format(self.perfume)

    objects = querysets.SyrupQueryset.as_manager()


class VanillaStrawberryChocolate(BasePerfume):
    """
        VanillaStrawberryChocolate class
    """
    perfume = models.CharField(
        max_length=35,
        default="Vani-stra-choc",
        verbose_name=_("Vanilla Strawberry Chocolate")
    )

    class Meta:
        app_label = "django_cookie_app"
        verbose_name = "{} ice cream.".format(_("Vanilla-Strawberry-Chocolate"))

    def __str__(self):
        return "{} ice cream.".format(self.perfume)

    objects = querysets.VanillaStrawberryChocolateQueryset.as_manager()


class RaspberryWhiteChocolate(BasePerfume):
    """
        RaspberryWhiteChocolate class
    """
    perfume = models.CharField(
        max_length=35,
        default="rasp-whit-choc",
        verbose_name=_("Raspberry white chocolate")
    )

    class Meta:
        app_label = "django_cookie_app"
        verbose_name = "{} ice cream.".format(_("Raspberry-white-chocolate"))

    def __str__(self):
        return "{} ice cream.".format(self.perfume)

    objects = querysets.RaspberryWhiteChocolateQueryset.as_manager()


class Order(models.Model):
    """
        Order class
    """
    price = models.IntegerField()
    count_ball = models.IntegerField()
    code = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=uuid.uuid1().hex,
        verbose_name=_("Code")
    )
    date = models.DateTimeField(verbose_name=_("Date"))
    choco_oran = models.ForeignKey(
        ChocoOrange,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Chocolat orange"))
    mint_choco = models.ForeignKey(
        MintChoco,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Mint choco"))
    syrup = models.ForeignKey(
        Syrup,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Maple syrup"))
    vanilla = models.ForeignKey(
        VanillaStrawberryChocolate,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Vanilla strawberry chocolate"))
    raspberry = models.ForeignKey(
        RaspberryWhiteChocolate,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Raspberry white chocolate"))
    is_last = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name=_("Is last")
    )

    #inspect_order = reverse('rest:order-inspect')

    objects = querysets.OrderQueryset.as_manager()

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        """
            get_absolute_url method
        """
        return reverse('order-detail-view', args=[self.id])

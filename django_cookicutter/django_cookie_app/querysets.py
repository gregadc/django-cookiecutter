from datetime import datetime

from django.db import models
from django.contrib.auth.models import UserManager

from django_cookie_app import models as django_cookie_models


class UserCookieManager(UserManager):
    """
        UserCookieManager class
    """
    pass


class BaseQueryset(models.QuerySet):
    """
        BaseQueryset class
    """
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def inspect(self, *args):
        """
            Inspect data
        """
        choco_balls = 40
        number_time_fill = 0
        ball_bought = args[2]
        if self.model.objects.all().exists():
            choco_balls = self.model.objects.last().total_ball
            number_time_fill = self.model.objects.last().number_time_fill
        if not choco_balls:
            return None
        tmp_choco_balls = choco_balls
        choco_balls -= int(args[0][args[1]][0])
        if choco_balls < 0:
            choco_balls = 0
            ball_bought = tmp_choco_balls
        bucket, _ = self.model.objects.get_or_create(
            date=self.date,
            ball_bought=ball_bought,
            number_time_fill=number_time_fill,
            percentage=choco_balls,
            total_ball=choco_balls)
        return bucket

    def update_last(self):
        """
            Update last data
        """
        if not self.model.objects.all().exists():
            bucket, _ = self.model.objects.get_or_create(
                date=self.date,
                ball_bought=40,
                number_time_fill=40,
                percentage=40,
                total_ball=40,)
            return {'bucket': bucket.id}
        bucket = self.model.objects.all().last()
        fill = int(bucket.number_time_fill)
        fill += 1
        bucket.total_ball = 40
        bucket.number_time_fill = fill
        bucket.percentage = float(40)
        bucket.save()
        return {'bucket': bucket.id}


class ChocoOrangeQueryset(BaseQueryset):
    """
         ChocoOrangeQueryset class
    """
    pass


class MintQueryset(BaseQueryset):
    """
        MintQueryset class
    """
    pass


class SyrupQueryset(BaseQueryset):
    """
        SyrupQueryset class
    """
    pass


class VanillaStrawberryChocolateQueryset(BaseQueryset):
    """
        VanillaStrawberryChocolateQueryset class
    """
    pass


class RaspberryWhiteChocolateQueryset(BaseQueryset):
    """
        RaspberryWhiteChocolateQueryset class
    """
    pass


class OrderQueryset(models.QuerySet):
    """
        OrderQueryset class
    """
    def inspect(self, order_dict, order=True):
        """
            Inspect data
        """
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            del order_dict['csrfmiddlewaretoken']
            if not sum([int(i[0]) for i in order_dict.values() if int(i[0]) >= 0]):
                return {'id': None, 'name': None}
        except ValueError:
            return {'id': None, 'name': None}
        balls = 0
        choco_oran = django_cookie_models.ChocoOrange.objects.inspect(
            order_dict, 'choco', int(order_dict['choco'][0]))
        if not choco_oran:
            return {'id': None, 'name': "chocolate-orange"}
        balls += choco_oran.ball_bought
        mint_choco = django_cookie_models.MintChoco.objects.inspect(
            order_dict, 'mint', int(order_dict['mint'][0]))
        if not mint_choco:
            return {'id': None, 'name': "mint"}
        balls += mint_choco.ball_bought
        vanilla = django_cookie_models.VanillaStrawberryChocolate.objects.inspect(
            order_dict, 'vanilla', int(order_dict['vanilla'][0]))
        if not vanilla:
            return {'id': None, 'name': "vanilla"}
        balls += vanilla.ball_bought
        syrup = django_cookie_models.Syrup.objects.inspect(
            order_dict, 'syrup', int(order_dict['syrup'][0]))
        if not syrup:
            return {'id': None, 'name': "syrup"}
        balls += syrup.ball_bought
        raspberry = django_cookie_models.RaspberryWhiteChocolate.objects.inspect(
            order_dict, 'raspberry', int(order_dict['raspberry'][0]))
        if not raspberry:
            return {'id': None, 'name': "raspberry"}
        balls += raspberry.ball_bought
        order, _ = self.model.objects.get_or_create(
            count_ball=balls,
            price=balls*2,
            date=date,
            choco_oran=choco_oran,
            mint_choco=mint_choco,
            vanilla=vanilla,
            syrup=syrup,
            raspberry=raspberry)
        return {'id': order.id}

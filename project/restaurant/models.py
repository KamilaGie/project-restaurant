from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


class Product(models.Model):
    name = models.CharField(max_length = 64, verbose_name = 'produkt')
    price = models.IntegerField(verbose_name = 'cena')
    category = models.ForeignKey('Category', verbose_name = 'kategoria')

    def __str__(self):
        return '{}'.format(self.name)


class Category(models.Model):
    name = models.CharField(max_length = 32, verbose_name = 'kategoria')

    def __str__(self):
        return self.name


class Order(models.Model):
    description = models.TextField(verbose_name = 'opis')
    quantity = models.IntegerField(default = 1, verbose_name = 'ilość')
    date_sent = models.DateTimeField(default = timezone.now(), verbose_name = 'wysłano')
    product = models.ForeignKey('Product', verbose_name="produkt")

    def __str__(self):
        return '{}raz(y) {} - {}, ({}) '.format(self.quantity, self.product, self.description, self.date_sent.time().strftime('%H:%M'))

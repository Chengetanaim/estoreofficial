from django.db import models

# Create your models here.


class Coupon(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Coupon'

    def __str__(self):
        return self.name



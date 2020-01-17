from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    name = models.CharField( max_length=250, default='', blank=False)
    CATEGORIES = (
        (u"Books",u'Books'),
        (u"Movies", u'Movies'),
    )
    category = models.CharField(choices=CATEGORIES,max_length=250, null=False, default='0000000', editable=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)



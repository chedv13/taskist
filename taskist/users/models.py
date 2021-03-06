# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField


@python_2_unicode_compatible
class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    # TODO: Разобраться с генерилкой тамбнейлов
    avatar = ThumbnailerImageField(upload_to='users/users/images/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

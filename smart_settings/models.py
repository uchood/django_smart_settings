# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

# Create your models here.


class ConfigOfServer(models.Model):
    TYPE_OPTIONS = {
        u'STRING': 0,
        u'INT': 1,
        u'FLOAT': 2
    }
    TYPE_OPTIONS_VERB = [
        (TYPE_OPTIONS[u'INT'], u'int'),
        (TYPE_OPTIONS[u'FLOAT'], u'float'),
        (TYPE_OPTIONS[u'STRING'], u'строка'),
    ]
    group = models.CharField(verbose_name=u'Группа',  max_length=255 , blank = True)
    key = models.CharField(verbose_name=u'Параметр',  unique = True, max_length = 255)
    value = models.CharField(verbose_name=u'Значение',  max_length=1024, blank = True)
    type_of_value = models.IntegerField(verbose_name=u'Тип', choices=TYPE_OPTIONS_VERB, default=TYPE_OPTIONS[u'STRING'])
    changed_on = models.DateTimeField(verbose_name=u'Дата изменения', auto_now=True, blank=True)
    description = models.CharField(verbose_name=u'Описание',  max_length=1024, blank = True)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s" % (content_type.app_label, content_type.model), args=(self.id,))

    def __unicode__(self):
        return self.key



    class Meta:
        ordering = ('group','key',)
        verbose_name = u'Параметр'
        verbose_name_plural = u'Параметры'
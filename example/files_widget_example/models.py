# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from topnotchdev import files_widget


@python_2_unicode_compatible
class MyModelFile_Widget(models.Model):
    name = models.CharField(verbose_name=('Name'), max_length=20, default='')
    image = files_widget.ImageField()
    images = files_widget.ImagesField()

    class Meta:
        verbose_name = ("MyModel")
        verbose_name_plural = ("MyModel")

    def __str__(self):
        return self.name or ""

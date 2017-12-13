# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your views here.

class Music(models.Model):
	video = models.FileField(upload_to='media/')

	def __str__(self):
		return str(self.pk)
